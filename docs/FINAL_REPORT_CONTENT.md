# Spatial Accessibility and Equity of Primary Healthcare Services in Kano State, Nigeria: A Network-Based 2SFCA Analysis

## 1. Project Overview

Access to primary healthcare is influenced not only by the physical
distance between populations and health facilities, but also by the
relationship between healthcare supply and the population competing
for available services.

This project evaluated spatial accessibility to primary healthcare
facilities across Kano State, Nigeria using road-network analysis,
high-resolution population data and the Two-Step Floating Catchment
Area (2SFCA) method.

The analysis covered all 44 Local Government Areas,
484 operational wards, 1,584 primary healthcare
facilities and an estimated 2025 population of 18,771,134.

## 2. Problem Statement

Conventional facility counts and straight-line proximity measures can
create an incomplete picture of healthcare accessibility. Communities
may be geographically close to a health facility while still
experiencing inadequate access because large surrounding populations
compete for limited healthcare supply.

The project therefore examined both:

- physical accessibility through road-network travel time; and
- spatial supply-demand accessibility using 2SFCA.

The analysis further identified underserved wards and evaluated
strategic locations where additional PHC capacity could improve
healthcare equity.

## 3. Objectives

The project aimed to:

1. map the spatial distribution of primary healthcare facilities;
2. estimate road-network travel time from population demand locations
   to the nearest PHC;
3. calculate healthcare supply-demand accessibility using a
   15-minute 2SFCA model;
4. identify wards experiencing multiple dimensions of healthcare
   underservice;
5. develop a ward-level healthcare planning-priority index; and
6. evaluate strategic PHC expansion scenarios.

## 4. Data

### Administrative Boundaries
GRID3 operational wards and Kano State/LGA administrative boundaries
were used. The final framework contained 44 LGAs and
484 operational wards.

### Population
GRID3/WorldPop Nigeria Population v3.0 (2025) was used to represent
population demand. Kano State's validated modeled population was
18,771,134.

Population was aggregated into 1-km routing demand cells while
preserving ward-level population allocation.

### Healthcare Facilities
GRID3 Nigeria Health Facilities v2.0 was used to extract primary-level
facilities. A total of 1,584 PHCs were retained after
validation.

### Road Network
OpenStreetMap drivable-road data were retrieved using OSMnx. The final
routing graph contained 151,507 nodes and 444,940 directed edges.

## 5. Methodology

### Road-Network Accessibility

Population demand points and PHCs were snapped to the road network.
Road-class-specific travel speeds were assigned and shortest-path
analysis was conducted from each population origin to the nearest PHC.

### 2SFCA

A 15-minute network-based Two-Step Floating Catchment Area model was
implemented.

Step 1 calculated the supply-to-demand ratio for each PHC catchment.

Step 2 summed accessible facility ratios for each population demand
location, producing a spatial accessibility score expressed as PHCs
per 10,000 population.

### Underserved-Ward Identification

Three relative access dimensions were evaluated:

- low 2SFCA supply accessibility;
- high network travel time; and
- low population coverage within five minutes.

Wards disadvantaged in all three dimensions were classified as
Critical Underserved. Wards disadvantaged in two dimensions were
classified as Compound Underserved.

### Planning Priority

A composite planning-priority index combined:

- 35% supply deficit;
- 30% travel-time severity;
- 20% low five-minute coverage; and
- 15% population exposure.

The resulting score was used to rank all 484 wards.

## 6. Key Results

### Network Accessibility

Population-weighted mean travel time to the nearest PHC was
2.45 minutes.

Approximately:

- 86.41% of the population was within
  five minutes;
- 97.78% was within ten minutes; and
- 99.67% was within fifteen minutes.

The ward with the highest population-weighted mean travel time was
Yangizo in Warawa LGA at
9.81 minutes.

### 2SFCA Accessibility

The statewide population-weighted 15-minute 2SFCA score was
0.8438 PHCs per 10,000 people.

Dawakin Kudu recorded the lowest LGA-level weighted 2SFCA score
at 0.4615 PHCs per 10,000.

The results demonstrate that short travel time does not necessarily
translate into adequate healthcare supply because densely populated
communities may experience greater competition for nearby facilities.

### Underserved Communities

The analysis identified:

- 29 Critical Underserved wards containing
  904,163 people;
- 55 Compound Underserved wards containing
  1,855,073 people.

Together, 84 wards containing approximately
2,759,236 people
(14.70% of the modeled
population) experienced multiple dimensions of healthcare
underservice.

### Planning Priority

A total of 97 wards were classified as Very High
planning priority, representing approximately
3,240,955 people.

The highest-ranked ward was Yangizo in
Warawa LGA with a planning-priority score of
77.88/100.

High and Very High priority wards together contained approximately
8,152,461 people
(43.43%).

## 7. Scenario Analysis

Strategic candidate sites for additional PHCs were identified using
population concentration, existing 2SFCA deficit, network travel time,
distance from existing PHCs and ward planning priority.

Three scenarios were tested:

- +5 PHCs;
- +10 PHCs; and
- +20 PHCs.

The +10 scenario was selected as the preferred medium-term
intervention.

Under this scenario:

- population-weighted mean travel time declined from
  2.455 to
  2.414 minutes;
- population-weighted 2SFCA increased from
  0.8438 to
  0.8492;
- approximately
  556,701 people
  experienced improved modeled supply accessibility.

## 8. Planning Implications

The results suggest that healthcare planning in Kano should move
beyond facility counts alone.

Although physical proximity to PHCs is generally high, substantial
spatial inequalities remain in healthcare supply relative to
population demand.

Investment should therefore prioritize wards where:

- supply-demand accessibility is low;
- travel-time disadvantage is high;
- short-distance population coverage is poor; and
- large populations are exposed.

The proposed +10 PHC scenario provides a phased intervention strategy
for improving access while retaining the option for longer-term
expansion.

## 9. Limitations

The analysis models spatial accessibility and does not measure actual
facility capacity, staffing levels, medicine availability, service
quality, operating hours or patient preferences.

Road travel speeds were modeled using road classes rather than
observed traffic conditions.

Candidate PHC locations are strategic accessibility intervention
points rather than parcel-level construction recommendations.
Detailed site feasibility studies would still be required.

## 10. Conclusion

Kano State demonstrates high geographical proximity to primary
healthcare facilities but substantial inequality in healthcare
supply relative to population demand.

Combining network analysis with 2SFCA revealed spatial inequalities
that simple nearest-facility analysis would not identify.

The project demonstrates how GIS-based accessibility modelling can
support evidence-based healthcare planning, identify underserved
communities and prioritize strategic infrastructure investment.