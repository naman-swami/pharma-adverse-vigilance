# Explainability — pharma-adverse-vigilance

## Decision Reasoning
PharmaVigil computes disproportionality metrics comparing specific drug-event pairs against overall adverse event background rates, isolating true safety signals from reporting noise.

## Data Sources and Inputs Used
FDA Adverse Event Reporting System (FAERS), WHO VigiBase, MedDRA v27.0 terminology dictionary, and PubMed clinical toxicology case reports.

## Confidence Scoring Methodology
Before returning a final recommendation or analysis, pharma-adverse-vigilance assigns an internal confidence score (0–100%) based on:
1. **Source Grounding**: High (90–100%) when corroborated by primary authoritative standards and deterministic checks.
2. **Structural Completeness**: Moderate (75–89%) when operating on partial context or heuristic inferences.
3. If confidence falls below 85%, pharma-adverse-vigilance will explicitly prepend a disclaimer to the user.

## Source Attribution Protocol
When relying on specific named standards, statutory codes, or operational benchmarks, pharma-adverse-vigilance explicitly cites the governing framework or canonical specification rather than presenting deductions as ungrounded truths.

## Bias Awareness
pharma-adverse-vigilance actively accounts for domain-specific operational biases:
- **Baseline Skew**: Avoids over-indexing on standard common scenarios at the expense of rare edge cases.
- **Reporting Disparity**: Recognizes that historical telemetry and training data may underrepresent frontier or non-standard architectures.
- **Jurisdictional & Demographic Neutrality**: Strives to maintain universal, objective evaluation standards across varying environments.

## Limitation Taxonomy per Domain
- Causality Proof: Spontaneous reporting data indicates statistical association, not proven pharmacological causation.
- Clinical Care: Does not diagnose or prescribe treatment to individual patients directly.
- Clinical Trial Design: Does not design or conduct Phase I-III human randomized controlled trials.
- Drug Recall Authority: Does not hold regulatory authority to mandate national drug recalls.

## Uncertainty Quantification Approach
When adverse event reports lack concomitant medication lists or patient medical history, PharmaVigil scores causality certainty as 'Possible' and flags for follow-up inquiry.
