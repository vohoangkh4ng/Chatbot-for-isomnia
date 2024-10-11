# Health impacts of changes in travel patterns in Greater Accra Metropolitan Area, Ghana

## A B S T R A C T

**Keywords:**
Active transportation
Air pollution
Traffic incident
Mode shift
Health impact assessment

**Background:** Health impact assessments of alternative travel patterns are urgently needed to inform transport and urban planning in African cities, but none exists so far.
**Objective:** To quantify the health impacts of changes in travel patterns in the Greater Accra Metropolitan Area, Ghana.
**Methods:** We estimated changes to population exposures to physical activity, air pollution, and road traffic fatality risk and consequent health burden (deaths and years of life lost prematurely – YLL) in response to changes in transportation patterns. Five scenarios were defined in collaboration with international and local partners and stakeholders to reflect potential local policy actions.
**Results:** Swapping bus and walking trips for car trips can lead to more than 400 extra deaths and 20,500 YLL per year than travel patterns observed in 2009. If part of the rise in motorisation is from motorcycles, we estimated an additional nearly 370 deaths and over 18,500 YLL per year. Mitigating the rise in motorisation by swapping long trips by car or taxi to bus trips is the most beneficial for health, averting more than 600 premature deaths and over 31,500 YLL per year. Without significant improvements in road safety, reduction of short motorised trips in favour of cycling and walking had no significant net health benefits as non-communicable diseases deaths and YLL benefits were offset by increases in road traffic deaths. In all scenarios, road traffic fatalities were the largest contributor to changes in deaths and YLL.
**Conclusions:** Rising motorisation, particularly from motorcycles, can cause significant increase in health burden in the Greater Accra Metropolitan Area. Mitigating rising motorisation by improving public transport would benefit population health. Tackling road injury risk to ensure safe walking and cycling is a top priority. In the short term, this will save lives from injury. Longer term it will help halt the likely fall in physical activity.

## 1. Introduction

The percentage of the world’s population living in urban areas is projected to increase from 56% in 2020 to 68% by 2050, and more than 90% of this growth will be in low- and middle-income countries (LMIC) ## 2. Methods

### 2.1. Site

Greater Accra Metropolitan Area is the economic and administrative hub of the Greater Accra region, the most urbanized region in Ghana and one of the fastest urbanizing areas in Africa. At the time of this work, Greater Accra Metropolitan Area was constituted of 12 major urban districts: Accra Metropolitan District, Tema Metropolis, Adentan, Ga East, Ga West, Ga South, Ga Central, La Nkwantang-Madina, Ledzokuku-Krowor, Ashaiman, Kpone-Katamanso, and La Dade-Kotopon. More than 4.4 million inhabitants live in Greater Accra Metropolitan Area according to 2017 estimates, the thirteenth-largest metropolitan area in Africa.

In terms of transportation infrastructure, Greater Accra Metropolitan Area has approximately 7600 km of roads, of which 6900 km are urban networks. However, footpaths are very limited – in Accra Metropolitan District, for instance, they account for less than 4% of the transport network – and the city of Accra does not have dedicated bicycle infrastructure. There are more than 1.2 million cars registered in the area, and an influx of 2.5 million commuters per day. Mass transportation services – buses and trotros – are largely operated by private individuals, companies, and quasi-government companies.

### 2.2. Overview of the process and context

This work was conducted under the umbrella of the Urban Health Initiative pilot project, a partnership between the World Health Organization, Accra Metropolitan Assembly, Ghana Health Service, Ghana Environmental Protection Agency, World Health Organization’s international implementing partners, UN-Habitat and the Local Governments for Sustainability, all members of the Climate and Clean Air Coalition. The main goal of the Urban Health Initiative is to strengthen the health evidence around urban environment issues affecting population health by making the best use of the local knowledge, data, and expertise. The primary entry point for the pilot project in Accra was tackling air pollution, particularly short-lived climate pollutants. Key steps within the Urban Health Initiative process include identification and engagement with relevant local stakeholders in the transport sector, mapping. existing transport policies and plans, assessing the potential health impacts of policy scenarios, and making best use of better health evidence to create demand for health-enhancing policies and interventions and inform local action (e.g., Accra’s climate change action plans). Further details on the World Health Organization’s work on urban health are available at

For this study, local stakeholders across a wide range of institutions and expertise and the MRC Epidemiology Unit’s Public Health Modelling joined the group and worked closely, including on data search and quality assessment, scenario development, and discussions about results, data gaps, research priorities, and implications for action. The engagement of all these actors over the entire modelling process was crucial to understand contextual aspects and gain access to the best data available, but also to build ownership, share technical capacities, and produce scenarios and results that are locally relevant.

This study uses a new version of the Integrated Transport and Health Impact Model (ITHIM), named ITHIM-Global. The model estimates changes in population levels of physical activity, exposure to air pollution, road traffic fatality risk, and consequent health impacts in response to changes in travel patterns (see details in Section 2.4). ITHIM-Global key advances in relation to the latest implementation of ITHIM are:

- The use of microsimulation approach rather than distributions to estimate population patterns of travel behaviour, non-travel physical activity, and exposure to air pollution. This was achieved by creating a synthetic population, a dataset containing representations of individuals obtained by merging datasets of travel and physical activity behaviour of people sampled from the population of interest. This approach allows the estimation of health impacts of more nuanced counterfactual scenarios by altering individual trips according to, for instance, distance or mode of travel, or by targeting specific population groups.
- Dose-response curves between air pollution exposure and disease endpoints have been updated, now including travel.
- Dose-response curves between physical activity levels and disease endpoints have been updated, using a larger evidence base and harmonised methods across all disease endpoints.
- The use of value-of-information analysis to identify the parameter or parameters that most drive variability in outcomes and prediction accuracy.
- The model code was moved to R.
- A new Shiny interface to visualise the results. The code is available at

The code and inputs used specifically for this work can be found at

Transport scenarios

A series of scenarios were co-developed with the local partners representing potential changes to trip mode share. Table 1 presents the scenarios and their rationale considering the policy landscape in the city at the time of the scenario development discussions. Building on the most recent data source that provides trip-level information, the 2009 Time Use Survey, we created a reference scenario where some bus and walking trips were switched to car trips. Next, four alternative scenarios were created from the reference scenario: long trips by car or taxi switched to bus trips; a fraction of car trips switched to motorcycle trips; short trips by car, taxi, or motorcycle switched to cycling trips; and short trips by car or taxi switched to walking trips. Shifts from motorized modes to cycling and walking only occurred within short trips (i.e., 0 to 6 km), reflecting the increased likelihood of using these modes in short trips as compared to longer trips. Trip mode share for each scenario were then recalculated accordingly.

Data and modelling process

As a simulation modelling study, we used multiple data sources. These covered travel patterns, non-travel physical activity, air pollution, and road traffic fatalities. Table 2 has a summary of the input data used in this work.

Table 1
Envisioned policy actions and trip mode share for Greater Accra Metropolitan Area, Ghana.

