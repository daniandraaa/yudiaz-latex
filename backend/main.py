from __future__ import annotations
import os
from pathlib import Path
from typing import Optional, List
from fastapi import FastAPI, HTTPException, UploadFile, File, Response, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles

from .models import (
    Folder, FolderCreate, FolderUpdate,
    ProjectMetadata, ProjectCreate, ProjectUpdate,
    FileItem, FileWriteRequest, CompileResult
)
from .storage import StorageManager
from .compiler import LatexCompiler
from .templates import TEMPLATES

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
STATIC_DIR = BASE_DIR / "frontend" / "static"

app = FastAPI(
    title="Yudiaz LaTeX Studio",
    description="Enterprise LaTeX Document Workspace & Real-time Compiler for Yudiaz Creative Studio",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

storage = StorageManager(DATA_DIR)
compiler = LatexCompiler(timeout_seconds=45)

# --- Health Check ---
@app.get("/health")
def health():
    return {
        "status": "ok",
        "app": "Yudiaz LaTeX Studio",
        "version": "1.0.0",
        "engine": "pdfTeX / latexmk",
        "workspace_projects": len(storage.list_projects())
    }

# --- Templates ---
@app.get("/api/templates")
def get_templates():
    return [
        {
            "id": key,
            "name": val["name"],
            "description": val["description"]
        }
        for key, val in TEMPLATES.items()
    ]

# --- Folders API ---
@app.get("/api/folders", response_model=List[Folder])
def list_folders():
    return storage.list_folders()

@app.post("/api/folders", response_model=Folder)
def create_folder(data: FolderCreate):
    return storage.create_folder(data)

@app.put("/api/folders/{folder_id}", response_model=Folder)
def update_folder(folder_id: str, data: FolderUpdate):
    folder = storage.update_folder(folder_id, data)
    if not folder:
        raise HTTPException(status_code=404, detail="Folder tidak ditemukan")
    return folder

@app.delete("/api/folders/{folder_id}")
def delete_folder(folder_id: str):
    success = storage.delete_folder(folder_id)
    return {"success": success}

# --- Projects API ---
@app.get("/api/projects", response_model=List[ProjectMetadata])
def list_projects(
    folder_id: Optional[str] = Query(None),
    search: Optional[str] = Query(None)
):
    return storage.list_projects(folder_id=folder_id, search=search)

@app.post("/api/projects", response_model=ProjectMetadata)
def create_project(data: ProjectCreate):
    project = storage.create_project(data)
    # Automatically compile newly created project to generate initial PDF
    try:
        pdir = storage._project_dir(project.id)
        comp_res = compiler.compile(pdir, project.main_file)
        storage.save_compile_status(project.id, comp_res.status)
    except Exception:
        pass
    return storage.get_project(project.id) or project

@app.get("/api/projects/{project_id}")
def get_project_detail(project_id: str):
    project = storage.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
    files = storage.list_project_files(project_id)
    return {
        "project": project,
        "files": files
    }

@app.put("/api/projects/{project_id}", response_model=ProjectMetadata)
def update_project(project_id: str, data: ProjectUpdate):
    project = storage.update_project(project_id, data)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
    return project

@app.delete("/api/projects/{project_id}")
def delete_project(project_id: str):
    success = storage.delete_project(project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
    return {"success": True}

# --- Project Files API ---
@app.get("/api/projects/{project_id}/files/{file_path:path}")
def read_project_file(project_id: str, file_path: str):
    content = storage.read_file(project_id, file_path)
    if content is None:
        raise HTTPException(status_code=404, detail="File tidak ditemukan")
    return {"path": file_path, "content": content}

@app.put("/api/projects/{project_id}/files/{file_path:path}")
def write_project_file(project_id: str, file_path: str, req: FileWriteRequest):
    success = storage.write_file(project_id, file_path, req.content)
    if not success:
        raise HTTPException(status_code=400, detail="Gagal menyimpan file")
    return {"success": True, "path": file_path}

@app.delete("/api/projects/{project_id}/files/{file_path:path}")
def delete_project_file(project_id: str, file_path: str):
    if file_path == "main.tex":
        raise HTTPException(status_code=400, detail="File 'main.tex' tidak boleh dihapus")
    success = storage.delete_file(project_id, file_path)
    if not success:
        raise HTTPException(status_code=404, detail="File tidak ditemukan")
    return {"success": True}

@app.post("/api/projects/{project_id}/upload")
async def upload_asset(project_id: str, file: UploadFile = File(...)):
    content = await file.read()
    rel_path = storage.save_uploaded_asset(project_id, file.filename, content)
    if not rel_path:
        raise HTTPException(status_code=400, detail="Gagal mengunggah file")
    return {"success": True, "path": rel_path}

# --- Compilation API ---
@app.post("/api/projects/{project_id}/compile", response_model=CompileResult)
def compile_project(project_id: str):
    project = storage.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
        
    pdir = storage._project_dir(project_id)
    result = compiler.compile(pdir, project.main_file)
    storage.save_compile_status(project_id, result.status)
    return result

@app.get("/api/projects/{project_id}/pdf")
@app.head("/api/projects/{project_id}/pdf")
def get_project_pdf(project_id: str):
    pdir = storage._project_dir(project_id)
    project = storage.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
        
    stem = Path(project.main_file).stem
    pdf_path = pdir / "build" / f"{stem}.pdf"
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="Dokumen PDF belum dikompilasi")
        
    return FileResponse(
        str(pdf_path),
        media_type="application/pdf",
        filename=f"{project.title}.pdf",
        headers={"Content-Disposition": f"inline; filename=\"{project.title}.pdf\""}
    )

@app.get("/api/projects/{project_id}/log")
def get_project_log(project_id: str):
    pdir = storage._project_dir(project_id)
    log_path = pdir / "build" / "main.log"
    if not log_path.exists():
        return {"log": "Belum ada log kompilasi."}
    return {"log": log_path.read_text(encoding="utf-8", errors="replace")}

@app.get("/api/projects/{project_id}/export-zip")
def export_project_zip(project_id: str):
    project = storage.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
    zip_buffer = storage.export_project_zip(project_id)
    if not zip_buffer:
        raise HTTPException(status_code=500, detail="Gagal membuat arsip ZIP")
    return StreamingResponse(
        zip_buffer,
        media_type="application/zip",
        headers={"Content-Disposition": f"attachment; filename=\"{project.title}.zip\""}
    )

# --- Public Share & Preview API ---
@app.post("/api/projects/{project_id}/share")
def toggle_share(project_id: str):
    project = storage.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Proyek tidak ditemukan")
    updated = storage.update_project(project_id, ProjectUpdate(is_public=not project.is_public))
    return {
        "share_id": updated.share_id,
        "is_public": updated.is_public,
        "preview_url": f"/preview/{updated.share_id}"
    }

@app.get("/api/preview/{share_id}/pdf")
@app.head("/api/preview/{share_id}/pdf")
def get_shared_pdf(share_id: str):
    project = storage.get_project_by_share_id(share_id)
    if not project or not project.is_public:
        raise HTTPException(status_code=404, detail="Dokumen preview tidak tersedia atau telah dinonaktifkan")
        
    pdir = storage._project_dir(project.id)
    stem = Path(project.main_file).stem
    pdf_path = pdir / "build" / f"{stem}.pdf"
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="PDF belum siap atau sedang dalam proses kompilasi")
        
    return FileResponse(
        str(pdf_path),
        media_type="application/pdf",
        filename=f"{project.title}.pdf",
        headers={"Content-Disposition": f"inline; filename=\"{project.title}.pdf\""}
    )

