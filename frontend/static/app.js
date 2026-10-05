// Yudiaz LaTeX Studio - Core Client Application & Localization Engine

const TRANSLATIONS = {
    id: {
        brand_sub: "Executive Cloud Workspace",
        workspace: "Workspace",
        doc_title_default: "Dokumen",
        search_placeholder: "Cari dokumen...",
        save_status_saved: "Tersimpan",
        save_status_saving: "Menyimpan...",
        compile_btn: "Kompilasi (Ctrl+Enter)",
        share: "Share",
        share_tooltip: "Bagikan link preview online",
        lang_switch_tooltip: "Ganti Bahasa / Switch Language",
        new_folder: "Folder Baru",
        new_doc: "Buat Dokumen",
        new_doc_btn: "Dokumen Baru",
        create_prefix: "Buat ",
        download_pdf: "Download PDF",
        download_zip: "Download Source ZIP",
        sidebar_title: "Folder Workspace",
        btn_folder_plus: "+ Folder",
        btn_close: "✕ Tutup",
        all_documents: "Semua Dokumen",
        all_documents_desc: "Daftar seluruh dokumen dan draft LaTeX aktif.",
        root_folder: "Tanpa Folder (Root)",
        root_folder_desc: "Dokumen yang belum dimasukkan ke folder kategori.",
        folder_desc_prefix: "Koleksi dokumen kategori",
        category_header: "KATEGORI & UNIT KERJA",
        empty_folder_title: "Belum ada dokumen di folder ini",
        empty_folder_desc: "Klik tombol \"Buat Dokumen\" untuk memulai draft LaTeX baru.",
        search_empty_title: "Tidak ada dokumen yang cocok",
        search_empty_desc: "Coba gunakan kata kunci pencarian yang lain.",
        status_never: "Belum Dikompilasi",
        status_success: "Terkonfirmasi (PDF)",
        status_error: "Compile Gagal",
        status_compiling: "Kompilasi...",
        badge_ready: "Siap",
        badge_error: "Error",
        badge_success: "Sukses",
        open_editor: "Buka Editor",
        preview_link: "Link Preview",
        delete: "Hapus",
        tab_structure: "Struktur",
        tab_code: "Kode LaTeX",
        tab_preview: "Pratinjau PDF",
        files_title: "Struktur File Proyek",
        btn_new_file: "+ File",
        btn_upload: "Upload",
        btn_upload_title: "Unggah Gambar / Aset",
        info_active_file: "File Aktif:",
        info_folder: "Folder:",
        toggle_log_title: "Lihat Log Kompilasi",
        btn_log: "Log",
        log_title: "Output Log & Diagnostik",
        btn_close_log: "✕ Tutup",
        preview_heading: "Pratinjau PDF Online",
        btn_refresh_pdf: "Segarkan PDF",
        btn_newtab_pdf: "Buka PDF di Tab Baru",
        compiling_overlay: "Mengompilasi dokumen LaTeX...",
        compile_mobile: "Kompilasi PDF",
        modal_project_title: "Buat Dokumen LaTeX Baru",
        label_doc_title: "Judul Dokumen",
        placeholder_doc_title: "Contoh: Proposal Pengembangan Soetahills Q4",
        label_folder: "Folder Penyimpanan (Folderisasi)",
        label_template: "Pilih Template Awal",
        label_desc: "Deskripsi Singkat (Opsional)",
        placeholder_desc: "Catatan atau tujuan dokumen...",
        btn_cancel: "Batal",
        btn_submit_project: "Buat Dokumen",
        modal_folder_title: "Buat Folder Baru",
        label_folder_name: "Nama Folder",
        placeholder_folder_name: "Contoh: Riset Skripsi",
        label_parent_folder: "Parent Folder (Opsional untuk Subfolder)",
        root_parent_option: "-- Root (Folder Utama) --",
        label_color_accent: "Aksen Warna",
        btn_submit_folder: "Simpan Folder",
        modal_share_title: "Pratinjau Online & Share Link",
        modal_share_desc: "Bagikan link ini kepada klien, mitra, atau tim untuk melihat dokumen PDF secara langsung di browser tanpa perlu login.",
        btn_copy: "Salin",
        label_public_access: "Akses Publik Aktif",
        btn_open_tab: "Buka Tab",
        btn_done: "Selesai",
        modal_file_title: "Buat File Baru di Proyek",
        label_file_path: "Nama File (dengan ekstensi .tex, .bib, dsb.)",
        placeholder_file_path: "contoh: sections/metodologi.tex",
        btn_submit_file: "Buat File",
        // Prompts and Toasts
        toast_copied_share: "Link preview online berhasil disalin!",
        toast_share_public_on: "Akses preview publik aktif.",
        toast_share_public_off: "Akses preview publik dinonaktifkan.",
        toast_share_error: "Gagal mengubah status share.",
        toast_file_saved: "File berhasil disimpan.",
        toast_compile_success: "Kompilasi sukses ({dur}s)",
        toast_compile_error: "Kompilasi menghasilkan error. Periksa tab log.",
        toast_compile_comm_error: "Error komunikasi kompilasi: ",
        toast_title_required: "Judul dokumen wajib diisi.",
        toast_doc_created: "Dokumen \"{title}\" berhasil dibuat.",
        toast_folder_name_required: "Nama folder wajib diisi.",
        toast_folder_created: "Folder \"{name}\" berhasil dibuat.",
        toast_folder_deleted: "Folder \"{name}\" dihapus.",
        toast_doc_deleted: "Dokumen \"{title}\" berhasil dihapus.",
        toast_file_created: "File \"{path}\" dibuat.",
        toast_file_deleted: "File \"{path}\" dihapus.",
        toast_asset_uploaded: "Asset \"{name}\" berhasil diunggah.",
        toast_jump_line: "Melompat ke baris {line}",
        toast_text_not_found: "Teks \"{text}...\" tidak ditemukan di file aktif",
        confirm_delete_project: "Hapus proyek \"{title}\" secara permanen?",
        confirm_delete_folder: "Hapus folder \"{name}\"? Dokumen di dalamnya akan dipindahkan ke Root.",
        confirm_delete_file: "Hapus file \"{path}\"?",
        default_doc_desc: "Dokumen kerja LaTeX Yudiaz Studio.",
        compile_log_empty: "Log kompilasi kosong."
    },
    en: {
        brand_sub: "Executive Cloud Workspace",
        workspace: "Workspace",
        doc_title_default: "Document",
        search_placeholder: "Search documents...",
        save_status_saved: "Saved",
        save_status_saving: "Saving...",
        compile_btn: "Compile (Ctrl+Enter)",
        share: "Share",
        share_tooltip: "Share live preview link online",
        lang_switch_tooltip: "Switch Language / Ganti Bahasa",
        new_folder: "New Folder",
        new_doc: "New Document",
        new_doc_btn: "New Document",
        create_prefix: "New ",
        download_pdf: "Download PDF",
        download_zip: "Download Source ZIP",
        sidebar_title: "Workspace Folders",
        btn_folder_plus: "+ Folder",
        btn_close: "✕ Close",
        all_documents: "All Documents",
        all_documents_desc: "List of all active LaTeX documents and drafts.",
        root_folder: "Uncategorized (Root)",
        root_folder_desc: "Documents not assigned to any category folder.",
        folder_desc_prefix: "Collection of documents in category",
        category_header: "CATEGORIES & TEAMS",
        empty_folder_title: "No documents in this folder yet",
        empty_folder_desc: "Click \"New Document\" button to start a new LaTeX draft.",
        search_empty_title: "No matching documents found",
        search_empty_desc: "Try searching with different keywords.",
        status_never: "Not Compiled",
        status_success: "Compiled (PDF)",
        status_error: "Compile Error",
        status_compiling: "Compiling...",
        badge_ready: "Ready",
        badge_error: "Error",
        badge_success: "Success",
        open_editor: "Open Editor",
        preview_link: "Preview Link",
        delete: "Delete",
        tab_structure: "Files",
        tab_code: "LaTeX Code",
        tab_preview: "PDF Preview",
        files_title: "Project Files",
        btn_new_file: "+ File",
        btn_upload: "Upload",
        btn_upload_title: "Upload Images or Assets",
        info_active_file: "Active File:",
        info_folder: "Folder:",
        toggle_log_title: "View Compilation Logs",
        btn_log: "Log",
        log_title: "Log Output & Diagnostics",
        btn_close_log: "✕ Close",
        preview_heading: "Live PDF Preview",
        btn_refresh_pdf: "Refresh PDF",
        btn_newtab_pdf: "Open PDF in New Tab",
        compiling_overlay: "Compiling LaTeX document...",
        compile_mobile: "Compile PDF",
        modal_project_title: "Create New LaTeX Document",
        label_doc_title: "Document Title",
        placeholder_doc_title: "e.g. Soetahills Development Proposal Q4",
        label_folder: "Target Folder",
        label_template: "Select Starter Template",
        label_desc: "Short Description (Optional)",
        placeholder_desc: "Notes or purpose of the document...",
        btn_cancel: "Cancel",
        btn_submit_project: "Create Document",
        modal_folder_title: "Create New Folder",
        label_folder_name: "Folder Name",
        placeholder_folder_name: "e.g. Thesis Research",
        label_parent_folder: "Parent Folder (Optional for Subfolder)",
        root_parent_option: "-- Root (Top Level) --",
        label_color_accent: "Color Accent",
        btn_submit_folder: "Save Folder",
        modal_share_title: "Online Preview & Share Link",
        modal_share_desc: "Share this link with clients, partners, or team members to view the PDF directly in browser without login.",
        btn_copy: "Copy Link",
        label_public_access: "Public Access Enabled",
        btn_open_tab: "Open Tab",
        btn_done: "Done",
        modal_file_title: "Create New File in Project",
        label_file_path: "File Name (with .tex, .bib extension, etc.)",
        placeholder_file_path: "e.g. sections/methodology.tex",
        btn_submit_file: "Create File",
        // Prompts and Toasts
        toast_copied_share: "Online preview link copied successfully!",
        toast_share_public_on: "Public preview access enabled.",
        toast_share_public_off: "Public preview access disabled.",
        toast_share_error: "Failed to update share status.",
        toast_file_saved: "File saved successfully.",
        toast_compile_success: "Compilation successful ({dur}s)",
        toast_compile_error: "Compilation produced errors. Check log tab.",
        toast_compile_comm_error: "Compilation communication error: ",
        toast_title_required: "Document title is required.",
        toast_doc_created: "Document \"{title}\" created successfully.",
        toast_folder_name_required: "Folder name is required.",
        toast_folder_created: "Folder \"{name}\" created successfully.",
        toast_folder_deleted: "Folder \"{name}\" deleted.",
        toast_doc_deleted: "Document \"{title}\" deleted successfully.",
        toast_file_created: "File \"{path}\" created.",
        toast_file_deleted: "File \"{path}\" deleted.",
        toast_asset_uploaded: "Asset \"{name}\" uploaded successfully.",
        toast_jump_line: "Jumped to line {line}",
        toast_text_not_found: "Text \"{text}...\" not found in active file",
        confirm_delete_project: "Permanently delete project \"{title}\"?",
        confirm_delete_folder: "Delete folder \"{name}\"? Documents inside will be moved to Root.",
        confirm_delete_file: "Delete file \"{path}\"?",
        default_doc_desc: "Yudiaz Studio LaTeX working document.",
        compile_log_empty: "Compilation log is empty."
    }
};