| Scenarios                                                                 | Trip mode share (%) | Bicycle | Bus   | Motorcycle | Private car | Taxi  | Walking |
|---------------------------------------------------------------------------|---------------------|---------|-------|------------|-------------|-------|---------|
| 2009 mode share                                                          |                     | 0.5     | 30.8  | 1.0        | 9.7         | 4.1   | 53.9    |
| Data based on the 2009 Time Use Survey.                                  |                     |         |       |            |             |       |         |
| Bus and walking trips → car trips (reference scenario)                   |                     | 0.5     | 16.2  | 1.0        | 28.6        | 4.1   | 49.6    |
| Envisioned changes from 2009 mode share: increased vehicle-kilometres...|                     |         |       |            |             |       |         |
| Long trips by car or taxi → bus trips                                     |                     | 0.5     | 35.5  | 1.0        | 11.9        | 1.5   | 49.6    |
| Envisioned changes from reference scenario: implementation of policy...  |                     |         |       |            |             |       |         |
| Car trips → motorcycle trips                                              |                     | 0.5     | 16.2  | 10.1       | 19.5        | 4.1   | 49.6    |
| Envisioned changes from reference scenario: high levels of traffic...     |                     |         |       |            |             |       |         |
| Short trips by car, taxi, or motorcycle → cycling trips                  |                     | 3.5     | 16.2  | 0.5        | 26.3        | 3.9   | 49.6    |
| Envisioned changes from reference scenario: support from transport...     |                     |         |       |            |             |       |         |
| Short trips by car or taxi → walking trips                                |                     | 0.5     | 16.2  | 1.0        | 24.0        | 3.6   | 54.7    |
| Envisioned changes from reference scenario: additional infrastructure...   |                     |         |       |            |             |       |         |

Short trips = 0 to 6 km. Long trips = 10 or more km. Table 2
Input data used in the different analysis modules.

| Input data                                     | Data source                                           | Reference  | Data description                                                                                       |
|------------------------------------------------|------------------------------------------------------|------------|--------------------------------------------------------------------------------------------------------|
| Sex, age, and travel patterns                  | Ghanaian 2009 Time Use Survey (Ghana Statistical Service, 2009) | 2009       | Sex, age, and travel behaviour (2549 trips) of 758 participants aged 15 to 69 living in the urban areas of Greater Accra region. More information in Section 2.4.1. |
| Non-travel physical activity level             | World Health Organization’s Study on Global Aging and Adult Health (SAGE), Wave 1 (World Health Organization, 2013) | 2007–2008  | Occupational and recreational physical activity from 397 people aged 18 to 69 living in the urban areas of Greater Accra region. More information in Sections 2.4.2 and 2.4.3. |
| Background PM2.5 concentrations                | Dionisio et al. (2010)                                | 2006–2008  | Data from ambient particulate matter monitors placed in four urban neighbourhoods in Accra with varying socio-economic status and biomass fuel use. |
| Fraction of PM2.5 concentration due to road transport and emission inventory | Ghanaian Second National Household Transport Survey (Ghana Ministry of Roads and Highways, 2013) | 2012       | Car and two-wheelers ownership of a representative sample of all households in Greater Accra region. |
|                                                | Goel and Guttikunda (2015)                            | 2007–2012  | Vehicle (buses, taxis, and trucks) registration numbers for Greater Delhi region.                     |
|                                                | Indian 2011 Population and Housing Census (India Office of the Registrar General and Census Commissioner, 2020) | 2011       | Population size and vehicle ownership for Greater Delhi region.                                       |
|                                                | Vehicular emission inventory for Ghana (Agency, 2014) | 2014       | Proportion of the fleet corresponding to different emission standards.                                 |
|                                                | Goel et al. (2015)                                    | 2012       | Daily mileage per vehicle type reported for Delhi.                                                   |
| Road traffic fatalities                        | Ghanaian Police Service (through the Building and Road Research Institute) | 2007–2016  | Road traffic fatality data for Accra, with types of vehicles involved in the collisions.              |
| Background numbers on deaths and years of life lost due to premature mortality (YLL) | Global Burden of Disease Study (Institute for Health Metrics and Evaluation. GBD results tool, 2020) | 2017       | Estimated deaths and years of life lost due to premature mortality for Ghana.                         |
|                                                | Ghanaian 2010 Population and Housing Census (Ghana Statistical Service, 2017) | 2010       | Age and sex profile of Greater Accra region.                                                          |
|                                                | Estimated total population (Ghana Statistical Service, 2017) | 2017       | Estimated 2017 total population for Greater Accra region.                                            |

2.4.1. Travel patterns
To form the basis of our synthetic population representing residents of the Greater Accra Metropolitan Area, demographics and travel behaviour was based on primary data of the 2009 Time Use Survey, as the most recent data source that provides trip-level information from a representative sample of people living in the region.
The survey sample is representative at national and regional level (e.g., Greater Accra region), as well as urban and rural locations. A confidence interval of 95% with an error margin of 0.025 and a non-response rate of 20% were considered in the sample size calculation. Three-hundred enumeration areas (EAs, from the 2010 Population and Housing Census) were selected across the country with probability proportional to EA size, and 16 households were selected systematically from each EA at the second stage. All residents aged 10 years or older of selected households were eligible to participate in the survey. Response rate was 86.5% nationally (no data by region was found). Pre-test training, fieldwork supervisors, and data entry checks were used to ensure quality.
For this study, sex, age, and travel behaviour (2549 trips) of 758 participants aged 15 to 69 and living in the urban areas of the Greater Accra region, which greatly overlaps with the Greater Accra Metropolitan Area boundaries, were used to create the synthetic population. We augmented the synthetic population by generating four synthetic individuals for each person in the Time Use Survey to improve the matching process with the physical activity survey by sex and age bands.
The survey questionnaire was administered as face-to-face interviews. A 24-hour diary, divided into one-hour slots, was used as the core instrument to record activities in the preceding day, including travelling. Duration and mode of transportation were reported for every trip.
The Time Use Survey did not ask about motorcycle trips, so in order to have them in the synthetic population with an approximate 1% mode share, 26 motorcycle trips added into the synthetic population. First, we converted 14 random trips labelled as “other modes” that lasted less than one hour into “motorcycle” trips. Next, we introduced to the synthetic population four men aged 15 to 49 with three motorcycle trips each (12 motorcycle trips). The estimates of motorcycling were based on expert opinion of the stakeholders and a qualitative assessment of Google Street View images for Greater Accra Metropolitan Area. The duration of each trip was drawn from a uniform distribution between 15 and 60 min. No further trips were assigned to the four added men, so no changes occurred in the total number or trips or distance travelled by the other modes.
Additionally, bus vehicles and truck trips were added to calculate their impact on road fatality risks. Truck trips added up to 0.21 of the total distance of car trips in the reference scenario and did not change across scenarios. This ratio was approximated from Indian cities, also a lower-middle-income setting, given no local specific data. Bus vehicle trips scaled proportionally to bus passenger trips with a constant ratio of 0.022 across all scenarios.
Short walks were included as part of all bus trips, representing walk to/from bus stops from/to the origin/destination. A duration was drawn from a lognormal distribution (μ = 5, σ2 = 1.2) and the same value was assigned to all short walks and subtracted from the bus-trip duration. Journeys converted to or from bus trips in any scenario were accompanied by changes in short walks as well.
Only trip duration was provided by the survey, so we assumed the following average speeds (in km/h) by mode to get trip distances: walk: 4.8; bicycle: 14.5; bus: 15.0; car and taxi: 21.0; motorcycle: 25.0. Based on trips distance, we divided trips into three categories: short (0 to 6 km), medium (>6 to <10 km), and long (10 km or more). We assumed trip distances would remain the same after switching modes. ## 2.4.2. Non-travel physical activity
Occupational and recreational physical activity data was obtained from the World Health Organization’s Study on Global Aging and Adult Health (SAGE) Wave 1 (2007–08), through face-to-face interviews using the Global Physical Activity Questionnaire. SAGE is a longitudinal study on adults aged 50 years and older, including a smaller comparison sample of adults aged 18 to 49 years, from nationally representative samples in six countries, including Ghana. For SAGE Wave 1, 397 people with 18 to 69 years of age living in urban settings in the Greater Accra region were interviewed.

