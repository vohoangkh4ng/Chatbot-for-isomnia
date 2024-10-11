## The effect of prenatal temperature and PM2.5 exposure on birthweight: Weekly windows of exposure throughout the pregnancy

### A R T I C L E I N F O

**Keywords:**
Air pollution
Temperature
Birth weight
PM2.5

### Background

Birthweight is a strong predictor of normal growth, healthy development, and survival. Several studies have found associations between temperature, fine particulate matter (PM2.5), and birth weight. However, the relevant timing of exposures varies between studies and is yet unclear. Therefore, we assessed the difference in term birthweight (TBW) associated with weekly exposure to temperature and PM2.5 throughout 37 weeks of gestation.

### Methods

We included all singleton live term births in Massachusetts, U.S between 2004 and 2015 (n = 712,438). Weekly PM2.5 and temperature predictions were estimated on a 1 km grid from satellite-based models. We utilized a distributed lag nonlinear model (DLNM) to estimate the difference in TBW associated with weekly exposures from the last menstrual period to 37 weeks of gestation.

### Results

We found a nonlinear association with prenatal temperature exposure. Larger effects were observed in warmer temperatures, where higher temperatures were negatively associated with TBW. Temperature effects were larger in the first and final weeks of gestation. We observed a negative difference in TBW associated with PM2.5 exposure. Overall, a 1 μg/m3 increase in prenatal exposure was associated with 3.9 g lower TBW (95% CI 5.0 g; 2.9 g). PM2.5 effects were larger in the final weeks of gestation.

### Conclusion

We found heat and PM2.5 exposure to be related to lower TBW. Our findings suggest that women are more susceptible to both exposures towards the end of pregnancy. Susceptibility to heat was higher in the initial weeks of pregnancy as well. These critical windows of susceptibility can be communicated to pregnant women during routine prenatal visits to increase awareness and target interventions to reduce exposures.

### 1. Introduction

Birth weight is a marker for development in early life with long-term health consequences in childhood and adulthood. The World Health Organization has targeted the achievement of a 30% reduction in low birth weight deliveries as a sustainable developmental goal, emphasizing the importance of birth weight as a predictor of morbidity and mortality. Although birth weight is mostly determined by genetic factors and length of gestation, it is also affected by maternal health and exposures during pregnancy. Several studies have found associations between temperature, particulate matter smaller than 2.5 μm (PM2.5), and birthweight. However, exposure assessment methods and the definition of the time windows of susceptibility vary across studies.

In most current studies, temperature and PM2.5 exposures are averaged over trimesters or the entire pregnancy. ## 2. Materials and methods

### 2.1. Study population

