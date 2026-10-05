from __future__ import annotations
import json
import os
import shutil
import time
import zipfile
import io
from pathlib import Path
from typing import List, Optional, Dict, Any
from .models import Folder, FolderCreate, FolderUpdate, ProjectMetadata, ProjectCreate, ProjectUpdate, FileItem
from .templates import TEMPLATES

class StorageManager:
    def __init__(self, base_dir: Path):
        self.base_dir = base_dir
        self.projects_dir = base_dir / "projects"
        self.folders_file = base_dir / "folders.json"
        
        self.base_dir.mkdir(parents=True, exist_ok=True)
        self.projects_dir.mkdir(parents=True, exist_ok=True)
        
        if not self.folders_file.exists():
            self._init_default_folders()

    def _init_default_folders(self):
        default_folders = [
            Folder(id="f_akademik", name="Akademik", parent_id=None, color="#3b82f6"),
            Folder(id="f_skripsi", name="Skripsi & Riset", parent_id="f_akademik", color="#60a5fa"),
            Folder(id="f_bisnis", name="Bisnis & Klien", parent_id=None, color="#10b981"),
            Folder(id="f_soetahills", name="Soetahills Real Estate", parent_id="f_bisnis", color="#059669"),
            Folder(id="f_yudiaz", name="Yudiaz Internal", parent_id=None, color="#d4af37"),
        ]
        self._save_folders(default_folders)

    def _load_folders(self) -> List[Folder]:
        if not self.folders_file.exists():
            return []
        try:
            data = json.loads(self.folders_file.read_text())
            return [Folder(**item) for item in data]
        except Exception:
            return []

    def _save_folders(self, folders: List[Folder]):
        data = [f.model_dump() for f in folders]
        self.folders_file.write_text(json.dumps(data, indent=2))

    # --- Folder Operations ---
    def list_folders(self) -> List[Folder]:
        return self._load_folders()

    def create_folder(self, data: FolderCreate) -> Folder:
        folders = self._load_folders()
        folder = Folder(
            name=data.name.strip(),
            parent_id=data.parent_id,
            color=data.color or "#d4af37"
        )
        folders.append(folder)
        self._save_folders(folders)
        return folder

    def update_folder(self, folder_id: str, data: FolderUpdate) -> Optional[Folder]:
        folders = self._load_folders()
        for f in folders:
            if f.id == folder_id:
                if data.name is not None:
                    f.name = data.name.strip()
                if data.parent_id is not None:
                    f.parent_id = data.parent_id if data.parent_id != "" else None
                if data.color is not None:
                    f.color = data.color
                self._save_folders(folders)
                return f
        return None

    def delete_folder(self, folder_id: str) -> bool:
        folders = self._load_folders()
        folders = [f for f in folders if f.id != folder_id and f.parent_id != folder_id]
        self._save_folders(folders)
        
        # Reset projects folder_id if in this deleted folder
        for p in self.list_projects():
            if p.folder_id == folder_id:
                self.update_project(p.id, ProjectUpdate(folder_id=""))
        return True

    # --- Project Operations ---
    def _project_dir(self, project_id: str) -> Path:
        return self.projects_dir / project_id

    def list_projects(self, folder_id: Optional[str] = None, search: Optional[str] = None) -> List[ProjectMetadata]:
        projects = []
        for pdir in self.projects_dir.iterdir():
            if pdir.is_dir() and (pdir / "project.json").exists():
                try:
                    meta = ProjectMetadata(**json.loads((pdir / "project.json").read_text()))
                    projects.append(meta)
                except Exception:
                    continue
        
        if folder_id is not None:
            if folder_id == "root" or folder_id == "":
                projects = [p for p in projects if not p.folder_id]
            else:
                projects = [p for p in projects if p.folder_id == folder_id]
                
        if search:
            q = search.lower()
            projects = [p for p in projects if q in p.title.lower() or (p.description and q in p.description.lower())]

        return sorted(projects, key=lambda x: x.updated_at, reverse=True)

    def get_project(self, project_id: str) -> Optional[ProjectMetadata]:
        meta_file = self._project_dir(project_id) / "project.json"
        if meta_file.exists():
            try:
                return ProjectMetadata(**json.loads(meta_file.read_text()))
            except Exception:
                return None
        return None

    def get_project_by_share_id(self, share_id: str) -> Optional[ProjectMetadata]:
        for p in self.list_projects():
            if p.share_id == share_id:
                return p
        return None

    def create_project(self, data: ProjectCreate) -> ProjectMetadata:
        meta = ProjectMetadata(
            title=data.title.strip(),
            description=data.description.strip() if data.description else "",
            folder_id=data.folder_id if data.folder_id else None,
            main_file="main.tex"
        )
        pdir = self._project_dir(meta.id)
        pdir.mkdir(parents=True, exist_ok=True)
        
        # Save metadata
        (pdir / "project.json").write_text(json.dumps(meta.model_dump(), indent=2))
        
        # Populate initial files from template
        tpl = TEMPLATES.get(data.template or "blank", TEMPLATES["blank"])
        for fname, fcontent in tpl.items():
            if fname in ["name", "description"]:
                continue
            fpath = pdir / fname
            fpath.parent.mkdir(parents=True, exist_ok=True)
            fpath.write_text(fcontent, encoding="utf-8")

        # Copy binary template assets if available
        tpl_assets_dir = self.base_dir.parent / "backend" / "templates_assets" / (data.template or "")
        if tpl_assets_dir.exists() and tpl_assets_dir.is_dir():
            for asset_file in tpl_assets_dir.iterdir():
                if asset_file.is_file():
                    shutil.copy2(asset_file, pdir / asset_file.name)
            
        return meta

    def update_project(self, project_id: str, data: ProjectUpdate) -> Optional[ProjectMetadata]:
        pdir = self._project_dir(project_id)
        meta_file = pdir / "project.json"
        if not meta_file.exists():
            return None
            
        meta = ProjectMetadata(**json.loads(meta_file.read_text()))
        if data.title is not None:
            meta.title = data.title.strip()
        if data.description is not None:
            meta.description = data.description.strip()
        if data.folder_id is not None:
            meta.folder_id = data.folder_id if data.folder_id != "" else None
        if data.is_public is not None:
            meta.is_public = data.is_public
            
        meta.updated_at = time.time()
        meta_file.write_text(json.dumps(meta.model_dump(), indent=2))
        return meta

    def save_compile_status(self, project_id: str, status: str):
        pdir = self._project_dir(project_id)
        meta_file = pdir / "project.json"
        if meta_file.exists():
            meta = ProjectMetadata(**json.loads(meta_file.read_text()))
            meta.compile_status = status
            meta.last_compiled_at = time.time()
            meta.updated_at = time.time()
            meta_file.write_text(json.dumps(meta.model_dump(), indent=2))

    def delete_project(self, project_id: str) -> bool:
        pdir = self._project_dir(project_id)
        if pdir.exists():
            shutil.rmtree(pdir, ignore_errors=True)
            return True
        return False

    # --- Project File Operations ---
    def list_project_files(self, project_id: str) -> List[FileItem]:
        pdir = self._project_dir(project_id)
        if not pdir.exists():
            return []
            
        items = []
        for root, dirs, files in os.walk(pdir):
            # Ignore build directory, git, and metadata
            dirs[:] = [d for d in dirs if d not in ["build", ".git", "__pycache__"]]
            rel_root = os.path.relpath(root, pdir)
            
            for file in files:
                if file == "project.json":
                    continue
                fpath = Path(root) / file
                rel_path = os.path.relpath(fpath, pdir)
                items.append(FileItem(
                    name=file,
                    path=rel_path,
                    is_dir=False,
                    size=fpath.stat().st_size,
                    updated_at=fpath.stat().st_mtime
                ))
        return sorted(items, key=lambda x: (x.name != "main.tex", x.path))

    def read_file(self, project_id: str, rel_path: str) -> Optional[str]:
        pdir = self._project_dir(project_id)
        target = (pdir / rel_path).resolve()
        # Security: prevent path traversal outside project_dir
        if not str(target).startswith(str(pdir.resolve())):
            return None
        if target.exists() and target.is_file():
            return target.read_text(encoding="utf-8", errors="replace")
        return None

    def write_file(self, project_id: str, rel_path: str, content: str) -> bool:
        pdir = self._project_dir(project_id)
        target = (pdir / rel_path).resolve()
        if not str(target).startswith(str(pdir.resolve())):
            return False
            
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        
        # Update project modified time
        meta_file = pdir / "project.json"
        if meta_file.exists():
            try:
                meta = ProjectMetadata(**json.loads(meta_file.read_text()))
                meta.updated_at = time.time()
                meta_file.write_text(json.dumps(meta.model_dump(), indent=2))
            except Exception:
                pass
        return True

    def delete_file(self, project_id: str, rel_path: str) -> bool:
        pdir = self._project_dir(project_id)
        target = (pdir / rel_path).resolve()
        if not str(target).startswith(str(pdir.resolve())):
            return False
        if target.exists() and target.is_file():
            target.unlink()
            return True
        return False

    def save_uploaded_asset(self, project_id: str, filename: str, content: bytes) -> Optional[str]:
        pdir = self._project_dir(project_id)
        # Clean filename
        clean_name = os.path.basename(filename)
        assets_dir = pdir / "assets"
        assets_dir.mkdir(parents=True, exist_ok=True)
        target = assets_dir / clean_name
        target.write_bytes(content)
        return f"assets/{clean_name}"

    def export_project_zip(self, project_id: str) -> Optional[io.BytesIO]:
        pdir = self._project_dir(project_id)
        if not pdir.exists():
            return None
            
        zip_buffer = io.BytesIO()
        with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(pdir):
                dirs[:] = [d for d in dirs if d not in [".git", "__pycache__"]]
                for file in files:
                    if file == "project.json":
                        continue
                    full_path = Path(root) / file
                    arcname = os.path.relpath(full_path, pdir)
                    zf.write(full_path, arcname)
                    
        zip_buffer.seek(0)
        return zip_buffer