@app.get("/preview/{share_id}", response_class=HTMLResponse)
@app.head("/preview/{share_id}")
def render_preview_page(share_id: str):
    project = storage.get_project_by_share_id(share_id)
    if not project or not project.is_public:
        return HTMLResponse(
            """<!DOCTYPE html>
            <html lang="id">
            <head>
                <meta charset="UTF-8"><title>Dokumen Tidak Ditemukan - Yudiaz Studio</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <style>
                    body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; text-align: center; }
                    .card { background: #1e293b; padding: 2.5rem; border-radius: 1rem; border: 1px solid #334155; max-width: 420px; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5); }
                    h2 { color: #f59e0b; margin-top: 0; }
                    p { color: #94a3b8; font-size: 0.95rem; }
                    a { display: inline-block; margin-top: 1rem; color: #d4af37; text-decoration: none; font-weight: 600; }
                </style>
            </head>
            <body>
                <div class="card">
                    <h2>Pratinjau Tidak Tersedia</h2>
                    <p>Tautan dokumen LaTeX ini tidak valid atau akses pratinjau publik telah dinonaktifkan oleh pemilik dokumen.</p>
                    <a href="/">← Kembali ke Workspace</a>
                </div>
            </body>
            </html>""",
            status_code=404
        )

    return HTMLResponse(
        f"""<!DOCTYPE html>
        <html lang="id">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
            <title>{project.title} - Online Preview | Yudiaz LaTeX Studio</title>
            <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>📄</text></svg>">
            
            <!-- PDF.js Multi-Page Continuous Engine -->
            <script src="/static/vendor/pdf.min.js"></script>
            <script src="/static/pdf-viewer.js?v=1.0.5"></script>
            <link rel="stylesheet" href="/static/style.css?v=1.0.5">

            <style>
                * {{ box-sizing: border-box; margin: 0; padding: 0; }}
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; background: #0b0f19; color: #f1f5f9; height: 100vh; height: 100dvh; display: flex; flex-direction: column; overflow: hidden; }}
                header {{ background: #111827; border-bottom: 1px solid #1f2937; padding: 0.65rem 1.25rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; z-index: 10; flex-shrink: 0; }}
                .brand-badge {{ display: flex; align-items: center; gap: 0.75rem; }}
                .badge-logo {{ width: 28px; height: 28px; background: linear-gradient(135deg, #d4af37, #b45309); border-radius: 6px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; color: #fff; }}
                .brand-title {{ font-size: 0.95rem; font-weight: 600; color: #f8fafc; }}
                .brand-subtitle {{ font-size: 0.72rem; color: #d4af37; letter-spacing: 0.05em; text-transform: uppercase; }}
                .header-actions {{ display: flex; align-items: center; gap: 0.5rem; }}
                .btn {{ background: #1e293b; color: #f1f5f9; border: 1px solid #374151; padding: 0.45rem 0.85rem; border-radius: 0.5rem; font-size: 0.82rem; font-weight: 500; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; gap: 0.35rem; transition: all 0.2s; }}
                .btn:hover {{ background: #374151; border-color: #4b5563; }}
                .btn-gold {{ background: linear-gradient(135deg, #d4af37, #92400e); color: #fff; border: none; font-weight: 600; box-shadow: 0 4px 12px rgba(212, 175, 55, 0.25); }}
                .btn-gold:hover {{ opacity: 0.95; box-shadow: 0 4px 16px rgba(212, 175, 55, 0.4); }}
                .pdf-container {{ flex: 1; width: 100%; height: calc(100vh - 56px); height: calc(100dvh - 56px); background: #182030; position: relative; overflow: hidden; }}
                @media (max-width: 600px) {{
                    header {{ padding: 0.5rem 0.75rem; }}
                    .brand-title {{ font-size: 0.85rem; max-width: 170px; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }}
                    .brand-subtitle {{ display: none; }}
                    .btn {{ padding: 0.4rem 0.65rem; font-size: 0.75rem; }}
                }}
            </style>
        </head>
        <body>
            <header>
                <div class="brand-badge">
                    <div class="badge-logo">Y</div>
                    <div>
                        <div class="brand-title">{project.title}</div>
                        <div class="brand-subtitle">Yudiaz LaTeX Studio &bull; Online Multi-Page Preview</div>
                    </div>
                </div>
                <div class="header-actions">
                    <a href="/api/preview/{share_id}/pdf" target="_blank" class="btn" title="Open Original PDF in New Tab">
                        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>
                        <span>PDF Asli / View</span>
                    </a>
                    <a href="/api/preview/{share_id}/pdf" download="{project.title}.pdf" class="btn btn-gold" title="Download PDF Document">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                        <span>Download PDF</span>
                    </a>
                </div>
            </header>
            <div class="pdf-container" id="preview-pdf-mount"></div>

            <script>
                window.addEventListener("DOMContentLoaded", () => {{
                    const viewer = new ContinuousPdfViewer("preview-pdf-mount");
                    viewer.load("/api/preview/{share_id}/pdf");
                }});
            </script>
        </body>
        </html>"""
    )

# --- Mount Static Frontend ---
STATIC_DIR.mkdir(parents=True, exist_ok=True)
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
@app.head("/")
def serve_index():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        content = index_file.read_text(encoding="utf-8")
        import time
        v_tag = str(int(time.time()))
        # Cache busting replacement
        import re
        content = re.sub(r'app\.js(\?v=[^"]*)?', f'app.js?v={v_tag}', content)
        content = re.sub(r'style\.css(\?v=[^"]*)?', f'style.css?v={v_tag}', content)
        resp = HTMLResponse(content)
        resp.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        resp.headers["Pragma"] = "no-cache"
        resp.headers["Expires"] = "0"
        return resp
    return HTMLResponse("<h1>Yudiaz LaTeX Studio Backend Ready</h1>")

@app.get("/editor/{project_id}", response_class=HTMLResponse)
@app.head("/editor/{project_id}")
def serve_editor(project_id: str):
    return serve_index()
