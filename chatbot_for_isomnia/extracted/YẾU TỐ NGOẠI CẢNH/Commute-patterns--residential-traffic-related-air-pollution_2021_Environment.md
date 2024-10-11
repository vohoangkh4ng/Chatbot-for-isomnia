# Commute patterns, residential traffic-related air pollution, and lung cancer risk in the prospective UK Biobank cohort study

## A R T I C L E I N F O

**Keywords:**
Commute patterns
Outdoor air pollution
Lung cancer
Prospective cohort study
UK Biobank

## Introduction

Commuting exposes millions of people to carcinogens from traffic-related air pollution (TRAP) but is seldomly considered in epidemiologic studies of lung cancer. In the prospective United Kingdom (UK) Biobank cohort study, we investigated associations between commute patterns, residential nitrogen dioxide concentrations (NO2; a surrogate for TRAP), and lung cancer risk.

## Methods

We analyzed 234,124 employed participants at baseline (2006–2010). There were 493 incident lung cancer cases diagnosed over an average 7-year follow-up. Subjects were cross-classified into exclusive categories of commute mode (automobile, public transportation, walking, cycling, active mixture, and other mixture) and frequency (regular: 1–4, often: ≥5 work-bound trips/week). Annual average residential NO2 concentrations in 2005–2007 were estimated with land use regression. Multivariable Cox regression was used to estimate associations between commute patterns, NO2 quartiles, and incident lung cancer. We conducted analyses stratified by NO2 (>, ≤median = 28.3 μg/m3) and potential confounders such as sex and smoking.

## Results

Compared to regular automobile use, commuting often by public transportation was associated with increased lung cancer risk (hazard ratio (HR) = 1.58, 95% confidence intervals (CI):1.08–2.33). Additionally, we found a positive exposure–response relationship with residential NO2 (HRQ2 = 1.21, 95 %CI: 0.90–1.62; HRQ3 = 1.48, 95 %CI: 1.10–1.99; HRQ4 = 1.58, 95 %CI: 1.13–2.23; p-trend = 3.1 × 10 3). The public transportation association was observed among those with higher NO2 (p-interaction = 0.02). Other commute categories were not associated with risk.

## Conclusions

Commuters residing in high-NO2 areas who often use public transportation could have elevated lung cancer risk compared to regular automobile users. These results warrant investigations into which component(s) of public transportation contribute to the observed association with increased lung cancer risk.

## 1. Introduction

Lung cancer is a substantial public health burden among western countries. In the United Kingdom (UK), an average of 47,235 new cases were diagnosed per year in 2014–2016. Furthermore, lung cancer is a significant economic burden, with an estimated £10 billion spent annually on direct costs to the UK National Health Service (NHS) for treatment and care, along with £1 billion lost each year to missed workdays. Understanding modifiable lung cancer risk factors is crucial for developing population-level interventions. Besides cigarette smoking, other factors also contribute to lung carcinogenesis. One notable risk factor is traffic-related air pollution (TRAP), a complex mixture of components from motor vehicle emissions. TRAP is a significant contributor to outdoor air pollution and is composed of ultrafine, fine, and coarse particulate matter (PM), nitrogen oxides (NOx), sulfur oxides (SOx), metals, nitrated polycyclic aromatic hydrocarbons (nitro-PAHs) and other chemical compounds. Carcinogenic components of TRAP can infiltrate buildings and influence indoor air quality. Outdoor air pollution, which encompasses TRAP, is an established risk factor for lung cancer incidence and mortality. The nitrogen dioxide (NO2) component of TRAP is a widely accepted surrogate marker for outdoor concentrations and has been consistently associated with elevated lung cancer risk. However, the NO2-lung cancer associations were nominally stronger among the North American and Asian studies, and were marginally non-significant among European studies. Additionally, a recent study of never-smokers from the Women’s Health Initiative did not detect associations between NO2, PM2.5, and lung cancer risk. As such, further investigations are warranted.

A recent systematic literature review of commuting exposure and health outcomes suggested that few epidemiologic studies of cancer have considered or accounted for work-related commuting, an important source of TRAP exposure. To our knowledge, no prospective cohort study has reported associations between commute patterns and lung cancer risk. Commuters are especially impacted by TRAP due to their proximity and time spent near emission sources. Outdoor TRAP concentrations are correlated with roadway and population density in urban areas and vary by mode of transportation, which commonly includes automobiles, public transportation (e.g., buses, subways, and light rail), bicycles, and walking. Interestingly, TRAP concentrations at residences were found to be unrelated to neighborhood socioeconomic status in the UK, which makes it an encompassing environmental concern.

The relationships between commute patterns, exposure to outdoor residential TRAP, and lung cancer risk remain unclear. Our primary study aim was to assess whether commute mode and frequency, with focus on comparing public transportation to automobile use, is associated with risk of incident lung cancer, adjusted for outdoor residential NO2 levels and other confounders. Additionally, we explored whether this potential relationship differed by smoking status, sex, and outdoor residential NO2 levels in separate stratified analyses. Our secondary aim sought to provide additional evidence for a potential NO2-lung cancer relationship suggested in previous meta-analyses of European studies.

### Methods

#### Study design

The study design and data access procedures of the UK Biobank have been described. Briefly, the initial target population was adults aged 40–69 years who resided within 40 km of 22 assessment centers across the UK. Of the 9.2 million individuals registered in the UK’s National Health Service (NHS) who were mailed study invitations, 503,317 individuals (5.5%) responded and visited the study assessment centers in 2006–2010. Participants were administered touchscreen questionnaires, received physical examinations, and provided biological samples. Data from 502,616 participants were initially available and our analytic sample size was 234,124 after exclusions.

| UK Biobank Dataset (n=502,616) | Excluded: |
|----------------------------------|-----------|
| n=14,634 for genetic vs. reported sex discrepancy | n=304 for data quality issues/immunologic hematologic disorders |
| n=6,210 for baseline | n=43,801 for any baseline cancer diagnosis |
| n=64 for study withdrawal | n=36,150 for residing in sparse or remote geographic regions |
| n=64,020 who were not working and did not have commuting data | n=3,309 who did not have NO2 data |

| Analytic Sample (n=234,124) | Prospective Follow-Up |
|------------------------------|-----------------------|
| n=493 incident lung cancer cases (outcome) | n=2,733 died or administratively censored |
| n=230,898 no outcome; death, or censoring by end of follow-up |  |

