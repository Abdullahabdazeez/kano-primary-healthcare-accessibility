# Project Report: Primary Healthcare Accessibility in Kano State

## Background

Having a health facility nearby does not always mean that healthcare access is adequate. A PHC can be close to a community and still serve far more people than it can reasonably support.

I developed this project to look at primary healthcare access in Kano State from both sides: how long people need to travel to a PHC, and how much facility supply is available relative to surrounding population demand.

## What I did

The analysis covers **1,584 PHCs, 484 wards and 16,789 population-demand cells**.

I first measured road-network travel time to the nearest PHC. I then calculated a 15-minute two-step floating catchment area (2SFCA) score using facility count as the supply measure.

After mapping the baseline pattern, I identified wards where several access problems overlap, built a planning-priority classification and tested **97 possible new PHC locations**. From those candidates, I evaluated +5, +10 and +20 PHC expansion scenarios.

I also repeated the accessibility analysis under alternative distance-decay assumptions to see whether the overall conclusion depended too heavily on one modelling choice.

## What I found

The baseline population-weighted 2SFCA value was **0.8438 PHCs per 10,000 people**.

The tested expansion scenarios increased that value to:

- **0.8465** with +5 PHCs;
- **0.8492** with +10 PHCs; and
- **0.8545** with +20 PHCs.

The +20 scenario therefore improved the statewide population-weighted score by only **1.26%**.

Around **687,356 people (3.66%)** experienced some improvement in modelled accessibility under that scenario.

## What the result means

The result does not suggest that new PHCs are unimportant. It shows that location matters and that carefully targeted facilities can help specific underserved communities.

At the same time, adding facilities alone produces only a modest statewide change. That means a broader healthcare strategy also needs to consider what happens inside the facilities: staffing, equipment, operating hours, service volume and actual capacity.

## Why I do not call this healthcare quality

The project does not include staffing, beds, equipment, patient utilisation or service-quality information. For that reason, the 2SFCA score is a measure of **modelled spatial availability**, not realised healthcare quality.

That distinction is important. A location can look well served spatially while the facilities available to residents are still under-resourced.

## Validation and sensitivity

The final review reproduced all 20 selected candidate-site catchments and all four baseline/expansion scenarios within numerical tolerance.

I also checked whether low-access patterns remained similar under different distance-decay functions. Some local rankings changed, but the broad pattern was stable enough that I place more emphasis on persistent underserved areas than on small differences in exact rank.

## What I would add next

The strongest next step would be to include facility capacity and service data. That would make it possible to move from facility-count accessibility toward a more realistic measure of effective healthcare access.

Patient-flow or utilisation data would also help test whether the modelled catchments reflect how people actually use the health system.

## Main outputs

The final maps are in [`assets/maps`](../assets/maps/), charts in [`assets/charts`](../assets/charts/), result tables in [`data/core_results`](../data/core_results/) and validation records in [`validation`](../validation/).

## Final note

The main planning lesson from this project is not simply "build more PHCs." It is to place new facilities where they solve a clear spatial problem, while recognising that location is only one part of healthcare access.
