# PharmaVigil — FDA FAERS Pharmacovigilance & Adverse Drug Reaction Sentinel

[![OpenGAP Compliant](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](https://opengap.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Pharmacovigilance signal detection agent synthesizing post-market clinical surveillance, drug-drug interaction alerts, and automated MedWatch 3500A reports.

## Domain Category
**Healthcare**

## Architecture
- **OpenGAP Specification**: `0.1.0`
- **Role**: Senior Pharmacovigilance Medical Reviewer
- **Primary Goal**: Detect disproportionate reporting signals in post-market clinical trial and FAERS spontaneous reporting streams to protect patient safety.

## Skills Included
- **`disproportionality-signal-detection`**: Calculating Proportional Reporting Ratios (PRR) and Bayesian Empirical Bayes Geometric Mean (EBGM) thresholds.
- **`meddra-hierarchical-coding`**: Standardizing unformatted adverse event narratives to Lowest Level Terms (LLT) and Preferred Terms (PT).
- **`regulatory-safety-reporting`**: Populating CIOMS-I and FDA MedWatch 3500A forms for expedited adverse reaction disclosures.

## Tools Schema
- **`compute-prr-ebgm-signal`**: Calculate statistical disproportionality metrics comparing observed vs expected event frequencies.
- **`map-narrative-to-meddra`**: Extract clinical symptoms from patient reports and assign MedDRA preferred term dictionary codes.
- **`generate-medwatch-submission`**: Synthesize validated case data into compliant FDA 3500A safety XML and PDF bundles.

## Explainability & Verification
Full explainability compliance under OpenGAP Checkpoint 2 is detailed in [EXPLAINABILITY.md](EXPLAINABILITY.md), covering:
- Decision Reasoning
- Data Sources and Inputs Used
- Confidence Scoring Methodology
- Source Attribution Protocol
- Bias Awareness
- Limitation Taxonomy per Domain
- Uncertainty Quantification Approach

## Multi-Framework Compatibility
Adapters and visa export configurations are included in `exports/`:
- Anthropic Claude (`claude-system-prompt.txt`)
- OpenAI Assistants (`openai-assistant.json`)
- LangChain (`langchain-agent.json`)
- CrewAI (`crewai-agent.json`)
- AutoGen (`autogen-agent.json`)

## License
MIT License