For each participant, follow-up time started at the date of visit to the assessment center and ended at the date of primary incident lung cancer diagnosis (outcome), death (censored), or administrative censoring. Using ArcGIS Pro, we generated a density heat-map of the study population’s residences in the UK based on their north and east grid coordinates (1 km² resolution). Density (sq km)
| Location               | Density |
|-----------------------|---------|
| Aberdeen              | 33.7    |
| Dundee                |         |
| Glasgow               |         |
| Edinburgh             |         |
| Hunterston            |         |
| Gateshead             |         |
| South Shields         |         |
| Teesport              |         |
| Leeds                 |         |
| Liverpool             |         |
| Manchester            |         |
| Sheffield             |         |
| Stoke-on-Trent        |         |
| Nottingham            |         |
| Birmingham            |         |
| Cambridge             |         |
| Oxford                |         |
| Cardiff               |         |
| London                |         |
| Bristol               |         |
| Reading               |         |
| Southampton           |         |
| Fawley                |         |

Fig. 2. Density heat-map of the study population’s residences in the United Kingdom based on north and east grid coordinates (1 km2 resolution), generated using ArcGIS Pro.

January 31, 2016 for England and Wales and November 30, 2015 for Scotland), whichever came first. The NHS Information Centre and the NHS Central Register Scotland provided vital status, as well as date and primary underlying cause of death for participants. The UK Biobank study was approved by the National Information Governance Board for Health and Social Care and the NHS North West Multicenter Research Ethics Committee. Electronic informed consent was obtained from all volunteer participants.

2.2. Mode, frequency, and distance of commute

Commute data were available for a subset of participants who answered employment-related questions at baseline. Among those who were currently working, the commute variables of interest included mode of travel (i.e., automobile only, public transportation only, cycle only, walk only, active mixture of cycling and walking, other mixture, missing/unknown), frequency (number of work-bound trips/week), and distance between home and work (km). We analyzed commute frequency dichotomized as regular: 1–4 and often: ≥5 work-bound trips/ ## 2.3. Outdoor residential NO2 concentrations

Exposure assessment and modeling of outdoor NO2 concentrations of baseline residential location were previously described. Briefly, air pollution estimates in 2005–2007 were derived from European Union (EU)-wide air pollution maps with 100 × 100 m resolution generated with land use regression (LUR) models. The grid coordinates of the residences of the UK Biobank participants were overlaid on these maps projected to the British National Grid and assigned their corresponding NO2 concentrations. Annual average NO2 concentrations were derived for each participant and were subsequently analyzed as quartiles (Q), dichotomized at the median, and continuous (per 10 μg/m3).

## 2.4. Lung cancer ascertainment

Incident and prevalent cancer diagnoses were provided to UK Biobank by the Health and Social Care Information Centre (HSCIC) and the NHS Central Register (NHSCR). Details of the lung cancer ascertainment can be found at the UK Association of Cancer Registries. Lung cancer diagnosis was defined by International Classification of Diseases 10th revision (ICD-10 codes) C34.0-C34.9. ICD-O-3 code 8140 was used to define adenocarcinoma, while 8052, 8084, 8073, and 8083 were used for squamous cell carcinoma (SCC).

## 2.5. Covariates

The baseline questionnaire collected information on various demographics, lifestyle factors, socioeconomic status, and anthropometric measurements. A detailed 25-level smoking variable was created as previously described. A cross-classification variable for sex and smoking was created for subsequent analyses (i.e., never-smoking women, never-smoking men, former-smoking women, former-smoking men, current-smoking women, current-smoking men, female cigar smokers, male cigar smokers, unknown/missing). We also created a variable for smoking duration (years) based on age started and stopped smoking and age at recruitment. A 6-level variable for alcohol intake was generated by combining data on drinking status and intensity (never, former, current infrequent (<3 times per month), current modest (<1 drink per day), current frequent (≥1 to ≤3 drinks per day), and current heavy (>3 drinks per day)). Body mass index (BMI) was categorized as <18.5, ≥18.5 to <25.0, ≥25.0 to <30.0, ≥30.0 to <35.0, and ≥35.0 kg/m2. Self-reported race/ethnicity/ancestry was categorized as European, Asian (East and South), Black (African ancestry), mixed, other, and missing/unknown/no answer. Annual income was categorized as <£18,000, £18,000–£30,999, £31,000–£51,999, £52,000–100,000, >£100,000, and missing/no answer/unknown. We created an indicator variable for current employment in high-risk occupations/industries for lung cancer based on the Health and Safety Executive (HSE) 2012 report using 172 unique UK Standard Occupational Classification (SOC) 2000 occupation/industry codes that were derived via crosswalk with SOC 1990 codes.

## 3. Statistical analyses

### 3.1. Main analyses

Multivariable Cox regression models were used to estimate hazard ratios (HR) and 95% confidence intervals (CI) of incident lung cancer in relation to: (1) commute mode and frequency adjusted for residential NO2 quartiles in 2005, and (2) residential NO2 quartiles in 2005 adjusted for commute mode and frequency. These models were further adjusted for age at recruitment (continuous), a sex-smoking cross-classification variable (reference: never-smoking women), smoking duration (years), self-reported race/ethnicity/ancestry (reference: European), study assessment center, BMI (reference: ≥18.5 to <25.0 kg/m2), annual income (reference: £18,000–£30,999), commute distance (reference: <4.82 km), and alcohol intake (reference: never-drinker). Follow-up time (days; “time-on-study”) was used as the underlying timescale.

We also considered physical activity (days/week with >10 mins of moderate-vigorous activity), secondhand smoke (SHS) exposure, self-reported respiratory disease at/before baseline, and current employment in a high-risk occupation/industry for lung cancer as covariates in the model. However, they did not change the estimates >10% and a more parsimonious model was chosen.