const TEMPLATE_TRANSLATIONS = {
    en: {
        blank: { name: "Blank Document", description: "Minimal clean LaTeX starter document" },
        surat_undangan: { name: "Official Invitation Letter", description: "Formal institutional letter with official header, letterhead, reference numbers, and signatures" },
        justifikasi_anggaran: { name: "Budget Justification & Urgency", description: "Procurement urgency document with cost breakdown, technical justification, and risk assessment" },
        proposal_kegiatan: { name: "Activity & Event Proposal", description: "Complete event proposal template with executive summary, committee structure, and detailed budget (RAB)" },
        lpj_kegiatan: { name: "Activity Accountability Report (LPJ)", description: "Post-event accountability report with division evaluation, realization vs budget comparison, and documentation" },
        proposal: { name: "Executive Project Proposal", description: "Professional project proposal with timeline, milestones, deliverable tables, and budget breakdown" },
        paper: { name: "Academic Research Paper", description: "Standard IEEE / ACM style research manuscript with abstract, equations, and bibliography" },
        skripsi: { name: "Undergraduate Thesis / Final Project", description: "Academic thesis template with cover, signature sheet, preface, and chapters" },
        camtech_progress_report: { name: "CamTech Virtubis Progress Report", description: "Official Virtubis Internship Programme end-of-term progress report with CamTech headers, banners, and evaluation tables" }
    }
};

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
        
        // Language state
        this.currentLang = localStorage.getItem("yudiaz_latex_lang") || "id";

        this.init();
    }

    async init() {
        this.initEditor();
        this.applyLanguage(this.currentLang, false);
        await this.loadTemplates();
        await this.loadFolders();
        await this.loadProjects();
        this.renderMobileFolderCarousel();
        this.setupKeyboardShortcuts();
    }

    t(key, params = {}) {
        const langDict = TRANSLATIONS[this.currentLang] || TRANSLATIONS.id;
        let str = langDict[key] || TRANSLATIONS.id[key] || key;
        for (const [k, v] of Object.entries(params)) {
            str = str.replace(new RegExp(`\\{${k}\\}`, "g"), v);
        }
        return str;
    }

    setLanguage(lang) {
        if (lang !== "id" && lang !== "en") return;
        this.currentLang = lang;
        localStorage.setItem("yudiaz_latex_lang", lang);
        this.applyLanguage(lang, true);
    }

    applyLanguage(lang, triggerRender = true) {
        document.documentElement.lang = lang;

        // Switcher button visual state
        const btnId = document.getElementById("btn-lang-id");
        const btnEn = document.getElementById("btn-lang-en");
        if (btnId && btnEn) {
            btnId.classList.toggle("active", lang === "id");
            btnEn.classList.toggle("active", lang === "en");
        }

        // Update all elements with data-i18n
        document.querySelectorAll("[data-i18n]").forEach(el => {
            const key = el.getAttribute("data-i18n");
            el.innerHTML = this.t(key);
        });

        // Update placeholders
        document.querySelectorAll("[data-i18n-placeholder]").forEach(el => {
            const key = el.getAttribute("data-i18n-placeholder");
            el.placeholder = this.t(key);
        });

        // Update titles / tooltips
        document.querySelectorAll("[data-i18n-title]").forEach(el => {
            const key = el.getAttribute("data-i18n-title");
            el.title = this.t(key);
        });

        // Update aria-labels
        document.querySelectorAll("[data-i18n-aria]").forEach(el => {
            const key = el.getAttribute("data-i18n-aria");
            el.setAttribute("aria-label", this.t(key));
        });

        if (triggerRender) {
            this.updateFolderSelects();
            this.renderFolders();
            this.renderProjects();
            this.renderTemplates();
            this.renderMobileFolderCarousel();
            this.updateHeaderDynamicLabels();
        }
    }

    updateHeaderDynamicLabels() {
        const titleEl = document.getElementById("active-folder-title");
        const descEl = document.getElementById("active-folder-desc");
        if (!this.activeFolderId) {
            if (titleEl) titleEl.textContent = this.t("all_documents");
            if (descEl) descEl.textContent = this.t("all_documents_desc");
        } else if (this.activeFolderId === "root") {
            if (titleEl) titleEl.textContent = this.t("root_folder");
            if (descEl) descEl.textContent = this.t("root_folder_desc");
        } else {
            const folderObj = this.folders.find(f => f.id === this.activeFolderId);
            if (titleEl) titleEl.textContent = folderObj ? folderObj.name : "Folder";
            if (descEl) descEl.textContent = `${this.t("folder_desc_prefix")} ${folderObj ? folderObj.name : ''}.`;
        }

        // If in editor view, refresh breadcrumb labels
        if (this.currentProject) {
            const folderObj = this.folders.find(f => f.id === this.currentProject.folder_id);
            const folderName = folderObj ? folderObj.name : "Root";
            const crumbFolder = document.getElementById("crumb-folder");
            if (crumbFolder) crumbFolder.textContent = folderName;
            const folderInfoVal = document.getElementById("active-project-folder-name");
            if (folderInfoVal) folderInfoVal.textContent = folderName;
        }
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
        if (!el) return;
        el.textContent = message;
        el.classList.add("show");
        setTimeout(() => el.classList.remove("show"), duration);
    }

    markUnsaved() {
        const dot = document.querySelector("#save-status-indicator .dot");
        const txt = document.getElementById("save-status-text");
        if (dot && txt) {
            dot.className = "dot yellow";
            txt.textContent = this.t("save_status_saving");
        }
    }

    markSaved() {
        const dot = document.querySelector("#save-status-indicator .dot");
        const txt = document.getElementById("save-status-text");
        if (dot && txt) {
            dot.className = "dot green";
            txt.textContent = this.t("save_status_saved");
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
        if (!container) return;
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
                <span class="tree-label">${this.escapeHtml(folder.name)}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.4rem;">
                <span class="badge">${count}</span>
                <button class="icon-btn-sm" onclick="event.stopPropagation(); app.deleteFolderPrompt('${folder.id}', '${this.escapeHtml(folder.name)}')" title="${this.t('delete')}">✕</button>
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
            projSelect.innerHTML = `<option value="">${this.t('root_parent_option')}</option>`;
            this.folders.forEach(f => {
                const prefix = f.parent_id ? "— " : "";
                projSelect.innerHTML += `<option value="${f.id}">${prefix}${this.escapeHtml(f.name)}</option>`;
            });
        }

        if (folderParentSelect) {
            folderParentSelect.innerHTML = `<option value="">${this.t('root_parent_option')}</option>`;
            this.folders.filter(f => !f.parent_id).forEach(f => {
                folderParentSelect.innerHTML += `<option value="${f.id}">${this.escapeHtml(f.name)}</option>`;
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

            // Check if English translation is available
            let tName = t.name;
            let tDesc = t.description;
            if (this.currentLang === "en" && TEMPLATE_TRANSLATIONS.en[t.id]) {
                tName = TEMPLATE_TRANSLATIONS.en[t.id].name;
                tDesc = TEMPLATE_TRANSLATIONS.en[t.id].description;
            }

            card.innerHTML = `
                <div class="template-name">${this.escapeHtml(tName)}</div>
                <div class="template-desc">${this.escapeHtml(tDesc)}</div>
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
        if (!grid) return;
        grid.innerHTML = "";

        if (this.projects.length === 0) {
            grid.innerHTML = `
                <div style="grid-column: 1 / -1; text-align: center; padding: 4rem 1rem; color: var(--text-muted);">
                    <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📑</div>
                    <h3>${this.t("empty_folder_title")}</h3>
                    <p style="margin-top: 0.35rem; font-size: 0.85rem;">${this.t("empty_folder_desc")}</p>
                </div>
            `;
            return;
        }

        this.projects.forEach(p => {
            const folderObj = this.folders.find(f => f.id === p.folder_id);
            const folderName = folderObj ? folderObj.name : "Root";
            const folderColor = folderObj ? folderObj.color : "#d4af37";

            let statusPillClass = "never";
            let statusText = this.t("status_never");
            if (p.compile_status === "success") {
                statusPillClass = "success";
                statusText = this.t("status_success");
            } else if (p.compile_status === "error") {
                statusPillClass = "error";
                statusText = this.t("status_error");
            } else if (p.compile_status === "compiling") {
                statusPillClass = "compiling";
                statusText = this.t("status_compiling");
            }

            const locale = this.currentLang === "en" ? "en-US" : "id-ID";
            const updatedStr = new Date(p.updated_at * 1000).toLocaleString(locale, {
                dateStyle: 'medium',
                timeStyle: 'short'
            });

            const card = document.createElement("div");
            card.className = "project-card";
            card.innerHTML = `
                <div class="card-top">
                    <h3 class="card-title">${this.escapeHtml(p.title)}</h3>
                    <span class="card-folder-tag" style="color: ${folderColor}; background: ${folderColor}22;">
                        ${this.escapeHtml(folderName)}
                    </span>
                </div>
                <p class="card-desc">${p.description ? this.escapeHtml(p.description) : this.t("default_doc_desc")}</p>
                <div class="card-meta">
                    <span class="status-pill ${statusPillClass}">
                        ● ${statusText}
                    </span>
                    <span>${updatedStr}</span>
                </div>
                <div class="card-actions" onclick="event.stopPropagation()">
                    <button class="btn btn-primary" style="flex: 1;" onclick="app.openEditor('${p.id}')">
                        ${this.t("open_editor")}
                    </button>
                    <button class="btn btn-icon" onclick="app.showCardShareModal('${p.id}')" title="${this.t("preview_link")}">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><line x1="8.59" y1="13.51" x2="15.42" y2="17.49"/><line x1="15.41" y1="6.51" x2="8.59" y2="10.49"/></svg>
                    </button>
                    <button class="btn btn-icon" onclick="app.downloadProjectPdf('${p.id}')" title="${this.t("download_pdf")}">
                        <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>
                    </button>
                    <button class="btn btn-icon" onclick="app.deleteProjectPrompt('${p.id}', '${this.escapeHtml(p.title)}')" title="${this.t("delete")}">
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
            document.getElementById("active-folder-title").textContent = this.t("all_documents");
            document.getElementById("active-folder-desc").textContent = this.t("all_documents_desc");
        } else if (folderId === "root") {
            document.getElementById("folder-root")?.classList.add("active");
            document.getElementById("active-folder-title").textContent = this.t("root_folder");
            document.getElementById("active-folder-desc").textContent = this.t("root_folder_desc");
        } else {
            document.getElementById(`folder-tree-${folderId}`)?.classList.add("active");
            const folderObj = this.folders.find(f => f.id === folderId);
            document.getElementById("active-folder-title").textContent = folderObj ? folderObj.name : "Folder";
            document.getElementById("active-folder-desc").textContent = `${this.t("folder_desc_prefix")} ${folderObj ? folderObj.name : ''}.`;
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
        allChip.innerHTML = `<span>📂 ${this.t("all_documents")}</span> <span class="badge">${this.projects.length}</span>`;
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
            this.toast("Error: " + e.message);
        }
    }

    // --- Editor & File Handling ---
    renderProjectFiles() {
        const list = document.getElementById("project-files-list");
        if (!list) return;
        list.innerHTML = "";

        this.currentFiles.forEach(file => {
            const item = document.createElement("div");
            item.className = `file-item ${file.path === this.activeFilePath ? 'active' : ''}`;
            item.innerHTML = `
                <span style="overflow: hidden; text-overflow: ellipsis; white-space: nowrap;">
                    ${file.name.endsWith('.tex') ? '📄' : file.name.endsWith('.bib') ? '📚' : '🖼️'} ${this.escapeHtml(file.path)}
                </span>
                ${file.path !== 'main.tex' ? `<button class="icon-btn-sm" onclick="event.stopPropagation(); app.deleteFilePrompt('${file.path}')" title="${this.t('delete')}">✕</button>` : ''}
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
            if (!silent) this.toast(this.t("toast_file_saved"));
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
            btn.querySelector("span").textContent = this.t("compiling");
        }
        if (btnMobile) {
            btnMobile.disabled = true;
            btnMobile.classList.add("compiling");
            btnMobile.querySelector("span").textContent = this.t("compiling");
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
            consoleEl.textContent = result.log || this.t("compile_log_empty");

            if (result.success) {
                badge.className = "badge-mini green";
                badge.textContent = this.t("badge_success");
                errSummary.style.display = "none";
                this.toast(this.t("toast_compile_success", { dur: result.duration_seconds }));
                this.refreshPdfPreview();
                
                // If on mobile screen, switch to preview tab after short delay so user sees result
                if (window.innerWidth <= 850 && this.mobileEditorTab === 'editor') {
                    setTimeout(() => {
                        this.setMobileEditorTab('preview');
                    }, 400);
                }
            } else {
                badge.className = "badge-mini red";
                badge.textContent = this.t("badge_error");
                errSummary.style.display = "block";
                
                let errHtml = `<strong>${this.t("status_error")}:</strong><ul>`;
                (result.errors || []).forEach(err => {
                    errHtml += `<li>Baris ${err.line || '?'}: ${this.escapeHtml(err.message)}</li>`;
                });
                errHtml += `</ul>`;
                errSummary.innerHTML = errHtml;

                // Auto open log drawer on failure
                document.getElementById("log-drawer").style.display = "flex";
                this.toast(this.t("toast_compile_error"));
            }
        } catch (e) {
            this.toast(this.t("toast_compile_comm_error") + e.message);
        } finally {
            this.isCompiling = false;
            if (btn) {
                btn.disabled = false;
                btn.classList.remove("compiling");
                btn.querySelector("span").textContent = this.t("compile_btn");
            }
            if (btnMobile) {
                btnMobile.disabled = false;
                btnMobile.classList.remove("compiling");
                btnMobile.querySelector("span").textContent = this.t("compile_mobile");
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
            const locale = this.currentLang === "en" ? "en-US" : "id-ID";
            timeEl.textContent = new Date().toLocaleTimeString(locale);
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
            this.toast(this.t("toast_jump_line", { line: cursor.row + 1 }));
        } else {
            this.toast(this.t("toast_text_not_found", { text: clean.slice(0, 20) }));
        }
    }

    toggleLogDrawer() {
        const drawer = document.getElementById("log-drawer");
        if (!drawer) return;
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
        if (!input) return;
        input.select();
        navigator.clipboard.writeText(input.value);
        this.toast(this.t("toast_copied_share"));
    }

    async toggleSharePublic() {
        if (!this._shareTargetProject) return;
        const toggle = document.getElementById("share-public-toggle");
        
        try {
            const res = await fetch(`/api/projects/${this._shareTargetProject.id}/share`, { method: "POST" });
            const data = await res.json();
            this._shareTargetProject.is_public = data.is_public;
            toggle.checked = data.is_public;
            this.toast(data.is_public ? this.t("toast_share_public_on") : this.t("toast_share_public_off"));
        } catch (e) {
            this.toast(this.t("toast_share_error"));
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
            this.toast(this.t("toast_title_required"));
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
            this.toast(this.t("toast_doc_created", { title }));
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
            this.toast(this.t("toast_folder_name_required"));
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
            this.toast(this.t("toast_folder_created", { name }));
            await this.loadFolders();
        } catch (e) {
            this.toast("Error: " + e.message);
        }
    }

    async deleteFolderPrompt(folderId, folderName) {
        if (!confirm(this.t("confirm_delete_folder", { name: folderName }))) return;
        
        try {
            await fetch(`/api/folders/${folderId}`, { method: "DELETE" });
            this.toast(this.t("toast_folder_deleted", { name: folderName }));
            if (this.activeFolderId === folderId) this.activeFolderId = null;
            await this.loadFolders();
            await this.loadProjects();
        } catch (e) {
            this.toast("Gagal menghapus folder.");
        }
    }

    async deleteProjectPrompt(projectId, projectTitle) {
        if (!confirm(this.t("confirm_delete_project", { title: projectTitle }))) return;
        
        try {
            await fetch(`/api/projects/${projectId}`, { method: "DELETE" });
            this.toast(this.t("toast_doc_deleted", { title: projectTitle }));
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
            this.toast(this.t("toast_file_created", { path }));
            
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
        if (!confirm(this.t("confirm_delete_file", { path }))) return;
        try {
            await fetch(`/api/projects/${this.currentProject.id}/files/${path}`, { method: "DELETE" });
            this.toast(this.t("toast_file_deleted", { path }));
            
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
            if (!res.ok) throw new Error("Gagal upload");
            this.toast(this.t("toast_asset_uploaded", { name: file.name }));
            
            const pRes = await fetch(`/api/projects/${this.currentProject.id}`);
            const pData = await pRes.json();
            this.currentFiles = pData.files;
            this.renderProjectFiles();
        } catch (e) {
            this.toast("Gagal mengunggah file asset: " + e.message);
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
