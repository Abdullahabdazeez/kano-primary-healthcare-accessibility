# Spatial Accessibility and Equity of Primary Healthcare Services in Kano State, Nigeria: A Network-Based 2SFCA Analysis

## Problem

Healthcare facilities may be geographically close to communities
without providing equitable access when large populations compete for
limited services. I developed a GIS-based accessibility model to
identify where primary healthcare access is weakest across Kano State.

## What I Did

I integrated:

- GRID3 health-facility data;
- GRID3/WorldPop 2025 population estimates;
- GRID3 operational wards;
- OpenStreetMap road-network data.

I created a 1,584-facility PHC inventory, a
18.77-million-person population-demand framework
and a statewide routable road network.

Using Python, GeoPandas, OSMnx and NetworkX, I calculated network
travel time to the nearest PHC and implemented a 15-minute
Two-Step Floating Catchment Area model.

I then developed a multi-dimensional underserved-community typology
and a composite healthcare planning-priority index for all
484 wards.

Finally, I identified strategic candidate sites for new PHCs and
tested +5, +10 and +20 facility expansion scenarios.

## Key Findings

- 97.78% of the modeled population is
  within 10 minutes of a PHC.
- Statewide population-weighted 2SFCA accessibility is
  0.8438 PHCs per 10,000 people.
- 84 critical/compound underserved wards contain
  approximately 2.76
  million people.
- 97 wards were classified as Very High planning
  priority.
- Yangizo in Warawa ranked as the
  highest-priority ward.
- A strategic +10 PHC scenario improves modeled 2SFCA accessibility
  for approximately
  556,701 people.

## Skills Demonstrated

GIS network analysis | Health GIS | 2SFCA | Spatial equity analysis |
Population modelling | OSMnx | NetworkX | GeoPandas | Python |
Spatial decision support | Scenario analysis | Cartography

## Planning Value

The project demonstrates how spatial planning can move beyond simple
facility distribution maps by integrating population demand,
transport networks and healthcare supply to support evidence-based
infrastructure investment.