The analyses were further stratified by sex (male, female), age (≥ and < median of 53 years), smoking status (ever- and never-smoking), NO2 in 2005 (> and ≤ median of 28.33 μg/m3), length of time living at current residence (≥ and < 25 years chosen based on evidence of approximate exposure-disease latency); ≥ and < median of 13 years), commute distance (> and ≤ median of 8.0 km), annual income (> and ≤£30,999), and main job duration (> and ≤10 years). Multiplicative effect modification was tested using interaction terms. When testing for effect modification in the Cox regression models, smoking was categorized as ever vs. never and sex was analyzed as male vs. female. We tested for effect modification of the indicator variables for commute mode/frequency by: (1) ever vs. never smoking, (2) male vs. female, (3) ordinal categories of outdoor residential NO2, and (4) continuous age. Additionally, we tested for effect modification of outdoor residential NO2 by: (1) ever vs. never smoking, (2) male vs. female, (3) continuous age, (4) length at current residence, (5) commute distance, (6) income, and (7) job duration. Missing categorical data were handled in the analyses by classifying subjects with missing data in a separate categorical indicator variable.

### 3.2. Sensitivity analyses

We also conducted a sensitivity analysis restricted to European participants to assess the influence of race/ethnicity/ancestry. Additionally, we restricted to those who reported not being exposed to SHS (<1 h/week) and those who reported never having a history of respiratory diseases in separate analyses. To investigate the influence of occupational diesel exhaust on our findings, we excluded 870 participants who reported being often exposed at work at baseline, as well as 286 participants who reported being often exposed in all past jobs. We also conducted additional analyses with confirmed lung cancer histological subtypes (i.e., adenocarcinoma and SCC) as outcomes. Smoking duration is arguably the most consistent measure of tobacco use related to lung cancer risk; however, we did not have complete data on smoking behavior (multiple starts and cessations) throughout the lifecourse. We conducted a sensitivity analysis that excluded ever-smokers who reported quitting >6 months any time before baseline to evaluate its potential influence on lung cancer and smoking duration. Additionally, we restricted analyses to current smokers and stratified by median smoking duration (≥ and <36 years) and separately by smoking intensity (≥ and <20 cigs/day).

SAS version 9.4 and the computational resources of the National Institutes of Health’s (NIH) High-Performance Computing Biowulf cluster were used to conduct the analyses. P-values <0.05 were considered significant. To conservatively account for multiple comparisons, we indicated highly significant p-values below a Bonferroni-adjusted alpha threshold of 0.0026 (0.05/19 total tests) in the tables showing the commute-lung cancer results. ## Results

### Table 1
UK Biobank Study Population Characteristics at Baseline (n = 234,124)

| Commute type and frequency (regular: 1–4, often: ≥5 work-bound trips/week) | n          | %       |
|---------------------------------------------------------------------------|------------|---------|
| Automobile only, regular                                                  | 39,140     | 16.72   |
| Automobile only, often                                                    | 93,204     | 39.81   |
| Walk only, regular                                                        | 3,677      | 1.57    |
| Walk only, often                                                          | 7,964      | 3.40    |
| Public transportation only, regular                                        | 5,935      | 2.53    |
| Public transportation only, often                                          | 13,598     | 5.81    |
| Cycle only, regular and often                                             | 5,114      | 2.18    |
| Active mixture of walking and cycling, regular and often                  | 8,405      | 3.59    |
| Other mixture, regular and often                                           | 16,969     | 7.25    |
| Unknown, missing, no answer                                               | 40,118     | 17.13   |
| Commute distance (km), median, IQR                                       | 9.65 (9.65–19.31) |         |
| Outdoor residential NO2 concentration, annual average (μg/m3), median, IQR |            |         |
| 2005                                                                     | 28.33 (23.08, 34.66) |         |
| 2006                                                                     | 27.84 (22.79, 33.27) |         |
| 2007                                                                     | 28.85 (23.61, 34.90) |         |
| ONS-defined urban density of residential location, n, %                  |            |         |
| England/Wales – Urban – sparse                                            | 2 (0.0009) |         |
| England/Wales – Urban – less sparse                                       | 202,004    | 86.28   |
| England/Wales – Town and Fringe – less sparse                             | 15,858     | 6.77    |
| Scotland – Large Urban Area                                               | 13,672     | 5.83    |
| Scotland – Other Urban Area                                               | 2,588      | 1.10    |
| Study Assessment Center, n, %                                            |            |         |
| Stockport                                                                 | 278        | 0.12    |
| Manchester                                                                | 7,429      | 3.17    |
| Oxford                                                                    | 6,432      | 2.75    |
| Cardiff                                                                   | 8,992      | 3.84    |
| Glasgow                                                                   | 8,909      | 3.80    |
| Edinburgh                                                                 | 7,350      | 3.14    |
| Stoke                                                                     | 84,450     | 3.61    |
| Reading                                                                   | 14,202     | 6.07    |
| Bury                                                                      | 13,153     | 5.62    |
| Newcastle                                                                 | 16,984     | 7.25    |
| Leeds                                                                     | 21,082     | 9.00    |
| Bristol                                                                   | 20,381     | 8.70    |
| Barts                                                                     | 7,041      | 3.01    |
| Nottingham                                                                | 14,976     | 6.40    |
| Sheffield                                                                 | 13,317     | 5.69    |
| Liverpool                                                                 | 14,594     | 6.23    |
| Middlesborough                                                             | 8,568      | 3.66    |
| Hounslow                                                                  | 14,865     | 6.35    |
| Croydon                                                                   | 13,959     | 5.96    |
| Birmingham                                                                | 12,074     | 5.16    |
| Swansea                                                                   | 834        | 0.36    |
| Wrexham                                                                   | 254        | 0.11    |

### 4.2. Associations between commute patterns and risk of lung cancer

There were 493 incident lung cancer cases diagnosed among 1.63 million person-years over an average 7-year follow-up (10-year maximum). Among the cases, the median time interval from baseline to lung cancer diagnosis was 3.5 years (IQR: 2.1–4.9).

Compared to regular automobile use, commuting often only by public transportation was associated with elevated lung cancer risk (HR = 1.58, 95% CI: 1.08–2.33, p = 0.02), adjusted for residential NO2 and other potential confounders. In the stratified analyses, the association was observed among ever-smokers, men, and participants living in high-NO2 areas.

The public transportation-lung cancer associations were modestly stronger among those who lived at their current residence for ≥13 years (HR = 1.70, 95% CI: 1.04, 2.76, p = 0.03); among those who lived at their current residence for <25 years (HR = 1.62, 95% CI: 1.02, 2.56, p = 0.04); and among those who earned ≤£30,999 per year (HR = 1.88, 95% CI: 1.12, 3.16, p = 0.02). Conversely, the main findings were similar, but not significant, among participants ≥53 years of age and those with a commute distance ≥8.0 km.

