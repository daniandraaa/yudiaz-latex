// Yudiaz LaTeX Studio - Continuous Mobile-Ready Multi-Page PDF Viewer with TextLayer & Reverse-Sync
if (window.pdfjsLib) {
    pdfjsLib.GlobalWorkerOptions.workerSrc = '/static/vendor/pdf.worker.min.js';
}

class ContinuousPdfViewer {
    constructor(containerId, options = {}) {
        this.container = document.getElementById(containerId);
        this.options = Object.assign({
            defaultScale: 1.0,
            onPageChange: null,
            onLoaded: null,
            onError: null,
            onTextDblClick: null
        }, options);

        this.pdfDoc = null;
        this.currentScale = this.options.defaultScale;
        this.currentPage = 1;
        this.isLoading = false;
        this.currentUrl = null;
        this.observer = null;

        this.initDOM();
    }

    initDOM() {
        if (!this.container) return;
        this.container.innerHTML = `
            <div class="pdf-viewer-root">
                <div class="pdf-controls-bar">
                    <div class="pdf-controls-left">
                        <button class="pdf-btn" id="${this.container.id}-btn-prev" title="Halaman Sebelumnya">▲</button>
                        <span class="pdf-page-indicator">
                            <span id="${this.container.id}-page-current">1</span> / <span id="${this.container.id}-page-total">1</span>
                        </span>
                        <button class="pdf-btn" id="${this.container.id}-btn-next" title="Halaman Berikutnya">▼</button>
                    </div>
                    <div class="pdf-controls-center">
                        <button class="pdf-btn" id="${this.container.id}-btn-zoom-out" title="Perkecil">−</button>
                        <span class="pdf-zoom-level" id="${this.container.id}-zoom-level">100%</span>
                        <button class="pdf-btn" id="${this.container.id}-btn-zoom-in" title="Perbesar">+</button>
                        <button class="pdf-btn" id="${this.container.id}-btn-fit-width" title="Sesuaikan Lebar Layar">Fit</button>
                    </div>
                    <div class="pdf-controls-right">
                        <button class="pdf-btn pdf-btn-action" id="${this.container.id}-btn-open" title="Buka PDF Asli di Tab Baru">↗ PDF Asli</button>
                    </div>
                </div>
                <div class="pdf-scroll-container" id="${this.container.id}-scroll">
                    <div class="pdf-loading-spinner" id="${this.container.id}-loader">
                        <div class="spinner"></div>
                        <span id="${this.container.id}-loader-text">Memuat dokumen PDF...</span>
                    </div>
                    <div class="pdf-pages-wrapper" id="${this.container.id}-pages"></div>
                </div>
            </div>
        `;

        document.getElementById(`${this.container.id}-btn-prev`)?.addEventListener('click', () => this.goToPage(this.currentPage - 1));
        document.getElementById(`${this.container.id}-btn-next`)?.addEventListener('click', () => this.goToPage(this.currentPage + 1));
        document.getElementById(`${this.container.id}-btn-zoom-in`)?.addEventListener('click', () => this.zoom(0.15));
        document.getElementById(`${this.container.id}-btn-zoom-out`)?.addEventListener('click', () => this.zoom(-0.15));
        document.getElementById(`${this.container.id}-btn-fit-width`)?.addEventListener('click', () => this.fitToWidth());
        document.getElementById(`${this.container.id}-btn-open`)?.addEventListener('click', () => {
            if (this.currentUrl) window.open(this.currentUrl, '_blank');
        });

        const scrollEl = document.getElementById(`${this.container.id}-scroll`);
        this.observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const pageNum = parseInt(entry.target.getAttribute('data-page-num'), 10);
                    if (pageNum) {
                        this.currentPage = pageNum;
                        this.updatePageIndicator();
                    }
                }
            });
        }, {
            root: scrollEl,
            threshold: 0.3
        });
    }

    async load(url) {
        if (!url) return;
        this.currentUrl = url;
        this.isLoading = true;

        const loader = document.getElementById(`${this.container.id}-loader`);
        const pagesWrapper = document.getElementById(`${this.container.id}-pages`);
        if (loader) loader.style.display = 'flex';
        if (pagesWrapper) pagesWrapper.innerHTML = '';

        try {
            const loadingTask = pdfjsLib.getDocument({
                url: url,
                cMapUrl: 'https://cdnjs.cloudflare.com/ajax/libs/pdf.js/3.11.174/cmaps/',
                cMapPacked: true
            });

            this.pdfDoc = await loadingTask.promise;
            const totalPages = this.pdfDoc.numPages;

            document.getElementById(`${this.container.id}-page-total`).textContent = totalPages;
            document.getElementById(`${this.container.id}-page-current`).textContent = 1;
            this.currentPage = 1;

            await this.calculateOptimalScale();
            await this.renderAllPages();

            if (loader) loader.style.display = 'none';
            this.isLoading = false;

            if (this.options.onLoaded) {
                this.options.onLoaded(this.pdfDoc);
            }
        } catch (err) {
            console.error("PDF load error:", err);
            if (loader) {
                loader.innerHTML = `
                    <div style="color: #ef4444; text-align: center; padding: 1rem;">
                        <p style="font-weight: 600; margin-bottom: 0.5rem;">Gagal memuat pratinjau PDF</p>
                        <p style="font-size: 0.8rem; color: #94a3b8;">${err.message || 'Dokumen belum berhasil dikompilasi.'}</p>
                    </div>
                `;
            }
            this.isLoading = false;
            if (this.options.onError) {
                this.options.onError(err);
            }
        }
    }

    async calculateOptimalScale() {
        if (!this.pdfDoc) return;
        try {
            const firstPage = await this.pdfDoc.getPage(1);
            const scrollEl = document.getElementById(`${this.container.id}-scroll`);
            const containerWidth = (scrollEl ? scrollEl.clientWidth : window.innerWidth) - 24;
            const unscaledViewport = firstPage.getViewport({ scale: 1.0 });

            const optimal = Math.min(Math.max(containerWidth / unscaledViewport.width, 0.5), 2.2);
            this.currentScale = optimal;
            this.updateZoomDisplay();
        } catch (e) {
            this.currentScale = 1.0;
        }
    }

    async renderAllPages() {
        if (!this.pdfDoc) return;
        const pagesWrapper = document.getElementById(`${this.container.id}-pages`);
        if (!pagesWrapper) return;
        pagesWrapper.innerHTML = '';

        const totalPages = this.pdfDoc.numPages;

        for (let num = 1; num <= totalPages; num++) {
            const pageCard = document.createElement('div');
            pageCard.className = 'pdf-page-card';
            pageCard.setAttribute('data-page-num', num);
            pageCard.id = `${this.container.id}-page-${num}`;

            const canvas = document.createElement('canvas');
            canvas.className = 'pdf-canvas';
            pageCard.appendChild(canvas);

            // TextLayer container for selection and double-click to source
            const textLayerDiv = document.createElement('div');
            textLayerDiv.className = 'textLayer';
            pageCard.appendChild(textLayerDiv);

            // Bottom badge
            const badge = document.createElement('div');
            badge.className = 'pdf-page-number-badge';
            badge.textContent = `Halaman ${num} dari ${totalPages}`;
            pageCard.appendChild(badge);

            // Double click handler for SyncTeX navigation to source code
            pageCard.addEventListener('dblclick', (e) => {
                let sel = window.getSelection().toString().trim();
                if (!sel && e.target && e.target.textContent) {
                    sel = e.target.textContent.trim();
                }
                if (sel) {
                    if (this.options.onTextDblClick) {
                        this.options.onTextDblClick(sel);
                    } else if (window.app && window.app.jumpToSourceText) {
                        window.app.jumpToSourceText(sel);
                    }
                }
            });

            // Mobile double tap handler
            let lastTap = 0;
            pageCard.addEventListener('touchend', (e) => {
                const currentTime = new Date().getTime();
                const tapLength = currentTime - lastTap;
                if (tapLength < 350 && tapLength > 0) {
                    setTimeout(() => {
                        let sel = window.getSelection().toString().trim();
                        if (!sel && e.target && e.target.textContent) {
                            sel = e.target.textContent.trim();
                        }
                        if (sel) {
                            if (this.options.onTextDblClick) {
                                this.options.onTextDblClick(sel);
                            } else if (window.app && window.app.jumpToSourceText) {
                                window.app.jumpToSourceText(sel);
                            }
                        }
                    }, 60);
                }
                lastTap = currentTime;
            });

            pagesWrapper.appendChild(pageCard);

            await this.renderPageCanvas(num, canvas, textLayerDiv);

            if (this.observer) {
                this.observer.observe(pageCard);
            }
        }
    }

    async renderPageCanvas(pageNum, canvas, textLayerDiv) {
        try {
            const page = await this.pdfDoc.getPage(pageNum);
            const viewport = page.getViewport({ scale: this.currentScale });
            const dpr = Math.min(window.devicePixelRatio || 1, 2.5);

            canvas.width = Math.floor(viewport.width * dpr);
            canvas.height = Math.floor(viewport.height * dpr);
            canvas.style.width = `${Math.floor(viewport.width)}px`;
            canvas.style.height = `${Math.floor(viewport.height)}px`;

            const ctx = canvas.getContext('2d');
            ctx.scale(dpr, dpr);

            await page.render({
                canvasContext: ctx,
                viewport: viewport
            }).promise;

            // Render TextLayer for high precision selection & double click
            if (textLayerDiv) {
                textLayerDiv.innerHTML = '';
                textLayerDiv.style.width = `${Math.floor(viewport.width)}px`;
                textLayerDiv.style.height = `${Math.floor(viewport.height)}px`;

                const textContent = await page.getTextContent();
                if (pdfjsLib.renderTextLayer) {
                    pdfjsLib.renderTextLayer({
                        textContentSource: textContent,
                        container: textLayerDiv,
                        viewport: viewport,
                        textDivs: []
                    });
                }
            }
        } catch (e) {
            console.error(`Error rendering page ${pageNum}:`, e);
        }
    }

    async zoom(delta) {
        if (!this.pdfDoc || this.isLoading) return;
        const newScale = Math.min(Math.max(this.currentScale + delta, 0.4), 3.0);
        if (Math.abs(newScale - this.currentScale) < 0.01) return;

        this.currentScale = newScale;
        this.updateZoomDisplay();
        await this.reRenderCanvases();
    }

    async fitToWidth() {
        await this.calculateOptimalScale();
        await this.reRenderCanvases();
    }

    async reRenderCanvases() {
        if (!this.pdfDoc) return;
        const totalPages = this.pdfDoc.numPages;
        for (let num = 1; num <= totalPages; num++) {
            const card = document.getElementById(`${this.container.id}-page-${num}`);
            if (card) {
                const canvas = card.querySelector('canvas');
                const textLayerDiv = card.querySelector('.textLayer');
                if (canvas) {
                    await this.renderPageCanvas(num, canvas, textLayerDiv);
                }
            }
        }
    }

    goToPage(pageNum) {
        if (!this.pdfDoc) return;
        const target = Math.min(Math.max(pageNum, 1), this.pdfDoc.numPages);
        const card = document.getElementById(`${this.container.id}-page-${target}`);
        if (card) {
            card.scrollIntoView({ behavior: 'smooth', block: 'start' });
            this.currentPage = target;
            this.updatePageIndicator();
        }
    }

    updatePageIndicator() {
        const curEl = document.getElementById(`${this.container.id}-page-current`);
        if (curEl) curEl.textContent = this.currentPage;
        if (this.options.onPageChange) {
            this.options.onPageChange(this.currentPage, this.pdfDoc ? this.pdfDoc.numPages : 1);
        }
    }

    updateZoomDisplay() {
        const zoomEl = document.getElementById(`${this.container.id}-zoom-level`);
        if (zoomEl) {
            zoomEl.textContent = `${Math.round(this.currentScale * 100)}%`;
        }
    }
}

window.ContinuousPdfViewer = ContinuousPdfViewer;
