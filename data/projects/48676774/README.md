# IEEE Access - PVC Localization - Daniandra (Draft)

SCAFFOLD ONLY — not submission-ready, no completed experiments, no acceptance or Q1 claim.

## Editing and compilation
- Main file: `main.tex`; editable English sections: `sections/00-abstract.tex` through `sections/11-biographies.tex`.
- Class: supplied `ieeeaccess.cls`; it internally loads supplied `IEEEtran.cls`. This is not a replacement generic IEEEtran manuscript.
- Official class, font maps, font metrics, Type 1 fonts, and required logo/bullet assets are copied unchanged into the working root.
- `official-template/` is an untouched, byte-identical copy of every file in the uploaded extracted official template, including its sample PDF, sample authors, and example metadata. Those belong to the official sample ONLY, never this manuscript.
- Run `latexmk -pdf -interaction=nonstopmode -halt-on-error -no-shell-escape -outdir=build main.tex` from this project directory.
- Backend compile: `POST /api/projects/48676774/compile`. PDF: `build/main.pdf`.
- Editor: https://latex.daniandraaa.my.id/editor/48676774
- Preview: https://latex.daniandraaa.my.id/preview/a40b21a3-6f4
- The source PDF is public through the requested studio preview. No proposal PDF, student identifier, or private research data has been copied into the project.

## Provenance
- Prepared: 2026-10-08T15:30:20.373216+00:00.
- Supplied proposal PDF: `/home/daniilham/.hermes/cache/documents/doc_bfedf470082f_PROPOSAL TA.pdf`.
- Proposal text reviewed: `/home/daniilham/.hermes/cache/scratch/proposal-ta.txt`, cover, approval page and abstract.
- Original title: Analisis Kinerja Arsitektur Hybrid CNN-Transformer untuk Lokalisasi Sumber Premature Ventricular Contraction (PVC) pada Sinyal EKG 12-Lead.
- English working title copied from proposal approval page, not invented.
- Draft author: Daniandra Prayudisty Ilham; institution: Telkom University. English affiliation wording, final author list, corresponding author, email and ORCID need author confirmation.
- Satria Mandala, PhD is named as prospective supervisor in the proposal, NOT automatically a coauthor. No additional author is inserted.
- Proposal mentions CNN-transformer variants, DWT, GAN augmentation, cross-validation, grid search, fine-tuning, held-out evaluation and SHAP. All remain tentative, not finalized or executed.
- Intended methodological direction: patient-wise leakage-free PVC source localization. Dataset, ground-truth labels, splits, ethics, experiments, clinical implications and all results remain pending.
- Official uploaded template: `/home/daniilham/.hermes/cache/scratch/ieee-access-template/ACCESS_latex_template_20260513`. SHA-256 provenance is in `PROVENANCE.json`.
- Official guidance retrieved: https://ieeeaccess.ieee.org/authors/submission-guidelines/; current page links the May 2026 template.
- Stylistic example supplied by user: IEEE article 10897988, OCADN: Improving Accuracy in Multi-Class Arrhythmia Detection From ECG Signals With a Hyperparameter-Optimized CNN; DOI 10.1109/ACCESS.2025.3544273. Bibliographic details are user-supplied, not independently verified here. No metrics, results, or authors are copied and it is not silently cited as localization evidence.
- Hermes Agent (Nous Research), session model cx/gpt-6.1-sol via 9router, generated scaffold prompts and organizational text. A provisional acknowledgment and AI-tool citation appear in retained AI-assisted section prompts. Authors must review and update exact system identity/version and citations before submission.
- No Mac mini or Mac source-folder access was attempted.

## Submission checklist — all substantive gates remain open
- [ ] Replace every placeholder and scaffold warning only after author-approved contents exist.
- [ ] Keep required IEEE Access double-column, single-spaced format; do not override geometry or line spacing.
- [ ] Submit source and PDF with exactly matching contents; keep submission file sizes <=40 MB (official guideline: should not exceed 40 MB).
- [ ] Write a single-paragraph 150–250-word self-contained abstract; final current abstract is intentionally not compliant because it is a draft warning.
- [ ] Confirm 3–10 accurate keywords (six provisional keywords currently present).
- [ ] Confirm full author list/ordering, affiliations, corresponding email, authorship contributions and all authors' approval; match source, PDF and submission portal.
- [ ] Submitting author: account-associated ORCID with publicly visible, populated profile.
- [ ] Approved short biographies for ALL authors below references.
- [ ] Verify relevant references, retraction status, permissions, and first-use acronym definitions.
- [ ] Finalize ethics/data permissions, dataset and labeling provenance; patient-disjoint leakage audit; training-only preprocessing and tuning; appropriate baselines, ablations and uncertainty.
- [ ] Insert only genuinely executed, verified results; no clinical utility without appropriate evidence.
- [ ] Retain/update AI-generated-text disclosure in Acknowledgments and citations to the actual AI system in every affected section, per IEEE policy. Scaffold text was AI-assisted; no results were fabricated.
- [ ] Finalize funding, competing interests, contributor acknowledgments and data/code availability.
- [ ] Grammar review, manuscript type selection and supplementary material if applicable.
- [ ] Recommend <20 pages; longer articles may require EIC pre-submission inquiry per current guidance and exclusions. No minimum length is inferred.
- [ ] Exclusive submission, no fabricated DOI/publication/acceptance metadata. Current DOI/volume/year are explicit unassigned/unpublished markers.

## Verified layout notes
The working PDF has two pages. Both pages were visually inspected: two columns, legible text, no visible overlaps or clipping. TeX overfull/underfull box diagnostics remain: the title and output-routine diagnostics also occur when compiling the untouched official sample, and a small body overfull line occurs in placeholder text. These are nonfatal; revisit typography when replacing prompts with final prose. The official sample compiles to eight pages in a separate scratch build. Do not treat warnings absent from an up-to-date backend response as proof that the complete TeX log has no box diagnostics.