There was evidence of multiplicative interactions between commuting often by public transportation and residential NO2 interaction and sex, but not smoking status and age. Other categories of commuting were not associated with lung cancer risk.

While the direction of the association with often using only public transportation was the same for overall lung cancer and lung adenocarcinoma, no significant associations were found with the histological subtypes. However, the case numbers for subtype analyses were limited. When the analyses were stratified by main job duration, the magnitude of the estimates were generally consistent with Table 1 (continued)
| Income Level                          | n, %          |
|---------------------------------------|---------------|
| £52,000–£100,000                     | 59,622 (25.47)|
| >£100,000                             | 14,929 (6.38) |
| Missing/no answer/do not know         | 22,596 (9.65) |

Sex-smoking status cross-classification, n, %
| Category                               | n, %          |
|---------------------------------------|---------------|
| Female, never-smoker                  | 72,189 (30.83)|
| Female, former-smoker                 | 34,868 (14.89)|
| Female, current-smoker                | 11,013 (4.70) |
| Female, cigar-smoker                  | 85 (0.04)     |
| Male, never-smoker                    | 62,143 (26.54)|
| Male, former-smoker                   | 37,359 (15.96)|
| Male, current-smoker                  | 13,152 (5.62) |
| Male, cigar-smoker                    | 2,654 (1.13)  |
| Unknown/missing                       | 661 (0.28)    |

Secondhand smoke exposure at home or outside, n, %
| Exposure Status                        | n, %          |
|---------------------------------------|---------------|
| Unexposed (<1 h/week)                 | 185,993 (79.44)|
| Exposed (≥1 h/week)                   | 48,131 (20.56) |

History of respiratory disease, n, %
| Status                                 | n, %          |
|---------------------------------------|---------------|
| No                                    | 206,018 (88.00)|
| Yes                                   | 28,106 (12.00) |

Alcohol Consumption, n, %
| Consumption Level                     | n, %          |
|---------------------------------------|---------------|
| Never                                 | 8,273 (3.53)  |
| Former                                | 6,427 (2.74)  |
| Current, <3 drinks/month             | 51,709 (22.09)|
| Current, <1 drink/day                | 59,087 (25.24)|
| Current, 1–3 drinks/day              | 87,967 (37.57)|
| Current, >3 drinks/day               | 20,394 (8.71) |
| Missing                               | 267 (0.11)    |

Time to diagnosis of incident lung cancer, years, median, IQR
| Time                                   | Value         |
|---------------------------------------|---------------|
| Median                                 | 3.5 (2.1–4.9) |

the overall analyses, but similarly imprecise. Excluding ever-smokers who reported ever quitting for >6 months before baseline did not considerably change the estimates. Among current smokers, the estimates for those who smoked <36 years and ≥36 years, and <20 cigs/day and ≥20 cigs/day were similar to estimates from the overall analyses; however, the case numbers in the strata were limited. Lastly, excluding those who reported often being exposed to occupational diesel engine exhaust did not affect the results.

4.3. Associations between residential outdoor NO2 and risk of lung cancer

We found a positive exposure–response relationship between residential NO2 and lung cancer risk (p-trend = 3.1 × 10 3). The association was driven by the two highest quartiles of NO2-exposure (HRQ2 = 1.21, 95 %CI: 0.90–1.62; HRQ3 = 1.48, 95 %CI: 1.10–1.99; HRQ4 = 1.58, 95 %CI: 1.13–2.23) while mutually adjusted for commute patterns and other potential confounders. When analyzed as a continuous variable, each 10 μg/m3 increase in NO2 was associated with a 1.02 (95% CI: 1.00–1.03, p = 0.01) times increase in risk. The exposure–response relationship was apparent among participants who lived in their current residence <25 years, but not ≥25 years; which was similar when stratified by a median of 13 years. Further, the trend was apparent among those who commuted ≥8.0 km, but not <8.0 km. We found some evidence for a positive interaction between NO2 and ever-smoking.

Restricting the analyses to those of European ancestry, those who were not exposed to SHS, and those who reported not having respiratory diseases at/before baseline had little or no impact on the risk estimates for both commute patterns and NO2.

5. Discussion

In our primary analyses, we found that commuting often and exclusively by public transportation was associated with increased lung cancer risk compared to regularly commuting only by automobile, among those residing in high-NO2 areas and men. In our secondary analyses, we found a positive exposure–response relationship between residential NO2 concentrations and lung cancer risk that was in agreement with previous meta-analyses of European studies. There was some evidence that ever smoking strengthened the NO2-lung cancer association, which was consistent with findings from a study of air pollution, smoking, and lung cancer mortality in the U.S. Cancer Prevention Study cohort. However, another study of PM and lung cancer risk found stronger associations among never-smokers. Taken together, our findings suggest that the elevated lung cancer risk found among those who often use public transportation could be enhanced by residing in areas with high NO2 levels, which is a surrogate for levels of TRAP.

Several studies have found the highest concentrations of certain air pollutants (e.g., PM and black carbon) were in public transportation microenvironments (e.g., urban buses and subways), followed by automobiles, urban cycling and walking, and suburban walking. In particular, the higher particulate levels in public buses compared to automobiles in London, UK and Dublin, Ireland are thought to be attributed to lower infiltration of particulates into automobile cabins or perhaps differences in fuel types. In contrast, some studies have found higher air pollutant concentrations in automobiles, followed by buses and other active commute modes. There is a high degree of variance between modes of travel and these trends can depend on many factors including the time of daily commute, season, city and country, route density.

