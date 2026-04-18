---
title: VitalIntel — ML Heart Disease Detection
layout: project
---

## VitalIntel (Junior Design)

VitalIntel is a machine-learning decision-support concept for earlier heart disease detection using structured clinical features and ECG-related inputs.

## Clinical Problem

Heart disease remains a leading cause of mortality, and delayed/missed diagnosis contributes to avoidable complications and cost. The project focused on improving speed and consistency of risk stratification so frontline clinicians can escalate high-risk patients earlier.

## Approach

The workflow in the report combines:

- Data preprocessing (missing-value handling, one-hot encoding, feature scaling)
- Feature engineering and selection (including permutation feature importance)
- Multiple classifiers (Logistic Regression, linear SVM, Random Forest)
- Binary risk prediction with confusion matrix and ROC-based evaluation

## Results Highlighted in the Report

- Logistic Regression accuracy reported at **86.13%**
- Balanced class performance with strong recall on heart-disease-positive cases
- Feature-importance analysis identified ST-slope and related clinical variables as key contributors

## Practical Use Cases

- **Early diagnostics:** support primary care referral decisions
- **Emergency triage:** faster prioritization in high-volume ER settings
- **Population health:** identify high-risk cohorts for preventive interventions

## VitalIntel Images

![VitalIntel F1 table](/assets/img/vitalintel/vitalintel-f1-table.png)
![VitalIntel GUI](/assets/img/vitalintel/vitalintel-gui.png)
![VitalIntel model output](/assets/img/vitalintel/vitalintel-03.png)

## Deep Link to Source Exhibit

- [VitalIntel Published Design Report](https://docs.google.com/document/d/e/2PACX-1vTpEIEVWWKseOMeI5Z3GfCj4N7P16D9rR7LF7zS3gaaMkNicMZiD7-vzXuMO1B7Bg/pub)
- [GitHub Repository](https://github.com/kadinelbak/VitalIntel)
