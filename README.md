# Primary Healthcare Accessibility in Kano State, Nigeria

<p align="center">
  <img src="assets/project_cover/kano_phc_accessibility_project_cover.png" alt="Kano primary healthcare accessibility project" width="100%">
</p>

## The question

**Where are the main gaps in primary healthcare access across Kano State, and where could new PHCs make the greatest difference?**

I combined road-network travel time, population demand and a **15-minute two-step floating catchment area (2SFCA)** analysis. The final dataset covers **1,584 PHCs, 484 wards and 16,789 population-demand cells**. I then tested **97 possible new PHC locations** and compared +5, +10 and +20 facility scenarios.

## What I found

| Scenario | Population-weighted 2SFCA |
|---|---:|
| Baseline | **0.8438** |
| +5 PHCs | **0.8465** |
| +10 PHCs | **0.8492** |
| +20 PHCs | **0.8545** |

The +20 scenario raised the statewide population-weighted 2SFCA value by **1.26%**. Around **687,356 people (3.66%)** experienced some improvement in modelled accessibility.

The result is useful because it tempers a simple assumption: **building more PHCs can help selected underserved communities, but new facilities alone do not solve statewide access.**

## The access gap

<p align="center">
  <img src="assets/maps/04_Multi_Dimensional_Underserved_Wards.png" alt="Multi-dimensional underserved wards in Kano State" width="100%">
</p>
<p align="center"><em>Underserved wards identified from overlapping access problems rather than a single indicator.</em></p>

<p align="center">
  <img src="assets/maps/05_Healthcare_Planning_Priority_Wards.png" alt="Healthcare planning-priority wards in Kano State" width="100%">
</p>
<p align="center"><em>A planning screen showing wards that deserve closer attention when future PHC investment is considered.</em></p>

## Travel time is only part of the story

A nearby facility can still be under pressure when it serves a large surrounding population. I therefore compared travel time with spatial availability instead of treating distance alone as access.

<p align="center">
  <img src="assets/maps/02_Network_Travel_Time_to_Nearest_PHC.png" alt="Road-network travel time to the nearest PHC in Kano State" width="100%">
</p>
<p align="center"><em>Modelled road-network travel time to the nearest mapped PHC.</em></p>

<p align="center">
  <img src="assets/maps/03_Validated_15min_2SFCA_Healthcare_Accessibility.png" alt="15-minute 2SFCA healthcare accessibility in Kano State" width="100%">
</p>
<p align="center"><em>The 2SFCA result adds surrounding population demand to the location of PHCs.</em></p>

## Where new PHCs could help

<p align="center">
  <img src="assets/maps/07_Validated_Top20_New_PHC_Candidate_Sites.png" alt="Top 20 candidate PHC locations in Kano State" width="100%">
</p>
<p align="center"><em>Twenty model-selected candidate locations. These are planning candidates, not approved facility sites.</em></p>

<p align="center">
  <img src="assets/charts/01_Validated_Statewide_2SFCA_Expansion.png" alt="Statewide accessibility under PHC expansion scenarios" width="90%">
</p>
<p align="center"><em>Statewide improvement remains modest as facilities are added, which supports targeted rather than blanket expansion.</em></p>

## Method

1. Measured road-network travel time from population-demand locations to existing PHCs.
2. Calculated 15-minute 2SFCA accessibility using facility count as the supply measure.
3. Summarised the results at ward level and identified places where several access problems overlap.
4. Built a healthcare planning-priority classification.
5. Evaluated 97 possible new PHC locations and tested +5, +10 and +20 scenarios.
6. Repeated the analysis under alternative distance-decay assumptions.
7. Reproduced the final candidate catchments and scenario results during validation.

## Checks and uncertainty

The final review reproduced all **20 selected candidate-site catchments** and all **4 binary expansion scenarios** within numerical tolerance. The broad conclusion also remained stable under alternative distance-decay assumptions, although some local rankings changed.

For that reason, I place more weight on **places that remain underserved across several tests** than on small differences in exact rank. Validation material is in [`validation`](validation/), and the main result tables are in [`data/core_results`](data/core_results/).

## What this means for planning

The analysis supports targeted PHC expansion, but it also shows the limit of location-only planning. A stronger assessment would include staffing, equipment, opening hours, service volume, patient use and facility capacity. Those variables are outside this project, so the 2SFCA result should be read as **modelled spatial availability**, not healthcare quality.

## Project files

The seven final maps are in [`assets/maps`](assets/maps/), analytical charts are in [`assets/charts`](assets/charts/), and the technical report is in [`reports`](reports/).

**Tools:** Python · GeoPandas · NetworkX · Pandas · Matplotlib · GIS · road-network analysis · 2SFCA

## Author

**Abdullah Abdazeez Ayomide**  
Geospatial Planner · GIS & Remote Sensing Analyst

[GitHub](https://github.com/Abdullahabdazeez) · [LinkedIn](https://ng.linkedin.com/in/abdazeez-abdullah-4b814719a)

## Citation and licence

Citation metadata is provided in [`CITATION.cff`](CITATION.cff). External datasets remain subject to their original providers' terms.