Table 2
Commute patterns and risk of incident lung cancer in the UK Biobank.
| Commute Pattern                          | No. incident lung cancer cases | Total No. of Subjects | Cumulative person-years | HR  | 95 %CI Lower | 95 %CI Upper | p-Value |
|------------------------------------------|-------------------------------|-----------------------|------------------------|-----|---------------|---------------|---------|
| Automobile only, regular (Reference)    | 78                            | 39,140                | 272,768                | 1.00| –             | –             | –       |
| Automobile only, often                    | 202                           | 93,204                | 655,529                | 1.26| 0.96          | 1.64          | 0.10    |
| Public transportation only, regular       | 10                            | 5,935                 | 39,999                 | 0.71| 0.37          | 1.39          | 0.32    |
| Public transportation only, often         | 44                            | 13,598                | 92,144                 | 1.58| 1.08          | 2.33          | 0.02*   |
| Walk only, regular                        | 14                            | 3,677                 | 25,427                 | 1.58| 0.87          | 2.88          | 0.13    |
| Walk only, often                          | 19                            | 7,964                 | 55,933                 | 1.14| 0.67          | 1.95          | 0.63    |
| Cycle only, regular and often             | 5                             | 5,114                 | 36,244                 | 0.78| 0.31          | 1.95          | 0.59    |
| Active mixture, regular and often         | 14                            | 8,405                 | 58,790                 | 1.10| 0.61          | 1.99          | 0.74    |
| Other mixture, regular and often          | 28                            | 16,969                | 117,377                | 1.05| 0.68          | 1.62          | 0.83    |
| Unknown, missing, no answer               | 79                            | 40,118                | 277,823                | 1.04| 0.72          | 1.49          | 0.84    |

*P-values < 0.05. **P-values below a Bonferroni adjusted alpha-threshold of 0.0026. Analyses were restricted to currently working participants. Travel frequency: regular: 1–4, often: ≥5 work-bound trips/week. II) Cox regression model was adjusted for average annual residential NO, age, sex-smoking status, smoking duration, study site, race/ethnicity, body mass index, alcohol, income, and commute distance. Abbreviations: Hazard Ratio (HR), Confidence Intervals (CI). There were 17,111 employed participants, including 33 lung cancer cases, who reported commuting zero times a week and did not report commute mode. These participants were assigned to the missing/unknown/no answer indicator category. Table 3
Commute patterns and risk of incident lung cancer among ever- and never-smokers of the UK Biobank.

| (I) Ever-Smokers | No. incident lung cancer cases | Total No. of subjects | person-years | Cumulative HR | 95 % CI Lower | 95 % CI Upper | p-Value | (II) Never-Smokers | No. incident lung cancer cases | Total No. of subjects | person-years | Cumulative HR | 95 % CI Lower | 95 % CI Upper | p-Value |
|------------------|-------------------------------|-----------------------|--------------|----------------|----------------|----------------|---------|--------------------|-------------------------------|-----------------------|--------------|----------------|----------------|----------------|---------|
| Automobile only, regular (Reference) | 58 | 16,342 | 113,781 | 1.00 | – | – | – | 20 | 2,798 | 158,987 | 1.00 | – | – | – |
| Automobile only, often | 17 | 640 | 557 | 284,718 | 1.41 | 1.04 | 1.92 | 0.03* | 26 | 52,647 | 370,811 | 0.75 | 0.41 | 1.36 | 0.34 |
| Public transportation only, regular | 8 | 2,535 | 17,034 | 0.73 | 0.35 | 1.55 | 0.42 | 23 | 4,400 | 22,965 | 0.67 | 0.15 | 2.88 | 0.59 |
| Public transportation only, often | 39 | 5,851 | 39,634 | 1.76 | 1.15 | 2.69 | 0.01* | 57 | 7,747 | 52,510 | 0.98 | 0.35 | 2.70 | 0.96 |
| Walk only, regular | 11 | 1,517 | 10,505 | 1.52 | 0.77 | 2.99 | 0.22 | 32 | 1,160 | 14,922 | 2.11 | 0.57 | 7.82 | 0.27 |
| Walk only, often | 17 | 3,332 | 23,396 | 1.20 | 0.68 | 2.14 | 0.53 | 24 | 6,632 | 32,538 | 0.85 | 0.18 | 3.96 | 0.84 |
| Cycle only, regular and often | 22 | 150 | 15,190 | 0.41 | 0.10 | 1.71 | 0.22 | 32 | 964 | 21,054 | 2.00 | 0.56 | 7.19 | 0.29 |
| Active mixture, regular and often | 133 | 214 | 22,473 | 1.36 | 0.73 | 2.54 | 0.33 | 15 | 191 | 36,317 | 0.35 | 0.05 | 2.68 | 0.31 |
| Other mixture, regular and often | 226 | 792 | 46,769 | 1.13 | 0.69 | 1.85 | 0.64 | 6 | 10,177 | 70,608 | 0.82 | 0.32 | 2.05 | 0.66 |
| Unknown, missing, no answer | 591 | 7,502 | 121,129 | 0.93 | 0.61 | 1.40 | 0.72 | 202 | 2,616 | 156,694 | 1.63 | 0.79 | 3.36 | 0.18 |

*P-values <0.05. **P-values below a Bonferroni adjusted alpha-threshold of 0.0026. Analyses were restricted to currently working participants living. There were 405 lung cancer cases among 99,792 ever-smokers and 88 cases among 134,332 never-smokers. Travel frequency: regular: 1–4, often: ≥5 work-bound trips/week. Cox regression model was adjusted for average annual residential NO, age, sex, study site, race/ethnicity, body mass index, alcohol, income, and commute distance. Ever-smokers were further adjusted for smoking duration. Abbreviations: Hazard Ratio (HR), Confidence Intervals (CI).

Table 4
Commute patterns and risk of incident lung cancer among men and women of the UK Biobank.