## 2.4.3. Physical activity energy expenditure
For occupational and recreational physical activity, marginal metabolic equivalent of tasks per week (mMET-h/week) was calculated for all adults living in the urban Greater Accra region following the Global Physical Activity Questionnaire’s protocol. Briefly, we multiplied weekly frequency, daily volume, and intensity to obtain mMET-h/week. A scalar drawn from a lognormal distribution (μ = 1, σ2 = 1.2) was applied to the time reported in occupational and recreational physical activity to account for survey respondents’ under or over reporting.
A similar procedure was followed to obtain active travel (i.e., walking and cycling) energy expenditure, based on daily travel duration obtained from the Time Use Survey. As the Time Use Survey only captures one day, weekly duration was obtained multiplying daily duration by seven. Average walking and cycling mMET were estimated assuming speeds of 4.8 and 14.5 km/h, respectively.
Table 3 presents the energy expenditure assumed for each intensity or activity based on the Compendium of Physical Activities.

For every person in the synthetic population, we randomly selected one person from the SAGE dataset with same sex and age band (15 to 55, 56 to 69), appended their occupational and recreational energy expenditure, and combined it with the active travel energy expenditure. Occupational and recreational physical activity were kept constant across scenarios, so that health impacts refer to the marginal change that occurred in transport-related physical activity only.
For every person in the synthetic population and every scenario, relative risks of coronary heart disease, stroke, diabetes type 2, lung cancer, endometrial cancer, breast cancer, and colorectal cancer were estimated based on their total physical activity energy expenditure. Relative risks were obtained from meta-analyses of longitudinal cohort studies. The original studies included in the meta-analyses estimated risk based on the first observed disease-specific event, which in many times, but not always, is death. Our model assumes that these relative risks can be applied to mortality. We used non-linear dose–response relationships between physical activity and health outcomes, meaning that those with lower levels of physical activity would benefit most from increases in active travel. Based on the dose–response functions, we set a threshold of 35.0 mMET-h/week beyond which there was no further change in relative risk for all diseases, with the exceptions of lung cancer (threshold of 10.0 mMET-h/week), stroke (threshold of 32.0 mMET-h/week), and diabetes, for which there was no upper limit.

### Table 3
Marginal metabolic equivalent of tasks (mMET) of different physical activities by domain.

