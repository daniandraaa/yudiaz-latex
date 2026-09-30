from __future__ import annotations
import os
import re
import time
import subprocess
from pathlib import Path
from typing import Dict, Any, List
from .models import CompileResult

class LatexCompiler:
    def __init__(self, timeout_seconds: int = 45):
        self.timeout_seconds = timeout_seconds

    def compile(self, project_dir: Path, main_file: str = "main.tex") -> CompileResult:
        start_time = time.time()
        build_dir = project_dir / "build"
        build_dir.mkdir(parents=True, exist_ok=True)
        
        main_path = project_dir / main_file
        if not main_path.exists():
            return CompileResult(
                success=False,
                status="error",
                log=f"File utama '{main_file}' tidak ditemukan dalam proyek.",
                duration_seconds=0.0,
                errors=[{"file": main_file, "line": 0, "message": f"File '{main_file}' tidak ditemukan."}]
            )

        # Command using latexmk with security guardrails:
        # -no-shell-escape disables dangerous system calls
        # -interaction=nonstopmode prevents hanging on errors
        # -halt-on-error stops on fatal errors
        # -outdir=build isolates auxiliary and output files
        cmd = [
            "latexmk",
            "-pdf",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-no-shell-escape",
            "-outdir=build",
            main_file
        ]

        try:
            process = subprocess.run(
                cmd,
                cwd=str(project_dir),
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                timeout=self.timeout_seconds
            )
            raw_log = process.stdout or ""
            return_code = process.returncode
        except subprocess.TimeoutExpired as e:
            raw_log = (e.stdout or "") + f"\n\n[TIMEOUT] Proses kompilasi melebihi batas waktu ({self.timeout_seconds} detik)."
            return CompileResult(
                success=False,
                status="timeout",
                log=raw_log,
                duration_seconds=round(time.time() - start_time, 2),
                errors=[{"file": main_file, "line": 0, "message": "Proses kompilasi melebihi batas waktu."}]
            )
        except Exception as e:
            return CompileResult(
                success=False,
                status="error",
                log=str(e),
                duration_seconds=round(time.time() - start_time, 2),
                errors=[{"file": main_file, "line": 0, "message": str(e)}]
            )

        duration = round(time.time() - start_time, 2)
        pdf_file = build_dir / f"{Path(main_file).stem}.pdf"
        
        # Parse logs for errors and warnings
        errors, warnings = self._parse_log(raw_log)

        if return_code == 0 and pdf_file.exists():
            return CompileResult(
                success=True,
                status="success",
                log=raw_log,
                pdf_url=f"build/{pdf_file.name}",
                duration_seconds=duration,
                errors=errors,
                warnings=warnings
            )
        else:
            return CompileResult(
                success=False,
                status="error",
                log=raw_log,
                pdf_url=f"build/{pdf_file.name}" if pdf_file.exists() else None,
                duration_seconds=duration,
                errors=errors if errors else [{"file": main_file, "line": 0, "message": "Kompilasi LaTeX gagal. Periksa log detail."}],
                warnings=warnings
            )

    def _parse_log(self, log_text: str) -> tuple[List[Dict[str, Any]], List[str]]:
        errors = []
        warnings = []
        lines = log_text.splitlines()
        
        i = 0
        while i < len(lines):
            line = lines[i]
            # Match error starting with '!'
            if line.startswith("!"):
                msg = line[1:].strip()
                err_line = 0
                err_file = "main.tex"
                
                # Look ahead for l.XX (line number)
                for j in range(i + 1, min(i + 8, len(lines))):
                    l_match = re.search(r"l\.(\d+)", lines[j])
                    if l_match:
                        err_line = int(l_match.group(1))
                        break
                errors.append({
                    "message": msg,
                    "line": err_line,
                    "file": err_file
                })
            elif "LaTeX Warning:" in line:
                warnings.append(line.strip())
            i += 1
            
        return errors, warnings