| (I) Men | No. incident lung cancer cases | Total No. of subjects | person-years | Cumulative HR | 95 % CI Lower | 95 % CI Upper | p-Value | (II) Women | No. incident lung cancer cases | Total No. of subjects | person-years | Cumulative HR | 95 % CI Lower | 95 % CI Upper | p-Value |
|---------|-------------------------------|-----------------------|--------------|----------------|----------------|----------------|---------|------------|-------------------------------|-----------------------|--------------|----------------|----------------|----------------|---------|
| Automobile only, regular (Reference) | 31 | 3,734 | 95,550 | 1.00 | – | – | – | 47 | 25,406 | 177,218 | 1.00 | – | – | – |
| Automobile only, often | 13 | 554 | 195 | 380,743 | 1.48 | 0.99 | 2.20 | 0.06 | 67 | 39,009 | 274,786 | 1.07 | 0.73 | 1.57 | 0.72 |
| Public transportation only, regular | 31 | 947 | 12,958 | 0.71 | 0.22 | 2.35 | 0.57 | 73 | 988 | 27,041 | 0.69 | 0.31 | 1.55 | 0.37 |
| Public transportation only, often | 32 | 6,159 | 41,466 | 2.51 | 1.49 | 4.22 | 5.4 × 10 | 127 | 439 | 50,678 | 0.78 | 0.40 | 1.49 | 0.44 |
| Walk only, regular | 46 | 62 | 4,586 | 2.48 | 0.84 | 7.35 | 0.10 | 103 | 15 | 20,841 | 1.30 | 0.62 | 2.70 | 0.48 |
| Walk only, often | 82 | 989 | 20,997 | 1.42 | 0.62 | 3.26 | 0.40 | 114 | 975 | 34,936 | 0.96 | 0.47 | 1.94 | 0.90 |
| Cycle only, regular and often | 23 | 411 | 24,046 | 0.51 | 0.12 | 2.15 | 0.36 | 31 | 703 | 12,198 | 1.36 | 0.41 | 4.50 | 0.62 |
| Active mixture, regular and often | 42 | 538 | 17,838 | 1.06 | 0.37 | 3.09 | 0.91 | 105 | 867 | 40,953 | 1.06 | 0.52 | 2.16 | 0.88 |
| Other mixture, regular and often | 97 | 815 | 53,916 | 0.78 | 0.37 | 1.65 | 0.52 | 199 | 154 | 63,461 | 1.24 | 0.72 | 2.12 | 0.44 |
| Unknown, missing, no answer | 44 | 22 | 185 | 153,644 | 1.07 | 0.64 | 1.81 | 0.79 | 35 | 17 | 933 | 124,179 | 1.06 | 0.63 | 1.76 | 0.84 |

*P-values < 0.05. **P-values below a Bonferroni adjusted alpha-threshold of 0.0026. Analyses were restricted to currently working participants. Travel frequency: regular: 1–4, often: ≥5 work-bound trips/week. Cox regression model was adjusted for average annual residential NO, age, smoking status and duration, study site, race/ethnicity, body mass index, alcohol, income, and commute distance. Abbreviations: Hazard Ratio (HR), Confidence Intervals (CI). Table 5
Commute patterns and risk of incident lung cancer among residences with high and low outdoor NO2 concentrations in the UK Biobank.

| Commute Type                     | (I) High NO2 residences (>28.33 μg/m³) | (II) Low NO2 residences (≤28.33 μg/m³) |
|----------------------------------|----------------------------------------|----------------------------------------|
|                                  | No. incident lung cancer cases         | Total No. of subjects                  | person-years | Cumulative HR | 95 % CI Lower | 95 % CI Upper | p-Value | No. incident lung cancer cases | Total No. of subjects | person-years | Cumulative HR | 95 % CI Lower | 95 % CI Upper | p-Value |
| Automobile only, regular         | 351                                  | 7,758                                  | 122,459     | 1.00          | –              | –              | –       | 432                                  | 1,382              | 150,309     | 1.00          | –              | –              | –       |
| Automobile only, often           | 114                                  | 45,708                                 | 318,514     | 1.44          | 0.98           | 2.12           | 0.07    | 88                                   | 47,496            | 337,016     | 1.12          | 0.77           | 1.64           | 0.55    |
| Public transportation, regular    | 64                                   | 246                                    | 27,976      | 0.70          | 0.29           | 1.68           | 0.43    | 41                                   | 689               | 12,023      | 0.88          | 0.31           | 2.47           | 0.81    |
| Public transportation, often      | 401                                  | 10,389                                 | 68,982      | 2.23          | 1.40           | 3.57           | 8.2 × 10 | 43                                   | 209               | 23,162      | 0.53          | 0.19           | 1.50           | 0.23    |
| Walk only, regular               | 92                                   | 292                                    | 15,739      | 1.79          | 0.83           | 3.85           | 0.14    | 51                                   | 385               | 9,688       | 1.46          | 0.54           | 3.91           | 0.45    |
| Walk only, often                 | 135                                  | 412                                    | 37,749      | 1.22          | 0.62           | 2.40           | 0.56    | 62                                   | 552               | 18,184      | 1.24          | 0.50           | 3.09           | 0.65    |
| Cycle only, regular              | 33                                   | 397                                    | 23,357      | 0.78          | 0.24           | 2.59           | 0.69    | 21                                   | 717               | 12,887      | 0.90          | 0.21           | 3.87           | 0.89    |
| Cycle only, often                | 74                                   | 816                                    | 33,498      | 1.05          | 0.46           | 2.42           | 0.91    | 73                                   | 589               | 25,292      | 1.28          | 0.55           | 2.95           | 0.57    |
| Active mixture, regular          | 179                                  | 825                                    | 66,499      | 1.20          | 0.67           | 2.15           | 0.54    | 117                                  | 144               | 50,878      | 0.94          | 0.48           | 1.83           | 0.86    |
| Active mixture, often            | 572                                   | 4,346                                  | 165,313     | 1.36          | 0.85           | 2.19           | 0.20    | 22                                   | 15,772            | 112,510     | 0.73          | 0.40           | 1.34           | 0.31    |

*P-values <0.05. **P-values below a Bonferroni adjusted alpha-threshold of 0.0026. Analyses were restricted to currently working participants. Travel frequency: regular: 1–4, often: ≥5 work-bound trips/week. Cox regression model was adjusted for continuous age, sex-smoking status, smoking duration, study site, race/ethnicity, body mass index, alcohol, income, and commute distance. Abbreviations: Hazard Ratio (HR), Confidence Intervals (CI). Table 6
Traffic-related air pollution as reflected by annual average residential NO2 concentrations and risk of incident lung cancer in the UK Biobank.

| Annual average residential NO2 concentration in 2005, μg/m3 | No. incident lung cancer cases | Total No. of Subjects | Cumulative person-years | HR  | 95 %CI Lower | 95 %CI Upper | p-Value |
|--------------------------------------------------------------|-------------------------------|-----------------------|------------------------|-----|---------------|---------------|---------|
| Q1, ≤23.08                                                  | 70                            | 44,622                | 315,803                | 1.00|               |               |         |
| Q2, >23.08 to ≤28.33                                        | 122                           | 61,313                | 436,147                | 1.21| 0.90          | 1.62          | 0.21    |
| Q3, >28.33 to ≤34.66                                        | 153                           | 62,967                | 444,468                | 1.48| 1.10          | 1.99          | 9.2 × 10−3 |
| Q4, >34.66                                                  | 148                           | 65,222                | 435,618                | 1.58| 1.13          | 2.23          | 8.3 × 10−3 |
|                                                              |                               |                       |                        |     |               |               |         |
| p-trend                                                     |                               |                       |                        |     |               |               | 3.1 × 10−3 |
| Continuous, per 10 μg/m3 increase                           | 493                           | 234,124               | 1,632,035              | 1.02| 1.00          | 1.03          | 0.01* |

