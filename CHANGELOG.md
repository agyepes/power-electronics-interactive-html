# Interactive HTML Learning Resources for Power Electronics

## Change log

Author: Alejandro Gómez Yepes  
Affiliation: Universidade de Vigo  
Collection version: 1.0  
Status: public GitHub release; Zenodo deposit pending  
First public release date: 2026-10-07  
Zenodo DOI: pending  
Online collection: [https://agyepes.github.io/power-electronics-interactive-html/](https://agyepes.github.io/power-electronics-interactive-html/)  
Archived GitHub release: [version 1.0](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0)

### Version 1.0 — 7 October 2026

**First public release.** The collection is available through [GitHub Pages](https://agyepes.github.io/power-electronics-interactive-html/) and the [version 1.0 GitHub release](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0). The Zenodo deposit and DOI remain pending. The entries below describe preparation of this first release, not earlier published versions.

The released collection contains the homepage and 13 numbered laboratories listed in [COLLECTION_DESCRIPTION.md](COLLECTION_DESCRIPTION.md). Their public filenames use English names and an ordered 01–13 prefix; `index.html` remains the homepage.

The preparation established the common collection title, author, Universidade de Vigo affiliation and version 1.0 label, repaired collection navigation, and added CC BY 4.0/MIT notices with distinct educational-content and implementation-code scopes. The AI-tool acknowledgement was retained.

The educational/functionality review on 6 October 2026 corrected saved-work recovery, calculation-failure handling and print flow, and repaired expanded-plot legend layout in the controlled rectifiers. The recorded checks covered numerical reference cases, assessment content and grading, languages, exports, notes, local HTTP, offline extraction and printing within the scope described in the collection description.

The subsequent source-voltage updates to laboratories 09 and 13 added all six directed line voltages and separate phase-voltage visibility. The default view displays line voltages and hides phase voltages. The numerical models were preserved.

The documentation preparation on **7 October 2026 (Europe/Madrid)** added the user guide, collection description, citation instructions, this change log, a browser-readable documentation page, and an exact file manifest and SHA-256 list. The homepage links the documentation in EN/ES/GL. These preparation entries identify work completed before release; the first public release date is 7 October 2026.

The publication preparation added the stable website and download addresses, current release citation and publication date. GitHub deployment configuration and repository citation metadata are kept outside the downloadable collection. The original 13 laboratory files and their numerical, storage and export behavior are unchanged from the reviewed preparation.

### Planned future work

Dedicated laboratories on inverters and DC/DC converters are planned for a future collection version, tentatively version 2. Additional modules and their eventual release date will be recorded when they exist and are reviewed; they are not files in version 1.0.

### Identify an exact package

The public collection label is **1.0**. Individual HTMLs also retain internal release identifiers and parent provenance, which identify their source revisions. [MANIFEST.json](MANIFEST.json) records the current file sizes, SHA-256 values and HTML provenance; [SHA256SUMS.txt](SHA256SUMS.txt) includes the manifest's own hash.

The two integrity files cannot both include their own hashes without a circular dependency. `MANIFEST.json` therefore inventories every package file **except `MANIFEST.json` and `SHA256SUMS.txt`**. `SHA256SUMS.txt` hashes every package file **except itself**, including `MANIFEST.json`. The manifest also records the complete expected filename set.

Regenerate both integrity files after any content or metadata edit. A checksum establishes equality with the bytes listed in this package; it does not independently authenticate the author or a download source. Keep the final released archive and its externally recorded archive checksum with the publication record.
