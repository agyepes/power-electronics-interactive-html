# Interactive HTML Learning Resources for Power Electronics

## Collection overview

Author: Alejandro Gómez Yepes  
Affiliation: Universidade de Vigo  
Collection version: 1.0  
Status: public GitHub release; Zenodo deposit pending  
First public release date: 2026-10-07  
Zenodo DOI: pending  
Online collection: [https://agyepes.github.io/power-electronics-interactive-html/](https://agyepes.github.io/power-electronics-interactive-html/)  
Archived GitHub release: [version 1.0](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0)

Thirteen interactive HTML laboratories support university-level Power Electronics learning through explanations, calculations, plots and self-assessment. The collection is intended for students, instructors using demonstrations or guided activities, and independent learners with basic circuit knowledge.

### Start here

Use the [online collection](https://agyepes.github.io/power-electronics-interactive-html/) or [download the complete version 1.0 ZIP](https://github.com/agyepes/power-electronics-interactive-html/releases/download/v1.0/Interactive_HTML_Learning_Resources_for_Power_Electronics_v1.0.zip). The [GitHub release](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0) identifies this exact collection snapshot.

Open [index.html](index.html) in a browser with JavaScript enabled. For a download, extract the whole collection first and retain the filenames and folder contents. Each laboratory contains its own scripts and styling and can run offline; external reference links require an internet connection.

Read [DOCUMENTATION.html](DOCUMENTATION.html) for the browser-readable user guide, module description, licensing summary, citation instructions and change log. Its content is also supplied in the editable documents below.

### Accompanying documents

| Document | Purpose |
| --- | --- |
| [USER_GUIDE.md](USER_GUIDE.md) | Opening the collection, languages, levels, exports, printing, offline use and the per-laboratory saving table |
| [COLLECTION_DESCRIPTION.md](COLLECTION_DESCRIPTION.md) | Audience, prerequisites, learning objectives, exact module inventory, model limits and verification scope |
| [LICENSING.txt](LICENSING.txt) | Component-specific reuse terms and attribution guidance |
| [LICENSE-CONTENT.txt](LICENSE-CONTENT.txt) and [LICENSE-CODE.txt](LICENSE-CODE.txt) | Complete CC BY 4.0 and MIT legal terms |
| [THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt) | External references, third-party terms and credits |
| [CITATION.md](CITATION.md) | Author, title, version, publication fields, citation templates and version/concept DOI guidance |
| [CHANGELOG.md](CHANGELOG.md) | The prepared first release, subsequent version plans and integrity-file conventions |
| [MANIFEST.json](MANIFEST.json) and [SHA256SUMS.txt](SHA256SUMS.txt) | Exact expected filenames, sizes, SHA-256 checksums and HTML source provenance |
| [ZENODO_METADATA.txt](ZENODO_METADATA.txt) | Local preparation for entering a future Zenodo record |

### Laboratories in version 1.0

| No. | Laboratory | File |
| --- | --- | --- |
| 01 | Power semiconductor devices | [01 - Power Semiconductor Devices.html](01%20-%20Power%20Semiconductor%20Devices.html) |
| 02 | Control and protection in power electronics | [02 - Control and Protection in Power Electronics.html](02%20-%20Control%20and%20Protection%20in%20Power%20Electronics.html) |
| 03 | RMS and mean value calculation | [03 - RMS and Mean Value Calculation Review.html](03%20-%20RMS%20and%20Mean%20Value%20Calculation%20Review.html) |
| 04 | Fourier harmonic decomposition | [04 - Fourier Harmonic Decomposition.html](04%20-%20Fourier%20Harmonic%20Decomposition.html) |
| 05 | Three-phase electrical system review | [05 - Three-Phase Electrical System Review.html](05%20-%20Three-Phase%20Electrical%20System%20Review.html) |
| 06 | Single-phase half-wave diode rectifier | [06 - Uncontrolled Rectifiers - Single-Phase Half-Wave.html](06%20-%20Uncontrolled%20Rectifiers%20-%20Single-Phase%20Half-Wave.html) |
| 07 | Single-phase full-wave diode bridge | [07 - Uncontrolled Rectifiers - Single-Phase Full-Wave.html](07%20-%20Uncontrolled%20Rectifiers%20-%20Single-Phase%20Full-Wave.html) |
| 08 | Three-phase half-wave diode rectifier | [08 - Uncontrolled Rectifiers - Three-Phase Half-Wave.html](08%20-%20Uncontrolled%20Rectifiers%20-%20Three-Phase%20Half-Wave.html) |
| 09 | Three-phase full-wave diode bridge | [09 - Uncontrolled Rectifiers - Three-Phase Full-Wave.html](09%20-%20Uncontrolled%20Rectifiers%20-%20Three-Phase%20Full-Wave.html) |
| 10 | Single-phase half-wave SCR rectifier | [10 - Controlled Rectifiers - Single-Phase Half-Wave.html](10%20-%20Controlled%20Rectifiers%20-%20Single-Phase%20Half-Wave.html) |
| 11 | Single-phase fully controlled SCR bridge | [11 - Controlled Rectifiers - Single-Phase Full-Wave.html](11%20-%20Controlled%20Rectifiers%20-%20Single-Phase%20Full-Wave.html) |
| 12 | Three-phase half-wave SCR rectifier | [12 - Controlled Rectifiers - Three-Phase Half-Wave.html](12%20-%20Controlled%20Rectifiers%20-%20Three-Phase%20Half-Wave.html) |
| 13 | Three-phase fully controlled SCR bridge | [13 - Controlled Rectifiers - Three-Phase Full-Wave.html](13%20-%20Controlled%20Rectifiers%20-%20Three-Phase%20Full-Wave.html) |

Version 1.0 includes power semiconductor devices, control and protection, three concept reviews and eight rectifier laboratories. Each diode/SCR group covers single-phase and three-phase half-wave and full-wave circuits. Dedicated inverter and DC/DC laboratories are planned for a future version. Existing controlled rectifiers already address inverting operation where their circuit assumptions permit it.

### Languages and prerequisites

The laboratory interfaces provide English, Spanish and Galician; explanatory documentation is in English. A first opening without a saved preference starts in English. Each laboratory can remember its own last selected language when browser storage is available.

Basic circuit analysis, R/L/C behaviour, algebra, trigonometry and sinusoidal AC signals are the foundations. Integration, Fourier representation and differential equations support the more advanced sections. Use the reviews and stated model assumptions before interpreting a calculated result.

### Preserve student work

Laboratory **03 — RMS and mean values** keeps notes and answers **only in the open page**. Export them before reloading, closing or navigating away. The other 12 laboratories can retain student notes and assessment records in local browser storage when it is available; that storage is not a portable backup.

Export notes and answers using the controls listed in [USER_GUIDE.md](USER_GUIDE.md). Fourier and rectifier numerical CSVs do not include their self-assessment notes: use the separate TXT export too. Do not assume work transfers between local files and the hosted website, different addresses, browsers or computers. There is no general import or automatic synchronisation facility.

### Authorship and licences

Alejandro Gómez Yepes is the named author, affiliated with Universidade de Vigo. He used ChatGPT (OpenAI) and Claude (Anthropic) as AI tools to help generate and refine the HTMLs; this does not imply company collaboration or endorsement.

Original educational content and diagrams, educational strings/questions embedded in scripts, explanatory documentation and collection metadata use **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)**. Original implementation code, CSS and structural HTML use **[MIT](https://opensource.org/license/mit)**. The grants apply to different components of each mixed file. The code drawing a diagram is MIT; its original educational visual content is CC BY 4.0.

Both licences permit commercial reuse subject to their terms. Preserve the content attribution, licence link and change notices required by CC BY 4.0, and the copyright/permission notice required by MIT. Student-authored work remains the students' own work; third-party material retains its own terms. Read [LICENSING.txt](LICENSING.txt) and the full legal texts.

### Verify the package

[MANIFEST.json](MANIFEST.json) inventories the payload files and records the complete expected filename set. [SHA256SUMS.txt](SHA256SUMS.txt) lists SHA-256 values for every package file except itself, including the manifest. The manifest excludes both integrity files to avoid self-reference.

On Windows, open PowerShell in the extracted folder and run:

```powershell
# SPDX-License-Identifier: MIT
$packageRoot = (Get-Location).Path
$manifest = Get-Content -LiteralPath (Join-Path $packageRoot 'MANIFEST.json') -Raw -Encoding utf8 | ConvertFrom-Json
$expectedNames = @($manifest.package.expected_filenames)
$actualNames = @(Get-ChildItem -LiteralPath $packageRoot -File | Select-Object -ExpandProperty Name)
if (Compare-Object $expectedNames $actualNames) { throw 'The package has missing or additional files.' }
$seenNames = @{}
$checksumRows = Get-Content -LiteralPath (Join-Path $packageRoot 'SHA256SUMS.txt') -Encoding utf8
foreach ($row in $checksumRows) {
    if ($row -notmatch '^([0-9a-f]{64})  (.+)$') { throw "Invalid checksum row: $row" }
    $expectedHash = $Matches[1]
    $packageName = $Matches[2]
    if ($packageName -ne [IO.Path]::GetFileName($packageName)) { throw 'Unexpected package path' }
    if ($seenNames.ContainsKey($packageName)) { throw "Duplicate checksum: $packageName" }
    $seenNames[$packageName] = $true
    $packagePath = Join-Path $packageRoot $packageName
    if (-not (Test-Path -LiteralPath $packagePath -PathType Leaf)) { throw "Missing file: $packageName" }
    $packageStream = [IO.File]::OpenRead($packagePath)
    $packageHashAlgorithm = [Security.Cryptography.SHA256]::Create()
    try {
        $actualHash = [BitConverter]::ToString($packageHashAlgorithm.ComputeHash($packageStream)).Replace('-', '').ToLowerInvariant()
    } finally {
        $packageStream.Dispose()
        $packageHashAlgorithm.Dispose()
    }
    if ($actualHash -ne $expectedHash) { throw "Checksum mismatch: $packageName" }
}
if (Compare-Object @($expectedNames | Where-Object { $_ -ne 'SHA256SUMS.txt' }) @($seenNames.Keys)) { throw 'The checksum list does not cover the expected files.' }
'The expected filenames and all listed checksums match.'
```

The Windows example checks the complete expected filename set as well as all listed hashes. On systems with GNU coreutils, `sha256sum -c SHA256SUMS.txt` checks the listed hashes from the extracted folder; compare the filename set separately to detect additional unlisted files. These commands read files; they do not modify the package. Checksum equality does not independently authenticate its source.

The PowerShell code example above is original implementation code under MIT; the surrounding explanatory text uses CC BY 4.0. Retain the notice in [LICENSE-CODE.txt](LICENSE-CODE.txt) when reusing that code.

### Publication information

Version 1.0 was first released publicly on **7 October 2026** through GitHub Pages and the [GitHub release](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0). The collection website is [https://agyepes.github.io/power-electronics-interactive-html/](https://agyepes.github.io/power-electronics-interactive-html/). Zenodo publication and its DOI remain pending; no Zenodo record is claimed by this package.

[CITATION.md](CITATION.md) gives the current website/release citation and explains future Zenodo citation. [ZENODO_METADATA.txt](ZENODO_METADATA.txt) prepares a later deposit and records the first public release date; it is not an uploaded record.

Keep the files and checksums in this archived release unchanged. Record corrections or additions in a new collection release, and retain the earlier archive. Public HTML basenames stay stable so course and external links continue working.