*P-values <0.05. Analyses were restricted to currently working participants. Cox regression model was adjusted for commute mode, frequency, and distance, along with age, sex-smoking status, smoking duration, study site, race/ethnicity, body mass index, alcohol, and income. Abbreviations: Hazard Ratio (HR), Confidence Intervals (CI), Quartile (Q).

residential TRAP components. PM2.5 measurements started in 2010, a few years into the prospective follow-up in which many of the incident lung cancer cases had already occurred. Lastly, we did not have information on time spent commuting, a likely determinant of TRAP exposure. However, we accounted for commute distance, which is correlated with commute time within modes of travel.
In conclusion, our findings suggest that commuters who frequently used public transit could be at greater risk for lung cancer compared to commuters who regularly used automobiles. This increased risk could be further enhanced by residing in areas with high levels of NO2, which is a surrogate measure of overall outdoor TRAP levels. However, caution is recommended when interpreting these results. We emphasize that NO2 and TRAP levels experienced while commuting are not addressed in our study and can be largely different from NO2 and TRAP levels at the place of residence, with some overlapping constituents. There are numerous global and public health benefits of public transit. The overall health benefits of active travel may outweigh the risks related to air pollution exposure. Our findings require replication and refinement to determine which, if any, component of public transportation use might be associated with lung cancer risk. It is important to explore further in a larger sample of never-smokers as well as smokers. Future studies would also benefit from assessing commute duration and personal TRAP exposure along travel routes and within transit microenvironments. J.Y.Y. Wong et al.
Environment International 155 (2021) 106698

