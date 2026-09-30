// Yudiaz LaTeX Studio - Core Client Application
class LatexStudioApp {
    constructor() {
        this.folders = [];
        this.projects = [];
        this.activeFolderId = null;
        this.currentProject = null;
        this.currentFiles = [];
        this.activeFilePath = "main.tex";
        this.selectedTemplate = "blank";
        this.templates = [];
        
        this.aceEditor = null;
        this.autosaveTimer = null;
        this.isCompiling = false;
        this.searchQuery = "";
        this.mobileEditorTab = "editor";

        this.init();
    }

    async init() {
        this.initEditor();
        await this.loadTemplates();
        await this.loadFolders();
        await this.loadProjects();
        this.renderMobileFolderCarousel();
        this.setupKeyboardShortcuts();
    }

    initEditor() {
        if (!window.ace) {
            console.error("Ace Editor not loaded yet");
            return;
        }
        this.aceEditor = ace.edit("ace-editor");
        this.aceEditor.setTheme("ace/theme/one_dark");
        this.aceEditor.session.setMode("ace/mode/latex");
        this.aceEditor.setOptions({
            fontSize: "14px",
            fontFamily: "Fira Code, monospace",
            tabSize: 2,
            useSoftTabs: true,
            wrap: true,
            showPrintMargin: false,
            highlightActiveLine: true,
            enableBasicAutocompletion: true,
            enableLiveAutocompletion: true
        });

        this.aceEditor.session.on('change', () => {
            if (this.currentProject) {
                this.markUnsaved();
                clearTimeout(this.autosaveTimer);
                this.autosaveTimer = setTimeout(() => {
                    this.saveCurrentFile(true);
                }, 1200);
            }
        });
    }

