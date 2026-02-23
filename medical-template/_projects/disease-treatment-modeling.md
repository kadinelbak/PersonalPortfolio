---
title: Disease & Treatment Modeling
layout: page
---

## Disease & Treatment Modeling in Ovarian Cancer

### Biological Context
Ovarian cancer is characterized by high rates of recurrence and treatment resistance, making it a prime candidate for therapeutic strategies that move beyond maximum tolerated dose (MTD) paradigms. A growing body of theory suggests that resistance can be shaped by **competitive interactions between drug-naïve and resistant cell populations**, raising the possibility that adaptive therapy may improve long-term control by exploiting these dynamics rather than attempting eradication.

However, translating these ideas into practice requires **data-driven, interpretable models** that connect observable experimental measurements to biologically meaningful mechanisms.

---

## Core Question
**Can data-driven growth and interaction models reveal exploitable asymmetries between drug-naïve and resistant ovarian cancer cell populations that inform adaptive therapy strategies?**

This work aims to answer that question by integrating scalable measurement, phenomenological modeling, and interaction analysis across monoculture and co-culture experimental conditions.

---

## Measurement & Reproducibility Pipeline
The project began with a practical measurement challenge: manual cell counting from fluorescent microscopy images does not scale and introduces subjectivity. Before automating analysis, I first established **biologically meaningful definitions of what constituted a cell**, validating automated threshold-based approaches against manual counts.

This resulted in a reproducible image-analysis pipeline that enabled rapid, consistent quantification of cell populations across plates, conditions, and timepoints. Establishing reliable measurement was essential before any modeling could be meaningfully interpreted.

---

## Modeling Single-Population Growth Dynamics
To understand baseline behavior, I first modeled monoculture growth of drug-naïve and resistant ovarian cancer cell lines.

Rather than assuming exponential growth, I used a **generalized (θ-)logistic formulation** to capture density-dependent effects. This allowed intra-population competition to be expressed flexibly and compared across phenotypes.

**Key insight:**  
Resistant populations exhibited substantially greater sensitivity to density-dependent constraints than naïve populations. In contrast, naïve cells were comparatively robust to crowding effects. This asymmetry suggests that resistance carries an intrinsic fitness cost that becomes apparent under competitive pressure.

---

## Mechanistic Treatment Response via Multi-Compartment Modeling
To interpret treated conditions, I developed a **phenomenological multi-compartment model** representing observable treatment-response states rather than attempting a full molecular description.

Cells transition between:
- **Healthy**
- **Damaged**
- **Arrested**

Cell death was constrained to occur only from the arrested compartment, reflecting experimentally observed dynamics. While simplified, this structure allowed treatment effects to be expressed mechanistically and fit complex response geometries seen in the data.

This approach emphasized interpretability over maximal complexity, enabling direct reasoning about how therapies alter population trajectories.

---

## Competitive Interactions in Untreated Co-Culture
The most informative results emerged in untreated co-culture experiments. Interaction terms revealed **asymmetric competition**:

- Resistant populations were strongly suppressed by the presence of naïve cells.
- Naïve populations showed little sensitivity to resistant cell abundance.

These findings are **consistent with competition-based resistance theory**, suggesting that resistant cells may persist primarily when ecological pressure from naïve populations is removed.

---

## Implications for Adaptive Therapy
Taken together, these results support a framework in which:
- Resistance is not merely drug-induced, but context-dependent
- Competitive suppression may be leveraged therapeutically
- Growth-trajectory–level interpretation provides more insight than endpoint measurements alone

The long-term goal of this work is to inform **adaptive therapy schedules** that intentionally preserve drug-sensitive populations to suppress resistant ones, rather than eliminating all sensitive cells via MTD.

---

## Model Limits & Experimental Constraints
Several important limitations currently bound interpretation:

- **Carrying capacity** in in-vitro systems may not map cleanly to in-vivo tumor environments, limiting direct translational extrapolation.
- **Effective drug concentration over time** is uncertain due to degradation and uptake dynamics in culture media, introducing parameter uncertainty in treated conditions.
- While interaction asymmetries are robust in untreated co-culture, **treated co-culture experiments are required** to validate model-based adaptive therapy predictions.

These limits motivate ongoing experimental work rather than undermine the modeling framework.

---

## Reproducibility & Future Work
This project is being developed as part of an undergraduate senior thesis and is currently **unpublished**. In parallel, I am packaging the parameter estimation methods and image-analysis workflows into reusable tools to support reproducible modeling in other experimental cancer systems.

Next steps include:
- Treated co-culture experiments to test adaptive therapy hypotheses
- Explicit modeling of time-varying drug exposure
- Refinement of model identifiability under constrained data regimes

---

## Selected Artifacts
- **Compartmental model schematic** (phenomenological treatment response)
- **Untreated co-culture growth dynamics** (asymmetric competition)
- **Adaptive therapy schedule simulations** (conceptual)

*Technical implementation details and code are available as a supporting appendix.*
---
title: Disease & Treatment Modeling
layout: project
---

## Clinical Motivation

[**PLACEHOLDER**: Describe the clinical variability in treatment response—what specific disease and patient population? Why does this matter?]

Example framing: *Why do some patients respond to this treatment while others don't? Understanding this variability is critical because [clinical consequence].*

## Question

Can simple, interpretable models quantify treatment effect heterogeneity to inform clinical decisions?

## Approach (high-level)

[**PLACEHOLDER**: Describe your modeling strategy. Include:]
- Growth dynamics model (logistic, Gompertz, etc.)
- Parameter estimation method (data source, technique)
- Treatment response quantification
- Uncertainty/identifiability considerations

Example: *We parameterized logistic growth models from published cohorts, estimated treatment-induced changes in growth rate, and quantified parameter identifiability to bound clinical interpretability.*

## Key Results

[**PLACEHOLDER**: 2–3 figures showing:]
1. Growth curves (untreated vs treated trajectories)
2. Dose–parameter relationship or heterogeneity distribution
3. Model fit or validation comparison

*Include brief interpretation of each.*

## What I Learned

[**PLACEHOLDER**: What did this work teach you about modeling, uncertainty, or medicine? Examples:]
- Handling censored data and communicating bounds to clinicians
- Trade-offs between model complexity and interpretability
- Importance of sensitivity analysis in treatment planning

## Connection to Medicine

[**PLACEHOLDER**: How does this inform clinical practice? Example:]
*Results identified subgroups likely to benefit from early intervention, suggesting a patient-stratification strategy for [clinical scenario].*

## Technical Resources

[Optional] GitHub repositories for methods & implementation:
- [Cancer Growth Dynamics](https://github.com/kadinelbak/[REPO-NAME])
- [Parameter Estimation](https://github.com/kadinelbak/[REPO-NAME])

## Artifacts

- Technical appendix: link to one GitHub repo and one PDF in `assets/pdf/`.
