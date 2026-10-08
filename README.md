# Interactive HTML Learning Resources for Power Electronics

**Alejandro Gómez Yepes · Universidade de Vigo**  
Collection version **1.0** · First public release **7 October 2026**

Thirteen interactive laboratories for university-level Power Electronics learning, with interfaces in English, Spanish and Galician. The collection covers power semiconductor devices, control and protection, mean/RMS values, Fourier harmonics, three-phase electrical systems and eight diode/SCR rectifier laboratories.

- **[Use the laboratories online](https://agyepes.github.io/power-electronics-interactive-html/)**
- **[Download the complete version 1.0 ZIP](https://github.com/agyepes/power-electronics-interactive-html/releases/download/v1.0/Interactive_HTML_Learning_Resources_for_Power_Electronics_v1.0.zip)**
- **[Read the user guide](https://agyepes.github.io/power-electronics-interactive-html/DOCUMENTATION.html)**
- **[View the version 1.0 release](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0)**
- **[View the version 1.0 Zenodo archive](https://doi.org/10.5281/zenodo.23244291)**

For offline use, extract the complete ZIP and open `index.html`. Retain the delivered filenames and accompanying files. The HTML laboratories contain their own scripts and styling.

## Preserve your work

Export notes and answers before leaving or changing files. Laboratory 03 (RMS and mean values) keeps work only in the open page. The other twelve laboratories can retain work in local browser storage when available. Browser storage is not a portable backup. Work does not automatically transfer between the website and downloaded files, browsers or computers. Numerical CSVs and student-work TXT exports are separate where provided.

## Citation and Zenodo archive

> Gómez Yepes, A. (2026). *Interactive HTML Learning Resources for Power Electronics* (Version 1.0) [Interactive educational resources]. Zenodo. https://doi.org/10.5281/zenodo.23244291

Version 1.0 was first released on GitHub on **7 October 2026** and archived on Zenodo on **8 October 2026**. Both locations provide the identical reviewed ZIP and its original checksum companion. The ZIP's SHA-256 is `1b5dca09820dec1eda8ecd50f9c3410dfd5456be116d19cce2778c0132d94418`.

Use the **[version 1.0 DOI](https://doi.org/10.5281/zenodo.23244291)** when citing these exact materials. The **[collection concept DOI](https://doi.org/10.5281/zenodo.23244290)** represents all versions and resolves to the latest published version.

[CITATION.cff](CITATION.cff) provides GitHub citation metadata for version 1.0. The [citation instructions](collection/CITATION.md) and other metadata inside the frozen package were written before the Zenodo archive existed and therefore still record the DOI as pending. Use the verified DOI above; the original package files and checksums are preserved.

## Licences and authorship

Original educational content, diagrams and explanatory documentation use **CC BY 4.0**. Original implementation code, CSS and structural HTML use **MIT**. These licences apply to different components, including within each mixed HTML file, and are not alternative whole-file licences. Student-authored work and third-party material retain their own rights. Read the [scope statement](collection/LICENSING.txt), [content licence](collection/LICENSE-CONTENT.txt), [code licence](collection/LICENSE-CODE.txt) and [third-party notices](collection/THIRD_PARTY_NOTICES.txt).

The author used ChatGPT (OpenAI) and Claude (Anthropic) as AI tools to help generate and refine the resources. This acknowledgement does not imply collaboration with or endorsement by those companies.

## Collection and release maintenance

The `collection` folder contains exactly the downloadable educational package. Repository citation metadata and publishing configuration are outside it. [MANIFEST.json](collection/MANIFEST.json) and [SHA256SUMS.txt](collection/SHA256SUMS.txt) identify the exact package files. Git is configured to preserve their bytes.

GitHub Pages publishes the exact contents of `collection` through its built-in deployment workflow. The `gh-pages` publishing branch contains those files unchanged, plus separate publishing controls that disable Jekyll and Git newline conversion. The downloadable ZIP contains only the 27 collection files.

The publishing script verifies the complete filename set, checksums and committed source bytes before updating that branch. To publish an intentionally reviewed update, run `python scripts/publish_collection.py` from `main` with Git and GitHub CLI available and authenticated. This explicitly updates the public website; a push to `main` alone does not deploy it. Record any revised collection as a new release before broad distribution.

The version 1.0 release tag and downloadable package are retained unchanged; citation links in release notes may be updated. Later corrections or additions receive new releases in this same repository. Keep public HTML basenames stable. Dedicated inverter and DC/DC laboratories are planned for a future collection version.

For each later release, use **New version** on [this Zenodo record](https://zenodo.org/records/23244291), reserve that version's DOI before freezing its package, and include it in the new citation files. Upload the identical new release ZIP to GitHub and that Zenodo version. Each published version has its own DOI; all versions share the concept DOI above. Retain previous downloads and cite their specific version DOIs when the exact materials matter.

Continue using directly managed Zenodo deposits for this collection. Avoid enabling automatic GitHub-to-Zenodo archiving alongside this route, which could create duplicate records for the same release.

Original explanatory text in this README uses CC BY 4.0. Original publishing/verification code uses MIT; retain its notices when reusing it.
