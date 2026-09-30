from __future__ import annotations
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
import time
import uuid

class Folder(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    name: str
    parent_id: Optional[str] = None
    created_at: float = Field(default_factory=time.time)
    color: Optional[str] = "#d4af37"

class FolderCreate(BaseModel):
    name: str
    parent_id: Optional[str] = None
    color: Optional[str] = "#d4af37"

class FolderUpdate(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[str] = None
    color: Optional[str] = None

class ProjectMetadata(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4())[:8])
    title: str
    description: Optional[str] = ""
    folder_id: Optional[str] = None
    created_at: float = Field(default_factory=time.time)
    updated_at: float = Field(default_factory=time.time)
    last_compiled_at: Optional[float] = None
    compile_status: str = "never"  # never, compiling, success, error
    share_id: str = Field(default_factory=lambda: str(uuid.uuid4())[:12])
    is_public: bool = True
    main_file: str = "main.tex"

class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = ""
    folder_id: Optional[str] = None
    template: Optional[str] = "blank"  # blank, proposal, paper, skripsi, report

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    folder_id: Optional[str] = None
    is_public: Optional[bool] = None

class FileItem(BaseModel):
    name: str
    path: str
    is_dir: bool = False
    size: int = 0
    updated_at: float = 0

class FileWriteRequest(BaseModel):
    content: str

class CompileResult(BaseModel):
    success: bool
    status: str
    log: str
    pdf_url: Optional[str] = None
    duration_seconds: float = 0.0
    errors: List[Dict[str, Any]] = []
    warnings: List[str] = []