We included all eligible singleton live births in the Massachusetts birth registry data (n = 712,438 births) for years with available exposures data (2004–2015). The birth registry data included 834,886 records within the study years. This data includes the newborn’s information (date of birth, sex (male or female), birth weight in grams, gestational age at birth), maternal sociodemographic information (age at birth, race (White, Black, or other), parity (first delivery/ 2nd or more), whether the mother received government support for prenatal care (yes/no), smoking before or during pregnancy (yes/no), the highest level of education attained (no high school diploma, high school, some college, or college), chronic conditions (e.g. diabetes (yes/no) or hypertension (yes/no)), and geocoded residential address at birth. We excluded a total of 122,448 (14.6%) of the births according to the following exclusion criteria: preterm births (<37 weeks, n = 57,557), records of gestational age > 42 weeks (n = 8,506), records of birthweight < 400 g (n = 10) or over 6 kg (n = 20), and records that had missing covariates, or residence information (n = 93,527). Most of the missingness was driven by missing address information, and missing information on diabetes and hypertension. Since we only included term births, we a priori assumed linear relationship between gestational age and the outcomes. We observed stronger negative associations between maternal age and TBW among the youngest and eldest mothers and therefore used a penalized spline function to allow for a nonlinear association with maternal age at delivery. This study was approved by the Massachusetts Department of Public Health and the human subjects committee at the Harvard T. H. Chan School of Public Health.

We assessed the association between weekly mean temperature and PM2.5 exposures during gestation and TBW using DLNMs. We utilized a DLNM generalized additive model to estimate the difference in TBW associated with weekly exposures from the last menstrual period to 37 weeks of gestation. Both exposures were included in simultaneously in the multivariate model. The advantage of the DLNM framework is that it allows nonlinear exposure–response and time-response functions. Associations between temperature exposure and birth outcomes are often nonlinear. Therefore, we modeled the association between weekly mean temperature and TBW using a natural cubic spline with two degrees of freedom and modeled the lag function using a penalized spline. For PM2.5 exposure, we assumed a linear association with TBW and modeled the lag function using a natural cubic spline with three degrees of freedom. Both for the association with temperature and for the lag function of PM2.5, we selected the number of degrees of freedom that minimizes the Akaike Information Criterion (AIC).

We estimated the overall cumulative exposure–response curve of temperature and PM2.5 exposure effects on TBW. We additionally assessed the difference in TBW associated with increases in PM2.5 and low and high temperatures. We adjusted the model for the variables available in the birth records shown to be potential confounders of the associations between temperature, PM2.5, and birthweight: season and year of birth, a cyclic spline of day of the year, government support for prenatal care, race, age of mother at birth, parity, maternal smoking before or during pregnancy, the maternal highest level of education attained, chronic diabetes, chronic hypertension, and gestational age at birth. We additionally adjusted the model for census block-group socioeconomic characteristics (i.e., population density and median household income).

We present the results of the cumulative exposure–response curves, defined as the net effect of PM2.5 or temperature across the entire lag period. birthweight, associated with 1 μg/m3 increase in PM2.5, and 1 ◦C increase in temperature in different weeks of gestation. Since the cumulative exposure–response curve suggested a nonlinear association with temperature exposure, we present the effect estimates associated with a rise of 1◦C in the 5th (4◦C) and the 95th (23 ◦C) percentiles of the temperature distribution.

## 2.3.1. Secondary analyses

To identify a potential modification of the associations by maternal race and income, and by newborn sex, we repeated our model separately among White versus non-White mothers, among mothers who receive governmental support for prenatal care versus mothers who do not receive governmental support, and among male versus female newborns. We treat eligibility to governmental support as a proxy for socioeconomic status. Additionally, to capture the effects of the studied exposures on extreme abnormal fetal growth, we have assessed the effects of temperature and PM2.5 exposures in pregnancy on newborns small for gestational age (SGA). We calculate the newborn size for gestational age (SGA, appropriate for gestational age (AGA) or large for gestational age (LGA)) using the Fenton sex-specific reference growth curves.

## 2.3.2. Sensitivity analysis

The DLNM requires identical length exposure periods across the study population. This poses a challenge in defining the exposure period when studying pregnancy outcomes where the intrauterine exposures differ in length and depend on the gestational age at birth. To overcome this limitation, we defined the exposure period in our main analysis as the first 37 weeks of gestation, starting at date of last menstrual period (LMP), and limited our data to term births. For women who gave birth after the start of 37 weeks of gestation, exposures following the 37th week were unaccounted for in our main model. We, therefore, added a sensitivity analysis aimed to examine the robustness of our findings. We created a subcohort of women who delivered at 39 weeks of gestation. Among this population, we compared the results obtained when assessing the weekly effects of temperature and PM2.5 exposure at the first 37 weeks of gestation versus the entire pregnancy (39 weeks of gestation).

## 3. Theory

Multiple factors determine birthweight; some are not fully understood. It is, therefore, hard to identify a single etiology of lower birth weight. Maternal exposure to high temperatures during pregnancy can affect birthweight through different mechanisms. The first trimester of pregnancy is crucial for the correct implantation of the placenta. Maternal exposure to heat in the early stages of pregnancy can reduce placental weight and umbilical cord flow. The final stages of pregnancy are characterized by the fastest somatic growth of the fetus. Therefore, high-temperature exposures in late gestation can also affect birth weight. Higher heat production during pregnancy, alongside weight gain and the burden of the fetus, limit the maternal ability to tolerate heat stress. Heat stress and dehydration during pregnancy can cause uterine constriction and impair the uterine blood flow. The PM2.5 effect on intrauterine growth can be attributed to the limited placental ability to filter environmental chemicals. Maternal exposure to air pollution during pregnancy may cause oxidative stress and endocrine disruption in the placenta, impair the transport of oxygen and nutrients to the fetus, and adversely affect the intrauterine growth. PM2.5 has also been shown to impair vascular development in the placenta, decrease placental methylation in the leptin gene promotor, and decrease mitochondrial DNA content and increase mitochondrial DNA methylation in the placenta.

## 4. Results

We included 712,438 births; 71.9% were of White mothers. The mean maternal age at delivery was 30 years, 6.8% reported smoking during pregnancy, 0.9% had diabetes mellitus, and 1.3% had chronic hypertension. Half of the newborns were males, the mean gestational age at birth was 39.3 weeks, and the mean TBW was 3.4 kg (Table 1). The median household income at the maternal block group of residences was $51,700 on average. During the study period, the mean temperature exposure was 10.2◦C, and mean PM2.5 exposure was 8.9 μg/m3. Weekly temperature exposures ranged from 16.7◦C to 30.2 ◦C with a standard deviation of 9.2 ◦C. The births were distributed evenly throughout the year, with slightly more births in the summer months. The correlation between weekly temperature and PM2.5 exposures was low (r = 0.15, p < 0.001). We observed significant associations between temperature and TBW, independent of PM2.5 exposure. The cumulative temperature exposure–response curves over 37 weeks of gestation are presented in Fig. 2. In temperatures below zero, we observed a positive difference in TBW associated with higher temperatures. The associations in colder temperatures were mostly non-significant. In warmer temperatures, we observed a negative difference in TBW associated with higher temperatures. For example, we observed a positive non-significant difference in TBW for a rise in 1◦C in temperature exposure from 4◦C to 3◦C (2.4 g, 95% CI 0.1 g; 4.9 g). However, a rise in 10C in temperature exposure from 23◦C to 24 ◦C was associated with 7.9 g lower TBW (95% CI 11.2 g; 4.6 g). We observed a negative cumulative difference in TBW associated with PM2.5 exposure, independent of temperature exposure. A 1 μg/m3 increase was associated with 3.9 g lower TBW (95% CI 5.0 g; 2.9 g).

Table 1
Population characteristics.

| Population characteristics                                             | N ¼ 712,438 |
|-----------------------------------------------------------------------|-------------|
| Maternal age, Mean (SD)                                              | 30.08 (5.92) |
| Maternal race, n (%)                                                  |             |
| White                                                                | 512,355 (71.9) |
| Black                                                                | 67,435 (9.5) |
| Other                                                                | 132,648 (18.6) |
| Maternal education, n (%)                                            |             |
| Less than high school                                                | 75,511 (10.6) |
| High school                                                          | 158,733 (22.3) |
| Some college                                                         | 162,002 (22.7) |
| College or more                                                      | 316,192 (44.4) |
| Governmental support for prenatal care, n (%)                        | 251,633 (35.3) |
| Chronic hypertension, n (%)                                          | 9,073 (1.3) |
| Diabetes mellitus, n (%)                                             | 6,280 (0.9) |
| Smoking in pregnancy, n (%)                                          | 48,405 (6.8) |
| Gestational age in weeks, Mean (SD)                                  | 39.31 (1.18) |
| Parity > 1, n (%)                                                    | 387,393 (54.4) |
| Newborn sex, female, n (%)                                           | 349,086 (49.0) |
| Birthweight in g, Mean (SD)                                         | 3428.90 (464.14) |
| Birthweight for gestational age, n (%)                               |             |
| AGA                                                                  | 590,715 (82.9) |
| LGA                                                                  | 81,300 (11.4) |
| SGA                                                                  | 40,423 (5.7) |
| Term low birthweight (<2500 g), n (%)                                | 15,510 (2.1) |
| Median household income, Mean (SD)                                   | 51,700 (21,099) |

SD = standard deviation; AGA = appropriate for gestational age; LGA = large for gestational age; SGA = small for gestational age. Newborn size for gestational age was calculated using the Fenton sex-specific reference growth curves. Mean (SD): 10.2 (9.2)

| Exposure metrics                                   | Summary statistics |
|---------------------------------------------------|--------------------|
| Mean temperature over gestation, °C                |                    |
| Mean (SD)                                         | 10.2 (9.2)         |
| 25th percentile                                   | 2.3                |
| 50th percentile                                   | 10.4               |
| 75th percentile                                   |                    |
| Mean PM2.5 over gestation, μg/m³                  |                    |
| Mean (SD)                                         | 8.9 (3.5)          |
| 25th percentile                                   | 6.4                |
| 50th percentile                                   | 8.2                |
| 75th percentile                                   | 10.8               |
| Season of birth, n (%)                            |                    |
| Winter                                            | 167,435 (23.5)     |
| Spring                                            | 180,110 (25.3)     |
| Summer                                            | 188,097 (26.4)     |
| Fall                                              | 176,796 (24.8)     |

SD = standard deviation, PM2.5 = fine particulate matter.

percentile of temperature (23 °C), we observed larger TBW reductions associated with temperature exposure at the first and final weeks of gestation. We found smaller TBW reductions associated with weekly temperature exposure around the second trimester of pregnancy. We observed stronger temperature effects among mothers who received governmental support, and among female newborns. Additionally, we observed stronger effects of hotter temperatures among White mothers. The effects of colder temperatures did not differ by race. The effects of PM2.5 exposure were similar in all sub cohorts. For temperature at the 5th percentile

| Weeks of gestation | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
|--------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Temperature (°C)   | -18 | -12 | 22 | 10 | 16 | 22 | 28 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

For temperature at the 95th percentile (23°C)

| Weeks of gestation | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
|--------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Temperature (°C)   | 0 | 2 | 4 | 6 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

For PM2.5

| Weeks of gestation | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 |
|--------------------|---|---|---|---|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| PM2.5 (μg/m³)      | 0 | 2 | 4 | 6 | 8 | 10 | 15 | 20 | 25 | 30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Fig. 4. The cumulative exposure–response curves for the odds ratio of SGA, associated with weekly (a) temperature and (b) PM2.5 exposures in weeks 0–37 of pregnancy. This figure presents the cumulative exposure–response curves for the association between temperature, PM2.5, and newborns small for gestational age (SGA), defined as the net effects of the exposures across the entire lag period (weeks 0–37 of pregnancy). The model is adjusted for: season and year of birth, a cyclic spline of day of the year, government support for prenatal care, race, age of mother at birth, parity, maternal smoking before or during pregnancy, the maternal highest level of education attained, chronic diabetes, chronic hypertension, gestational age at birth, and census block-group socio-economic characteristics (i.e., population density and median household income).

5. Discussion

5.1. Main findings

Our findings show that the first and final weeks of gestation are the critical windows of exposure to heat. We observed a nonlinear temperature effect, with higher temperatures associated with lower TBW in warmer temperatures. We found a significant decrease in TBW and a significant increase in the odds of SGA associated with PM2.5 exposure. The negative association of PM2.5 exposure with TBW was larger towards the end of pregnancy.

To date, there is no consensus regarding the critical windows of exposure to heat during pregnancy. As pointed in the examples above, most studies identify the third trimester as the important window of susceptibility. However, our findings show that the first trimester of pregnancy is critical as well. We found that newborns are more susceptible to maternal heat exposure in the initial and final weeks of pregnancy, adjusting for the exposure across all other weeks of gestation. With the progression of pregnancy towards the 19th week of gestation, the observed effects gradually became smaller. After remaining constant in mid-pregnancy, following the 25th week of gestation, the effects gradually became larger. The early pregnancy exposure-effect might not be captured in studies averaging the exposures over trimesters or the whole pregnancy. The added value of our study is the finer isolation of the critical windows of susceptibility.

Unlike temperature exposure, the lag-structure of the PM2.5 effect on TBW followed a linear trend with larger effects in later weeks of gestation. The increased odds of SGA, associated with PM2.5 exposures were very similar across the different weeks of gestation. Similar to our analysis, numerous studies have found significant associations between PM2.5 and low birth weight, TBW or SGA. 5.3. Nonlinear association with temperature exposure

Another important finding of this study is the nonlinear relationship between temperature and TBW. The same exposure response curve was reported in animal studies which found extremely high and low temperatures to be associated with maternal stress, lower birthweight, placental weight and diameter. We observed an inverted U-shaped exposure–response curve, which suggested that both temperature extremes were associated with lower TBW. The effects were stronger in warmer temperatures, where higher exposure was associated with lower TBW. These findings are in line with current evidence, suggesting that the adverse neonatal effects of temperature exposure are stronger for heat than for cold.

5.4. Susceptible groups

The results of our sub cohort analyses varied by exposure. We found similar associations for PM2.5 regardless of sex, socioeconomic and racial groups. Similarly, Bell et al also found similar air pollution effects on birthweight among male and female newborns. Unlike our findings, other studies have found racial minorities and lower socioeconomic groups to be more susceptible to air pollution effects. This may be related to higher exposure concentrations, higher frequency of psychological stressors, or limited access to health care.

In accordance with the literature, we did find mothers of lower socioeconomic status to be more susceptible to both colder and hotter temperatures. This may be related to limited access to air conditioning, and residence in densely populated neighborhoods. Unexpectedly, White mothers were more susceptible to hotter temperatures compared to non-White mothers. With 80% White population in Massachusetts, it is possible that our findings were not robust due to a small sample size among minority groups.

Finally, we found larger TBW reductions associated with temperature among females, especially in hotter temperatures. Boys and girls are different in terms of fetal growth patterns, placental efficiency, and susceptibility to various prenatal exposures. The underlying mechanisms of susceptibility are unclear and only a few studies have investigated potential modification by sex. Additional studies are required to investigate the differential vulnerability to prenatal temperature exposure among males and females.

This is a statewide analysis incorporating time-varying exposures to PM2.5 and temperature throughout the pregnancy. The large sample size and the use of fine spatiotemporally resolved exposure models are the major strengths of this analysis. Another strength is the use of DLNM, which allowed us to flexibly investigate exposure-effects in different stages of gestation.

Our study had several limitations. Since we did not collect the data for this analysis but used routinely collected data, 12% of the records had missing covariates data. This problem is common in retrospective studies. Second, since we assigned exposure based on maternal place of residence at birth, we might have had misclassified exposure for women who changed addresses during pregnancy. However, since the new residence choice is unlikely to be based on air pollution or temperature exposure and unlikely to differ greatly in terms of the socioeconomic environment, we expect the exposure measurement error to be non-differential. Moreover, since we assign ambient exposures, and do not have information on indoor exposures or air conditioning use, we might have misclassified the exposure. If the true exposure of women during heat events tends to be much lower than the ambient temperature exposure due to use of air conditioning, this may have attenuated our results. If the misclassification was non differential, the results may be biased either toward or away from the null. Third, since we could not control for all potential confounders (such as maternal weight), residual confounding may still be present although the specific temporal pattern of associations decreases the likelihood to non-time varying confounding factors. In addition, since our study population is restricted to live births, we do not have information on spontaneous abortions. Therefore, our findings do not reflect the exposure effects on pregnancies which ended in an early stage. Finally, since most of our study population were White mothers, we might have not had enough representation of minority groups to allow the investigation of modification by racial group.

6. Conclusions

We found heat and PM2.5 exposure to be related to lower birth weight among term singleton births. Our findings suggest that women are more susceptible to both exposures towards the end of pregnancy. Susceptibility to heat was higher in the initial weeks of pregnancy as well. These critical windows of susceptibility can be communicated to pregnant women during routine prenatal visits to increase awareness and motivate them to reduce exposure. M. Yitshak-Sade et al.
Environment International 155 (2021) 106588

**Declaration of Competing Interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

**Acknowledgments**

This research was funded by grant 2017277 from the Binational Science Foundation (BSF) and NIH grants UH3 OD023337 and P30 ES023515.

**Appendix A. Supplementary material**

Supplementary data to this article can be found online at https://doi.org/10.1016/j.envint.2021.106588.

| Author(s) | Title | Journal | Year | Volume | Pages |
|-----------|-------|---------|------|--------|-------|
| Abdo M, Ward I, O’Dell K, Ford B, Pierce JR, Fischer EV, Crooks JL | Impact of Wildfire Smoke on Adverse Pregnancy Outcomes in Colorado, 2007-2015 | Int J Environ Res Public Health | 2019 | 16(19) |  |
| Basu, R., Rau, R., Pearson, D., Malig, B. | Temperature and term low birth weight in California | Am. J. Epidemiol. | 2018 | 187 | 2306–2314 |
| Bekkar, B., Pacheco, S., Basu, R., DeNicola, N. | Association of air pollution and heat exposure with preterm birth, low birth weight, and stillbirth in the US: A systematic review | JAMA Network Open | 2020 | 3(6) | e208243 |
| Belbasis, L., Savvidou, M.D., Kanu, C., Evangelou, E., Tzoulaki, I. | Birth weight in relation to health and disease in later life: an umbrella review of systematic reviews and meta-analyses | Bmc Med. | 2016 | 14 |  |
| Bell, M.L., Ebisu, K., Belanger, K. | The relationship between air pollution and low birth weight: effects by mother’s age, infant sex, co-pollutants, and pre-term births | Environ. Res. Lett. | 2008 | 3(4) | 44003 |
| Beltran, A.J., Wu, J., Laurent, O. | Associations of meteorology with adverse pregnancy outcomes: a systematic review of preeclampsia, preterm birth and birth weight | Int. J. Environ. Res. Public Health | 2014 | 11(1) | 91–172 |
| Carrión D, Arfer K, Rush J, Dorman M, Rowland S, Kioumourtzoglou M-A, Kloog I, Just A | Development and application of a 1-km hourly air-temperature model for the Northeastern and Mid-Atlantic United States using remotely sensed and ground-based measurements | 2020 |  |  |  |
| Casey, J.A., James, P., Rudolph, K.E., Wu, C.D., Schwartz, B.S. | Greenness and birth outcomes in a range of Pennsylvania Communities | Int. J. Environ. Res. Public Health | 2016 | 13(3) |  |
| Chen, L., Bell, E.M., Caton, A.R., Druschel, C.M., Lin, S. | Residential mobility during pregnancy and the potential for ambient air pollution exposure misclassification | Environ. Res. | 2010 | 110(2) | 162–168 |
| Cheng, P., Peng, L., Hao, J., Li, S., Zhang, C., Dou, L., Fu, W., Yang, F., Hao, J. | Short-term effects of ambient temperature on preterm birth: a time-series analysis in Xuzhou | China, Environ Sci Pollut Res Int | 2020 |  |  |
| Chersich, M.F., Pham, M.D., Areal, A., Haghighi, M.M., Manyuchi, A., Swift, C.P., Wernecke, B., Robinson, M., Hetem, R., Boeckmann, M., et al. | Associations between high temperatures in pregnancy and risk of preterm birth, low birth weight, and stillbirths: systematic review and meta-analysis | BMJ | 2020 | 371 | m3811 |
| Chodick, G., Flash, S., Deoitch, Y., Shalev, V. | Seasonality in birth weight: review of global patterns and potential causes | Hum. Biol. | 2009 | 81(4) | 463–477 |
| Dadvand, P., Ostro, B., Figueras, F., Foraster, M., Basagana, X., Valentin, A., Martinez, D., Beelen, R., Cirach, M., Hoek, G., et al. | Residential proximity to major roads and term low birth weight the roles of air pollution, heat, noise, and road-adjacent trees | Epidemiology | 2014 | 25(4) | 518–525 |
| Diaz, J., Arroyo, V., Ortiz, C., Carmona, R.O., Linares, C. | Effect of environmental factors on low weight in non-premature births: a time series analysis | PLoS ONE | 2016 | 11(10) |  |
| Dugandzic, R., Dodds, L., Stieb, D., Smith-Doiron, M. | The association between low level exposures to ambient air pollution and term low birth weight: a retrospective cohort study | Environ. Health : A Global Access Science Source | 2006 | 5 | 3-3 |
| Ebisu, K., Holford, T.R., Bell, M.L. | Association between greenness, urbanicity, and birth weight | Sci. Total Environ. | 2016 | 542 | 750–756 |
| Elter, K., Ay, E., Uyar, E., Kavak, Z.N. | Exposure to low outdoor temperature in the midtrimester is associated with low birth weight | Aust. N. Z. J. Obstet. Gynaecol. | 2004 | 44(6) | 553–557 |
| Fenton, T.R., Kim, J.H. | A systematic review and meta-analysis to revise the Fenton growth chart for preterm infants | BMC Pediatr. | 2013 | 13 | 59 |
| Fleischer, N.L., Merialdi, M., van Donkelaar, A., Vadillo-Ortega, F., Martin, R.V., Betran, A.P., Souza, J.P., O’Neill, M.S. | Outdoor air pollution, preterm birth, and low birth weight: analysis of the world health organization global survey on maternal and perinatal health | Environ. Health Perspect. | 2014 | 122(4) | 425–430 |
| Fong, K.C., Kloog, I., Coull, B.A., Koutrakis, P., Laden, F., Schwartz, J.D., James, P. | Residential Greenness and Birthweight in the State of Massachusetts, USA | Int. J. Environ. Res. Public Health | 2018 | 15(6) |  |
| Gasparrini, A. | Modeling exposure-lag-response associations with distributed lag non-linear models | Stat. Med. | 2014 | 33(5) | 881–899 |
| Geer, L.A., Weedon, J., Bell, M.L. | Ambient air pollution and term birth weight in Texas from 1998 to 2004 | J. Air & Waste Manage. Assoc. (1995) | 2012 | 62(11) | 1285-1295 |
| Goldenberg, R.L., Culhane, J.F. | Low birth weight in the United States | Am. J. Clin. Nutr. | 2007 | 85(2) | 584S–590S |
| Goldenberg, R.L., Culhane, J.F., Iams, J.D., Romero, R. | Epidemiology and causes of preterm birth | Lancet (London, England) | 2008 | 371(9606) | 75–84 |
| Ha, S., Zhu, Y., Liu, D., Sherman, S., Mendola, P. | Ambient temperature and air quality in relation to small for gestational age and term low birthweight | Environ. Res. | 2017 | 155 | 394–400 |
| Holstius, D.M., Reid, C.E., Jesdale, B.M., Morello-Frosch, R. | Birth weight following pregnancy during the 2003 Southern California wildfires | Environ. Health Perspect. | 2012 | 120(9) | 1340–1345 |
| Hyder, A., Lee, H.J., Ebisu, K., Koutrakis, P., Belanger, K., Bell, M.L. | PM2.5 exposure and birth outcomes use of satellite- and monitor-based data | Epidemiology | 2014 | 25(1) | 58–67 |
| Jakpor, O., Chevrier, C., Kloog, I., Benmerad, M., Giorgis-Allemand, L., Cordier, S., Seyve, E., Vicedo-Cabrera, A.M., Slama, R., Heude, B., et al. | Term birthweight and critical windows of prenatal exposure to average meteorological conditions and meteorological variability | Environ. Int. | 2020 | 142 | 105847 |
| Janssen, B.G., Byun, H.M., Gyselaers, W., Lefebvre, W., Baccarelli, A.A., Nawrot, T.S. | Placental mitochondrial methylation and exposure to airborne particulate matter in the early life environment: An ENVIRONAGE birth cohort study | Epigenetics | 2015 | 10(6) | 536–544 |
| Just AC, Arfer KB, Rush J, Dorman M, Shtein A, Lyapustin A, Kloog I | Advancing methodologies for applying machine learning and evaluating spatiotemporal models of fine particulate matter (PM(2.5)) using satellite data over large regions | Atmos Environ (1994) | 2020 | 239 |  |
| Kloog, I. | Air pollution, ambient temperature, green space and preterm birth | Curr. Opin. Pediatr. | 2019 | 31(2) | 237–243 |
| Kloog, I., Melly, S.J., Ridgway, W.L., Coull, B.A., Schwartz, J. | Using new satellite based exposure methods to study the association between pregnancy pm(2.5) exposure, premature birth and birth weight in Massachusetts | Environ. Health | 2012 | 11(8) |  |
| Kloog, I., Melly, S.J., Coull, B.A., Nordio, F., Schwartz, J.D. | Using satellite-based spatiotemporal resolved air temperature exposure to study the association between ambient air temperature and birth outcomes in Massachusetts | Environ. Health Prospectives | 2015 |  |  |
| Kloog, I., Novack, L., Erez, O., Just, A.C., Raz, R. | Associations between ambient air temperature, low birth weight and small for gestational age in term neonates in southern Israel | Environ. Health | 2018 | 17 | 9 |
| Kuehn L, McCormick S | Heat Exposure and Maternal Health in the Face of Climate Change | International journal of environmental research and public health | 2017 | 14(8) |  |
| Kumar, N. | The exposure uncertainty analysis: the association between birth weight and trimester specific exposure to particulate matter (PM2.5 vs. PM10) | Int. J. Environ. Res. Public Health | 2016 | 13(9) |  |
| Li, X.Y., Huang, S.Q., Jiao, A.Q., Yang, X.H., Yun, J.F., Wang, Y.X., Xue, X.W., Chu, Y.Y., Liu, F.F., Liu, Y.S., et al. | Association between ambient fine particulate matter and preterm birth or term low birth weight: An updated systematic review and meta-analysis | Environ. Pollut. | 2017 | 227 | 596–605 |
| Li, Z., Tang, Y., Song, X., Lazar, L., Li, Z., Zhao, J. | Impact of ambient PM2.5 on adverse birth outcome and potential molecular mechanism | Ecotoxicol. Environ. Saf. | 2019 | 169 | 248–254 |
| Li, S., Wang, J., Xu, Z., Wang, X., Xu, G., Zhang, J., Shen, X., Tong, S. | Exploring associations of maternal exposure to ambient temperature with duration of gestation and birth weight: a prospective study | BMC Pregnancy and Childbirth | 2018 | 18(1) | 513 |
| Mann, N. | Birth weight symposium | Archives of Disease in Childhood | 2002 | 86(1) | F2-F2 |
| Nieuwenhuijsen, M.J., Ristovska, G., Dadvand, P. | WHO Environmental Noise Guidelines for the European Region: A Systematic Review on Environmental Noise and Adverse Birth Outcomes | Int. J. Environ. Res. Public Health | 2017 | 14(10) |  |
| World Health Organization (WHO) | Health in 2015: from MDGs to SDGs | In. | 2015 |  | 90-91 |
| Proietti, E., Roosli, M., Frey, U., Latzin, P. | Air pollution during pregnancy and neonatal outcome: a review | J. Aerosol Med. Pulmonary Drug Delivery | 2013 | 26(1) | 9–23 |
| Saenen, N.D., Vrijens, K., Janssen, B.G., Roels, H.A., Neven, K.Y., Vanden Berghe, W., Gyselaers, W., Vanpoucke, C., Lefebvre, W., De Boever, P., et al. | Lower placental leptin promoter methylation in association with fine particulate matter air pollution during pregnancy and placental nitrosative stress at birth in the ENVIRONAGE cohort | Environ. Health Perspect. | 2017 | 125(2) | 262–268 |
| Savitz, D.A., Bobb, J.F., Carr, J.L., Clougherty, J.E., Dominici, F., Elston, B., Ito, K., Ross, Z., Yee, M., Matte, T.D. | Ambient fine particulate matter, nitrogen dioxide, and term birth weight in New York | Am J Epidemiol | 2014 | 179(4) | 457–466 |
| Schlesinger, R.B., Kunzli, N., Hidy, G.M., Gotschi, T., Jerrett, M. | The health relevance of ambient particulate matter characteristics: coherence of toxicological and epidemiological inferences | Inhalation Toxicol. | 2006 | 18(2) | 95–125 |
| Smith, R.B., Fecht, D., Gulliver, J., Beevers, S.D., Dajnak, D., Blangiardo, M., Ghosh, R.E., Hansell, A.L., Kelly, F.J., Anderson, H.R., et al. | Impact of London’s road traffic air and noise pollution on birth weight: retrospective population based cohort study | Bmj-Br. Med. J. | 2017 | 359 |  | M. Yitshak-Sade et al.
Environment International 155 (2021) 106588

Song, J., Lu, J., Wang, E., Lu, M., An, Z., Liu, Y., Zeng, X., Li, W., Li, H., Xu, D., et al., 2019. Short-term effects of ambient temperature on the risk of premature rupture of membranes in Xinxiang, China: A time-series analysis. Sci. Total Environ. 689, 1329–1335.
Thayamballi, N., Habiba, S., Laribi, O., Ebisu, K., 2020. Impact of maternal demographic and socioeconomic factors on the association between particulate matter and adverse birth outcomes: a systematic review and meta-analysis. J. Racial Ethn. Health Disparities.
Warren, J.L., Son, J.Y., Pereira, G., Leaderer, B.P., Bell, M.L., 2018. Investigating the impact of maternal residential mobility on identifying critical windows of susceptibility to ambient air pollution during pregnancy. Am. J. Epidemiol. 187 (5), 992–1000.
Wells, J.C.K., 2002. Thermal environment and human birth weight. J. Theor. Biol. 214 (3), 413–425.
Westergaard, N., Gehring, U., Slama, R., Pedersen, M., 2017. Ambient air pollution and low birth weight - are some women more vulnerable than others? Environ. Int. 104, 146–154.
Wilson A, Chiu Y-HM, Hsu H-HL, Wright RO, Wright RJ, Coull BA: Potential for Bias When Estimating Critical Windows for Air Pollution in Children’s Health. American journal of epidemiology 2017, 186(11):1281-1289.
Yitshak-Sade, M., Novack, L., Landau, D., Kloog, I., Sarov, B., Hershkovitz, R., Karakis, I., 2016. Relationship of ambient air pollutants and hazardous household factors with birth weight among Bedouin-Arabs. Chemosphere 160, 314–322.
Yitshak-Sade, M., Fabian, M.P., Lane, K.J., Hart, J.E., Schwartz, J.D., Laden, F., James, P., Fong, K.C., Kloog, I., Zanobetti, A., 2020. Estimating the combined effects of natural and built environmental exposures on birthweight among urban residents in Massachusetts. Int. J. Environ. Res. Public Health 17 (23).
Yitshak-Sade, M., Lane, K.J., Fabian, M.P., Kloog, I., Hart, J.E., Davis, B., Fong, K.C., Schwartz, J.D., Laden, F., Zanobetti, A., 2020. Race or racial segregation? Modification of the PM2. 5 and cardiovascular mortality association. PLoS ONE 15 (7), e0236479.
Yue, H., Ji, X., Zhang, Y., Li, G., Sang, N., 2019. Gestational exposure to PM(2.5) impairs vascularization of the placenta. Sci. Total Environ. 665, 153–161.
Zhang, Y., Yu, C., Wang, L., 2017. Temperature exposure during pregnancy and birth outcomes: An updated systematic review of epidemiological evidence. Environ. Pollut. 225, 700–712.
Zhu, X.X., Liu, Y., Chen, Y.Y., Yao, C.J., Che, Z., Cao, J.Y., 2015. Maternal exposure to fine particulate matter (PM2.5) and pregnancy outcomes: a meta-analysis. Environ. Sci. Pollut. Res. 22 (5), 3383–3396. 