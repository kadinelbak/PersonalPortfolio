title: Health-Focused Data Analysis / ML
layout: project

## Clinical Motivation

[**PLACEHOLDER**: Describe a specific clinical question that requires data analysis. Example:]

*Why do some patients with [condition] have [outcome]? Electronic health records contain signals that could inform [clinical decision], but they're buried in unstructured data.*

## Question

[**PLACEHOLDER**: Frame this carefully—avoid "predict" and emphasize interpretability. Examples:]

## Approach (high-level)

[**PLACEHOLDER**: Emphasize interpretability and caution. Include:]

Example: *We used logistic regression with feature selection to identify [associations], validated on [holdout set], and quantified sources of model error and potential bias.*

## Key Insights

[**PLACEHOLDER**: 2–3 figures or results. For each, include:]
1. **What the model shows** (with caveats)
2. **Why this matters clinically**
3. **Limitations**

Example:

## What This Doesn't Do

[**PLACEHOLDER**: Critical section. What are the failure modes? Examples:]

## What I Learned

[**PLACEHOLDER**: Key insights about data analysis in medicine. Examples:]

## Connection to Medicine

[**PLACEHOLDER**: How could this inform practice?]

Example: *If validated prospectively, these associations could flag [patient group] for [specific clinical action]. However, this requires clinical validation first; the model is a hypothesis, not a diagnostic tool.*

## Technical Resources

[**PLACEHOLDER**: Optional GitHub link]


---
layout: page
title: Health Data Modeling — Cardiovascular Risk (Non-Clinical)
---

## Health Data Modeling — Cardiovascular Risk (Non-Clinical)

### Clinical Context
Cardiovascular disease remains one of the leading causes of morbidity and mortality worldwide, and risk stratification is a central component of both preventive care and population-level health research. Data-driven models are increasingly used to explore associations between physiological variables and disease risk, but their utility depends strongly on data quality, interpretability, and appropriate clinical boundaries.

This project explored cardiovascular risk modeling as a **learning and analysis exercise**, not as a diagnostic or clinical decision tool.

---

### Data Source & Inputs
The model was developed using structured clinical data derived from **MIMIC**, a large, de-identified critical care database. Inputs included routinely collected physiological and demographic variables such as:
- Age
- Blood pressure
- Cholesterol-related measures
- Heart rate
- Other standard cardiovascular risk indicators

The dataset was treated as a static snapshot rather than a true longitudinal cohort.

---

### Modeling Approach
A neural network model was trained to learn associations between available features and the presence or absence of heart disease as defined by ground truth labels in the dataset. The objective was not to outperform existing clinical tools, but to explore how multivariate physiological data can be combined into a probabilistic risk signal.

No baseline models (e.g., logistic regression) were used for formal comparison, and the model was evaluated only against labeled outcomes within the dataset.

Importantly, this project did **not** attempt to assign causal importance or clinical weight to individual features. While a feature tree was examined qualitatively to understand model behavior, no formal interpretability methods were applied.

---

### Evaluation & Observations
Model performance was assessed relative to known outcomes in the dataset, with attention paid to false positives, false negatives, and overall behavior rather than absolute performance metrics.

Several observations emerged:
- Predictive performance was sensitive to feature availability and missing data
- Model outputs reflected dataset biases inherent to critical care populations
- Apparent “important” features varied depending on sampling and training conditions

These findings reinforced the need for caution when interpreting model outputs in health contexts.

---

### Limits & Ethical Boundaries
This work has several important limitations:
- **Dataset constraints:** MIMIC represents a specific, high-acuity population and does not generalize to broader or preventative care settings.
- **Lack of longitudinal depth:** True cardiovascular risk unfolds over years to decades, which cannot be captured meaningfully in short observational windows.
- **Interpretability:** Without formal interpretability methods, feature contributions cannot be reliably translated into clinical reasoning.
- **Non-clinical scope:** This model does not provide medical advice, diagnosis, or treatment recommendations and is not validated for patient use.

These constraints are not shortcomings of the model alone, but reflections of broader challenges in applying machine learning to health data.

---

### What This Taught Me
This project highlighted that technical feasibility does not equate to clinical readiness. Even when models appear to perform well, limitations in data provenance, population bias, and interpretability can severely restrict their usefulness in medical decision-making.

The experience reinforced the importance of:
- Longitudinal data collection
- Transparent model behavior
- Clear ethical boundaries between research exploration and clinical application

These considerations continue to shape how I approach health-related data science and research questions.

---

### Supporting Materials
Technical implementation details and exploratory code are available as a **supporting appendix**.

