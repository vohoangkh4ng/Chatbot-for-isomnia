Environment International 155 (2021) 106612

## The associations of phthalate biomarkers during pregnancy with later glycemia and lipid profiles

### A R T I C L E I N F O

**Background:** Pregnancy induces numerous cardiovascular and metabolic changes. Alterations in these sensitive processes may precipitate long-term post-delivery health consequences. Studies have reported associations between phthalates and metabolic complications of pregnancy, but no study has investigated metabolic outcomes beyond pregnancy.

**Objectives:** To examine associations of exposure to phthalates during pregnancy with post-delivery metabolic health.

**Design:** We quantified 15 urinary phthalate biomarker concentrations during the second and third trimesters among 618 pregnant women from Mexico City. Maternal metabolic health biomarkers included fasting blood measures of glycemia [glucose, insulin, Homeostatic Model Assessment of Insulin Resistance [HOMA-IR], % hemoglobin A1c (HbA1c%)] and lipids (total, high-density lipoprotein (HDL), low-density lipoprotein (LDL) cholesterol, triglycerides), at 4–5 and 6–8 years post-delivery. To estimate the influence of the phthalates mixture, we used Bayesian weighted quantile sum regression and Bayesian kernel machine regression; for individual biomarkers, we used linear mixed models.

**Results:** As a mixture, higher urinary phthalate biomarker concentrations during pregnancy were associated with post-delivery concentrations of plasma glucose (interquartile range [IQR] difference: 0.13 SD, 95%CrI: 0.05, 0.20), plasma insulin (IQR difference: 0.06 SD, 95%CrI: 0.02, 0.14), HOMA-IR (IQR difference: 0.08 SD, 95%CrI: 0.01, 0.16), and HbA1c% (IQR difference: 0.15 SD, 95%CrI: 0.05, 0.24). Associations were primarily driven by (∑mono-2-ethyl-5-carboxypentyl terephthalate (MECPTP) and the sum of dibutyl phthalate biomarkers (DBP). The phthalates mixture was associated with lower HDL (IQR difference: ∑DBP and monoethyl phthalate (MEP), and higher triglyceride levels (IQR difference: 0.15 SD, 95%CrI: 0.08, 0.22), driven by MECPTP and MEP. The overall mixture was not associated with total cholesterol and LDL. However, ∑DBP were associated with lower LDL. Conclusions: Phthalate exposure during pregnancy is associated with adverse long-term changes in maternal metabolic health. A better understanding of timing of the exact biological changes and their implications on metabolic disease risk is needed.

1. Introduction

Phthalates are synthetic organic chemicals with widespread global human exposure. Many phthalates are recognized endocrine disrupting compounds and numerous countries have restricted their use. In response, some phthalates, such as di(2-ethylhexyl) phthalate (DEHP), have been partially replaced by alternatives, such as di(2-ethylhexyl) terephthalate (DEHTP). Consequently, global exposure to these replacement phthalates has substantially increased.

Pregnancy induces a series of cardiovascular and metabolic changes. Adaptations in glucose and fat metabolism, specifically, are necessary to meet the increased energy needs of the mother and fetus. For example, in the 2nd trimester, increased secretion of diabetogenic hormones cause the mothers to develop insulin resistance, which peaks in the 3rd trimester before rebounding in the postpartum. Similarly, maternal fasting and postprandial glucose levels vary throughout the course of pregnancy. In parallel to these changes in glucose metabolism, serum cholesterol, including both high- (HDL) and low- (LDL) density lipoproteins, and triglyceride levels are higher during pregnancy. These physiologic changes may represent a period of heightened susceptibility to environmental exposures and alterations in these potentially sensitive processes may precipitate long-term post-delivery health consequences.

Past studies have reported associations of phthalate metabolites with gestational diabetes (GDM), impaired glucose tolerance, and blood glucose during pregnancy, implicating monoethyl phthalate (MEP), DEHP, mono(carboxy-isooctyl) phthalate (MCOP), mono-iso-butyl phthalate (MiBP), and monobenzyl phthalate (MBzP). A study comparing women from Mexico City reported that MEHP and mono-n-butyl phthalate (MBP) were associated with serum expression of miR-29a-3p, a miRNA upregulated in GDM that targets Insulin-induced gene 1 (Insig1). Furthermore, a recent analysis of postpartum women from the Netherlands showed that nearly all measured phthalate metabolites were individually associated with greater maternal weight gain at 6 years post-delivery. However, no study has examined whether exposure to phthalates is associated with longer term changes in maternal metabolic health indicators. Here, we investigated that association and hypothesized that phthalate exposure during pregnancy is associated with higher glycemia biomarkers and altered lipid profiles at 4–5 and 6–8 years post-delivery.

2. Methods

2.1. Cohort recruitment and data collection

From 2007 to 2011, the Programming Research in Obesity, Growth, Environment and Social Stressors (PROGRESS) study recruited 948 pregnant women who subsequently delivered a live birth. All women were receiving prenatal care from Mexican Social Security System (IMSS) in Mexico City and were eligible if they were 18 years or older, less than 20 weeks’ gestation at the time of recruitment, planned to reside in Mexico City for the next 3 years, free of heart or kidney disease, did not use steroids or anti-epilepsy drugs, and were not daily consumers of alcohol. Written informed consent was obtained from all participants. The study protocols were approved by institutional review boards at the Brigham and Women’s Hospital, Icahn School of Medicine at Mount Sinai, and the Mexican National Institute of Public Health. The analysis of blinded specimens at the Centers for Disease Control and Prevention (CDC) laboratory was determined not to constitute engagement in human subjects research. The current analysis comprises 618 women with at least one gestational urine sample and outcome data at 4–5 and/or 6–8 year follow-up visits.

2.2. Urine collection and phthalate biomarker quantification

Details of urinary phthalate biomarker assessment are described elsewhere. In brief, maternal urine samples were collected during the 2nd and 3rd trimesters study visits. The samples were analyzed by isotope dilution high-performance liquid chromatography coupled with tandem mass spectrometry for 15 phthalate biomarkers: mono-n-butyl phthalate (MBP), MiBP, mono-hydroxybutyl phthalate (MHBP), mono-hydroxyisobutyl phthalate (MHiBP), mono-3-carboxypropyl phthalate (MCPP), MEP, mono-2-ethyl-5-carboxypentyl phthalate (MECPP), mono-2-ethylhexyl phthalate (MEHP), mono-2-ethyl-5-hydroxyhexyl phthalate (MEHHP), mono-2-ethyl-5-oxohexyl phthalate (MEOHP), MBzP, mono(carboxy-isononyl) phthalate (MCNP), monooxononyl phthalate (MONP), and MECPTP. Concentrations below the limit of detection were replaced by the instrument reported value while zero values were replaced by the lowest instrument reported value.

To address urine dilution, we measured specific gravity using a digital handheld refractometer. Specific gravity corrected metabolite concentrations were calculated prior to data analysis. Due to the close correlations between metabolites of the same parent compound, we calculated molar sums of metabolites of DEHP (ΣDEHP), diisononyl phthalate (ΣDiNP), diisobutyl phthalate (ΣDiBP), and dibutyl phthalate (ΣDBP). Prior to modeling, we computed the geometric mean of each metabolite across 2nd and 3rd trimester measurements. Exclusion of 157 women who did not have phthalate metabolite measurements at the 3rd trimester visit did not substantively change our results. Therefore, we present our results based on the full sample.

2.3. Outcome measurement

At the 4–5 and 6–8 year post-delivery visits, phlebotomists collected fasting venous blood samples from participants. Glucose, triglycerides, total cholesterol, and HDL cholesterol were measured in plasma by enzymatic photometric assays on a Response 910 automated analyzer. Hemoglobin A1c (HbA1c%) was measured in whole blood by a particle enhanced immunoturbidimetric test (Response 910 analyzer). Plasma insulin was measured by a solid-phase, enzyme-labeled chemiluminiscent immunoassay, on an Immulite 1000 analyzer. LDL concentration was calculated from the following formula: LDL = total cholesterol - HDL - (triglycerides/5). ## 2.4. Covariates

Information regarding maternal age, gestational age at birth, education (# high school), socioeconomic status (Mexican Association of Research and Public Opinion Agencies [AMAI] index), parity, height, alcohol use during pregnancy (yes/no), cigarette smoking during pregnancy (yes/no), and secondhand smoke exposure during pregnancy (yes/no) were collected by trained personnel at baseline. Anthropometric measurements (height and weight) were taken at every visit, including 4–5 and 6–8 years post-delivery.

## 2.5. Statistical analysis

We used linear mixed models with random intercepts to estimate the relationships of geometric mean phthalate biomarker concentrations with glycemia and lipid biomarkers. We built models of individual exposure biomarkers and mutually adjusted models with all biomarkers. Prior to modeling, all specific gravity corrected phthalate biomarker concentrations, plasma glucose, plasma insulin, HOMA-IR, and blood triglyceride levels were log2 transformed. For these transformed outcomes, the resulting estimates were converted to concentration ratios (CR) and can be interpreted as the relative change in geometric mean of outcome.

We used several mixture models to estimate the impact of the total mixture and relative contribution of each component. First, we used Bayesian Kernel Machine Regression (BKMR), which is adaptable to repeated measurements, can flexibly model multiple exposures simultaneously, and explore non-linearity and interactions between mixture components. For all BKMR models, we scaled exposures, non-transformed outcomes, and continuous covariates, and specified 50,000 iterations. Then, because BKMR identified metabolites with potential opposite directions of effect, we used Bayesian Weighted Quantile Sum Regression (BWQS), the recent Bayesian extension of the frequentist weighted quantile sum (WQS) regression. BWQS retains many features of the frequentist WQS approach but does not require a priori specification of a single direction of effect for the entire mixture or splitting of the original dataset, improving statistical power and stability of the estimates. Leveraging these advantages to quantify potentially competing effects, we specified two phthalate mixtures where we grouped the components based on the direction of effect suggested by the linear mixed models and BKMR models (e.g. components with positive associations were grouped together). Because BWQS does not allow repeated measures, the glycemia and lipid biomarkers were averaged across visits. To check the robustness of our BKMR and our two-mixture BWQS models, we modeled one-mixture BWQS and frequentist WQS models for comparison. For the frequentist WQS model, we used the repeated holdout approach, with 100 random partitions, 60/40 validation-test split, and 200 bootstraps.

Maternal age, socioeconomic status, education, parity, and second trimester body mass index (BMI, kg/m2) were included in all multivariable models. Time since delivery (days) was included in all models except for BWQS, where we used variables indicating whether the participant had both measurements, 4–5 years only, or 6–8 years only. All models excluded women who were diagnosed with preeclampsia (n = 26) or became pregnant during the follow-up (n = 30). Alcohol use, cigarette smoking, and secondhand smoke exposure during pregnancy were not included but in all cases, the exclusion of smokers and the addition of alcohol use and secondhand smoke exposure during pregnancy did not substantively change the results. Because phthalates biomarker concentrations may be associated with weight differences over time, models with and without time-varying BMI measured at 4–5 year and 6–8 year visits were compared.

For interpretation, we scaled all presented estimates to the

## 3. Results

### 3.1. Participant characteristics

Summary statistics of participant demographics can be found in Table 1. Of the 618 women with available outcome data, the average age and BMI of the mothers at enrollment were 27.3 years and 26.4 kg/m2, respectively. The majority were of low socioeconomic status, did not advance beyond high school, and had at least one previous pregnancy. Few women reported current cigarette smoking or alcohol intake during pregnancy and follow-up. Most phthalate biomarkers were detected in ≥ 99% of the samples (Table 2). Phthalate biomarkers showed moderate to strong pairwise correlations with one another (Spearman rho = 0.44–0.86), with the exception of MEP, which was weakly correlated with all other metabolites (Spearman rho = 0.21–0.40). Most participants had normal levels of glycemia and lipid profile biomarkers.

### 3.2. Glycemia biomarkers

In BKMR models, concurrent increase in all mixture components was associated with higher plasma glucose (IQR difference: 0.13 SD, 95% Credible Intervals: 0.05, 0.20), plasma insulin (IQR difference: 0.06 SD, 95% CrI: 0.02, 0.14), HOMA-IR (IQR difference: 0.08 SD, 95% CrI: 0.01, 0.16), and HbA1c% (IQR difference: 0.15 SD, 95% CrI: 0.05, 0.24). In the same BKMR models, single-metabolite dose–response curves showed that DEHP, MECPTP, DBP, and MEP were associated with HbA1c%. MECPTP was additionally associated with plasma insulin and HOMA-IR.

### Table 1
Demographics of PROGRESS Participants.

|                                         | Total Cohort (n = 948) | Have Outcome Data (n = 618) |
|-----------------------------------------|-------------------------|------------------------------|
| Mean (SD)                               |                         |                              |
| Age (years, 2nd trimester)             | 27.7 (5.5)              | 27.3 (5.6)                   |
| BMI (kg/m2, 2nd trimester)             | 26.9 (4.2)              | 26.4 (4.1)                   |
| Socioeconomic Status Index*             | N (%)                   |                              |
| 1 (lowest)                             | 86 (9%)                 | 56 (9%)                      |
| 2                                      | 400 (42%)               | 272 (44%)                    |
| 3                                      | 218 (23%)               | 145 (23%)                    |
| 4                                      | 138 (15%)               | 84 (14%)                     |
| 5                                      | 88 (9%)                 | 52 (8%)                      |
| 6 (highest)                            | 18 (2%)                 | 9 (1%)                       |
| Education                               |                         |                              |
| < High School                           | 385 (41%)               | 251 (41%)                    |
| High School                             | 334 (35%)               | 225 (36%)                    |
| >High School                            | 229 (24%)               | 142 (23%)                    |
| Parity**0                               | 428 (45%)               | 236 (38%)                    |
| 1                                      | 382 (40%)               | 212 (34%)                    |
| 2                                      | 122 (13%)               | 120 (19%)                    |
| 3+                                     | 16 (2%)                 | 50 (8%)                      |
| Secondhand Cigarette Smoking at Home    |                         |                              |
| No                                      | 644 (68%)               | 425 (69%)                    |
| Yes                                     | 297 (31%)               | 189 (31%)                    |
| Current Cigarette Smoking               |                         |                              |
| Second Trimester (# Yes, %)            | 6 (1%)                  | 4 (1%)                       |
| Third Trimester (# Yes, %)             | 4 (1%)                  | 3 (1%)                       |
| Alcohol in the last 3 months***        |                         |                              |
| Yes                                     | 25 (3%)                 | 13 (2%)                      |
| No                                      | 770 (81%)               | 537 (87%)                    |
| Missing                                 | 153 (16%)               | 68 (11%)                     |

* Calculated based on AMAI criteria and collapsed into 3 categories (1–2, 3–4, 5–6) for modelling.
** Collapsed into primiparous and non-primiparous for modelling.
*** Asked at third trimester. Table 2
Distribution of Specific Gravity Corrected Urinary Phthalate Biomarker Concentrations (ng/mL) in the PROGRESS cohort by Trimester.

| Parent | Metabolite | Geometric Mean | 25th percentile | 75th percentile | Detection Rate (%) | Geometric Mean | 25th percentile | 75th percentile | Detection Rate (%) |
|--------|------------|----------------|------------------|------------------|--------------------|----------------|------------------|------------------|--------------------|
| DEHP   | MEHP       | 5.61           | 2.79             | 10.88            | 96%                | 5.56           | 2.70             | 10.70            | 96%                |
|        | MEOHP      | 18.4           | 9.88             | 34.47            | 100%               | 22.23          | 11.45            | 41.19            | 100%               |
|        | MEHHP      | 20.03          | 11.00            | 38.30            | 100%               | 22.79          | 11.60            | 43.27            | 100%               |
|        | MECPP      | 42.42          | 24.09            | 74.58            | 100%               | 48.73          | 24.97            | 85.55            | 100%               |
| DEHTP  | MECPTP     | 1.88           | 1.00             | 3.52             | 98%                | 2.31           | 1.13             | 4.53             | 98%                |
| DINP   | MONP       | 1.32           | 0.68             | 2.53             | 87%                | 1.61           | 0.85             | 3.10             | 92%                |
|        | MCOP       | 4.56           | 2.47             | 8.49             | 100%               | 4.58           | 2.49             | 8.38             | 100%               |
| DIDP   | MCNP       | 0.97           | 0.60             | 1.46             | 98%                | 1.01           | 0.61             | 1.71             | 98%                |
| DOP    | MCPP*      | 1.41           | 0.81             | 2.45             | 92%                | 1.47           | 0.81             | 2.66             | 93%                |
| BBzP   | MBzP       | 5.18           | 2.56             | 10.90            | 98%                | 5.26           | 2.52             | 11.23            | 98%                |
| DIBP   | MHiBP      | 3.4            | 1.94             | 6.25             | 98%                | 3.72           | 2.00             | 6.87             | 99%                |
|        | MiBP       |                |                  |                  |                    |                |                  |                  |                    |
|        | MBP**      | 8.81           | 4.98             | 17.02            | 99%                | 10.29          | 5.78             | 18.26            | 99%                |
| DBP    |            | 78.94          | 39.60            | 149.25           | 100%               | 84.76          | 42.11            | 164.39           | 100%               |
|        | MHBP       | 6.91           | 3.58             | 14.28            | 99%                | 7.45           | 3.79             | 15.28            | 99%                |
| DEP    | MEP        | 142.9          | 57.83            | 360.68           | 100%               | 150.54         | 55.96            | 386.20           | 100%               |

Detection Rate is defined as proportion above limit of detection (LOD).
* Also a minor metabolite of several high molecular weight phthalates.
** Also a minor metabolite of BBzP.

Fig. 1. The impact of increasing phthalate biomarker mixture on maternal post-delivery (A) glycemia and (B) lipid biomarkers at 4–5 and 6–8 years post-delivery. The estimates represent the estimated change (y-axis, in standard deviations) when all of the mixture components are at a given percentile (x-axis) compared with when all components are at the 25th percentile. All plots range from 25th to 75th percentile, in increments of 5 percent. The models were adjusted for maternal age, SES, education, parity, BMI at baseline, and post-delivery visit day.

comprising MECPTP,∑DINP, ∑DIBP, and ∑DBP, were associated with higher plasma glucose, plasma insulin, HOMA-IR, and HbA1c%. Consistent with BKMR and linear mixed models, MECPTP had the highest weight in the positive-mixture for plasma insulin, HOMA-IR, and HbA1c%. Increases in the negative mixture, comprising∑DEHP, MCNP, MCPP, MBzP, and MEP, was associated with HbA1c% and the weights were mixed. Single-mixture BWQS and frequentist Plasma Glucose (CR) | Plasma Insulin (CR) | HOMA-IR (CR) | HbA1c (%)
--- | --- | --- | ---
Positive | Negative | 0.95 | 1.00 | 1.05Estimated Change in Outcome per Interquartile Increase in Exposure 0.00.7 | 0.9 | 1.1 | 1.3 | 0.8 | 1.0 | 1.2 | 1.4 | -0.2 | 0.2 | 0.4

Plasma Glucose (CR) | Plasma Insulin (CR) | HOMA-IR (CR) | HbA1c
--- | --- | --- | ---
MECPTP | ZDINP | ZDIBP | ZDBP | ZDEHP | MCNP | MCPP | MBzP | MEP | 0.0 | 0.2 | 0.4 | 0.6 | 0.0 | 0.2 | 0.4 | 0.6 | 0.0 | 0.2 | 0.4 | 0.6 | 0.0 | 0.2 | 0.4 | 0.6
Loading Weights | Positive | Negative

Results from Bayesian Weighted Quantile Sum (BWQS) regression models for maternal post-delivery glycemia biomarkers with two mixtures, including the overall mixture effect (A) and the estimated weight of each biomarker to the mixture (B). The models were adjusted for maternal age, SES, education, parity, BMI at baseline, and whether the individual had outcomes at both time periods, 4–5 years only, or 6–8 years only.

WQS models support the findings from BKMR with overall positive associations between the mixture and all four glycemia outcome biomarkers, primarily driven by MECPTP, ∑DBP, and MEP. MECPTP was positively associated with HDL and triglycerides and negatively associated with LDL. DBP was associated with lower total cholesterol, HDL, and LDL. MEP was associated with higher total cholesterol and triglycerides and lower HDL.

In linear mixed models, IQR change in urinary MECPTP concentration was associated with 9% relative change in plasma insulin (95% confidence interval [CI]: 1.02, 1.16), 9% relative change in HOMA-IR (95% CI: 1.02, 1.18), and 0.13% absolute increase in HbA1c% (95% CI: 0.7, 0.18). Absolute HbA1c% was also associated with ∑DEHP (IQR β = -0.09%, 95% CI: 0.11, 0.01), ∑DBP (IQR β = 0.09%, 95% CI: 0.00, 0.18), and MEP (IQR β = -0.06%, 95% CI: 0.00, 0.19), while the latter was driven by MECPTP and MEP. The two-mixture BWQS showed potential bi-directional impact of the mixture on total cholesterol, HDL, and LDL. The negative-direction mixture was driven by ∑DBP for total cholesterol, ∑DBP and MEP for HDL, and DBP for LDL. In contrast, the positive mixture was more evenly distributed except for triglycerides, which was primarily driven by MECPTP and ∑DBP.

Lipid profiles
∑DBP was associated with lower total cholesterol (IQR β = -6.68 mg/dL, 95% CI: 13.11, 0.24) and HDL (β = 2.16 mg/dL, 95% CI: 4.16, 0.01) and higher triglycerides (IQR difference: 0.15 SD, 95% CrI: 0.08, 0.22), but not total cholesterol and LDL. At the individual biomarker level, MECPTP was associated with lower LDL (IQR β = -4.19 mg/dL, 95% CI: 7.37, 1.01); MEP was associated with higher total cholesterol (IQR β = 3.86 mg/dL, 95% CI: 0.08, 7.65). All of these associations persisted after the addition of time-varying BMI to the model. Plasma Glucose (CR)* | Insulin (CR)* | HOMA-IR (CR)* | HbAIc (%)
--- | --- | --- | ---
ZDEHP | 1 | 17 | H
MECPTP |  | E |
ZDINP |  |  |
MCNP |  |  |
MCPP |  |  |
MBzP |  |  |
ZDIBP |  |  |
ZBP |  |  |
MEP | 8 | 8 | 8 | 8
| 2 | 2 - ~ | 8 8 3

Difference in Metabolic Health Biomarkers

Estimated difference in maternal glycemia biomarkers at 4–5 and 6–8 years post-delivery per interquartile range increase in mean gestational urinary phthalate biomarker concentrations. Concentration Ratios (CR*) are interpreted as the relative change in biomarker levels per doubling of exposure. In addition to mutually adjusted exposures, the models also adjusted for maternal age, SES, education, parity, BMI at baseline, and post-delivery visit day.

Total Cholesterol (mg/dL) | HDL (mg/dL) | LDL (mg/dL) | Triglycerides (CR)
--- | --- | --- | ---
Positive | Negative | 20 -10 | 10 20
| 20 | 10 | 20 | 0.9 | 1.0 | 1.1 | 1.2 | 1.3

Estimated Change in Outcome per Interquartile Increase in Exposure

Positive | Negative
--- | ---
Total Cholesterol | HDL | LDL | Triglycerides
ZDIBP | MECPTP | ZDIBP | MECPTP
MEP | ZDINP | MEP | ZDBP
MCPP | MCPP | MCPP | ZDIBP
MBzP | ZDIBP | MBzP | ZDINP
ZDEHP | MBzP | ZDEHP | MCNP
ZDBP | ZDBP | ZDBP | ZDEHP
MECPTP | MEP | MECPTP | MBzP
ZDINP | ZDEHP | ZDINP | MEP
MCNP | MCNP | MCNP | MCPP

Loading weights

Results from Bayesian Weighted Quantile Sum (BWQS) regression models for maternal post-delivery lipid biomarkers with two mixtures, including the overall mixture effect (A) and the estimated weight of each biomarker to the mixture (B). The models were adjusted for maternal age, SES, education, parity, BMI at baseline, and whether the individual had outcomes at both time periods, 4–5 years only, or 6–8 years only. | Cholesterol (mg/dL) | HDL (mg/dL) | LDL (mg/dL) | Triglycerides (CR)* |
|----------------------|--------------|--------------|---------------------|
| MECPTPZDEHP          |              |              |                     |
| ZDINP                |              |              |                     |
| MCPP                 |              |              |                     |
| MCNP                 | 0            |              |                     |
| ZDIBP                |              |              |                     |
| ZDBP                 | F            |              |                     |
| MEP                  |              |              |                     |
|                      | Y            | N            |                     |
|                      | 8            | 8            | 8                   |
|                      | 8            |              |                     |

### Difference in Metabolic Health Biomarkers

Fig. 5. Estimated difference in maternal lipid biomarkers at 4–5 and 6–8 years post-delivery per interquartile range increase in mean gestational urinary phthalate biomarker concentrations. Concentration Ratios (CR*) are interpreted as the relative change in biomarker levels per doubling of exposure. In addition to mutually adjusted exposures, the models also adjusted for maternal age, SES, education, parity, BMI at baseline, and post-delivery visit day.

### Preeclampsia

To assess whether the removal of participants with preeclampsia could have introduced collider stratification bias, we compared models with and without participants with preeclampsia. We found no meaningful difference between the two sets of models.

### Discussion

Our study found that higher phthalate concentrations during pregnancy, as a mixture, was associated with more insulin resistance and adverse lipid profiles up to 8 years post-delivery, as indicated by higher levels of plasma glucose, plasma insulin, HOMA-IR, HbA1c%, and triglycerides, and lower levels of HDL. Associations with glycemia biomarkers appear to be primarily driven by MECPTP and ∑DBP while associations with lipid biomarkers were driven by MECPTP, ∑DBP, and MEP.

While our study was the first to investigate the influence of phthalate exposure during pregnancy on long-term maternal post-delivery metabolic health biomarkers, our strong positive associations are supported by previous evidence in other settings. Specifically, a previous study of women from the Netherlands showed that total phthalate metabolites as well as all individual metabolites were associated greater weight gain between pre-pregnancy and 6 years post-delivery. These results are consistent with our overall mixture results and estimates from individual metabolite models. Further, there is compelling evidence that phthalate metabolite concentrations are associated with glycemia and insulin resistance in both pregnant and general populations. However, one differentiating aspect between previous studies and our own is that our study identified MECPTP and DBP as the primary contributors to these associations. DBP has been previously linked to diabetes and insulin resistance while no prior studies have investigated the impact of MECPTP. In contrast to previous studies that reported associations of MEP, DEHP, MCOP, MiBP, and MBzP with blood glucose levels and impaired insulin resistance during pregnancy, our study did not identify these as primary contributors to the overall mixture association with glycemia biomarkers. There are several possible explanations. First, our study investigated long-term maternal glycemic health and measured outcomes 4–8 years post-delivery, which may not necessarily reflect or correlate with metabolic health during pregnancy. Second, it is plausible that these other exposures do contribute to the overall mixture effect, but not as strongly as MECPTP, a relatively new compound that was not measured in other studies. Third, there were methodological differences such as single exposure models applied in previous studies versus the mixture approaches we employed. Taken together, while direct comparisons with past studies are difficult, our observed results align with existing evidence.

There were instances where the estimated impact of individual biomarkers was contrary to the total mixture effect. ∑DEHP and MEP concentrations were negatively associated with HbA1c%, contrary to the overall positive mixture effect. While we cannot fully rule out the possibility that ∑DEHP and MEP may have protective effects, it is more likely that these were artefacts because neither were found to have high importance in BKMR and WQS models. In particular, potential biases introduced by co-exposure adjustment could have produced spurious relationships at the individual biomarker level that differ from the total mixture effects, which does not suffer from this bias. For total cholesterol and LDL, there were no total mixture effects, but some plausible associations were observed for MECPTP, ∑DBP, and MEP, the three primary drivers of the total mixture effect on HDL and triglycerides. Consequently, the absence of overall mixture effect in this population is likely a reflection of the competing effects from different phthalates measured in our population. Importantly, it does not imply that individual phthalate compounds are not associated with altered lipid profiles. The consistency of the results within each exposure biomarker (across outcomes) suggests that different phthalate biomarkers may have unique associations with specific lipid biomarkers.

While previous studies explored the health impacts of legacy phthalates such as DEHP, these compounds are now restricted in their use by many countries. Exposure to their replacements, such as DEHTP, are increasing globally and it is of great public health interest for us to investigate their potential health impacts. DEHTP, in particular, is a direct replacement for DEHP and can be found in sources commonly associated with DEHP such as food and toys. However, urinary DEHTP metabolites do not necessarily correlate with DEHP metabolites, which may suggest selective replacement and exposure sources. Here, we find that MECPTP, one metabolite of DEHTP, is the strongest driver behind the phthalate mixture effect on higher glycemia markers and triglycerides. It was also individually associated with higher HDL and lower LDL in the absence of an overall mixture effect, controlling for other metabolite concentrations. A recent analysis of NHANES data showed that DEHTP concentrations was associated with differences in serum sex hormone concentrations in postmenopausal women. Thus, the emerging evidence suggests that DEHTP, the parent compound of MECPTP, may have biological impact similar to its predecessors and harmful to cardiometabolic health. Future studies should seek to not only replicate these results, but to examine whether the observed glycemic and lipid profile changes associated with MECPTP translate to higher risks of cardiometabolic diseases.

There is a paucity of research linking phthalate exposure during pregnancy and long-term post-delivery maternal health and it is unclear whether phthalates affect pregnancy-specific processes or if its actions are broader. Some phthalates are putative agonists of peroxisome proliferator-activated receptor gamma (PPARγ), known regulators of glucose homeostasis and lipid metabolism. These phthalates are also endocrine disruptors linked to changes in sex hormones and reproductive outcomes, which in turn regulate energy homeostasis and glucose metabolism. No study has yet explored the mechanisms by which DEHTP may act on glucose and lipid metabolism homeostasis. Given our results, further studies to investigate its biological activities are of interest.

Our study has several key strengths. We implemented multiple mixtures analyses to address highly correlated exposures to identify the most relevant biomarkers within the mixture. We were able to measure and study MECPTP, reflecting an emerging exposure to DEHTP with potential global implications. Timely investigations of replacement compounds will provide evidence toward new policies and regulations. Another strength of our study is that we were able to study relevant pre-clinical biomarkers of metabolic disorders. This knowledge can then be applied to prevention and other public health efforts. However, it is also important that future studies investigate clinical endpoints such as diabetes mellitus or incident cardiovascular disease to understand the full public health impacts.

Our study also has some limitations. We did not have metabolic measures before 4–5 years post-delivery and thus were not able to examine their full trajectory. This broadly relates to another limitation, which is that our study only examined pregnancy exposures and the influence of earlier exposures and post-delivery exposures on the observed associations are unknown. Thus, it is unclear whether the observed associations were results of altered trajectory during pregnancy or if there were disturbances before or shortly after pregnancies. Without additional evidence, it is difficult to confidently establish the temporal sequence of the relationship, the affected populations, and the sensitive windows. Elucidation of this temporality and affected population will improve our understanding of the relationship and offer information for risk stratification and public health strategies. There was likely non-differential misclassification of exposure. The use of two spot urine samples weeks apart better approximates exposure across pregnancy compared to a single sample, but it could not reflect the total variability in exposure given the short biological half-lives and episodic nature of phthalate exposures. We were also limited by the lack of dietary data during pregnancy. In particular, DEHP and DEHTP are found in plastic food packages and diet is a determinant of metabolic health. We did adjust for BMI at baseline and at the time of outcome measurements, which may act somewhat as proxies for diet, but residual confounding is possible. However, if the uncontrolled confounder acts as common sources for the exposure components, then mixture modeling is overall beneficial as it partially removes the bias. Additionally, total mixture effects are unaffected by co-exposure amplification bias and can be interpreted with greater confidence. Lastly, our results may not be generalizable to other populations, considering potential differences in phthalate exposure profiles and potential modifying factors across populations.

## Conclusion

Our study suggests that phthalate exposure during pregnancy may be associated with markers of metabolic health up to 8 years post-delivery. All of these observed associations were consistently driven by MECPTP, ∑DBP, and MEP. Additional studies are warranted to investigate whether these changes translate to chronic disease development, such type 2 diabetes and cardiovascular disease. Disclaimer

The findings in this article are the opinions of the authors and do not necessarily reflect the official opinion of the Centers for Disease Control and Prevention. Use of trade names is for identification only and does not imply endorsement by the CDC, the Public Health Service, or the US Department of Health and Human Services.

Appendix A. Supplementary material

Supplementary data to this article can be found online at https://doi.org/10.1016/j.envint.2021.106612.

| Author(s) | Year | Title | Journal | Volume | Pages |
|-----------|------|-------|---------|--------|-------|
| Adrian Villegas Carrasco | 2019 | The AMAI system of classifying households by socio-economic level |  |  |  |
| Angueira, A.R., Ludvik, A.E., Reddy, T.E., Wicksteed, B., Lowe, W.L., Layden, B.T. | 2015 | New Insights Into Gestational Glucose Metabolism: Lessons Learned From 21st Century Approaches | Diabetes | 64 | 327–334 |
| Api, A.M. | 2001 | Toxicological profile of diethyl phthalate: a vehicle for fragrance and cosmetic ingredients | Food Chem. Toxicol. | 39 | 97–108 |
| Benjamin, S., Masai, E., Kamimura, N., Takahashi, K., Anderson, R.C., Faisal, P.A. | 2017 | Phthalates impact human health: Epidemiological evidences and plausible mechanism of action | J. Hazard. Mater. | 340 | 360–383 |
| Bobb, J.F., Valeri, L., Claus Henn, B., et al. | 2015 | Bayesian kernel machine regression for estimating the health effects of multi-pollutant mixtures | Biostatistics | 16 | 493–508 |
| Bobb, J.F., Claus Henn, B., Valeri, L., Coull, B.A. | 2018 | Statistical Software for analyzing the health effects of multiple concurrent exposures via Bayesian kernel machine regression | Environ Health | 17 | 67 |
| Boeniger, M.F., Lowry, L.K., Rosenberg, J. | 1993 | Interpretation of urine results used to assess chemical exposure with emphasis on creatinine adjustments: a review | Am. Ind. Hyg. Assoc. J. | 54 | 615–627 |
| Buckley, J.P., Kim, H., Wong, E., Rebholz, C.M. | 2019 | Ultra-processed food consumption and exposure to phthalates and bisphenols in the US National Health and Nutrition Examination Survey, 2013–2014 | Environ. Int. | 131 | 105057 |
| Carrico, C., Gennings, C., Wheeler, D.C., Factor-Litvak, P. | 2015 | Characterization of Weighted Quantile Sum Regression for Highly Correlated Data in a Risk Analysis Setting | J. Agric. Biol. Environ. Stat. | 20 | 100–120 |
| Casals-Casas, C., Desvergne, B. | 2011 | Endocrine Disruptors: From Endocrine to Metabolic Disruption | Annu. Rev. Physiol. | 73 | 135–162 |
| Colicino, E., Pedretti, N.F., Busgang, S.A., Gennings, C. | 2020 | Per- and poly-fluoroalkyl substances and bone mineral density | Environ Epidemiol. | 4 |  |
| Czarnota, J., Gennings, C., Wheeler, D.C. | 2015 | Assessment of weighted quantile sum regression for modeling chemical mixtures and cancer risk | Cancer Inform. | 14 | 159–171 |
| Dales, R.E., Kauri, L.M., Cakmak, S. | 2018 | The associations between phthalate exposure and insulin resistance, β-cell function and blood glucose control in a population-based sample | Sci. Total Environ. | 612 | 1287–1292 |
| Desvergne, B., Feige, J.N., Casals-Casas, C. | 2009 | PPAR-mediated activity of phthalates: A link to the obesity epidemic? | Mol. Cell. Endocrinol. | 304 | 43–48 |
| Dirinck, E., Dirtu, A.C., Geens, T., Covaci, A., Van Gaal, L., Jorens, P.G. | 2015 | Urinary phthalate metabolites are associated with insulin resistance in obese subjects | Environ. Res. | 137 | 419–423 |
| Eastman Chemical Company | 2014 | Why Eastman 168 Is a Non-Phthalate Plasticizer: A Regulatory Memo | Eastman Chemical Company |  |  |
| Fisher, M., Arbuckle, T.E., Mallick, R., et al. | 2015 | Bisphenol A and phthalate metabolite urinary concentrations: Daily and across pregnancy variability | J. Expo Sci. Environ. Epidemiol. | 25 | 231–239 |
| Gore, A.C., Chappell, V.A., Fenton, S.E., et al. | 2015 | EDC-2: The Endocrine Society’s Second Scientific Statement on Endocrine-Disrupting Chemicals | Endocr. Rev. | 36 | E1–E150 |
| Güven, C., Dal, F., Aydo˘gan Ahbab, M., et al. | 2016 | Low dose monoethyl phthalate (MEP) exposure triggers proliferation by activating PDX-1 at 1.1B4 human pancreatic beta cells | Food Chem. Toxicol. | 93 | 41–50 |
| Huang, T., Saxena, A.R., Isganaitis, E., James-Todd, T. | 2014 | Gender and racial/ethnic differences in the associations of urinary phthalate metabolites with markers of diabetes risk: national health and nutrition examination survey 2001–2008 | Environmental Health | 13 | 6 |
| James-Todd, T.M., Meeker, J.D., Huang, T., et al. | 2016 | Pregnancy urinary phthalate metabolite concentrations and gestational diabetes risk factors | Environ. Int. | 96 | 118–126 |
| Kaaja, R.J., Greer, I.A. | 2005 | Manifestations of chronic disease during pregnancy | JAMA | 294 | 2751–2757 |
| Katsikantami, I., Sifakis, S., Tzatzarakis, M.N., et al. | 2016 | A global assessment of phthalates burden and related links to health effects | Environ. Int. | 97 | 212–236 |
| Kim, J.H., Park, H.Y., Bae, S., Lim, Y.-H., Hong, Y.-C. | 2013 | Diethylhexyl Phthalates Is Associated with Insulin Resistance via Oxidative Stress in the Elderly: A Panel Study | PLoS ONE | 8 | e71392 |
| Kumar, N., Sharan, S., Srivastava, S., Roy, P. | 2014 | Assessment of estrogenic potential of diethyl phthalate in female reproductive system involving both genomic and non-genomic actions | Reprod. Toxicol. | 49 | 12–26 |
| Lapinskas, P.J., Brown, S., Leesnitzer, L.M., et al. | 2005 | Role of PPARalpha in mediating the effects of phthalates and metabolites in the liver | Toxicology | 207 | 149–163 |
| Lessmann, F., Correia-S´a, L., Calhau, C., et al. | 2017 | Exposure to the plasticizer di(2-ethylhexyl) terephthalate (DEHTP) in Portuguese children - Urinary metabolite levels and estimated daily intakes | Environ. Int. | 104 | 25–32 |
| Lessmann, F., Kolossa-Gehring, M., Apel, P., et al. | 2019 | German Environmental Specimen Bank: 24-hour urine samples from 1999 to 2017 reveal rapid increase in exposure to the para-phthalate plasticizer di(2-ethylhexyl) terephthalate (DEHTP) | Environ. Int. | 132 | 105102 |
| Long, S.E., Kahn, L.G., Trasande, L., Jacobson, M.H. | 2021 | Urinary phthalate metabolites and alternatives and serum sex steroid hormones among pre- and postmenopausal women from NHANES, 2013–16 | Sci. Total Environ. | 769 | 144560 |
| Martínez-Ibarra, A., Martínez-Razo, L.D., V´azquez-Martínez, E.R., et al. | 2019 | Unhealthy Levels of Phthalates and Bisphenol A in Mexican Pregnant Women with Gestational Diabetes and Its Association to Altered Expression of miRNAs Involved with Metabolic Disease | Int. J. Mol. Sci. | 20 | 13 |
| Mauvais-Jarvis, F., Clegg, D.J., Hevener, A.L. | 2013 | The role of estrogens in control of energy balance and glucose homeostasis | Endocr. Rev. | 34 | 309–338 |
| Noor, N., Ferguson, K.K., Meeker, J.D., et al. | 2019 | Pregnancy phthalate metabolite concentrations and infant birth weight by gradations of maternal glucose tolerance | Int. J. Hyg. Environ. Health | 222 | 395–401 |
| Philips, E.M., Jaddoe, V.W.V., Deierlein, A., et al. | 2020 | Exposures to phthalates and bisphenols in pregnancy and postpartum weight gain in a population-based longitudinal birth cohort | Environ. Int. | 144 | 106002 |
| Picard, F., Auwerx, J. | 2002 | PPARγ and glucose homeostasis | Annu. Rev. Nutr. | 22 | 167–197 |
| Radke, E.G., Galizia, A., Thayer, K.A., Cooper, G.S. | 2019 | Phthalate exposure and metabolic effects: a systematic review of the human epidemiological evidence | Environ. Int. | 132 | 104768 |
| Rich-Edwards, J.W., McElrath, T.F., Karumanchi, A., Seely, E.W. | 2010 | Breathing life into the lifecourse approach: Pregnancy history and cardiovascular disease in women | Hypertension | 56 | 331–334 |
| Robledo, C.A., Peck, J.D., Stoner, J., et al. | 2015 | Urinary phthalate metabolite concentrations and blood glucose levels during pregnancy | Int. J. Hyg. Environ. Health | 218 | 324–330 |
| Schisterman, E.F., Vexler, A., Whitcomb, B.W., Liu, A. | 2006 | The Limitations due to Exposure Detection Limits for Regression Models | Am. J. Epidemiol. | 163 | 374–383 |
| Shaffer, R.M., Ferguson, K.K., Sheppard, L., et al. | 2019 | Maternal urinary phthalate metabolites in relation to gestational diabetes and glucose intolerance during pregnancy | Environ. Int. | 123 | 588–596 |
| Silva, M.J., Samandar, E., Preau, J.L., Reidy, J.A., Needham, L.L., Calafat, A.M. | 2007 | Quantification of 22 phthalate metabolites in human urine | J. Chromatogr. B Analyt. Technol. Biomed. Life Sci. | 860 | 106–112 |
| Silva, M.J., Wong, L.-Y., Samandar, E., Preau, J.L., Calafat, A.M., Ye, X. | 2017 | Exposure to di-2-ethylhexyl terephthalate in a convenience sample of U.S. adults from 2000 to 2016 | Arch. Toxicol. | 91 | 3287–3291 |
| Soma-Pillay, P., Catherine, N.-P., Tolppanen, H., Mebazaa, A. | 2016 | Physiological changes in pregnancy | Cardiovasc. J. Afr. | 27 | 89–94 |
| Sun, Qi, Cornelis, Marilyn C., Townsend, Mary K., et al. | 2014 | Association of Urinary Concentrations of Bisphenol A and Phthalate Metabolites with Risk of Type 2 Diabetes: A Prospective Investigation in the Nurses’ Health Study (NHS) and NHSII Cohorts | Environ. Health Perspect. | 122 | 616–623 | H. Wu et al.
Environment International 155 (2021) 106612

Tanner, E.M., Bornehag, C.-G., Gennings, C., 2019. Repeated holdout validation for weighted quantile sum regression. MethodsX. 6, 2855–2860.

Venkata, N.G., Robinson, J.A., Cabot, P.J., Davis, B., Monteith, G.R., Roberts-Thomson, S.J., 2006. Mono(2-ethylhexyl)phthalate and mono-n-butyl phthalate activation of peroxisome proliferator activated-receptors alpha and gamma in breast. Toxicol. Lett. 163 (3), 224–234.

Walczak, R., Tontonoz, P., 2002. PPARadigms and PPARadoxes: expanding roles for PPARγ in the control of lipid metabolism. J. Lipid Res. 43 (2), 177–186.

Webster, T.F., Weisskopf, M.G., 2021. Epidemiology of exposure to mixtures: we cant be casual about causality when using or testing methods.

Weisskopf, M.G., Seals, R.M., Webster, T.F., 2018. Bias Amplification in Epidemiologic Analysis of Exposure to Mixtures. Environ. Health Perspect. 126 (4), 047003

Wu, H., Kupsco, A.J., Deierlein, A.L., et al., 2020. Trends and Patterns of Phthalates and Phthalate Alternatives Exposure in Pregnant Women from Mexico City during 2007–2010. Environ. Sci. Technol. 54 (3), 1740–1749.

Zhao, C., Dong, J., Jiang, T., et al., 2011. Early second-trimester serum miRNA profiling predicts gestational diabetes mellitus. PLoS ONE 6 (8), e23925. 