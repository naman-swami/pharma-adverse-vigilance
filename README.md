# Pharma Adverse Vigilance & Safety Signal Hunter

> **Post-Market Pharmacovigilance & FDA FAERS Disproportionality Mining**  
> Operationalizing Proportional Reporting Ratios (PRR) and Reporting Odds Ratios (ROR).

---

### Spontaneous Reporting $2 \times 2$ Contingency Table

Disproportionality analysis isolates potential drug-adverse event associations within large spontaneous report databases (FDA FAERS, WHO VigiBase):

| Surveillance Cohort | Specific Adverse Reaction ($E$) | All Other Adverse Reactions ($\bar{E}$) | Total Reports |
| :--- | :--- | :--- | :--- |
| **Suspect Drug ($D$)** | $a$ | $b$ | $a + b$ |
| **All Other Drugs ($\bar{D}$)** | $c$ | $d$ | $c + d$ |

---

### Evans Signal Detection Criteria

A statistical drug safety signal is flagged when all three Evans criteria are met:

1. **Proportional Reporting Ratio ($PRR$)**:
   $$PRR = \frac{a / (a + b)}{c / (c + d)} \ge 2.0$$
2. **Chi-Square Statistic with Yates Correction**:
   $$\chi^2 = \frac{N (|ad - bc| - N/2)^2}{(a + b)(c + d)(a + c)(b + d)} \ge 4.0$$
3. **Report Frequency Threshold**: $a \ge 3$ verified adverse event cases.

---

### Pharmacovigilance CLI Execution

```bash
# Screen FDA FAERS benchmark safety reports
python vigilance.py --demo

# Run epidemiological signal detection tests
pytest tests/ -v
```

MedWatch reporting procedures, MedDRA coding standards, and safety escalation policies are detailed in [MEDWATCH_PROTOCOL.md](MEDWATCH_PROTOCOL.md).
