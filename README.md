# Pharma Adverse Vigilance & Safety Signal Engine

[![OpenGAP](https://img.shields.io/badge/OpenGAP-0.1.0-blue.svg)](agent.yaml)
[![Pharma](https://img.shields.io/badge/Domain-Pharmacovigilance_Epidemiology-crimson.svg)](docs/ich_e2e_pharmacovigilance.md)
[![Standard](https://img.shields.io/badge/Standard-ICH_E2E_FAERS-purple.svg)](docs/ich_e2e_pharmacovigilance.md)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](requirements.txt)
[![CI](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](.github/workflows/ci.yml)

A clinical pharmacovigilance and drug safety surveillance engine automating disproportionality signal detection (PRR/ROR) on FDA FAERS MedWatch adverse event registries.

```
                    ┌─────────────────────────┐
                    │ FDA MedWatch Case Series│
                    │ (Drug-Event 2x2 Counts) │
                    └────────────┬────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │ epidemiology/disproport │
                    └────────────┬────────────┘
                                 │
                 ┌───────────────┴───────────────┐
                 ▼                               ▼
      ┌─────────────────────┐         ┌─────────────────────┐
      │  PRR Calculation    │         │  ROR Odds Ratio     │
      │  PRR >= 2.0 Signal  │         │ (Statistical Assoc) │
      └──────────┬──────────┘         └──────────┬──────────┘
                 │                               │
                 └───────────────┬───────────────┘
                                 ▼
                    ┌─────────────────────────┐
                    │ Drug Safety Alert Gate  │
                    │ (SAFETY_COMMUNICATION)  │
                    └─────────────────────────┘
```

## Features

- **Evans Disproportionality Signal Detection**: Identifies adverse event associations exceeding PRR $\ge 2.0$.
- **Reporting Odds Ratio (ROR)**: Computes statistical odds ratios with background control normalizations.
- **FAERS Registry Benchmarks**: Comes pre-packaged with real-world MedWatch drug-reaction pair series.

## Directory Structure

```
pharma-adverse-vigilance/
├── agent.yaml                       # OpenGAP 0.1.0 Manifest
├── EXPLAINABILITY.md                # 7-checkpoint pharmacovigilance provenance
├── epidemiology/
│   └── disproportionality_engine.py # PRR & ROR epidemiology engine
├── fixtures/
│   └── medwatch/
│       └── fda_faers_reports.json   # Benchmark MedWatch adverse events
├── docs/
│   └── ich_e2e_pharmacovigilance.md # Regulatory pharmacovigilance guide
├── tests/
│   └── test_agent.py                # Epidemiological test suite
├── main.py                          # Drug safety CLI
└── requirements.txt
```

## Quick Start

```bash
# Run drug safety tests
pytest tests/ -v

# Audit sample MedWatch adverse event reports
python main.py --demo
```