| Author(s) | Year | Title | Journal | Volume | Pages |
|-----------|------|-------|---------|--------|-------|
| Brook, J.R., Burnett, R.T., Dann, T.F., Cakmak, S., Goldberg, M.S., Fan, X.H., Wheeler, A.J. | 2007 | Further interpretation of the acute effect of nitrogen dioxide observed in Canadian time-series studies | J. Expo Sci. Env. Epid. | 17 | S36–S44 |
| Brown, T., Cherrie, J., Van Tongeren, M.V., Fortunato, L., Hutchings, S., Rushton, L. | 2012 | The Burden of Occupational Cancer in Great Britain - Lung Cancer | Health and Safety Executive | | |
| Cancer Research UK | 2019 | | | | |
| Celis-Morales, C.A., Lyall, D.M., Welsh, P., Anderson, J., Steell, L., Guo, Y.B., Maldonado, R., Mackay, D.F., Pell, J.P., Sattar, N., Gill, J.M.R. | 2017 | Association between active commuting and incident cardiovascular disease, cancer, and mortality: prospective cohort study | Bmj-Brit. Med. J. | 357 | |
| Cepeda, M., Schoufour, J., Freak-Poli, R., Koolhaas, C.M., Dhana, K., Bramer, W.M., Franco, O.H. | 2017 | Levels of ambient air pollution according to mode of transport: a systematic review | Lancet Public Health | 2 | e23–e34 |
| Cui, P., Huang, Y., Han, J., Song, F., Chen, K. | 2015 | Ambient particulate matter and lung cancer incidence and mortality: a meta-analysis of prospective studies | Eur. J. Public Health | 25 | 324–329 |
| Curren, K.C., Dann, T.F., Wang, D.K. | 2006 | Ambient air 1,3-butadiene concentrations in Canada (1995–2003): seasonal, day of week variations, trends, and source influences | Atmos. Environ. | 40 | 170–181 |
| Dinu, M., Pagliai, G., Macchi, C., Sofi, F. | 2019 | Active Commuting and Multiple Health Outcomes: A Systematic Review and Meta-Analysis | Sports Med. | 49 | 437–452 |
| Fan, M., Lv, J., Yu, C., Guo, Y., Bian, Z., Yang, S., Yang, L., Chen, Y., Huang, Y., Chen, B., Fan, L., Chen, J., Chen, Z., Qi, L., Li, L., China Kadoorie Biobank Collaborative, G. | 2019 | Association Between Active Commuting and Incident Cardiovascular Diseases in Chinese: A Prospective Cohort Study | J. Am. Heart Assoc. | 8 | e012556 |
| Fry, A., Littlejohns, T.J., Sudlow, C., Doherty, N., Adamska, L., Sprosen, T., Collins, R., Allen, N.E. | 2017 | Comparison of Sociodemographic and Health-Related Characteristics of UK Biobank Participants With Those of the General Population | Am. J. Epidemiol. | 186 | 1026–1034 |
| Gowda, S.N., DeRoos, A.J., Hunt, R.P., Gassett, A.J., Mirabelli, M.C., Bird, C.E., Margolis, H.G., Lane, D., Bonner, M.R., Anderson, G., Whitsel, E.A., Kaufman, J.D., Bhatti, P. | 2019 | Ambient air pollution and lung cancer risk among never-smokers in the Women’s Health Initiative | Environ. Epidemiol. | 3 | e076 |
| Hamra, G.B., Guha, N., Cohen, A., Laden, F., Raaschou-Nielsen, O., Samet, J.M., Vineis, P., Forastiere, F., Saldiva, P., Yorifuji, T., Loomis, D. | 2014 | Outdoor particulate matter exposure and lung cancer: a systematic review and meta-analysis | Environ. Health Perspect. | 122 | 906–911 |
| Hamra, G.B., Laden, F., Cohen, A.J., Raaschou-Nielsen, O., Brauer, M., Loomis, D. | 2015 | Lung Cancer and Exposure to Nitrogen Dioxide and Traffic: A Systematic Review and Meta-Analysis | Environ. Health Perspect. | 123 | 1107–1112 |
| Ito, K., Thurston, G.D., Silverman, R.A. | 2007 | Characterization of PM2.5, gaseous pollutants, and meteorological interactions in the context of time-series health effects models | J. Expo Sci. Environ. Epidemiol. | 17 (Suppl 2) | S45–S60 |
| Jones, N.C., Thornton, C.A., Mark, D., Harrison, R.M. | 2000 | Indoor/outdoor relationships of particulate matter in domestic homes with roadside, urban and rural locations | Atmos. Environ. | 34 | 2603–2612 |
| Jurj, A.L., Wen, W., Gao, Y.T., Matthews, C.E., Yang, G., Li, H.L., Zheng, W., Shu, X.O. | 2007 | Patterns and correlates of physical activity: a cross-sectional study in urban Chinese women | BMC Public Health | 7 | 213 |
| Karanasiou, A., Viana, M., Querol, X., Moreno, T., de Leeuw, F. | 2014 | Assessment of personal exposure to particulate air pollution during commuting in European cities–recommendations and policy implications | Sci. Total Environ. | 490 | 785–797 |
| Kaur, S., Nieuwenhuijsen, M.J., Colvile, R.N. | 2007 | Fine particulate matter and carbon monoxide exposure concentrations in urban street transport microenvironments | Atmos. Environ. | 41 | 4781–4810 |
| Loftfield, E., Cornelis, M.C., Caporaso, N., Yu, K., Sinha, R., Freedman, N. | 2018 | Association of Coffee Drinking With Mortality by Genetic Variation in Caffeine Metabolism: Findings From the UK Biobank | JAMA Intern. Med. | 178 | 1086–1097 |
| Lovett, C., Shirmohammadi, F., Sowlat, M.H., Sioutas, C. | 2018 | Commuting in Los Angeles: Cancer and Non-cancer Health Risks of Roadway, Light-Rail and Subway Transit Routes | Aerosol Air Qual. Res. | 18 | 2363–2374 |
| McNabola, A., Broderick, B.M., Gill, L.W. | 2008 | Relative exposure to fine particulate matter and VOCs between transport microenvironments in Dublin: Personal exposure and uptake | Atmos. Environ. | 42 | 6496–6512 |
| Moreno, T., Martins, V., Querol, X., Jones, T., BeruBe, K., Minguillon, M.C., Amato, F., Capdevila, M., de Miguel, E., Centelles, S., Gibbons, W. | 2015 | A new look at inhalable metalliferous airborne particles on rail subway platforms | Sci. Total Environ. | 505 | 367–375 |
| Patterson, R., Panter, J., Vamos, E.P., Cummins, S., Millett, C., Laverty, A.A. | 2020 | Associations between commute mode and cardiovascular disease, cancer, and all-cause mortality, and cancer incidence, using linked Census data over 25 years in England and Wales: a cohort study | Lancet Planet Health | 4 | e186–e194 |
| Rivas, B., Kumar, P., Hagen-Zanker, A. | 2017 | Exposure to air pollutants during commuting in London: Are there inequalities among different socio-economic groups? | Environ. Int. | 101 | 143–157 |
| Su, J.G., Apte, J.S., Lipsitt, J., Garcia-Gonzales, D.A., Beckerman, B.S., de Nazelle, A., Texcalac-Sangrador, J.L., Jerrett, M. | 2015 | Populations potentially exposed to traffic-related air pollution in seven world cities | Environ. Int. | 78 | 82–89 |
| Sudlow, C., Gallacher, J., Allen, N., Beral, V., Burton, P., Danesh, J., Downey, P., Elliott, P., Green, J., Landray, M., Liu, B., Matthews, P., Ong, G., Pell, J., Silman, A., Young, A., Sprosen, T., Peakman, T., Collins, R. | 2015 | UK biobank: an open access resource for identifying the causes of a wide range of complex diseases of middle and old age | PLoS Med. | 12 | e1001779 |
| Tainio, M., de Nazelle, A.J., Gotschi, T., Kahlmeier, S., Rojas-Rueda, D., Nieuwenhuijsen, M.J., de Sa, T.H., Kelly, P., Woodcock, J. | 2016 | Can air pollution negate the health benefits of cycling and walking? | Prev. Med. | 87 | 233–236 |
| Trueman, D.W., Hancock, E. | 2017 | Estimating the Economic Burden of Respiratory Illness in the UK | British Lung Foundation | | |
| Turner, M.C., Andersen, Z.J., Baccarelli, A., Diver, W.R., Gapstur, S.M., Pope 3rd, C.A., Prada, D., Samet, J., Thurston, G., Cohen, A. | 2020 | Outdoor air pollution and cancer: An overview of the current evidence and public health recommendations | CA Cancer J. Clin. | | |
| Turner, M.C., Cohen, A., Jerrett, M., Gapstur, S.M., Diver, W.R., Pope 3rd, C.A., Krewski, D., Beckerman, B.S., Samet, J.M. | 2014 | Interactions between cigarette smoking and fine particulate matter in the Risk of Lung Cancer Mortality in Cancer Prevention Study II | Am. J. Epidemiol. | 180 | 1145–1149 |
| United States Environmental Protection Agency | 1999 | Technical Bulletin: Nitrogen Oxides (NOx), Why and How They Are Controlled | | | |
| Valavanidis, A., Fiotakis, K., Vlachogianni, T. | 2008 | Airborne particulate matter and human health: toxicological assessment and importance of size and composition of particles for oxidative damage and carcinogenic mechanisms | J. Environ. Sci. Health C Environ. Carcinog. Ecotoxicol. Rev. | 26 | 339–362 |
| Vienneau, D., de Hoogh, K., Bechle, M.J., Beelen, R., van Donkelaar, A., Martin, R.V., Millet, D.B., Hoek, G., Marshall, J.D. | 2013 | Western European Land Use Regression Incorporating Satellite- and Ground-Based Measurements of NO2 and PM10 | Environ. Sci. Technol. | 47 | 13555–13564 |
| Wong, J.Y.Y., Bassig, B.A., Loftfield, E., Hu, W., Freedman, N.D., Ji, B.T., Elliott, P., Silverman, D.T., Chanock, S.J., Rothman, N., Lan, Q. | 2020 | White blood cell count and risk of incident lung cancer in the UK Biobank | JNCI Cancer Spectr. | 4 | pkz102 |
| Yang, W.S., Zhao, H., Wang, X., Deng, Q., Fan, W.Y., Wang, L. | 2016 | An evidence-based assessment for the association between long-term exposure to outdoor air pollution and the risk of lung cancer | Eur. J. Cancer Prev. | 25 | 163–172 | 