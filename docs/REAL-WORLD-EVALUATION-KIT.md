# Real-World Evaluation Kit

Use this kit to collect evidence that automated repository checks cannot establish. Do not treat completion of a template as proof of usability, accessibility, learning effectiveness, or operational fitness.

## Current evidence state

- **HUMAN UAT = NOT YET EVIDENCED**
- **ACCESSIBILITY HUMAN TESTING = NOT YET EVIDENCED**
- **PILOT USE = NOT YET EVIDENCED**

Automated and synthetic checks are machine evidence only. They do not satisfy these gates.

## Facilitator protocol

1. Record the exact deployed URL, commit, browser, operating system, device, display scale, input method, date, and facilitator.
2. State that scenarios are fictional and the simulation does not authorize real-world publication or action.
3. Obtain the participant's consent under the evaluator's applicable research, privacy, and workplace rules.
4. Ask the participant to complete one scenario without coaching. Use a second scenario only when the protocol calls for comparison.
5. Record observations and defects without collecting unnecessary personal or sensitive data.
6. Debrief using the participant-feedback questions below. Do not convert subjective feedback into a conformance claim.

## Human UAT task script

Record PASS, FAIL, BLOCKED, or NOT TESTED and a concrete evidence reference for each task.

1. Open the start screen and identify the release status and privacy boundary.
2. Start a scenario in the assigned mode.
3. Review every evidence item and explain the distinction among confidence, corroboration, and authenticity.
4. Select a bounded action plan within the simulated time and authority limits.
5. Choose public language proportionate to uncertainty and review the complete decision package.
6. Confirm the human decision, reach the result, and inspect the score explanation.
7. Download, copy, and print the After-Action Review using the available environment.
8. Resume a saved session, then delete local session data.

## Keyboard and accessibility protocol

Follow the detailed [accessibility plan](web/accessibility-plan.md) and record assistive technology and settings exactly.

- Complete the full journey with keyboard only; verify logical order, visible focus, skip-link behavior, and no keyboard trap.
- Test at 200% browser zoom and 320 CSS-pixel width without loss of content or two-dimensional page scrolling.
- Confirm headings, landmarks, fieldsets, labels, status messages, errors, and result updates are meaningfully announced by the selected screen reader.
- Verify focus remains understandable after dynamic updates, validation errors, back navigation, session restore, and AAR actions.
- Check reduced-motion preference, high-contrast or forced-colors mode where supported, and print/PDF output.

An automated contrast calculation or DOM assertion may support diagnosis but is not accessibility human-testing evidence.

## Browser and device matrix

| Browser / version | OS / version | Device | Input / assistive technology | Scenario / mode | Result | Evidence reference |
|---|---|---|---|---|---|---|
| Not tested | Not tested | Not tested | Not tested | Not tested | NOT TESTED | — |

Minimum independent coverage should include current Chromium, Firefox, and Safari/WebKit; a physical keyboard; a physical mobile device; and at least one commonly used screen reader appropriate to each tested platform.

## Defect and evidence record

| Field | Entry |
|---|---|
| Defect ID | |
| Exact commit and URL | |
| Environment | |
| Preconditions | |
| Steps to reproduce | |
| Expected result | |
| Observed result | |
| Severity and rationale | |
| Screenshot, recording, log, or note reference | |
| Reporter and date | |
| Resolution / retest | |

## Participant feedback

- Which instruction or decision was hardest to understand, and why?
- What did you believe the score measured?
- Which evidence changed your decision?
- Did any interface behavior cause you to lose context or confidence?
- Could you distinguish simulated authority from real-world authority?
- What would prevent you from using this in a facilitated learning setting?

Record direct feedback with consent. Separate quotation, facilitator observation, and inference.

## Learning and effectiveness evaluation

Define the evaluation question, participant population, comparison or pre/post method, scoring plan, exclusion criteria, and analysis method before collecting data. Candidate outcomes may include evidence-review accuracy, overclaim avoidance, civilian-protection choices, and explanation quality. Repository scores alone do not establish learning.

Report participant count, recruitment, completion and attrition, instrument versions, missing data, uncertainty, adverse events, limitations, and whether an independent reviewer examined the analysis.

## Pilot report template

1. Purpose and decision the pilot was intended to inform
2. Scope, dates, sites, facilitators, and participant population
3. Exact software commit, deployment, configurations, and materials
4. Ethics, consent, privacy, retention, and incident procedures
5. Completed browser/device/accessibility matrix
6. Task completion and defect results
7. Participant feedback and learning-analysis results
8. Limitations, unresolved risks, and conflicting evidence
9. Recommended disposition: continue evaluation, correct and retest, or stop
10. Named human approver and evidence references

Until completed evidence is reviewed and accepted by accountable humans, retain all three evidence states at the top of this document.
