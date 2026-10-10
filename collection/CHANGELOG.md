# Interactive HTML Learning Resources for Power Electronics

## Change log

Author: Alejandro Gómez Yepes  
Affiliation: Universidade de Vigo  
Collection version: 1.0.1  
Release date: 2026-10-10  
First collection release: 2026-10-07  
Zenodo version DOI: [10.5281/zenodo.23284179](https://doi.org/10.5281/zenodo.23284179)  
Collection concept DOI: [10.5281/zenodo.23244290](https://doi.org/10.5281/zenodo.23244290)  
Online collection: [https://agyepes.github.io/power-electronics-interactive-html/](https://agyepes.github.io/power-electronics-interactive-html/)  
Archived release: [Zenodo](https://zenodo.org/records/23284179) · [GitHub version 1.0.1](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0.1)

### Version 1.0.1 — 10 October 2026

**Documentation and publication-metadata correction.** Added the reserved version DOI [10.5281/zenodo.23284179](https://doi.org/10.5281/zenodo.23284179) to the homepage, citation instructions and release metadata before freezing this package. Replaced outdated current-release Zenodo notices, updated documentation and download links, and recorded the original version 1.0 archive separately.

Updated the common collection label to 1.0.1 in the homepage and all thirteen laboratory footers. Each changed HTML has a new internal revision identifier and its immediate parent hash. Filenames, model/application scripts, educational questions, browser-storage keys and export schemas are preserved. Regenerated the browser-readable documentation, manifest and SHA-256 list. The GitHub and Zenodo downloads use the identical new ZIP.

The original version 1.0 GitHub tag, release assets and Zenodo version DOI remain intact. This release adds no new laboratories. Numerical and browser checks from the original educational review retain the scope stated in [COLLECTION_DESCRIPTION.md](COLLECTION_DESCRIPTION.md).

### Version 1.0 — 7 October 2026

**First public release.** The collection is available through [GitHub Pages](https://agyepes.github.io/power-electronics-interactive-html/) and the [version 1.0 GitHub release](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0). The identical original ZIP was archived on Zenodo on **8 October 2026**, under [DOI 10.5281/zenodo.23244291](https://doi.org/10.5281/zenodo.23244291). The original package recorded that archive as pending because it was prepared before the deposit; its archived bytes are preserved. The entries below describe preparation of this first release, not earlier published versions.

The released collection contains the homepage and 13 numbered laboratories listed in [COLLECTION_DESCRIPTION.md](COLLECTION_DESCRIPTION.md). Their public filenames use English names and an ordered 01–13 prefix; `index.html` remains the homepage.

The preparation established the common collection title, author, Universidade de Vigo affiliation and version 1.0 label, repaired collection navigation, and added CC BY 4.0/MIT notices with distinct educational-content and implementation-code scopes. The AI-tool acknowledgement was retained.

The educational/functionality review on 6 October 2026 corrected saved-work recovery, calculation-failure handling and print flow, and repaired expanded-plot legend layout in the controlled rectifiers. The recorded checks covered numerical reference cases, assessment content and grading, languages, exports, notes, local HTTP, offline extraction and printing within the scope described in the collection description.

The subsequent source-voltage updates to laboratories 09 and 13 added all six directed line voltages and separate phase-voltage visibility. The default view displays line voltages and hides phase voltages. The numerical models were preserved.

The documentation preparation on **7 October 2026 (Europe/Madrid)** added the user guide, collection description, citation instructions, this change log, a browser-readable documentation page, and an exact file manifest and SHA-256 list. The homepage links the documentation in EN/ES/GL. These preparation entries identify work completed before release; the first public release date is 7 October 2026.

The publication preparation added the stable website and download addresses, current release citation and publication date. GitHub deployment configuration and repository citation metadata are kept outside the downloadable collection. The original 13 laboratory files and their numerical, storage and export behavior are unchanged from the reviewed preparation.

### Planned future work

Dedicated laboratories on inverters and DC/DC converters are planned for a future collection version, tentatively version 2. Additional modules and their eventual release date will be recorded when they exist and are reviewed; they are not files in version 1.0.1.

### Identify an exact package

The public collection label of this package is **1.0.1**. Individual HTMLs also retain internal release identifiers and parent provenance, which identify their source revisions. [MANIFEST.json](MANIFEST.json) records the current file sizes, SHA-256 values and HTML provenance; [SHA256SUMS.txt](SHA256SUMS.txt) includes the manifest's own hash.

The two integrity files cannot both include their own hashes without a circular dependency. `MANIFEST.json` therefore inventories every package file **except `MANIFEST.json` and `SHA256SUMS.txt`**. `SHA256SUMS.txt` hashes every package file **except itself**, including `MANIFEST.json`. The manifest also records the complete expected filename set.

Regenerate both integrity files after any content or metadata edit. A checksum establishes equality with the bytes listed in this package; it does not independently authenticate the author or a download source. Keep the final released archive and its externally recorded archive checksum with the publication record.