| Domain   | Intensity or activity | mMET |
|----------|-----------------------|------|
| Work     | Moderate              | 2.0  |
|          | Vigorous              | 5.0  |
| Leisure   | Moderate              | 3.0  |
|          | Vigorous              | 8.0  |
| Transport | Walking               | Lognormal (μ = 2.53, σ2 = 1.2) |
|          | Cycling               | Lognormal (μ = 4.63, σ |

## 2.4.4. Air pollution
For modelling changes in air pollution, we required estimates of background concentration of particulate matter with 2.5-μm diameter (PM2.5), the fraction of the concentration that comes from road transport, and emission factors by vehicle type. In the absence of local estimates, we utilised data from Indian cities – also a lower-middle-income setting. In applying these estimates to our local model, we augmented their uncertainty, as reflected in the parameters of the probability distributions. We analysed the impact of these uncertain variables on our results using value-of-information analysis.
We estimated changes in overall background PM2.5 concentrations in each scenario resulting from changes in total emissions of the vehicular modes. We used outdoor PM2.5 concentrations in residential areas in Accra reported by Dionisio et al. to inform a lognormal distribution (μ = 50, σ2 = 1.3) from which the background concentration value was drawn. Further, we used values reported by Zhou et al. to inform a beta distribution (α = 1.5, β = 5) to describe the fraction of PM2.5 concentration due to road transport.
We estimated the fleet size of cars and motorised two-wheelers using the household ownership estimates reported by Ministry of Transport and Ghana Statistical Service. In the absence of locally specific data, we estimated the fleet size of buses, taxis and trucks using approximations of per capita rates from Indian cities, also a lower-middle-income setting.
To estimate emission factors, we used the proportion of the fleet corresponding to different emission standards as reported in the vehicular emission inventory for Ghana, produced by the Ghana Environmental Protection Agency. With this we combined emission factors for the corresponding emission standards specific to different vehicle types reported by a road transport emission inventory study for Delhi. For the annual mileage specific to vehicle types, we used the daily mileage per vehicle reported for Delhi and scaled it down using the ratio of built-up areas of the two cities.

## 2.4.5. Personal daily exposure to air pollution
For a given scenario, using the predicted background PM2.5 concentration and the trip set, we estimated personal daily (travel plus non-travel) exposure to PM2.5 by accounting for higher levels of pollution exposure during on-road travel. The on-road exposure to PM2.5 was calculated using the duration of travel, air inhalation rate, and the ratio of in-vehicle exposure to background exposure. The air inhalation rate and exposure ratios were specific to each mode of travel. For example, walking has higher rate of air inhalation as well as exposure ratio than a closed-window car.
For every person in the synthetic population, we estimated the relative risk of fatal chronic obstructive pulmonary disease, lower respiratory infection, coronary heart disease, stroke, and lung cancer based on their daily exposure to air pollution using disease-specific mortality dose–response functions.

## 2.4.6. Road traffic fatalities
Road traffic fatality data was provided by the Ghanaian Police Service through the Building and Road Research Institute, one of the institutes under the Council for Scientific and Industrial Research. We had access to the type of vehicles involved in collisions that happened from 2007 to 2016. Only data on fatalities was used because only deaths are required to calculate the health impact summary measures in our model. substantial and differential (by mode) underreporting of non-fatal injuries in police data in all settings.

Table 4 shows the number of road traffic fatalities by types of victim and impacting road users. The road users who died in the collision are referred to as victims, while the other road user with whom the collision occurred is referred to as impacting road user. In the case that both road users died in the collision, each road user was counted once as victim and once as impacting road user, thus we modelled fatal injuries and not collisions. In the case of multiple impacting road users and one victim, each impacting road user was paired with the victim and given a weighting of one divided by the number of impacting road users, so that all vehicle types involved in the collision are represented in the table while avoiding double counting. It should be noted that this method does not attribute blame to those involved in the collision.

The road traffic fatality module estimates total and changes in fatalities based on changes in distance by both the victim and impacting vehicles. For all modes we assumed that the change in person-distance was linear to the change in vehicle-distance (for buses, occupancy is assumed to be constant). For non-passenger vehicles we assumed distances were unchanged. To account for underreporting of fatalities, an injury reporting rate scalar was considered and drawn from a beta distribution (α = 8, β = 3).

Change in fatalities was modelled as a non-linear (power) function of change in distances, based on the approach used in Woodcock et al. The non-linearity, referred to as safety-in-numbers, is operationalised using the power exponents reported in a meta-analysis by Elvik and Goel. The meta-analysis reported that the safety-in-numbers effect remain strong even when controlled for confounders such as pedestrian or cycle infrastructure and the relative volume of different road users, indicating that it may be applicable across diverse settings.

2.4.7. Health impacts

Deaths and years of life lost due to premature mortality (YLL) in consequence to changes in population exposures to physical activity, air pollution, and road traffic fatality risk were estimated for each scenario in comparison to the reference scenario (Table 1). Within each pathway (physical activity, air pollution, and road traffic fatalities), the same change in risks was assumed for estimating deaths and YLL. For diseases affected by both physical activity and air pollution (coronary heart disease, stroke, and lung cancer), relative risks were first combined through multiplication, assuming that these two risk pathways are not independent.

Ghana background numbers on deaths and YLL were taken from the 2017 Global Burden of Disease Study and scaled down for the age and sex specific demographic profile of Greater Accra Metropolitan Area population according to the 2010 census and the estimated 2017 total population. A scalar to account for under or overestimation of disease burden was described by a lognormal distribution (μ = 1, σ2 = 1.2).

2.4.8. Uncertainty analysis

We conducted value-of-information analysis calculating the expected value of partial perfect information (EVPPI), following Jackson et al. EVPPI reports how much the variance (i.e., uncertainty) in the outcomes (deaths and YLL) would be expected to reduce under perfect knowledge of the parameter tested. In this way we can identify the parameter or parameters that most drive variability in the outcome, identifying data gaps and further research that offer the greatest benefit in terms of prediction accuracy.

We included uncertainty in our evaluation of the model through assigning distributions to 10 input parameters and 12 dose–response relationships, sampling from them 1024 times, and each time evaluating the outcomes. Uncertainty intervals of 95% are provided alongside outcome point estimates.

For the dose–response relationships between physical activity or air pollution and diseases, we assumed that there is uncertainty, but no variability, in the relationship. We sampled a relationship from the distribution of relationships and applied that relationship to all individuals precisely.

By sampling a single standard uniform variable for each dose–response relationship, we can select the same quantile from the distribution over relationships for each person. For physical activity, each dose–response relationship was defined by a truncated normal distribution. For each dose, there is a mean value, an upper bound, and a lower bound. For each person, we take the same quantile from the response function by mapping the uniform random variable onto the truncated normal distribution defined by the mean and bounds for their dose.

For air pollution, there were four parameters per disease, for which posterior samples were available. We sampled from their joint distribution in an analogous manner, one parameter at a time, requiring four uniform random variables.

2.4.9. Sensitivity analysis

We conducted sensitivity analyses to test the robustness of our results by altering four underlying assumptions, each representing a plausible change in the city’s future wider context: road traffic fatality risks halved for a given distance (i.e., safer roads for all users); rate of non-communicable diseases doubled; levels of non-transport air pollution halved; and levels of non-transport physical activity halved. Changes were applied one at time. All scenarios in Table 1 were executed considering each new background condition, following the same procedures detailed in the previous sections.

3. Results

Tables 5 and 6 present, respectively, the average duration and distance travelled per person per day per mode in each scenario. In relation to the mode share observed in 2009, mean duration and distance travelled by car per person per day quadrupled in the reference scenario, at the expense of bus and walking trips. Changing long trips (10 km or more) by car or taxi to bus trips has the potential to almost reverse the

Table 4
Road traffic fatalities according to victim and impacting mode. Accra, Ghana, 2007–2016.

| Victim mode                     | Pedestrian | Bicycle | Motorcycle | Car, pick-up or van | Bus | Trucks | No other or fixed object | Unknown | TOTAL |
|----------------------------------|------------|---------|------------|---------------------|-----|--------|-------------------------|---------|-------|
| Pedestrian                       | 0          | 2       | 63         | 434                 | 218 | 76     | 1                       | 87      | 881   |
| Bicycle                          | 0          | 0       | 2          | 24                  | 11  | 10     | 0                       | 3       | 50    |
| Motorcycle                       | 6          | 0       | 9          | 56                  | 29  | 18     | 20                      | 5       | 143   |
| Car                              | 3          | 0       | 4          | 29                  | 25  | 22     | 47                      | 5       | 135   |
| Pick-up truck or van            | 0          | 0       | 0          | 3                   | 4   | 5      | 8                       | 0       | 20    |
| Bus                              | 1          | 1       | 1          | 8                   | 14  | 13     | 33                      | 3       | 74    |
| Heavy transport                  | 0          | 0       | 0          | 3                   | 4   | 4      | 22                      | 0       | 33    |
| TOTAL                            | 10         | 3       | 79         | 557                 | 305 | 148    | 131                     | 103     |       |

The same person can be both driving an impacting vehicle and a victim in a road traffic collision. The same collision can contribute with multiple victims. | Scenarios                                   | Walking | Bicycle | Bus  | Car  | Taxi | Motorcycle |
|---------------------------------------------|---------|---------|------|------|------|------------|
| 2009 mode share                             | 52.8    | 0.3     | 50.4 | 11.6 | 4.6  | 1.7        |
| Bus and walking trips → car trips (reference) | 44.9    | 0.3     | 3.5  | 48.1 | 4.6  | 1.7        |
| Long trips by car or taxi → bus trips      | 50.7    | 0.3     | 71.4 | 3.7  | 0.4  | 1.7        |
| Car trips → motorcycle trips                | 44.9    | 0.3     | 3.5  | 38.2 | 4.6  | 10.0       |
| Short trips by car, taxi, or motorcycle → cycling trips | 44.9    | 2.1     | 3.5  | 47.2 | 4.5  | 1.4        |
| Short trips by car or taxi → walking trips  | 52.4    | 0.3     | 3.5  | 46.6 | 4.4  | 1.7        |

Short trips = 0 to 6 km. Long trips = 10 km or more. Table 6
Median travel distance (in kilometres) per person per day per mode, by scenario.
| Scenarios                                               | Walking | Bicycle | Bus   | Car   | Taxi  | Motorcycle |
|--------------------------------------------------------|---------|---------|-------|-------|-------|------------|
| 2009 mode share                                        | 4.23    | 0.07    | 13.05 | 4.05  | 1.61  | 0.69       |
| Bus and walking trips → car trips (reference)         | 3.59    | 0.07    | 0.89  | 16.83 | 1.61  | 0.69       |
| Long trips by car or taxi → bus trips                 | 4.05    | 0.07    | 17.43 | 1.30  | 0.15  | 0.69       |
| Car trips → motorcycle trips                           | 3.59    | 0.07    | 0.89  | 13.36 | 1.61  | 4.17       |
| Short trips by car, taxi, or motorcycle → cycling trips| 3.59    | 0.50    | 0.89  | 16.53 | 1.58  | 0.59       |
| Short trips by car or taxi → walking trips            | 4.17    | 0.07    | 0.89  | 16.31 | 1.55  | 0.69       |

Short trips = 0 to 6 km. Long trips = 10 km or more.

Background PM2.5 concentration (Table 8) and personal exposure to PM2.5 (Table 9) increased in the reference scenario compared with 2009 and were lowest in relation to the reference scenario when swapping long trips by car or taxi for bus trips. The number of road fatalities in the reference scenario increased for all road users, except bus passengers, compared with 2009 (Table 10). Swapping long trips by car or taxi for bus trips was estimated to halve the number of road fatalities in comparison to the reference scenario, with significantly fewer deaths of pedestrians, cyclists, and car and motorcycle users. Conversely, increases in motorcycle trips can result in 40% more road fatalities than in the reference scenario, with a four-fold rise among motorcycle users. Swapping short trips by car, taxi, or motorcycle for cycling trips resulted in an almost four-fold increase in fatalities among cyclists in comparison to the reference scenario, although there was a reduction in fatality risk per cycling kilometres travelled (calculated based on the values presented in Tables 6 and 10).

3.2. Health impacts

Fig. 3 presents the health impacts of each scenario in terms of deaths averted per year (3.a) and reduction in YLL (3.b). Swapping bus and walking trips for car trips (reference scenario) was estimated to lead to a worse health situation than travel patterns observed in 2009, with more than 400 extra deaths and 20,500 YLL per year. Shifting from car to motorcycle trips is the most detrimental to health, with nearly 370 extra deaths and over 18,500 YLL per year in relation to the reference scenario, mostly because of the large increase in road traffic fatalities. Swapping long trips by car or taxi for bus trips is the most beneficial for health in comparison with the reference scenario, mostly due to reductions in road fatalities. In total, there was a gain of more than 600 premature deaths prevented, equating to over 31,500 YLL per year. Reduction of short motorised trips in favour of cycling and walking trips had no net significant health benefits as non-communicable diseases deaths and YLL that could be averted were offset by those caused by road traffic collisions. In all scenarios, road traffic fatalities were the largest contributor to changes in deaths and YLL. They contributed 84% and 89% of the changes in total deaths and YLL, respectively, when comparing 2009 and the reference scenario. Road fatalities contributed 99% of the changes in total deaths and YLL as a result of shifting from car to motorcycle trips, 85% to 90% of the changes in health burden following increases in long trips by bus, and around 66% and 75% of the changes in deaths and YLL, respectively, in the scenarios that favoured active modes of travel.

3.3. Uncertainty analysis

Through value-of-information analysis we found out that two parameters related to road traffic burden calculation drive a large portion of outcomes’ variance in all scenarios. The “injury reporting rate” scalar represents the rate at which road-traffic fatalities were reported to the police, that is, how well our dataset captures the true burden of road-collision fatality. As we allowed for the parameter for the number of injuries to be a non-linear function of the distances travelled by each mode involved in the collision, the “fraction of safety-in-numbers exponents due to casualty mode” relates to the nonlinearity of the injuries with respect to distance travelled by the mode of travel of the casualty.

Table 7
Distribution of total (travel plus non-travel) physical activity energy expenditure (mMET-h/week), by scenario. For each parameter, mean and uncertainty intervals of 95% were generated from 1024 repetitions.
| Scenarios                                                          | Min | 10th percentile | Median | Mean  | 90th percentile | Max   |
|-------------------------------------------------------------------|-----|-----------------|--------|-------|------------------|-------|
| 2009 mode share                                                   | 0   | 2.5             | 28.1   | 61.7  | 178.2            | 530.4 |
|                                                                   |     | (0 to 0)       | (1.5 to 3.3) | (23.3 to 33.4) | (47.0 to 80.9) | (130.1 to 244.3) | (375.7 to 715.5) |
| Bus and walking trips → car trips (reference)                     | 0   | 2.0             | 25.2   | 59.4  | 175.5            | 523.3 |
|                                                                   |     | (0 to 0)       | (1.3 to 3.1) | (20.6 to 30.2) | (44.8 to 78.6) | (127.2 to 241.7) | (373.0 to 708.7) |
| Long trips by car or taxi → bus trips                             | 0   | 3.2             | 27.3   | 61.1  | 177.3            | 524.3 |
|                                                                   |     | (0 to 0)       | (2.5 to 4.1) | (22.4 to 32.4) | (46.4 to 80.2) | (129.2 to 243.2) | (373 to 709.3) |
| Car trips → motorcycle trips                                      | 0   | 2.0             | 25.2   | 59.4  | 175.5            | 523.3 |
|                                                                   |     | (0 to 0)       | (1.3 to 3.1) | (20.6 to 30.2) | (44.8 to 78.6) | (127.2 to 241.7) | (373.0 to 708.7) |
| Short trips by car, taxi, or motorcycle → cycling trips          | 0   | 2.9             | 26.3   | 60.3  | 176.6            | 534.9 |
|                                                                   |     | (0 to 0)       | (2.1 to 3.5) | (21.8 to 31.4) | (45.9 to 79.5) | (128.8 to 243.2) | (382.9 to 718.9) |
| Short trips by car or taxi → walking trips                       | 0   | 3.0             | 28.1   | 61.5  | 177.4            | 527.8 |
|                                                                   |     | (0 to 0)       | (2.4 to 3.6) | (23.2 to 33.5) | (46.8 to 80.5) | (129.4 to 243.6) | (374.1 to 714.0) |

Short trips = 0 to 6 km. Long trips = 10 km or more. Table 9
Distribution of personal exposure to PM2.5 (μg/m3), by scenario. For each parameter, mean and uncertainty intervals of 95% were generated from 1024 repetitions.

| Scenarios                                                        | Min   | 10th percentile | Median | Mean  | 90th percentile | Max   |
|------------------------------------------------------------------|-------|-----------------|--------|-------|------------------|-------|
| 2009 mode share                                                  | 51.9  | 51.9            | 60.2   | 63.2  | 76.5             | 167.5 |
|                                                                  | (29.3 to 85.2) | (29.3 to 85.2) | (35.1 to 96.7) | (37.2 to 100.8) | (46.4 to 119.7) | (105.4 to 250.3) |
| Bus and walking trips → car trips (reference)                    | 55.1  | 55.1            | 62.1   | 65.1  | 77.6             | 174.6 |
|                                                                  | (31.1 to 90.3) | (31.1 to 90.3) | (35.7 to 99.4) | (37.6 to 103.5) | (46.1 to 121.3) | (110.5 to 262.2) |
| Long trips by car or taxi → bus trips                            | 51.2  | 51.2            | 59.1   | 62.0  | 74.4             | 165.6 |
|                                                                  | (28.8 to 83.8) | (28.8 to 83.8) | (34.3 to 94.5) | (36.1 to 98.7) | (44.5 to 116.6) | (105.1 to 247.8) |
| Car trips → motorcycle trips                                     | 54.5  | 54.5            | 61.6   | 64.6  | 77.1             | 173.4 |
|                                                                  | (30.6 to 89.4) | (30.6 to 89.4) | (35.5 to 98.7) | (37.4 to 102.7) | (45.8 to 120.0) | (109.4 to 259.9) |
| Short trips by car, taxi, or motorcycle → cycling trips          | 55.0  | 55.0            | 62.2   | 65.3  | 78.2             | 175.1 |
|                                                                  | (31.0 to 90.2) | (31.0 to 90.2) | (35.8 to 99.5) | (37.7 to 103.8) | (46.5 to 122.3) | (110.4 to 263.6) |
| Short trips by car or taxi → walking trips                       | 55.0  | 55.0            | 63.0   | 66.5  | 80.9             | 174.4 |
|                                                                  | (31.0 to 90.2) | (31.0 to 90.2) | (36.3 to 100.7) | (38.5 to 105.6) | (47.8 to 126.2) | (110.3 to 262.0) |

Short trips = 0 to 6 km. Long trips = 10 km or more.

Table 10
Road traffic fatalities by travel mode per year, by scenario. For each travel mode, mean and uncertainty intervals of 95% were generated from 1024 repetitions.

| Scenarios             | Walking | Bicycle | Bus | Car | Motorcycle | Total |
|----------------------|---------|---------|-----|-----|------------|-------|
| 2009 mode share      | 213     | 16      | 5   | 19  | 37         | 291   |
|                      | (160 to 341) | (12 to 26) | (4 to 8) | (14 to 30) | (28 to 60) | (218 to 464) |
| Bus and walking trips → car trips (reference) | 314     | 27      | 1   | 41  | 59         | 442   |
|                      | (201 to 536) | (18 to 46) | (0 to 2) | (24 to 72) | (40 to 99) | (303 to 743) |
| Long trips by car or taxi → bus trips | 155     | 12      | 6   | 5   | 29         | 207   |
|                      | (115 to 246) | (9 to 19) | (4 to 10) | (3 to 9) | (22 to 47) | (154 to 329) |
| Car trips → motorcycle trips | 309     | 26      | 1   | 41  | 240       | 617   |
|                      | (199 to 526) | (18 to 43) | (0 to 2) | (28 to 68) | (145 to 426) | (457 to 1003) |
| Short trips by car, taxi, or motorcycle → cycling trips | 311     | 105    | 1   | 40  | 51         | 508   |
|                      | (200 to 531) | (63 to 184) | (0 to 2) | (24 to 70) | (34 to 87) | (369 to 825) |
| Short trips by car or taxi → walking trips | 349     | 27      | 1   | 40  | 58         | 475   |
|                      | (233 to 589) | (18 to 44) | (0 to 2) | (24 to 70) | (40 to 97) | (331 to 787) |

Short trips = 0 to 6 km. Long trips = 10 km or more.
* Uncertainty intervals include uncertainty around 2009 mode share estimates as well as uncertainty in our scenario estimates.

The third most influential parameter was the scalar for non-communicable disease under or overestimation. Other sources of input uncertainty had no or very small impact on outcomes’ variance.

3.4. Sensitivity analysis
Sensitivity analysis results and comparisons between different background conditions are available.

Overall, the direction (i.e., benefit or harm) of the total health impact across scenarios was not significantly affected after considering changes in the city’s wider background context, with the magnitude of total and pathway-specific health impact affected only in few cases. When background road traffic fatalities halved, the scenarios with reduction of short motorised trips in favour of cycling and walking change from a non-significant harm to a close to zero net effect. When the background rate of non-communicable diseases doubled, we observed an approximately 50% increment in averted deaths and YLL due to non-communicable diseases in all scenarios when compared with the physical activity and air pollution. | NCDs | Road collisions | NCDs | Road collisions |
|------|----------------|------|----------------|
| 200  | 1000           | 1000 |                |
| 1150100 | 500        | 500  |                |
| 1    |                | 500  |                |
| 6000 | 50000         | 50000 |               |
| 14000 | 25000        | 25000 |               |
| 2000 |                |      |                |
| 2000 | 50000         | 50000 |               |

Reference scenario: Bus and walking trips to car trips
2009 mode share
Long trips by car to bus trips
Short trips by car or motorcycle to cycling trips
Short trips by car to walking trips

Fig. 3. Deaths and years of life lost due to premature mortality (YLLs) averted per year, by scenario. NCDs: non-communicable diseases. Uncertainty intervals of 95% generated from 1024 repetitions.

relatively high injury risks, and the young demographic with a correspondingly lower burden of non-communicable disease.
Our results indicate a policy challenge. In our reference scenario, in which car use rises, traffic injuries increase, air pollution increases, and physical activity falls. If this increase instead comes from motorcycles, then the injury burden is even higher. However, small increases in walking and cycling levels would not provide net health benefits as health benefits accrued from reducing short motorised trips in favour of active travel modes were offset by the increased number of road fatalities. To avoid this picture and garner the health benefits of a more active travel pattern, further policy action is required to reduce road danger and risk of road fatality. Key strategies include changes to road user behaviour (including speeding, drink driving, and helmet and seat belt use), safer roads (including infrastructure for pedestrians and cyclists), safer vehicles, and post-crash care. These measures are needed not just to directly avoid the burden of traffic injuries but to also support active travel policies to prevent the burden of non-communicable diseases rising with urbanisation and higher incomes.
It should be noted that even in the reference scenario, the walking level is much higher (45 min per day on average) than in many high-income settings (e.g., 23 min in Switzerland, 10.7 min in England and Wales, 7.5 min in California). If it halves to the levels of high-walking Switzerland, then there would be substantial physical activity harms unless the loss is replaced by cycling trips. In settings with such high (non-choice) walking as Accra, replacing some walking with cycling, at least for longer trips, is desirable as the latter provides faster speeds while retaining physical activity benefits. Thus, the importance of promoting and sustaining high levels of active travel should be emphasised. It should also be noted that, in line with the potential impact of policies being considered for the region and informed by local expertise, we only modelled an increase in cycling from 0.5% to 3.5%, still far from what is seen in the highest cycling European or Japanese cities (around 30%). Protecting and improving the conditions for the existing levels of walking combined with much more substantial increases in cycling levels may secure health benefits, providing that mitigation measures against potential increases in road traffic injuries are put in place, as previously mentioned.
ITHIM-Global builds on and expands the strengths of previous ITHIM implementations. The main improvements are the ability to do calculations and scenarios development using a synthetic population instead of aggregated values, which increases flexibility in applying the model in new settings, updates on the road fatality module, expansion of the list of diseases and update of dose–response curves, and implementation of new procedures to deal with and evaluate parametric uncertainty. ITHIM-Global is implemented in R, an open source and free software, and the model code is open access, allowing anyone to check, adapt, and improve it. We also launched a web-interface to make the Deaths
Walk-to-bus time
Cycling mMETs
Walking mMETs
Scalar for non-travel PA
Background PM concentration
Fraction of PM attributable to transport
Injury reporting rate
Safety-in-numbers (SIN) exponents
Fraction of SIN exponents due to casualty mode
Scalar for non-communicable diseases
RR of CHD attributable to PA
RR of stroke attributable to PA
RR of T2D attributable to PA
RR of lung cancer attributable to PA
RR of breast cancer attributable to PA
RR of colon cancer attributable to PA
RR of endometrial cancer attributable to PA
RR of CHD attributable to AP
RR of stroke attributable to AP
RR of lung cancer attributable to AP
RR of COPD attributable to AP
RR of LRI attributable to AP

| 2009 mode share | Long trips by car | Car trips to bus trips | motorcycle trips |
|------------------|------------------|-----------------------|------------------|
|                  |                  |                       |                  |
|                  |                  |                       |                  |

EVPPI (%)
10 20 30 40 50 60

Fig. 4. Expected value of partial perfect information (EVPPI), expressed as percentage of the outcome variance explained by parameter uncertainty, by outcome (deaths and years of life lost) and scenario. CHD: chronic heart disease; COPD: chronic obstructive pulmonary disease; LRI: lower respiratory infection; mMETs: marginal metabolic equivalent of tasks; PA: physical activity; PM: particulate matter with 2.5-μm diameter (PM2.5); RR: relative risk; SIN: safety-in-numbers; T2D: type-2 diabetes mellitus.

Short trips by car
Short trips by motorcycle
Short trips by cycling
Short trips by car to walking trips L. Garcia et al. Environment International 155 (2021) 106680

It should be noted that our approach to uncertainty analysis allowed us to thoroughly test the robustness of our results to the use less-than-optimal data (e.g., dated data sources and some data from Indian cities) to inform the assumptions and inputs of our model. The value-of-information analysis showed that most of these uncertainties had very limited impact on results, reassuring the confidence in our conclusions. It is not unusual that lower-income settings have less-good data than one would feel confident to work with. Nevertheless, arguably these are the settings where this kind of study and its insights are most needed. Value-of-information analysis can allow us to work in such contexts, rigorously testing the implications to conclusions resulting from the uncertainty in parameters, and informing local partners the priorities in terms of data and research gaps to obtain more accurate estimates. For instance, local actions to minimize underreporting rates of road fatalities would greatly reduce the uncertainty in future applications of our model in Accra.

This work has important implications for policy and practice in Ghana and other LMIC. Other cities in Ghana can replicate this model since the datasets used here are mostly subsets of national data, and most of the local stakeholders involved in the Urban Health Initiative and in this study in particular either have direct responsibilities or are linked with those who have responsibilities over multiple cities in Ghana. Because Accra is a strategic player in a number of networks of cities and initiatives targeting sustainable development (e.g., Urban Health Initiative, 100 Resilient Cities, C40 Cities, and Partnership for Healthy Cities), the city can lead and share experiences with other cities on this practical framework. The methodological advances made for Greater Accra Metropolitan Area have already helped to inform the adaptation and application of the model in ten other LMIC cities in Latin America (e.g. Sao Paulo, Bogota), India (e.g. New Delhi, Bengaluru), and Africa (e.g. Cape Town); the results will be published soon. Through the pilot project in Accra, the successful experience of applying the Urban Health Initiative model process to foster multisectoral work and make the best use of local assets (e.g. data, knowledge and expertise) will also contribute to advance World Health Organization’s work in other LMIC to improve the evidence around the population health impacts of decisions in transport.

Despite progress, our study has limitations. We used the best available data for Greater Accra Metropolitan Area to build the scenarios and to test effects of variations in key parameters. However, some data sources were dated (e.g., travel patterns are from 2009). As for the Time Use Survey and World Health Organization’s SAGE, both suffer from the usual limitations of self-reported data, the number of participants available to inform the synthetic population was too small to divide it into more age bands, and we restricted the sample to those living in urban settings in the Greater Accra region, which overlaps with Greater Accra Metropolitan Area but not perfectly. Physical activity behaviour is socially patterned and even though both surveys collected socioeconomic factors, the variables were incompatible and, therefore, could not be used to merge the travel behaviour and non-travel physical activity datasets more accurately. The Time Use Survey recorded activities only in the preceding day, which means that differences in individuals’ travel patterns across the week (e.g., work and non-work days) were not captured. Also, the survey did not ask about motorcycle trips or short walks to/from bus trips (rails trips were asked in the survey but excluded from the analysis because they accounted for only three trips in the dataset). Nevertheless, to the best of our knowledge, this is the first time that a time use survey successfully replaces a travel survey as a source of trip sets in studies of this type, providing reliable and detailed information on travel time and mode by trip over a full 24-hour period. By scaling down the Ghana background number on deaths and YLL for the age- and sex-specific demographic profile of Greater Accra Metropolitan Area population, we may have underestimated the share of non-communicable diseases and road injuries in the target population, highlighting the need for further improvements in the background number of deaths for the area.

Our scenarios assume the trips people make remain the same even if the mode changes. However, access to more motor vehicles might increase travel distances. If this happens then higher motor vehicle scenarios are likely to lead to larger increases in air pollution and traffic injuries.

Only some health impacts were included in the model. Although we tried to include the causes responsible for largest health burden, potential total impacts may be greater than we currently estimated. Other health pathways, such as noise pollution and other forms of interpersonal violence related to travel behaviour (e.g., street harassment) were also not included. Also, no lagged impacts on older age groups were modelled.

5. Conclusions

As in several urban areas in LMIC worldwide, one of the pressing challenges in the Greater Accra Metropolitan Area is how to overcome the negative consequences of an accelerated process of urbanization. Our results indicate that rise in motorisation, particularly in motorcycle trips, have the potential for large health harms, mainly due to road traffic fatalities. Limiting the growth of long trips by car or taxi by increasing bus trips can provide substantive population health benefits in Accra, mostly accrued through reductions in road traffic fatalities. Nevertheless, public transport faces new challenges to with COVID-19. Limiting growth of car, taxi, and particularly motorcycle trips by replacing them for walking and cycling is on the policy agenda for many cities across the globe. Our results show that for Accra realising substantial health benefits, significant improvements in protection of walking, promotion of cycling, and road safety is key.

Our aim was to inform future transport-based policy actions on how they can affect health. Decisions taken by transport and urban planning sectors of cities in LMIC can help to either curb or amplify the long-term health burden for millions of people. Partners and stakeholders engaged throughout the process agree that improving mobility will involve adopting approaches that also maximize the health benefits, with some transport-related policies under development already being informed by this understanding, such as the Accra Climate Action plan as well as Accra’s Resilience Strategy.

The experience also highlighted the importance of the health sector in actively engaging with other sectors within the transport community and supporting decision-making process by integrating health into transport planning. The multisectoral knowledge and data exchange resulting from this experience also highlighted opportunities for continued joint work in the region such through the incorporation of health considerations into the transport sector’s regulatory framework as well as the need for further strengthening the capacity of health authorities to perform integrated health impact assessments.

Walking, cycling and mass transit trips could be made the safest, cheapest, most pleasant, and convenient options for most everyday trips should efforts and investments be shifted towards a more sustainable transport profile that prioritise public transport and active travel. Declaration of Competing Interest
============================

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Acknowledgements
================

We would like to acknowledge the contribution and inputs of all stakeholders involved in the activities of the Urban Health Initiative pilot project in Accra, Ghana. The work was undertaken at the Centre for Diet and Activity Research (CEDAR), a UKCRC Public Health Research Centre of Excellence. Funding from the British Heart Foundation, Cancer Research UK, Economic and Social Research Council, Medical Research Council (MRC), the National Institute for Health Research (ES/G007462/1 and MR/K023187/1), and the Wellcome Trust (087636/Z/08/Z), under the auspices of the UK Clinical Research Collaboration, is gratefully acknowledged. Additionally, this work has been supported by the Climate and Clean Air Coalition through the grant provided for the Urban Health and SLCP Reduction project in Accra and by the Government of Norway through its financial contribution to advance WHO’s work on air pollution and urban health. LG, AA, RG, MT, and JW were supported by TIGTHAT, an MRC Global Challenges Project (MR/P024408/1). RJ’s work was partially supported by MRC grant (MR/U105260566). The authors alone are responsible for the views expressed in this article and they do not necessarily represent the views, decisions, or policies of the institutions with which they are affiliated.

References
==========

ActionAid, 2015. Women and the city III: a summary of baseline data on violence against women and girls in seven countries. ActionAid, Johannesburg.
Ainsworth B.E., Haskell W.L., Herrmann S.D., Meckes N., Bassett Jr D.R., Tudor-Locke C., et al. The compendium of physical activities tracking guide 2020.
Burnett, R.T., Pope III, C.A., Ezzati, M., Olives, C., Lim, S.S., Mehta, S., et al., 2014. An integrated risk function for estimating the global burden of disease attributable to ambient fine particulate matter exposure. Environ. Health Perspect. 122 (4), 397–403.
Dionisio, K.L., Arku, R.E., Hughes, A.F., Vallarino, J., Carmichael, H., Spengler, J.D., et al., 2010. Air pollution in Accra neighborhoods: spatial, socioeconomic, and temporal patterns. Environ. Sci. Technol. 44, 2270–2276.
Elvik, R., Goel, R., 2019. Safety-in-numbers: an updated meta-analysis of estimates. Accid. Anal. Prev. 129, 136–147.
Garcia, L.M.T., Strain, T., Abbas, A., Mok, A., Pearce, M., Crippa, A., et al., 2020. Physical activity and risk of cardiovascular disease, cancer, and mortality: a dose-response meta-analysis of prospective studies. PROSPERO record: CRD42018095481.
Ghana Environmental Protection Agency, 2014. Roadmap to emission and fuel economy standards in Ghana: period 2014-2020. Environmental Protection Agency, Accra.
Ghana Ministry of Roads and Highways, 2013. Ghana Ministry of Transport, Ghana Statistical Service. Second national household transport survey. Ghana Statistical Service, Accra.
Ghana Ministry of Transport, 2016. Transport master plan: Greater Accra region. Ghana Ministry of Transport, Accra.
Ghana Statistical Service, 2009. How Ghanaian women and men spend their time: Ghana time use survey 2009 - main report. Ghana Statistical Service, Accra.
Ghana Statistical Service. Population projection 2017.
Goel, R., Guttikunda, S.K., Mohan, D., Tiwari, G., 2015. Benchmarking vehicle and passenger travel characteristics in Delhi for on-road emissions analysis. Travel. Behav. Soc. 2 (2), 88–101.
Goel, R., Guttikunda, S.K., 2015. Evolution of on-road vehicle exhaust emissions in Delhi. Atmos. Environ. 105, 78–90.
Goel, R., Gani, S., Guttikunda, S.K., Wilson, D., Tiwari, G., 2015. On-road PM2.5 pollution exposure in multiple transport microenvironments in Delhi. Atmos. Environ. 123, 129–138.
G¨otschi, T., Tainio, M., Maizlish, N., Schwanen, T., Goodman, A., Woodcock, J., 2015. Contrasts in active transport behaviour across four countries: how do they translate into public health benefits. Prev. Med. 74, 42–48.
India Office of the Registrar General and Census Commissioner, 2020. Number of households availing banking services and number of households having each of the specified assets 2020.
Institute for Health Metrics and Evaluation. GBD results tool 2020.
International Energy Agency, 2019. CO2 Emissions from Fuel Combustion – Highlights. International Energy Agency, Paris.
Jackson, C., Presanis, A., Conti, S., De Angelis, D., 2019. Value of information: sensitivity analysis and research design in bayesian evidence synthesis. J. Am. Stat. Assoc. 114 (528), 1436–1449.
Korean International Cooperation Agency, 2016. Ghana Ministry of Transport. The transport master plan project in Greater Accra Region. Ghana Ministry of Transport, Accra.
Kwan, S.C., Tainio, M., Woodcock, J., Sutan, R., Hashim, J.H., 2017. The carbon savings and health co-benefits from the introduction of mass rapid transit system in Greater Kuala Lumpur, Malaysia. J. Transp. Health. 6, 187–200.
Ling-Yun, H.E., Lu-Yi, Q.I.U., 2016. Transport demand, harmful emissions, environment and health co-benefits in China. Energy Policy 97, 267–275.
Maizlish, N., Woodcock, J., Co, S., Ostro, B., Fanai, A., Fairley, D., 2013. Health co-benefits and transportation-related reductions in greenhouse gas emissions in the San Francisco Bay area. Am. J. Public Health 103 (4), 703–709.
Mueller, N., Rojas-Rueda, D., Cole-Hunter, T., de Nazelle, A., Dons, E., Gerike, R., et al., 2015. Health impact assessment of active transportation: a systematic review. Prev. Med. 76, 103–114.
Mueller, N., Rojas-Rueda, D., Basaga˜na, X., Cirach, M., Cole-Hunter, T., Dadvand, P., et al., 2017. Health impacts related to urban and transport planning: A burden of disease assessment. Environ. Int. 107, 243–257.
European Platform on Mobility Management. The EPOMM modal split tool 2020.
Roth, G.A., Abate, D., Abate, K.H., Abay, S.M., Abbafati, C., Abbasi, N., et al., 2018. Global, regional, and national age-sex-specific mortality for 282 causes of death in 195 countries and territories, 1980–2017: a systematic analysis for the Global Burden of Disease Study 2017. Lancet 392 (10159), 1736–1788.
S´a, T.H., Tainio, M., Goodman, A., Edwards, P., Haines, A., Gouveia, N., et al., 2017. Health impact modelling of different travel patterns on physical activity, air pollution and road injuries for S˜ao Paulo, Brazil. Environ. Int. 108, 22–31.
Smith, A.D., Crippa, A., Woodcock, J., Brage, S., 2016. Physical activity and incident type 2 diabetes mellitus: a systematic review and dose–response meta-analysis of prospective cohort studies. Diabetologia 59 (12), 2527–2545.
Tainio, M., Jovanovic Andersen, Z., Nieuwenhuijsen, M.J., Hu, L., de Nazelle, A., An, R., et al., 2021. Air pollution, physical activity and health: a mapping review of the evidence. Environ. Int. 147, 105954.
Tashayo, B., Alimohammadi, A., Sharif, M., 2017. A hybrid fuzzy inference system based on dispersion model for quantitative environmental health impact assessment of urban transportation planning. Sustainability. 9 (1), 134.
United Nations. World urbanization prospects 2018.
Vu, V.H., Le, X.Q., Pham, N.H., Hens, L., 2013. Application of GIS and modelling in health risk assessment for urban road mobility. Environ. Sci. Pollut. Res. Int. 20 (8), 5138–5149.
Whitmee, S., Haines, A., Beyrer, C., Boltz, F., Capon, A.G., Souza Dias, B.F., et al., 2015. Safeguarding human health in the Anthropocene epoch: report of The Rockefeller Foundation-Lancet Commission on planetary health. Lancet 386 (10007), 1973–2028.
Woodcock, J., Edwards, P., Tonne, C., Armstrong, B.G., Ashiru, O., Banister, D., et al., 2009. Public health benefits of strategies to reduce greenhouse-gas emissions: urban land transport. Lancet 374 (9705), 1930–1943.
Woodcock, J., Givoni, M., Morgan, A.S., 2013. Health impact modelling of active travel visions for England and Wales using an Integrated Transport and Health Impact Modelling Tool (ITHIM). PLoS One 8 (1), e51462.
Woodcock, J., Tainio, M., Cheshire, J., O’Brien, O., Goodman, A., 2014. Health effects of the London bicycle sharing system: health impact modelling study. BMJ 348, g425.
World Health Organization, 2013. Study on global aging and adult health (SAGE) wave 1: the Ghana national report. World Health Organization, Geneva.
World Health Organization, 2011. Urban Transport and Health: A Sourcebook for Policy-Makers in Developing Cities. World Health Organization, Geneva.
World Health Organization, 2016. Global report on urban health: equitable, healthier cities for sustainable development. World Health Organization, Geneva. L. Garcia et al.
Environment International 155 (2021) 106680

World Health Organization, 2018. Global status report on road safety 2018. World Health Organization, Geneva.
World Health Organization, 2020. Modelled global ambient air pollution estimates 2020.
World Health Organization. Global physical activity surveillance 2020.
Zhou, Z., Dionisio, K.L., Verissimo, T.G., Kerr, A.S., Coull, B., Howie, S., et al., 2014. Chemical characterization and source apportionment of household fine particulate matter in rural, peri-urban, and urban West Africa. Environ. Sci. Technol. 48 (2), 1343–1351. 