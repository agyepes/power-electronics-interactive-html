# Interactive HTML Learning Resources for Power Electronics

## Collection description

Author: Alejandro Gómez Yepes  
Affiliation: Universidade de Vigo  
Collection version: 1.0  
Status: public GitHub release; Zenodo deposit pending  
First public release date: 2026-10-07  
Zenodo DOI: pending  
Online collection: [https://agyepes.github.io/power-electronics-interactive-html/](https://agyepes.github.io/power-electronics-interactive-html/)  
Archived GitHub release: [version 1.0](https://github.com/agyepes/power-electronics-interactive-html/releases/tag/v1.0)

This collection supports university-level Power Electronics teaching through interactive explanations, calculations, plots, guided investigations and self-assessment. It is intended for students, instructors preparing demonstrations or guided activities, and independent learners with basic circuit knowledge.

### Scope of version 1.0

The collection contains **13 laboratories and one laboratory homepage**. Its topics are power semiconductor devices, control and protection, mean/RMS values, Fourier harmonics, balanced three-phase voltages, four diode rectifiers and four SCR rectifiers. The accompanying documentation page is a guide, not an additional laboratory.

The 194 authored self-assessment questions are distributed across these 13 laboratories. The question count exposed at a particular learning level can be smaller. Additional conceptual checks and investigations are provided where the laboratory offers them.

Dedicated laboratories on inverters and DC/DC converters are planned for future versions; they are not modules in this release. Some existing controlled-rectifier laboratories already discuss or calculate inverting operation under suitable circuit conditions.

### Prerequisites

Learners should know Kirchhoff's laws, basic resistor/inductor/capacitor behaviour, elementary algebra and trigonometry, and sinusoidal AC signals. Mean/RMS and Fourier work benefits from basic integration and harmonic representation. The more advanced inductive and capacitive rectifier sections use circuit differential equations, switching intervals and steady periodic operation. The three review laboratories help revisit the corresponding foundations.

### Common learning objectives

After appropriate study, learners should be able to identify voltage and current reference directions; distinguish peak, RMS, mean and instantaneous quantities; predict conduction paths before using a plot; relate parameters to waveforms, device currents, power and harmonics; and explain when an analytical formula applies.

The laboratories encourage a cycle of prediction, parameter change, observation and explanation. Students can use local notes and self-assessment to record that reasoning, then export a portable record. These activities support learning; local quiz results are not formal course grades.

### Module inventory

| No. | File and module | Learning objectives |
| --- | --- | --- |
| 01 | [Power semiconductor devices](01%20-%20Power%20Semiconductor%20Devices.html)<br>01 - Power Semiconductor Devices.html | Distinguish diode, SCR, BJT, MOSFET and IGBT behaviour; interpret conduction and switching losses, drive requirements and thermal constraints. |
| 02 | [Control and protection in power electronics](02%20-%20Control%20and%20Protection%20in%20Power%20Electronics.html)<br>02 - Control and Protection in Power Electronics.html | Explain gate drive, reference potentials, isolation, triggering, cooling, snubbers, clamps, fuses and crowbar coordination using their separate teaching models. |
| 03 | [RMS and mean value calculation](03%20-%20RMS%20and%20Mean%20Value%20Calculation%20Review.html)<br>03 - RMS and Mean Value Calculation Review.html | Calculate and distinguish mean, mean square and RMS; relate RMS to resistive heating and separate DC and zero-mean AC contributions. |
| 04 | [Fourier harmonic decomposition](04%20-%20Fourier%20Harmonic%20Decomposition.html)<br>04 - Fourier Harmonic Decomposition.html | Construct and decompose periodic currents; interpret coefficients, phase, RMS, DC, THD, truncation and the distinction between source and output currents. |
| 05 | [Three-phase electrical system review](05%20-%20Three-Phase%20Electrical%20System%20Review.html)<br>05 - Three-Phase Electrical System Review.html | Relate balanced phase and line voltages, subtraction polarity, phase sequence, RMS/peak values and three-pulse/six-pulse voltage envelopes. |
| 06 | [Single-phase half-wave diode rectifier](06%20-%20Uncontrolled%20Rectifiers%20-%20Single-Phase%20Half-Wave.html)<br>06 - Uncontrolled Rectifiers - Single-Phase Half-Wave.html | Explain single-device conduction, inductive current continuity, freewheeling, an opposing DC source, capacitor filtering and source-current distortion. |
| 07 | [Single-phase full-wave diode bridge](07%20-%20Uncontrolled%20Rectifiers%20-%20Single-Phase%20Full-Wave.html)<br>07 - Uncontrolled Rectifiers - Single-Phase Full-Wave.html | Follow the conducting diode pair, output polarity, load-current continuity, capacitor charging and the difference between source and output current. |
| 08 | [Three-phase half-wave diode rectifier](08%20-%20Uncontrolled%20Rectifiers%20-%20Three-Phase%20Half-Wave.html)<br>08 - Uncontrolled Rectifiers - Three-Phase Half-Wave.html | Follow phase ownership and the neutral return; explain three-pulse output, load branches, phase currents and harmonics. |
| 09 | [Three-phase full-wave diode bridge](09%20-%20Uncontrolled%20Rectifiers%20-%20Three-Phase%20Full-Wave.html)<br>09 - Uncontrolled Rectifiers - Three-Phase Full-Wave.html | Follow the conducting diode pair and six-pulse output; distinguish phase, line, device, resistor and complete output quantities. |
| 10 | [Single-phase half-wave SCR rectifier](10%20-%20Controlled%20Rectifiers%20-%20Single-Phase%20Half-Wave.html)<br>10 - Controlled Rectifiers - Single-Phase Half-Wave.html | Relate firing delay and gate-window duration to conduction, freewheeling, load current and power. |
| 11 | [Single-phase fully controlled SCR bridge](11%20-%20Controlled%20Rectifiers%20-%20Single-Phase%20Full-Wave.html)<br>11 - Controlled Rectifiers - Single-Phase Full-Wave.html | Explain paired SCR triggering, discontinuous/continuous current and rectifying or inverting operation under the stated load conditions. |
| 12 | [Three-phase half-wave SCR rectifier](12%20-%20Controlled%20Rectifiers%20-%20Three-Phase%20Half-Wave.html)<br>12 - Controlled Rectifiers - Three-Phase Half-Wave.html | Relate firing delay from natural commutation to three-pulse operation, phase ownership, load behaviour and signed power. |
| 13 | [Three-phase fully controlled SCR bridge](13%20-%20Controlled%20Rectifiers%20-%20Three-Phase%20Full-Wave.html)<br>13 - Controlled Rectifiers - Three-Phase Full-Wave.html | Explain six-pulse pair commutation, gate timing, load behaviour, harmonics and rectifying or inverting operation under the stated conditions. |

### Model assumptions and limitations

The on-page definitions and assumptions govern each model. Use the offered parameter ranges and the actual active load configuration. The following overview identifies the main limits needed when interpreting or comparing results.

| Modules | Important modelling limits |
| --- | --- |
| 01 | Device characteristics, loss waveforms, reverse recovery, gate charge, SCR/GTO actions and IGBT tail current are simplified or illustrative models. The steady thermal network has no thermal dynamics or temperature feedback into electrical loss. A favourable result does not establish device ratings or safe operating area. |
| 02 | The separate drive, isolation, triggering and protection models each have their own scope. RC gate models omit the Miller effect and do not predict drain/collector switching times; imposed flux and fault envelopes do not establish transformer saturation or real fuse operation. Thermal networks are steady-state; snubber, clamp, coordination and crowbar examples do not constitute hardware/component selection. |
| 03 | Prescribed ideal periodic current waveforms, not a load-circuit simulation. Mean/RMS calculations use analytical expressions; plot sampling is for drawing. Heating examples use a constant 2 Ω resistor. Meter bandwidth, transients, switching loss and temperature dependence are outside the model. |
| 04 | Metrics describe the active **finite** Fourier reconstruction. Changing the maximum order, order filter or enabled components changes the analyzed waveform. The optional ideal reference and its complete-waveform metrics are separate. The ideal rectifier source-current presets assume sinusoidal sources, ideal diodes and a pure resistive load. |
| 05 | Ideal balanced sinusoidal voltages with a fixed U–V–W sequence, equal phase peaks and an ideal neutral reference. It constructs voltage differences and envelopes; it does not calculate load/neutral currents, power or semiconductor states. The √3 and 30° relations require the stated balance, waveform and voltage ordering. |
| 06–13 | Periodic steady-state rectifier models with prescribed sinusoidal sources; the three-phase sources are balanced. Device drops use the constant-drop option where offered. Startup, source/transformer impedance, finite commutation overlap, reverse recovery, leakage, switching loss and temperature are excluded. Ideal charging-current peaks are not safe component ratings. |
| 10–13 | SCR rectifier models assume adequate logical gate drive, zero latching/holding thresholds and zero recovery time. They explain circuit conduction rather than validate a real SCR driver. The firing-angle cosine rule needs continuous series current and its other stated conditions. A firing angle above 90° alone does not establish inversion. |

For capacitor-filter comparisons, match the circuit branch explicitly. The diode filters in 06–08 use the ideal capacitor branch. Laboratory 09 offers both an ideal branch and a branch with a small charging resistance; the controlled rectifiers use the specified resistance in the capacitor branch. That resistor is **not** an AC-source resistance. Match this choice, active load, voltage convention, device drops and periodic state before comparing diode and SCR circuits.

For three-phase rectifiers, the input amplitude is phase-to-neutral peak; for a single-phase bridge it is the complete source peak. The half-wave three-phase topology has a neutral return, while the full-wave bridge uses three line conductors. Laboratories 09 and 13 show all six directed line voltages by default in **Source and output voltages**; phase voltages have a separate toggle and are initially hidden. Display toggles do not change the physical calculation.

Distinguish the resistor current from the complete rectifier output current when a capacitor branch is active. Check the stated denominator for distortion, power factor and efficiency. An undefined ratio is not a zero result. If a laboratory offers established and zero-current-start periodic states, use its stated conditions; selecting a state does not simulate the complete startup transient.

These models support circuit reasoning within their disclosed assumptions. Real hardware also requires appropriate datasheets, parasitic and thermal behaviour, ratings, layout, insulation and experimental validation.

### Languages and delivery

The laboratory interfaces are available in English, Spanish and Galician. The official collection title remains in English. The documentation is written in English. Each laboratory is a self-contained HTML and runs offline with JavaScript enabled; optional external references are supplementary.

Start from [index.html](index.html) and use the [user guide](USER_GUIDE.md). Notes and assessment records are saved locally when permitted in 12 laboratories; laboratory 03 keeps them only in the open page. See the guide's per-module export table. Offline and hosted storage must not be assumed to transfer or synchronise.

### Prepublication verification

The recorded educational review on 6 October 2026 checked independent analytical reference cases, all 194 English self-assessment questions, and numerical/sign equivalence and actual grading across EN/ES/GL. Browser checks covered Chrome 154.0.8037.98 and Microsoft Edge 154.0.4258.53, narrow layouts, printing/PDF, actual exports, local HTTP and extracted offline use.

The later six-line/phase-visibility revisions to laboratories 09 and 13 were checked separately in Chrome 154.0.8037.98, including exports, printing and narrow/expanded views. Those specific later plot revisions have not been retested in Edge. The documentation preparation in Chrome 155.0.8059.39 checked notes and submitted-answer retention in all 13 laboratories, 14 actual TXT exports and 25 actual CSV exports against the current HTMLs. It also checked the documentation and homepage through local HTTP and extracted offline use, in light/dark layouts at widths from 320 to 1440 pixels, and their native browser PDF output.

This scope does not establish compatibility with every browser or device, a complete screen-reader audit, or formal accessibility certification. Firefox, Safari and physical mobile devices were not exercised in those reviews. Results remain subject to the model assumptions above.

### Authorship and reuse

Alejandro Gómez Yepes is the named author, affiliated with Universidade de Vigo. He used ChatGPT (OpenAI) and Claude (Anthropic) as AI tools to help generate and refine the HTML resources. The acknowledgement does not imply personal assistance, collaboration or endorsement by those companies.

Original educational content, diagrams, explanatory documentation and collection metadata use CC BY 4.0; original implementation code uses MIT. The scopes are component-specific and apply within the author's rights. Student-authored work and third-party material have their own rights. See [LICENSING.txt](LICENSING.txt), [LICENSE-CONTENT.txt](LICENSE-CONTENT.txt), [LICENSE-CODE.txt](LICENSE-CODE.txt) and [THIRD_PARTY_NOTICES.txt](THIRD_PARTY_NOTICES.txt).

Use [CITATION.md](CITATION.md) to cite the collection and [CHANGELOG.md](CHANGELOG.md) to identify the prepared release. [MANIFEST.json](MANIFEST.json) and [SHA256SUMS.txt](SHA256SUMS.txt) identify this package's exact file bytes. Publication date, DOI and public URLs remain pending.
