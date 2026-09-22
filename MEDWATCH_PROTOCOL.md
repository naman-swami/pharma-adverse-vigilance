# Pharmacovigilance Protocols & FDA MedWatch Signal Detection

## 1. International Pharmacovigilance Standards
Pharma Adverse Vigilance conducts post-market drug safety surveillance in accordance with:
- **ICH Guideline E2E: Pharmacovigilance Planning**
- **FDA Guidance for Industry: Good Pharmacovigilance Practices and Pharmacoepidemiologic Assessment**
- **21 CFR Part 314.80 & Part 600.80 (Postmarketing Reporting of Adverse Drug Experiences)**

---

## 2. Spontaneous Reporting Disproportionality Algorithms
The surveillance engine monitors spontaneous adverse event databases (FDA FAERS, EudraVigilance, WHO VigiBase) using $2 \times 2$ contingency tables:

$$\begin{array}{c|c|c}
& \text{Event of Interest } (E) & \text{All Other Events } (\bar{E}) \\ \hline
\text{Suspect Drug } (D) & a & b \\ \hline
\text{All Other Drugs } (\bar{D}) & c & d
\end{array}$$

### A. Proportional Reporting Ratio (PRR)
$$PRR = \frac{a / (a + b)}{c / (c + d)}$$

### B. Reporting Odds Ratio (ROR)
$$ROR = \frac{a \cdot d}{b \cdot c}$$
With $95\%$ confidence interval:
$$\ln(ROR) \pm 1.96 \sqrt{\frac{1}{a} + \frac{1}{b} + \frac{1}{c} + \frac{1}{d}}$$

---

## 3. Evans Signal Detection Criteria
A validated drug-safety disproportionality signal is triggered when:
1. $PRR \ge 2.0$.
2. $\chi^2 \ge 4.0$ (with Yates continuity correction).
3. Number of observed co-occurrence cases $a \ge 3$.

### Urgent Regulatory Escalation:
Signals involving designated Medical Dictionary for Regulatory Activities (MedDRA) Important Medical Events (IMEs) — such as Stevens-Johnson Syndrome (SJS), Torsades de Pointes (TdP), or Drug-Induced Liver Injury (DILI) — mandate review by the Safety Review Committee within **15 calendar days**.