    setupKeyboardShortcuts() {
        window.addEventListener('keydown', (e) => {
            // Ctrl+S or Cmd+S: Save and compile
            if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === 's') {
                e.preventDefault();
                if (this.currentProject) {
                    this.saveCurrentFile(false).then(() => {
                        this.compileCurrentProject();
                    });
                }
            }
            // Ctrl+Enter or Cmd+Enter: Compile
            if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
                e.preventDefault();
                if (this.currentProject) {
                    this.compileCurrentProject();
                }
            }
        });
    }

    // --- Toast Notifications ---
    toast(message, duration = 3000) {
        const el = document.getElementById("toast");
        el.textContent = message;
        el.classList.add("show");
        setTimeout(() => el.classList.remove("show"), duration);
    }

    markUnsaved() {
        const dot = document.querySelector("#save-status-indicator .dot");
        const txt = document.getElementById("save-status-text");
        if (dot && txt) {
            dot.className = "dot yellow";
            txt.textContent = "Menyimpan...";
        }
    }

    markSaved() {
        const dot = document.querySelector("#save-status-indicator .dot");
        const txt = document.getElementById("save-status-text");
        if (dot && txt) {
            dot.className = "dot green";
            txt.textContent = "Tersimpan";
        }
    }

    // --- API Calls ---
    async loadTemplates() {
        try {
            const res = await fetch("/api/templates");
            this.templates = await res.json();
            this.renderTemplates();
        } catch (e) {
            console.error("Gagal memuat template:", e);
        }
    }

    async loadFolders() {
        try {
            const res = await fetch("/api/folders");
            this.folders = await res.json();
            this.renderFolders();
            this.updateFolderSelects();
        } catch (e) {
            console.error("Gagal memuat folder:", e);
        }
    }

    async loadProjects() {
        try {
            let url = "/api/projects";
            const params = new URLSearchParams();
            if (this.activeFolderId) {
                params.append("folder_id", this.activeFolderId);
            }
            if (this.searchQuery) {
                params.append("search", this.searchQuery);
            }
            if (params.toString()) url += `?${params.toString()}`;

            const res = await fetch(url);
            this.projects = await res.json();
            this.renderProjects();
            this.updateFolderCounts();
        } catch (e) {
            console.error("Gagal memuat proyek:", e);
        }
    }

    // --- Render Dashboard UI ---
    renderFolders() {
        const container = document.getElementById("custom-folders-container");
        container.innerHTML = "";

        // Separate root folders and subfolders
        const rootFolders = this.folders.filter(f => !f.parent_id);
        const subFoldersMap = {};
        this.folders.forEach(f => {
            if (f.parent_id) {
                if (!subFoldersMap[f.parent_id]) subFoldersMap[f.parent_id] = [];
                subFoldersMap[f.parent_id].push(f);
            }
        });

        rootFolders.forEach(folder => {
            const item = this.createFolderTreeElement(folder, false);
            container.appendChild(item);

            // Render children if any
            if (subFoldersMap[folder.id]) {
                subFoldersMap[folder.id].forEach(sub => {
                    const subItem = this.createFolderTreeElement(sub, true);
                    container.appendChild(subItem);
                });
            }
        });
    }

    createFolderTreeElement(folder, isSub) {
        const div = document.createElement("div");
        div.className = `tree-item ${isSub ? 'folder-sub-item' : ''} ${this.activeFolderId === folder.id ? 'active' : ''}`;
        div.id = `folder-tree-${folder.id}`;
        
        const count = this.projects.filter(p => p.folder_id === folder.id).length;

        div.innerHTML = `
            <div class="tree-content">
                <span class="folder-dot" style="background-color: ${folder.color || '#d4af37'}"></span>
                <span class="tree-label">${folder.name}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
                <span class="badge">${count}</span>
                <button class="icon-btn-sm" onclick="event.stopPropagation(); app.deleteFolderPrompt('${folder.id}', '${folder.name}')" title="Hapus Folder">✕</button>
            </div>
        `;
        div.onclick = () => this.selectFolder(folder.id);
        return div;
    }

    updateFolderCounts() {
        const countAll = this.projects.length;
        const countRoot = this.projects.filter(p => !p.folder_id).length;
        const elAll = document.getElementById("count-all");
        const elRoot = document.getElementById("count-root");
        if (elAll) elAll.textContent = countAll;
        if (elRoot) elRoot.textContent = countRoot;
    }

    updateFolderSelects() {
        const projSelect = document.getElementById("new-project-folder");
        const folderParentSelect = document.getElementById("new-folder-parent");
        
        if (projSelect) {
            projSelect.innerHTML = `<option value="">-- Tanpa Folder (Root) --</option>`;
            this.folders.forEach(f => {
                const prefix = f.parent_id ? "— " : "";
                projSelect.innerHTML += `<option value="${f.id}">${prefix}${f.name}</option>`;
            });
        }

        if (folderParentSelect) {
            folderParentSelect.innerHTML = `<option value="">-- Root (Folder Utama) --</option>`;
            this.folders.filter(f => !f.parent_id).forEach(f => {
                folderParentSelect.innerHTML += `<option value="${f.id}">${f.name}</option>`;
            });
        }
    }

    renderTemplates() {
        const container = document.getElementById("template-options-container");
        if (!container) return;
        container.innerHTML = "";

        this.templates.forEach(t => {
            const card = document.createElement("div");
            card.className = `template-card ${this.selectedTemplate === t.id ? 'selected' : ''}`;
            card.innerHTML = `
                <div class="template-name">${t.name}</div>
                <div class="template-desc">${t.description}</div>
            `;
            card.onclick = () => {
                document.querySelectorAll(".template-card").forEach(c => c.classList.remove("selected"));
                card.classList.add("selected");
                this.selectedTemplate = t.id;
            };
            container.appendChild(card);
        });
    }

    renderProjects() {
        const grid = document.getElementById("projects-grid");
        grid.innerHTML = "";

        if (this.projects.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--text-muted);">
                    <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📑</div>
                    <h3>Belum ada dokumen di folder ini</h3>
                    <p style="margin-top: 0.35rem; font-size: 0.85rem;">Klik tombol "Buat Dokumen" untuk memulai draft LaTeX baru.</p>
                </div>
            `;
            return;
        }

        this.projects.forEach(p => {
            const folderObj = this.folders.find(f => f.id === p.folder_id);
            const folderName = folderObj ? folderObj.name : "Root";
            const folderColor = folderObj ? folderObj.color : "#d4af37";

            let statusPillClass = "never";
            let statusText = "Belum Dikompilasi";
            if (p.compile_status === "success") {
                statusPillClass = "success";
                statusText = "Terkonfirmasi (PDF)";
            } else if (p.compile_status === "error") {
                statusPillClass = "error";
                statusText = "Compile Gagal";
            } else if (p.compile_status === "compiling") {
                statusPillClass = "compiling";
                statusText = "Kompilasi...";
            }

            const updatedStr = new Date(p.updated_at * 1000).toLocaleString('id-ID', {
                dateStyle: 'medium',
                timeStyle: 'short'
            });

            const card = document.createElement("div");
            card.className = "project-card";
            card.innerHTML = `
                <div class="card-top">
                    <h3 class="card-title">${this.escapeHtml(p.title)}</h3>
                    <span class="card-folder-tag" style="color: ${folderColor}; background: ${folderColor}22;">
                        ${folderName}
                    </span>
                </div>
                <p class="card-desc">${p.description ? this.escapeHtml(p.description) : "Dokumen kerja LaTeX Yudiaz Studio."}</p>
                <div class="card-meta">
                    <span class="status-pill ${statusPillClass}">
                        ● ${statusText}
                    </span>
                    <span>${updatedStr}</span>
                </div>
                <div class="card-actions" onclick="event.stopPropagation()">
                    <button class="btn btn-primary" style="flex: 1;" onclick="app.openEditor('${p.id}')">
                        Buka Editor
                    </button>
                    <button class="btn btn-icon" onclick="app.showCardShareModal('${p.id}')" title="Link Preview">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
                    </button>
                    <button class="btn btn-icon" onclick="app.downloadProjectPdf('${p.id}')" title="Download PDF">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                    </button>
                    <button class="btn btn-icon" onclick="app.deleteProjectPrompt('${p.id}', '${this.escapeHtml(p.title)}')" title="Hapus">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="3 6 5 6 21 6"/><path d="M19 6v14a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2V6m3 0V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
                    </button>
                </div>
            `;
            card.onclick = () => this.openEditor(p.id);
            grid.appendChild(card);
        });
    }

    selectFolder(folderId) {
        this.activeFolderId = folderId;
        
        document.querySelectorAll(".tree-item").forEach(item => item.classList.remove("active"));
        if (!folderId) {
            document.getElementById("folder-all")?.classList.add("active");
            document.getElementById("active-folder-title").textContent = "Semua Dokumen";
            document.getElementById("active-folder-desc").textContent = "Daftar seluruh dokumen dan draft LaTeX aktif.";
        } else if (folderId === "root") {
            document.getElementById("folder-root")?.classList.add("active");
            document.getElementById("active-folder-title").textContent = "Tanpa Folder (Root)";
            document.getElementById("active-folder-desc").textContent = "Dokumen yang belum dimasukkan ke folder kategori.";
        } else {
            document.getElementById(`folder-tree-${folderId}`)?.classList.add("active");
            const folderObj = this.folders.find(f => f.id === folderId);
            document.getElementById("active-folder-title").textContent = folderObj ? folderObj.name : "Folder";
            document.getElementById("active-folder-desc").textContent = `Koleksi dokumen kategori ${folderObj ? folderObj.name : ''}.`;
        }

        this.toggleMobileDrawer(false);
        this.renderMobileFolderCarousel();
        this.loadProjects();
    }

    onSearchInput(val) {
        this.searchQuery = val.trim();
        this.loadProjects();
    }

    // --- Mobile UX Methods ---
    toggleMobileDrawer(forceState) {
        const sidebar = document.getElementById("folders-sidebar");
        const backdrop = document.getElementById("mobile-drawer-backdrop");
        if (!sidebar || !backdrop) return;
        
        const isOpen = sidebar.classList.contains("drawer-open");
        const shouldOpen = forceState !== undefined ? forceState : !isOpen;
        
        if (shouldOpen) {
            sidebar.classList.add("drawer-open");
            backdrop.classList.add("active");
        } else {
            sidebar.classList.remove("drawer-open");
            backdrop.classList.remove("active");
        }
    }

    setMobileEditorTab(tabName) {
        this.mobileEditorTab = tabName;
        const layout = document.getElementById("editor-view");
        if (!layout) return;

        layout.classList.remove("tab-files", "tab-editor", "tab-preview");
        layout.classList.add(`tab-${tabName}`);

        document.querySelectorAll(".mobile-editor-tabs .tab-btn").forEach(btn => btn.classList.remove("active"));
        const activeBtn = document.getElementById(`tab-btn-${tabName}`);
        if (activeBtn) activeBtn.classList.add("active");

        if (tabName === "editor" && this.aceEditor) {
            setTimeout(() => this.aceEditor.resize(), 100);
        }
    }

    renderMobileFolderCarousel() {
        const bar = document.getElementById("mobile-folder-bar");
        if (!bar) return;
        bar.innerHTML = "";

        const allChip = document.createElement("div");
        allChip.className = `folder-chip ${this.activeFolderId === null ? 'active' : ''}`;
        allChip.innerHTML = `<span>📂 Semua</span> <span class="badge">${this.projects.length}</span>`;
        allChip.onclick = () => this.selectFolder(null);
        bar.appendChild(allChip);

        const rootCount = this.projects.filter(p => !p.folder_id).length;
        const rootChip = document.createElement("div");
        rootChip.className = `folder-chip ${this.activeFolderId === 'root' ? 'active' : ''}`;
        rootChip.innerHTML = `<span>📁 Root</span> <span class="badge">${rootCount}</span>`;
        rootChip.onclick = () => this.selectFolder('root');
        bar.appendChild(rootChip);

        this.folders.forEach(f => {
            const count = this.projects.filter(p => p.folder_id === f.id).length;
            const chip = document.createElement("div");
            chip.className = `folder-chip ${this.activeFolderId === f.id ? 'active' : ''}`;
            chip.innerHTML = `
                <span class="folder-dot" style="background-color: ${f.color || '#d4af37'}"></span>
                <span>${this.escapeHtml(f.name)}</span>
                <span class="badge">${count}</span>
            `;
            chip.onclick = () => this.selectFolder(f.id);
            bar.appendChild(chip);
        });
    }

    // --- Navigation ---
    showDashboard() {
        this.currentProject = null;
        document.getElementById("dashboard-view").style.display = "flex";
        document.getElementById("editor-view").style.display = "none";
        
        const folderBar = document.getElementById("mobile-folder-bar");
        if (folderBar) folderBar.style.display = "";

        document.getElementById("breadcrumb-container").style.display = "none";
        document.getElementById("search-box-wrapper").style.display = "flex";
        document.getElementById("dashboard-nav-actions").style.display = "flex";
        
        document.getElementById("editor-nav-actions").style.display = "none";
        document.getElementById("editor-nav-downloads").style.display = "none";

        this.renderMobileFolderCarousel();
        this.loadProjects();
    }

    async openEditor(projectId) {
        try {
            const res = await fetch(`/api/projects/${projectId}`);
            if (!res.ok) throw new Error("Gagal mengambil data proyek");
            const data = await res.json();
            
            this.currentProject = data.project;
            this.currentFiles = data.files;
            this.activeFilePath = "main.tex";

            // Switch Views
            document.getElementById("dashboard-view").style.display = "none";
            document.getElementById("editor-view").style.display = "flex";
            
            const folderBar = document.getElementById("mobile-folder-bar");
            if (folderBar) folderBar.style.display = "none";

            // Set default mobile tab to editor
            this.setMobileEditorTab("editor");

            // Breadcrumbs
            const folderObj = this.folders.find(f => f.id === this.currentProject.folder_id);
            const folderName = folderObj ? folderObj.name : "Root";
            
            document.getElementById("breadcrumb-container").style.display = "flex";
            document.getElementById("crumb-folder").textContent = folderName;
            document.getElementById("crumb-project").textContent = this.currentProject.title;
            
            document.getElementById("search-box-wrapper").style.display = "none";
            document.getElementById("dashboard-nav-actions").style.display = "none";
            
            document.getElementById("editor-nav-actions").style.display = "flex";
            document.getElementById("editor-nav-downloads").style.display = "flex";

            document.getElementById("active-project-folder-name").textContent = folderName;

            this.renderProjectFiles();
            await this.loadFile(this.activeFilePath);
            this.refreshPdfPreview();
        } catch (e) {
            this.toast("Error membuka proyek: " + e.message);
        }
    }

    // --- Editor & File Handling ---
    renderProjectFiles() {
        const list = document.getElementById("project-files-list");
        list.innerHTML = "";

        this.currentFiles.forEach(file => {
            const item = document.createElement("div");
            item.className = `file-item ${file.path === this.activeFilePath ? 'active' : ''}`;
            item.innerHTML = `
                <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                    ${file.name.endsWith('.tex') ? '📄' : file.name.endsWith('.bib') ? '📚' : '🖼️'} ${file.path}
                </span>
                ${file.path !== 'main.tex' ? `<button class="icon-btn-sm" onclick="event.stopPropagation(); app.deleteFilePrompt('${file.path}')">✕</button>` : ''}
            `;
            item.onclick = () => this.loadFile(file.path);
            list.appendChild(item);
        });
    }

    async loadFile(filePath) {
        if (!this.currentProject) return;
        this.activeFilePath = filePath;
        document.getElementById("active-filename").textContent = filePath;
        document.getElementById("tab-filename").textContent = filePath;
        
        document.querySelectorAll(".file-item").forEach(item => {
            item.classList.toggle("active", item.textContent.includes(filePath));
        });

        try {
            const res = await fetch(`/api/projects/${this.currentProject.id}/files/${filePath}`);
            if (!res.ok) throw new Error("Gagal membaca file");
            const data = await res.json();
            
            if (this.aceEditor) {
                this.aceEditor.setValue(data.content, -1);
                this.markSaved();
            }
        } catch (e) {
            this.toast("Gagal memuat isi file: " + e.message);
        }
    }

    async saveCurrentFile(silent = false) {
        if (!this.currentProject || !this.aceEditor) return;
        const content = this.aceEditor.getValue();
        
        try {
            const res = await fetch(`/api/projects/${this.currentProject.id}/files/${this.activeFilePath}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ content })
            });
            if (!res.ok) throw new Error("Gagal menyimpan ke server");
            this.markSaved();
            if (!silent) this.toast("File berhasil disimpan.");
        } catch (e) {
            this.toast("Error autosave: " + e.message);
        }
    }

    // --- Compilation Engine ---
    async compileCurrentProject() {
        if (!this.currentProject || this.isCompiling) return;
        
        this.isCompiling = true;
        const btn = document.getElementById("btn-compile");
        const btnMobile = document.getElementById("btn-compile-mobile");
        const overlay = document.getElementById("pdf-loading-overlay");
        
        if (btn) {
            btn.disabled = true;
            btn.classList.add("compiling");
            btn.querySelector("span").textContent = "Mengompilasi...";
        }
        if (btnMobile) {
            btnMobile.disabled = true;
            btnMobile.classList.add("compiling");
            btnMobile.querySelector("span").textContent = "Mengompilasi...";
        }
        if (overlay) overlay.style.display = "flex";

        // Save current open file first
        await this.saveCurrentFile(true);

        try {
            const res = await fetch(`/api/projects/${this.currentProject.id}/compile`, {
                method: "POST"
            });
            const result = await res.json();
            
            const badge = document.getElementById("log-status-badge");
            const durText = document.getElementById("compile-duration-text");
            const consoleEl = document.getElementById("log-console");
            const errSummary = document.getElementById("log-errors-summary");

            durText.textContent = `(${result.duration_seconds}s)`;
            consoleEl.textContent = result.log || "Log kompilasi kosong.";

            if (result.success) {
                badge.className = "badge-mini green";
                badge.textContent = "Sukses";
                errSummary.style.display = "none";
                this.toast(`Kompilasi sukses (${result.duration_seconds}s)`);
                this.refreshPdfPreview();
                
                // If on mobile screen, switch to preview tab after short delay so user sees result
                if (window.innerWidth <= 850 && this.mobileEditorTab === 'editor') {
                    setTimeout(() => {
                        this.setMobileEditorTab('preview');
                    }, 400);
                }
            } else {
                badge.className = "badge-mini red";
                badge.textContent = "Error";
                errSummary.style.display = "block";
                
                let errHtml = `<strong>Kompilasi Gagal:</strong><ul>`;
                (result.errors || []).forEach(err => {
                    errHtml += `<li>Baris ${err.line || '?'}: ${this.escapeHtml(err.message)}</li>`;
                });
                errHtml += `</ul>`;
                errSummary.innerHTML = errHtml;

                // Auto open log drawer on failure
                document.getElementById("log-drawer").style.display = "flex";
                this.toast("Kompilasi menghasilkan error. Periksa tab log.");
            }
        } catch (e) {
            this.toast("Error komunikasi kompilasi: " + e.message);
        } finally {
            this.isCompiling = false;
            if (btn) {
                btn.disabled = false;
                btn.classList.remove("compiling");
                btn.querySelector("span").textContent = "Kompilasi (Ctrl+Enter)";
            }
            if (btnMobile) {
                btnMobile.disabled = false;
                btnMobile.classList.remove("compiling");
                btnMobile.querySelector("span").textContent = "Kompilasi PDF";
            }
            if (overlay) overlay.style.display = "none";
        }
    }

    refreshPdfPreview() {
        if (!this.currentProject) return;
        const pdfUrl = `/api/projects/${this.currentProject.id}/pdf?t=${Date.now()}`;
        
        if (!this.pdfViewer) {
            this.pdfViewer = new ContinuousPdfViewer("pdf-viewer-container");
        }
        this.pdfViewer.load(pdfUrl);

        const timeEl = document.getElementById("pdf-updated-time");
        if (timeEl) {
            timeEl.textContent = new Date().toLocaleTimeString('id-ID');
        }
    }

    openPdfInNewTab() {
        if (!this.currentProject) return;
        window.open(`/api/projects/${this.currentProject.id}/pdf`, '_blank');
    }

    jumpToSourceText(searchText) {
        if (!searchText || !this.aceEditor) return;
        const clean = searchText.replace(/[\r\n\t]+/g, ' ').trim();
        if (clean.length < 2) return;

        // Switch to editor tab on mobile if currently in preview tab
        if (window.innerWidth <= 850 && this.mobileEditorTab === 'preview') {
            this.setMobileEditorTab('editor');
        }

        // Try candidate queries: 4 words, 3 words, 2 words, 1 word
        const words = clean.split(/\s+/).filter(w => w.length > 1);
        let found = false;

        const candidates = [];
        if (words.length >= 4) candidates.push(words.slice(0, 4).join(' '));
        if (words.length >= 3) candidates.push(words.slice(0, 3).join(' '));
        if (words.length >= 2) candidates.push(words.slice(0, 2).join(' '));
        if (words.length >= 1) candidates.push(words[0]);

        for (const query of candidates) {
            found = this.aceEditor.find(query, {
                caseSensitive: false,
                wholeWord: false,
                regExp: false,
                wrap: true
            });
            if (found) break;
        }

        if (found) {
            const cursor = this.aceEditor.getCursorPosition();
            this.aceEditor.scrollToLine(cursor.row, true, true, function() {});
            this.toast(`Melompat ke baris ${cursor.row + 1}`);
        } else {
            this.toast(`Teks "${clean.slice(0, 20)}..." tidak ditemukan di file aktif`);
        }
    }

    toggleLogDrawer() {
        const drawer = document.getElementById("log-drawer");
        drawer.style.display = drawer.style.display === "none" ? "flex" : "none";
    }

    // --- Share & Preview Link ---
    openShareModal() {
        if (!this.currentProject) return;
        this.setupShareModalData(this.currentProject);
        document.getElementById("modal-share").style.display = "flex";
    }

    showCardShareModal(projectId) {
        const p = this.projects.find(x => x.id === projectId);
        if (!p) return;
        this.setupShareModalData(p);
        document.getElementById("modal-share").style.display = "flex";
    }

    setupShareModalData(project) {
        const shareInput = document.getElementById("share-link-input");
        const toggle = document.getElementById("share-public-toggle");
        
        const fullUrl = `${window.location.origin}/preview/${project.share_id}`;
        shareInput.value = fullUrl;
        toggle.checked = project.is_public;
        
        // Save target project reference
        this._shareTargetProject = project;
    }

    copyShareLink() {
        const input = document.getElementById("share-link-input");
        input.select();
        navigator.clipboard.writeText(input.value);
        this.toast("Link preview online berhasil disalin!");
    }

    async toggleSharePublic() {
        if (!this._shareTargetProject) return;
        const toggle = document.getElementById("share-public-toggle");
        
        try {
            const res = await fetch(`/api/projects/${this._shareTargetProject.id}/share`, { method: "POST" });
            const data = await res.json();
            this._shareTargetProject.is_public = data.is_public;
            toggle.checked = data.is_public;
            this.toast(data.is_public ? "Akses preview publik aktif." : "Akses preview publik dinonaktifkan.");
        } catch (e) {
            this.toast("Gagal mengubah status share.");
        }
    }

    openSharePreviewTab() {
        const input = document.getElementById("share-link-input");
        if (input && input.value) {
            window.open(input.value, '_blank');
        }
    }

    // --- Modal Handlers ---
    openProjectModal() {
        document.getElementById("new-project-title").value = "";
        document.getElementById("new-project-desc").value = "";
        if (this.activeFolderId && this.activeFolderId !== "root") {
            document.getElementById("new-project-folder").value = this.activeFolderId;
        } else {
            document.getElementById("new-project-folder").value = "";
        }
        document.getElementById("modal-project").style.display = "flex";
    }

    async submitCreateProject() {
        const title = document.getElementById("new-project-title").value.trim();
        const folder_id = document.getElementById("new-project-folder").value || null;
        const description = document.getElementById("new-project-desc").value.trim();

        if (!title) {
            this.toast("Judul dokumen wajib diisi.");
            return;
        }

        try {
            const res = await fetch("/api/projects", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    title,
                    folder_id,
                    description,
                    template: this.selectedTemplate
                })
            });
            if (!res.ok) throw new Error("Gagal membuat dokumen");
            const newProj = await res.json();
            
            this.closeModal("modal-project");
            this.toast(`Dokumen "${title}" berhasil dibuat.`);
            await this.loadProjects();
            this.openEditor(newProj.id);
        } catch (e) {
            this.toast("Error: " + e.message);
        }
    }

    openFolderModal() {
        document.getElementById("new-folder-name").value = "";
        document.getElementById("modal-folder").style.display = "flex";
    }

    async submitCreateFolder() {
        const name = document.getElementById("new-folder-name").value.trim();
        const parent_id = document.getElementById("new-folder-parent").value || null;
        const colorRadio = document.querySelector('input[name="folder-color"]:checked');
        const color = colorRadio ? colorRadio.value : "#d4af37";

        if (!name) {
            this.toast("Nama folder wajib diisi.");
            return;
        }

        try {
            const res = await fetch("/api/folders", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, parent_id, color })
            });
            if (!res.ok) throw new Error("Gagal membuat folder");
            
            this.closeModal("modal-folder");
            this.toast(`Folder "${name}" berhasil dibuat.`);
            await this.loadFolders();
        } catch (e) {
            this.toast("Error: " + e.message);
        }
    }

    async deleteFolderPrompt(folderId, folderName) {
        if (!confirm(`Hapus folder "${folderName}"? Dokumen di dalamnya akan dipindahkan ke Root.`)) return;
        
        try {
            await fetch(`/api/folders/${folderId}`, { method: "DELETE" });
            this.toast(`Folder "${folderName}" dihapus.`);
            if (this.activeFolderId === folderId) this.activeFolderId = null;
            await this.loadFolders();
            await this.loadProjects();
        } catch (e) {
            this.toast("Gagal menghapus folder.");
        }
    }

    async deleteProjectPrompt(projectId, projectTitle) {
        if (!confirm(`Hapus proyek "${projectTitle}" secara permanen?`)) return;
        
        try {
            await fetch(`/api/projects/${projectId}`, { method: "DELETE" });
            this.toast(`Dokumen "${projectTitle}" berhasil dihapus.`);
            await this.loadProjects();
        } catch (e) {
            this.toast("Gagal menghapus proyek.");
        }
    }

    openNewFileModal() {
        document.getElementById("new-file-path").value = "";
        document.getElementById("modal-file").style.display = "flex";
    }

    async submitCreateFile() {
        const path = document.getElementById("new-file-path").value.trim();
        if (!path) return;
        
        try {
            const res = await fetch(`/api/projects/${this.currentProject.id}/files/${path}`, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ content: "% New LaTeX File\n" })
            });
            if (!res.ok) throw new Error("Gagal membuat file");
            
            this.closeModal("modal-file");
            this.toast(`File "${path}" dibuat.`);
            
            // Reload project files
            const pRes = await fetch(`/api/projects/${this.currentProject.id}`);
            const pData = await pRes.json();
            this.currentFiles = pData.files;
            this.renderProjectFiles();
            this.loadFile(path);
        } catch (e) {
            this.toast("Error: " + e.message);
        }
    }

    async deleteFilePrompt(path) {
        if (!confirm(`Hapus file "${path}"?`)) return;
        try {
            await fetch(`/api/projects/${this.currentProject.id}/files/${path}`, { method: "DELETE" });
            this.toast(`File "${path}" dihapus.`);
            
            const pRes = await fetch(`/api/projects/${this.currentProject.id}`);
            const pData = await pRes.json();
            this.currentFiles = pData.files;
            this.renderProjectFiles();
            this.loadFile("main.tex");
        } catch (e) {
            this.toast("Gagal menghapus file.");
        }
    }

    async handleAssetUpload(file) {
        if (!file || !this.currentProject) return;
        const formData = new FormData();
        formData.append("file", file);

        try {
            const res = await fetch(`/api/projects/${this.currentProject.id}/upload`, {
                method: "POST",
                body: formData
            });
            const data = await res.json();
            this.toast(`Asset "${file.name}" berhasil diunggah.`);
            
            const pRes = await fetch(`/api/projects/${this.currentProject.id}`);
            const pData = await pRes.json();
            this.currentFiles = pData.files;
            this.renderProjectFiles();
        } catch (e) {
            this.toast("Gagal mengunggah file asset.");
        }
    }

    downloadCurrentPdf() {
        if (!this.currentProject) return;
        window.location.href = `/api/projects/${this.currentProject.id}/pdf`;
    }

    downloadProjectPdf(projectId) {
        window.location.href = `/api/projects/${projectId}/pdf`;
    }

    downloadCurrentZip() {
        if (!this.currentProject) return;
        window.location.href = `/api/projects/${this.currentProject.id}/export-zip`;
    }

    closeModal(modalId) {
        document.getElementById(modalId).style.display = "none";
    }

    escapeHtml(str) {
        if (!str) return "";
        return str.replace(/[&<>"']/g, function(m) {
            return {
                '&': '&amp;',
                '<': '&lt;',
                '>': '&gt;',
                '"': '&quot;',
                "'": '&#039;'
            }[m];
        });
    }
}

// Instantiate on DOMContentLoaded
window.addEventListener("DOMContentLoaded", () => {
    window.app = new LatexStudioApp();
});
