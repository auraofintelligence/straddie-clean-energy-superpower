from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_TITLE = "Straddie Clean Energy Superpower"
BASE_URL = "https://auraofintelligence.github.io/straddie-clean-energy-superpower/"
ASSET_VERSION = "20260615-energy-superpower-v3"
DESCRIPTION = (
    "A self-sovereign public atlas for exploring clean energy options on Minjerribah / "
    "North Stradbroke Island: rooftop solar, solar thermal, sand batteries, compressed air, "
    "green hydrogen, desalination, brine loops, power sharing, water-height imagination, "
    "quiet marine energy, fractal no-blade wind and community wealth."
)


PAGES = [
    {
        "id": "home",
        "label": "Home",
        "href": "index.html",
        "title": "Straddie Clean Energy Superpower",
        "description": DESCRIPTION,
    },
    {
        "id": "options",
        "label": "Options",
        "href": "options.html",
        "title": "Energy Options Map",
        "description": "A plain-English map of which energy options look near-term, which invite bench tests, and which work best as careful questions for now.",
    },
    {
        "id": "solar",
        "label": "Solar",
        "href": "solar.html",
        "title": "Rooftops, Shade And Solar Heat",
        "description": "Could island roofs, shade structures, ferry-gateway car parks and solar thermal tests become the first clean energy layer?",
    },
    {
        "id": "storage",
        "label": "Storage",
        "href": "storage.html",
        "title": "Sand, Air And Heat Storage",
        "description": "Could sand, heat, pressure air, EVs and demand shifting turn island sunlight into evening abundance while the deeper pressure-carbon-response weave gets its own future repo?",
    },
    {
        "id": "hydrogen",
        "label": "Hydrogen",
        "href": "hydrogen.html",
        "title": "Green Hydrogen, Desal And Brine Loops",
        "description": "Could solar, desalinated water, electrolysis, oxygen, heat, brine minerals and bay repair questions become one transparent island water-energy loop?",
    },
    {
        "id": "sharing",
        "label": "Power sharing",
        "href": "sharing.html",
        "title": "Power Sharing And Neighbourhood Batteries",
        "description": "Could local solar be worth more when it is shared, stored, shifted into EVs or settled through a plain community ledger before it leaves the island cheaply?",
    },
    {
        "id": "water",
        "label": "Water height",
        "href": "water-height.html",
        "title": "Sand Hills, Lakes And Pumped-Hydro Lessons",
        "description": "Could Straddie learn from Snowy, Wivenhoe, Kidston, Borumba and pumped-hydro atlases while asking its own ocean, bay, sand-hill, perched-lake, aquifer and mineral-sands questions?",
    },
    {
        "id": "marine",
        "label": "Marine",
        "href": "marine.html",
        "title": "Wave And Tidal Without Underwater Blades",
        "description": "Could wave and tide be explored from first principles: flutter, vortex shedding, shrimp timing, mantis-shrimp strikes, reef geometry, sensors, play, modelling and maker-space tests?",
    },
    {
        "id": "reefs",
        "label": "Reefs",
        "href": "reefs.html",
        "title": "Reefs, Surf Banks And Sand Media",
        "description": "Could oyster reefs, living shorelines, surf banks, stable dunes, artificial islands and Sandworm tunnel material flows become one inspectable abundance map?",
    },
    {
        "id": "wind",
        "label": "Fractal wind",
        "href": "wind.html",
        "title": "Fractal Wind And No-Blade Harvesting",
        "description": "Could Straddie read wind as edge-flow, roof turbulence, vortex, flutter, electrostatic, piezo and triboelectric motion across many useful island places?",
    },
    {
        "id": "network",
        "label": "Network",
        "href": "network.html",
        "title": "Linked Local Labs",
        "description": "Deep links to the maker-space, Sandworm, ferry terminal lab, grants lab, community wealth and mutuals, and Ready S.E.T. Trust Hub.",
    },
    {
        "id": "wealth",
        "label": "Wealth",
        "href": "wealth.html",
        "title": "Community Wealth And Mutual Care",
        "description": "Could clean energy income, lower bills, mutual protection and grant readiness become patient local wealth rather than another extraction story?",
    },
    {
        "id": "builders",
        "label": "Builders",
        "href": "builders/index.html",
        "title": "Markdown Builders",
        "description": "Browser-only forms for clean energy option notes, boundaries, source trails and grant-ready project briefs.",
    },
    {
        "id": "boundaries",
        "label": "Boundaries",
        "href": "boundaries.html",
        "title": "Boundaries Before Momentum",
        "description": "Consent, Country, engineering review, marine life, pressure systems, response systems and public/private data boundaries.",
    },
    {
        "id": "sources",
        "label": "Sources",
        "href": "sources.html",
        "title": "Source Trail",
        "description": "Official sources, connected repos and research notes used to scaffold this first clean energy atlas.",
    },
    {
        "id": "licence",
        "label": "Licence",
        "href": "licence.html",
        "title": "Public Licence",
        "description": "The custom public-interest licence for learning from, sharing and adapting this clean-energy atlas without turning it into extractive repackaging.",
    },
    {
        "id": "site-map",
        "label": "Site map",
        "href": "site-map.html",
        "title": "Site Map",
        "description": "All public pages, builder pages, Markdown templates and source bridges.",
    },
]


HERO_IMAGES = {
    "home": "assets/img/heroes/home-energy.webp",
    "options": "assets/img/heroes/options-atlas.webp",
    "solar": "assets/img/heroes/home-energy.webp",
    "storage": "assets/img/heroes/storage-abundance.webp",
    "hydrogen": "assets/img/heroes/hydrogen-water-loop.webp",
    "sharing": "assets/img/heroes/sharing-commons.webp",
    "water": "assets/img/heroes/water-height-geography.webp",
    "marine": "assets/img/heroes/marine-energy.webp",
    "reefs": "assets/img/heroes/reef-sand-surf-banks.webp",
    "wind": "assets/img/heroes/fractal-wind-lab.webp",
    "network": "assets/img/heroes/local-labs-network.webp",
    "wealth": "assets/img/heroes/wealth-hours.webp",
    "builders": "assets/img/heroes/builders.webp",
    "boundaries": "assets/img/heroes/boundaries-care-map.webp",
    "sources": "assets/img/heroes/sources.webp",
    "licence": "assets/img/heroes/sources.webp",
    "site-map": "assets/img/heroes/site-map-tabletop.webp",
}


COMPANION_LINKS = [
    {
        "title": "Straddie Maker-Space Lab",
        "site": "https://auraofintelligence.github.io/straddie-makerspace-lab/",
        "repo": "https://github.com/auraofintelligence/straddie-makerspace-lab",
        "summary": "The practical workshop doorway: repair, tools, containers, sand and concrete tests, forms and public learning loops.",
    },
    {
        "title": "Sandworm Subterranean Systems",
        "site": "https://auraofintelligence.github.io/sandworm-subterranean-systems/",
        "repo": "https://github.com/auraofintelligence/sandworm-subterranean-systems",
        "summary": "The deeper systems map for sand batteries, reef-energy questions, future tunnels, material loops and source-aware builders.",
    },
    {
        "title": "Dunwich / Gumpi Ferry Terminal Open Data Lab",
        "site": "https://auraofintelligence.github.io/dunwich-gumpi-ferry-terminal-open-data-lab/",
        "repo": "https://github.com/auraofintelligence/dunwich-gumpi-ferry-terminal-open-data-lab",
        "summary": "The ferry gateway lab: public evidence, official-source trail, 360 photos, simulation workflows and capability transfer.",
    },
    {
        "title": "Stradbroke Grants Lab",
        "site": "https://auraofintelligence.github.io/stradbroke-grants-lab/",
        "repo": "https://github.com/auraofintelligence/stradbroke-grants-lab",
        "summary": "The grant-readiness layer for turning energy experiments into profile packs, milestones, watchlists and reporting evidence.",
    },
    {
        "title": "Community Wealth and Mutual Care",
        "site": "https://auraofintelligence.github.io/moreton-bay-community-wealth-and-mutuals/",
        "repo": "https://github.com/auraofintelligence/moreton-bay-community-wealth-and-mutuals",
        "summary": "The community wealth, data sovereignty and mutual-protection doorway for keeping value and risk legible.",
    },
    {
        "title": "Ready S.E.T. Co-op Trust Hub",
        "site": "https://auraofintelligence.github.io/ready-set-co-op-trust-hub/",
        "repo": "https://github.com/auraofintelligence/ready-set-co-op-trust-hub",
        "summary": "The trust, jobs, media, co-working and co-op pathway that could help people enter the energy work voluntarily.",
    },
    {
        "title": "Ballow Road Sand & Screen Hub",
        "site": "https://auraofintelligence.github.io/ballow-road-sand-screen-hub/",
        "repo": "https://github.com/auraofintelligence/ballow-road-sand-screen-hub",
        "summary": "A nearby public proposal for gateway activity, markets, screen culture and public-facing place energy.",
    },
    {
        "title": "Civilisation of Sand",
        "site": "https://auraofintelligence.github.io/civilisation-of-sand/",
        "repo": "https://github.com/auraofintelligence/civilisation-of-sand",
        "summary": "The bigger quest layer for capability growth, sand, storage, simulation rooms and local resource imagination.",
    },
]


SOURCE_LINKS = [
    {
        "title": "Dunwich / Gumpi Ferry Terminal Upgrade",
        "url": "https://www.yoursay-projects.tmr.qld.gov.au/dunwich-gumpi-ferry-terminal-upgrade",
        "publisher": "Queensland Department of Transport and Main Roads",
        "use": "Grounds the ferry gateway as a real public infrastructure node before any energy lab claim gets too abstract.",
    },
    {
        "title": "Small-scale installation postcode data",
        "url": "https://cer.gov.au/markets/reports-and-data/small-scale-installation-postcode-data",
        "publisher": "Clean Energy Regulator",
        "use": "Provides the public data trail for rooftop solar and newer solar-battery postcode checks.",
    },
    {
        "title": "Solar power for your home",
        "url": "https://www.qld.gov.au/housing/buying-owning-home/energy-water-home/solar",
        "publisher": "Queensland Government",
        "use": "Keeps home solar and battery guidance tied to practical household, electrical and network questions.",
    },
    {
        "title": "Feed-in tariffs",
        "url": "https://www.qld.gov.au/housing/buying-owning-home/energy-water-home/solar/feed-in-tariffs",
        "publisher": "Queensland Government",
        "use": "Clarifies that South East Queensland feed-in tariffs are market offers and that regional customers have a separate regulated pathway.",
    },
    {
        "title": "Solar feed-in tariffs",
        "url": "https://www.ergon.com.au/retail/residential/tariffs-and-prices/solar-feed-in-tariff",
        "publisher": "Ergon Energy Retail",
        "use": "Provides a current Queensland reference point for why exported solar value can be much lower than the value of useful local consumption.",
    },
    {
        "title": "Community Batteries for Household Solar program",
        "url": "https://www.dcceew.gov.au/energy/renewable/community-batteries",
        "publisher": "Australian Government DCCEEW",
        "use": "Grounds neighbourhood batteries as shared storage that can lower bills, store excess solar, reduce grid pressure and help households without their own solar.",
    },
    {
        "title": "Community batteries",
        "url": "https://www.ergon.com.au/network/manage-your-energy/smarter-energy/our-network-batteries/community-batteries",
        "publisher": "Ergon Energy Network",
        "use": "Shows Queensland network batteries storing rooftop solar locally and being tested through Battery Neighbourhoods.",
    },
    {
        "title": "Unlocking CER Benefits Through Flexible Trading rule change",
        "url": "https://energyinnovationtoolkit.gov.au/article/regulatory-changes/unlocking-cer-benefits-through-flexible-trading-rule-change-final",
        "publisher": "AER Energy Innovation Toolkit",
        "use": "Frames flexible trading, consumer energy resources, EV batteries, smart meters and multiple service providers as an emerging regulated pathway.",
    },
    {
        "title": "Virtual Power Plant demonstrations",
        "url": "https://www.aemo.com.au/initiatives/major-programs/nem-distributed-energy-resources-der-program/der-demonstrations/virtual-power-plant-vpp-demonstrations",
        "publisher": "AEMO",
        "use": "Defines virtual power plants as coordinated solar, storage and controllable loads that can provide value to customers and the energy system.",
    },
    {
        "title": "Virtual Power Plant regulatory use case",
        "url": "https://energyinnovationtoolkit.gov.au/regulatory-use-case-aggregation-distributed-energy-resources-through-virtual-power-plant",
        "publisher": "AER Energy Innovation Toolkit",
        "use": "Keeps VPP, community battery and network support revenue language tied to consumer obligations, telemetry, distributor agreements and uncertainty.",
    },
    {
        "title": "Queensland's Electric Vehicle Super Highway",
        "url": "https://www.tmr.qld.gov.au/community-and-environment/electric-vehicles/queenslands-electric-super-highway",
        "publisher": "Queensland Department of Transport and Main Roads",
        "use": "Connects island EV-charging questions to Queensland's public fast-charging network and transport planning context.",
    },
    {
        "title": "Powerledger",
        "url": "https://powerledger.io/",
        "publisher": "Powerledger",
        "use": "Provides an industry reference for blockchain-based tracking, tracing and trading of renewable energy.",
    },
    {
        "title": "Everything you want to know about peer-to-peer energy trading",
        "url": "https://powerledger.io/media/everything-you-want-to-know-about-peer-to-peer-energy-trading/",
        "publisher": "Powerledger",
        "use": "Supplies a non-government example of peer-to-peer energy trading claims, useful only as a prompt for questions about retailer, utility, price and consumer-law design.",
    },
    {
        "title": "Concentrated solar thermal",
        "url": "https://arena.gov.au/renewable-energy/concentrated-solar-thermal/",
        "publisher": "ARENA",
        "use": "Supports solar heat and thermal storage as a serious option, while keeping scale and cost questions visible.",
    },
    {
        "title": "Advanced solar thermal energy storage technologies",
        "url": "https://arena.gov.au/projects/advanced-solar-thermal-energy-storage-technologies/",
        "publisher": "ARENA / CSIRO",
        "use": "Shows that high-temperature solar thermal storage has an Australian research and demonstration trail.",
    },
    {
        "title": "Thermal Energy Storage Technology Strategy Assessment",
        "url": "https://www.energy.gov/sites/default/files/2023-07/Technology%20Strategy%20Assessment%20-%20Thermal%20Energy%20Storage_0.pdf",
        "publisher": "U.S. Department of Energy",
        "use": "Supports sand, rock and other earth-based heat storage as a research-backed long-duration storage lane.",
    },
    {
        "title": "Sand Battery",
        "url": "https://polarnightenergy.com/sand-battery/",
        "publisher": "Polar Night Energy",
        "use": "Provides a plain commercial reference for sand batteries as thermal storage, not magic electric batteries.",
    },
    {
        "title": "Australia's National Hydrogen Strategy 2024",
        "url": "https://www.dcceew.gov.au/energy/publications/australias-national-hydrogen-strategy",
        "publisher": "Australian Government DCCEEW",
        "use": "Sets the national green-hydrogen context: production, use, export, community benefit and infrastructure questions.",
    },
    {
        "title": "Hydrogen",
        "url": "https://www.csiro.au/en/research/environmental-impacts/fuels/hydrogen",
        "publisher": "CSIRO",
        "use": "Provides a plain science reference for hydrogen production, storage, transport, use and Australia's hydrogen opportunity.",
    },
    {
        "title": "Renewable hydrogen",
        "url": "https://arena.gov.au/renewable-energy/hydrogen/",
        "publisher": "ARENA",
        "use": "Grounds hydrogen as renewable electricity plus water electrolysis, while keeping cost, scale and end-use questions visible.",
    },
    {
        "title": "Beneficial reuse and disposal options for brine in Queensland",
        "url": "https://gisera.csiro.au/beneficial-reuse-and-disposal-options-for-brine-in-queensland/",
        "publisher": "CSIRO GISERA",
        "use": "Opens desalination brine as a resource-recovery and reuse question rather than a waste afterthought.",
    },
    {
        "title": "Mining valuable minerals from seawater: a critical review",
        "url": "https://pubs.rsc.org/en/content/articlelanding/2017/ew/c6ew00268d",
        "publisher": "Environmental Science: Water Research & Technology / RSC",
        "use": "Adds a research trail for seawater and brine mineral recovery, including lithium, magnesium and other dissolved resources.",
    },
    {
        "title": "South East Queensland Report Card",
        "url": "https://reportcard.hlw.org.au/",
        "publisher": "Healthy Land & Water",
        "use": "Gives the Moreton Bay water-quality context for asking what clean-energy wealth, sensors and brine research could help repair.",
    },
    {
        "title": "South East Queensland report card - Purpose",
        "url": "https://wetlandinfo.des.qld.gov.au/wetlands/facts-maps/report-card-organisation-healthy-land-and-water/",
        "publisher": "Queensland WetlandInfo",
        "use": "Frames the official report-card purpose: tracking waterway health, pollutant loads, ecosystem condition and progress over time.",
    },
    {
        "title": "Broken Hill Advanced Compressed Air Energy Storage Demonstration",
        "url": "https://arena.gov.au/projects/hydrostor-broken-hill-advanced-compressed-air-energy-storage-demonstration/",
        "publisher": "ARENA",
        "use": "Shows compressed air as a serious long-duration storage pathway when geology, pressure behaviour and economics line up.",
    },
    {
        "title": "Technical feasibility of CAES in an aquifer storage vessel",
        "url": "https://www.sandia.gov/files/ess/EESAT/2009_papers/Technical%20Feasibility%20of%20Compressed-Air%20Energy%20Storage%20in%20an%20Aquifer%20Storage%20Vessel.pdf",
        "publisher": "Sandia / Lawrence Berkeley National Laboratory authors",
        "use": "Opens the aquifer compressed-air question as a hydrology, geology, pressure and modelling topic rather than a casual slogan.",
    },
    {
        "title": "Pumped Hydro Energy Storage",
        "url": "https://arena.gov.au/renewable-energy/pumped-hydro-energy-storage/",
        "publisher": "ARENA",
        "use": "Explains pumped hydro as a serious long-duration storage family based on moving water between higher and lower reservoirs.",
    },
    {
        "title": "Snowy 2.0",
        "url": "https://www.snowyhydro.com.au/snowy-20/about/",
        "publisher": "Snowy Hydro",
        "use": "Reference system for large pumped-hydro storage: upper and lower reservoirs, tunnels, reversible generation and long-duration grid support.",
    },
    {
        "title": "Wivenhoe Pumped Storage Hydro Power Station",
        "url": "https://cleancoqueensland.com.au/portfolio/owned-and-operated/wivenhoe-pumped-storage-hydro-power-station/",
        "publisher": "CleanCo Queensland",
        "use": "Queensland pumped-hydro reference: water is lifted from Wivenhoe Dam to Splityard Creek Dam, then released for peak support.",
    },
    {
        "title": "250MW Kidston Pumped Storage Hydro Project",
        "url": "https://genexpower.com.au/250mw-kidston-pumped-storage-hydro-project/",
        "publisher": "Genex Power",
        "use": "Queensland reference for pairing pumped storage with renewable generation and long-duration evening supply.",
    },
    {
        "title": "Borumba Pumped Hydro Project",
        "url": "https://qldhydro.com.au/projects/borumba/",
        "publisher": "Queensland Hydro",
        "use": "Queensland reference for proposed long-duration pumped hydro and the scale of planning behind new water-height storage.",
    },
    {
        "title": "Global Greenfield Pumped Hydro Energy Storage Atlas",
        "url": "https://re100.eng.anu.edu.au/global/",
        "publisher": "ANU RE100 Group",
        "use": "Shows how pumped-hydro thinking can begin as open topographic screening before local informal ideas choose their own shape.",
    },
    {
        "title": "Coastal and subcoastal non-floodplain sand lake - Perched hydrology",
        "url": "https://wetlandinfo.detsi.qld.gov.au/wetlands/ecology/aquatic-ecosystems-natural/lacustrine/non-floodplain-perched-lake/hydrology.html",
        "publisher": "Queensland WetlandInfo",
        "use": "Grounds Straddie-style water thinking in sandmass hydrology: rapid infiltration, little overland run-off, local groundwater systems and perched lakes.",
    },
    {
        "title": "Saving Straddie's Sand",
        "url": "https://science.nasa.gov/earth/earth-observatory/saving-straddies-sand-146669/",
        "publisher": "NASA Earth Observatory",
        "use": "Adds a remote-sensing source for Straddie's sandmass, mineral-sands history and landform questions.",
    },
    {
        "title": "Vortex Bladeless",
        "url": "https://vortexbladeless.com/",
        "publisher": "Vortex Bladeless",
        "use": "Opens vortex-induced oscillation as one no-blade wind family for local energy-harvesting imagination.",
    },
    {
        "title": "The motionless wind energy system",
        "url": "https://aerominetechnologies.com/",
        "publisher": "Aeromine Technologies",
        "use": "Shows rooftop edge-flow wind harvesting as a real commercial research and product pathway.",
    },
    {
        "title": "EWICON",
        "url": "https://www.mecanoo.nl/projects/project/61/ewicon",
        "publisher": "Mecanoo / Delft project",
        "use": "Adds electrostatic wind conversion without moving mechanical parts to the no-blade wind source trail.",
    },
    {
        "title": "Low Wind Energy",
        "url": "https://smartshelterfoundation.org/collection/low-wind-energy",
        "publisher": "Smart Shelter Foundation",
        "use": "Provides a plain Windbelt-style doorway into low-velocity ribbon and flutter harvesting.",
    },
    {
        "title": "Vortex-induced vibration wind energy harvesting by piezoelectric MEMS device in formation",
        "url": "https://www.nature.com/articles/s41598-019-56786-0",
        "publisher": "Scientific Reports",
        "use": "Supports formation-scale micro-harvesters and the idea that many small wind motions can be studied together.",
    },
    {
        "title": "Recent progress on flutter-based wind energy harvesting",
        "url": "https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12035",
        "publisher": "Wiley",
        "use": "Supports flutter-based wind harvesting as a research family for microelectronics and small devices.",
    },
    {
        "title": "Structural design strategies of triboelectric nanogenerators for wind energy harvesting",
        "url": "https://link.springer.com/article/10.1186/s40486-025-00224-6",
        "publisher": "Springer",
        "use": "Adds wind-driven fluttering triboelectric films to the fractal wind-harvesting source trail.",
    },
    {
        "title": "Harvesting ambient wind energy with an inverted piezoelectric flag",
        "url": "https://pure.johnshopkins.edu/en/publications/harvesting-ambient-wind-energy-with-an-inverted-piezoelectric-fla",
        "publisher": "Johns Hopkins / Applied Physics Letters",
        "use": "Shows how flag geometry and aeroelastic flutter can turn low-speed wind into small electric output.",
    },
    {
        "title": "Ocean energy",
        "url": "https://arena.gov.au/renewable-energy/ocean/",
        "publisher": "ARENA",
        "use": "Grounds wave and tidal energy as a broad family of technologies, not one settled device type.",
    },
    {
        "title": "Marine Energy Basics",
        "url": "https://www.energy.gov/cmei/water/marine-energy-basics",
        "publisher": "U.S. Department of Energy",
        "use": "Keeps marine-energy language broad: waves, tides, currents, temperature gradients and many conversion pathways.",
    },
    {
        "title": "Australian Wave Energy Atlas",
        "url": "https://arena.gov.au/projects/australian-wave-energy-atlas/",
        "publisher": "ARENA / CSIRO",
        "use": "Supports wave-resource mapping as one doorway into the many unmapped wave and tide possibilities.",
    },
    {
        "title": "Review of wave energy converter power take-off systems",
        "url": "https://www.nrel.gov/docs/fy23osti/82807.pdf",
        "publisher": "NREL",
        "use": "Adds a research trail for non-standard wave power take-off concepts, including non-air-turbine pathways.",
    },
    {
        "title": "Vortex Hydro Energy develops transformational technology",
        "url": "https://www.energy.gov/cmei/success-stories/articles/eere-success-story-vortex-hydro-energy-develops-transformational",
        "publisher": "U.S. Department of Energy",
        "use": "Reference for vortex-induced vibration as a no-blade current-energy pathway inspired by how fish interact with vortices.",
    },
    {
        "title": "Energy harvesting by flow-induced flutter in an inverted piezoelectric flag",
        "url": "https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/energy-harvesting-by-flowinduced-flutter-in-a-simple-model-of-an-inverted-piezoelectric-flag/37FF699E5B55E238A41F056E4A06DBDB",
        "publisher": "Journal of Fluid Mechanics",
        "use": "Supports flutter and flexible-geometry energy harvesting as a real first-principles research lane.",
    },
    {
        "title": "Analysis of biomimetic stream energy device based on flapping foils",
        "url": "https://tethys-engineering.pnnl.gov/publications/analysis-biomimetic-stream-energy-device-based-flapping-foils",
        "publisher": "Tethys Engineering / PNNL",
        "use": "Reference for biomimetic oscillating foils as a hydrokinetic design family beyond standard turbines.",
    },
    {
        "title": "Shrimp metachronal swimming",
        "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10303694/",
        "publisher": "National Library of Medicine / open-access article",
        "use": "Opens shrimp-style appendage timing and cascading motion as geometry clues, not finished energy claims.",
    },
    {
        "title": "Mechanics of Movement: Mantis Shrimp",
        "url": "https://pateklab.biology.duke.edu/research/mechanics-of-ultrafast-movement/mechanics-of-movement-mantis-shrimp/",
        "publisher": "Patek Lab, Duke University",
        "use": "Gives a public biology reference for peacock mantis shrimp mouthparts reaching about 12-23 m/s in water, fast enough to form cavitation bubbles during a strike.",
    },
    {
        "title": "Prufrock",
        "url": "https://www.boringcompany.com/prufrock",
        "publisher": "The Boring Company",
        "use": "Provides the high-throughput tunnel reference point: Prufrock targets more than 1 mile of tunnel per week.",
    },
    {
        "title": "Music City Loop",
        "url": "https://www.boringcompany.com/music-city-loop",
        "publisher": "The Boring Company",
        "use": "Provides the Loop-scale diameter reference: each tunnel is described as having a 12-foot internal diameter.",
    },
    {
        "title": "Seawalls and artificial reefs",
        "url": "https://www.goldcoast.qld.gov.au/Environment-sustainability/Protecting-our-environment/Managing-our-beaches/Seawalls-artificial-reefs",
        "publisher": "City of Gold Coast",
        "use": "Australian coastal reference for Narrowneck and Palm Beach artificial reefs as erosion, beach and surf-amenity structures.",
    },
    {
        "title": "Tweed River Entrance Sand Bypassing Project",
        "url": "https://www.qld.gov.au/environment/coasts-waterways/beach/tweed-river",
        "publisher": "Queensland Government",
        "use": "Grounds the Snapper Rocks and southern Gold Coast sand-bank conversation in an operating sand bypass system.",
    },
    {
        "title": "Artificial reefs",
        "url": "https://www.qld.gov.au/environment/coasts-waterways/marine-parks/artificial-reefs",
        "publisher": "Queensland Government",
        "use": "Provides a Queensland public-source doorway for artificial reef types, locations and marine park context.",
    },
    {
        "title": "Moreton Bay trial artificial reef program",
        "url": "https://www.qld.gov.au/environment/coasts-waterways/marine-parks/artificial-reefs",
        "publisher": "Queensland Parks",
        "use": "Shows artificial reef sites already operating in Moreton Bay Marine Park for habitat and recreational fishing value.",
    },
    {
        "title": "Restoring Australia's lost shellfish reefs",
        "url": "https://www.nature.org/en-us/about-us/where-we-work/asia-pacific/australia/stories-in-australia/restoring-australias-lost-shellfish-reefs/",
        "publisher": "The Nature Conservancy",
        "use": "Frames shellfish reef restoration as a national habitat, water-quality, fish and coastal community pathway.",
    },
    {
        "title": "Windara Reef reviving the Gulf",
        "url": "https://www.natureaustralia.org.au/what-we-do/our-priorities/oceans/ocean-stories/restoring-shellfish-reefs/gulf-st-vincent/",
        "publisher": "The Nature Conservancy Australia",
        "use": "Australian oyster reef reference for restored shellfish reef benefits, including fish, water quality and biodiversity.",
    },
    {
        "title": "Moreton Bay Shellfish Reef Restoration",
        "url": "https://ozfish.org.au/projects/moreton-bay-shellfish-reef-restoration/",
        "publisher": "OzFish Unlimited",
        "use": "Connects Moreton Bay shellfish reef restoration to recycled shells, community work and bay habitat recovery.",
    },
    {
        "title": "Living Shorelines",
        "url": "https://www.oceanwatch.org.au/community/livingshorelines/",
        "publisher": "OceanWatch Australia",
        "use": "Australian living-shoreline reference for oyster shells, erosion control and habitat repair.",
    },
    {
        "title": "Raine Island Recovery Project",
        "url": "https://www.qld.gov.au/environment/plants-animals/conservation/raineisland-recovery",
        "publisher": "Queensland Parks",
        "use": "Australian island-shaping reference for beach re-profiling, turtle habitat and careful monitoring over time.",
    },
    {
        "title": "Future Port Expansion",
        "url": "https://www.portbris.com.au/major-projects/fpe",
        "publisher": "Port of Brisbane",
        "use": "Queensland reclamation reference for large-scale material placement, sea walls, staged ground improvement and monitoring.",
    },
    {
        "title": "Sand and Materials",
        "url": "https://auraofintelligence.github.io/straddie-makerspace-lab/sand.html",
        "publisher": "Straddie Maker-Space Lab",
        "use": "Connects sand, glass, ceramics, mineral literacy and resident-use home products to the material-flow question.",
    },
    {
        "title": "Concrete and Geopolymers",
        "url": "https://auraofintelligence.github.io/straddie-makerspace-lab/concrete.html",
        "publisher": "Straddie Maker-Space Lab",
        "use": "Connects blocks, pavers, tiles, reusable bases, geopolymers and visible recipe-led material testing to the surface design pathway.",
    },
    {
        "title": "10-12 Ballow Road Site",
        "url": "https://auraofintelligence.github.io/ballow-road-sand-screen-hub/site.html",
        "publisher": "Ballow Road Sand and Screen Hub",
        "use": "Links adaptive surface blocks, sand sport, screens, shade, seating and service plinths to the 10-12 Ballow Road public concept site.",
    },
    {
        "title": "Community concept images and design visualisations",
        "url": "https://auraofintelligence.github.io/dunwich-gumpi-ferry-terminal-open-data-lab/community-genai-examples.html",
        "publisher": "Dunwich / Gumpi Ferry Terminal Open Data Lab",
        "use": "Connects climate-ready surface blocks to ferry-terminal visualisation, arrival paths, seating, lighting, service edges and public design discussion.",
    },
    {
        "title": "Carbon capture and storage",
        "url": "https://www.ga.gov.au/aecr2024/carbon-capture-and-storage",
        "publisher": "Geoscience Australia",
        "use": "Frames carbon capture as capture, transport, compression and storage, not a casual add-on to local air tanks.",
    },
    {
        "title": "Carbon dioxide as a fire suppressant: examining the risks",
        "url": "https://www.epa.gov/snap/carbon-dioxide-fire-suppressant-examining-risks",
        "publisher": "US EPA",
        "use": "Adds an authority source for CO2 fire-suppression questions, especially where people may occupy the space.",
    },
    {
        "title": "Naree Budjong Djara National Park",
        "url": "https://parks.qld.gov.au/parks/naree-budjong-djara",
        "publisher": "Queensland Parks",
        "use": "Keeps protected-area, lake, wetland and Country boundaries visible before infrastructure imagination runs ahead.",
    },
    {
        "title": "Quandamooka Yoolooburrabee Aboriginal Corporation",
        "url": "https://qyac.net.au/",
        "publisher": "QYAC",
        "use": "Names the public organisational doorway for Quandamooka land and sea management rather than implying authority.",
    },
]


LOCAL_DRAFT_INPUTS = [
    {
        "title": "Straddie Sovereign Wealth Fund And Civilisation Of Sand Research Brief",
        "file": "Straddie_Sovereign_Wealth_Fund_&_Civilisation_of_Sand_Research_Brief.md",
        "use": "Working concept fuel only. Adds wave and tidal options, solar resource framing, sand batteries, vanadium flow batteries, salt-gradient questions, oyster-crete reefs, sovereign wealth fund architecture, token questions and a source-trail habit.",
    }
]


STYLE_RESEARCH = [
    {
        "repo": "straddie-makerspace-lab",
        "learning": "Use plain questions, practical workshop language, 8px radii, Atkinson Hyperlegible and Nunito Sans, sequence nav, source notes and public pages before repo links.",
    },
    {
        "repo": "Sandworm-subterranean-systems",
        "learning": "Use a generated static site, source-aware builders, page-specific hero images, dropdown nav groups, site map and careful boundary language for speculative infrastructure.",
    },
    {
        "repo": "dunwich-gumpi-ferry-terminal-open-data-lab",
        "learning": "Make the ferry terminal a live civic lab: official trail, open data, public photos, simulation workflow and evidence before claims.",
    },
    {
        "repo": "stradbroke-grants-lab",
        "learning": "Connect project ideas to grant windows, profiles, checklists, milestones and reporting, not just inspiration.",
    },
    {
        "repo": "moreton-bay-community-wealth-and-mutuals",
        "learning": "Frame wealth and risk as local stewardship questions: who holds value, who carries risk and how do receipts stay inspectable?",
    },
    {
        "repo": "ready-set-co-op-trust-hub",
        "learning": "Keep trust, training, media and voluntary pathways clear. Avoid treating people as labour inventory.",
    },
]


BUILDERS = [
    {
        "id": "entry-trail",
        "title": "Energy Entry Trail Builder",
        "purpose": "Choose a clean-energy doorway without needing to accept the whole atlas.",
        "filename": "straddie-energy-entry-trail",
        "boundary": "The note is an invitation, not an approval claim. People can use one part, reject another, or ask for better evidence.",
        "next_step": "Name one small thing that could make the option easier to test, explain or dismiss.",
        "fields": [
            ("doorway", "Which doorway feels alive?", "Rooftop solar, sand battery, compressed air, wave pressure, no-blade wind, pumped hydro model, grants, wealth, or another doorway."),
            ("question", "What is the plain question?", "Write it as a real question, not a conclusion."),
            ("useful_output", "What could be useful to leave with?", "A map, source list, cost question, source review, workshop test, grant note or public explainer."),
        ],
    },
    {
        "id": "solar-rooftop-note",
        "title": "Rooftop Solar And Shade Note Builder",
        "purpose": "Turn a roof, car park, shade structure or public building into a first clean-energy question.",
        "filename": "straddie-rooftop-solar-note",
        "boundary": "A solar note is stronger when owner consent, electrical review, cyclone/wind loading, heritage and visual checks, fire access and network rules are visible.",
        "next_step": "Check the roof or site, the owner pathway, the load profile and the public data trail before promising savings.",
        "fields": [
            ("site", "Which site or roof is being imagined?", "Home, business, school, club, ferry gateway, car park shade, community hall or concept only."),
            ("load", "What load could it help?", "Household bills, EV charging, kiosk, fridge, workshop, lighting, water pumping, battery charging or emergency backup."),
            ("storage", "Does storage matter here?", "Home battery, community battery, sand heat store, hot water, EV battery, no storage, or not sure."),
            ("checks", "What could be useful to check first?", "Owner, electrician, roof, fire access, insurance, network export, grant path, shading, public benefit or maintenance."),
        ],
    },
    {
        "id": "sand-air-storage",
        "title": "Storage, Hydrogen And Water-Loop Builder",
        "purpose": "Explore sand, heat, pressure-air, green-hydrogen, desal and brine-mineral loops as open questions for island abundance.",
        "filename": "straddie-sand-air-storage-brief",
        "boundary": "Thermal sand storage, compressed air, hydrogen, desalination, brine minerals, CO2, pressure vessels and response systems can share a conversation while each keeps its own source trail and learning path.",
        "next_step": "Choose one storage question and one hands-on learning step before connecting it to a bigger network.",
        "fields": [
            ("need", "What energy problem is being solved?", "Evening power, heat, workshop process heat, emergency backup, ferry gateway load, water pumping, or seasonal resilience."),
            ("medium", "Which storage or water medium is in play?", "Hot sand, rock, hot water, compressed air vessel, hydrogen, desal loop, brine minerals, aquifer question, battery, or hybrid."),
            ("place", "Where could the first learning step live?", "Maker-space yard, service zone, ferry lab, bay sensor node, existing industrial site, digital model, or not known."),
            ("review", "Which lenses could help?", "Pressure behaviour, water source, brine recovery, response systems, electrical, geology, heat insulation, public access, noise, access paths or economics."),
        ],
    },
    {
        "id": "marine-no-turbine",
        "title": "No-Underwater-Blades Marine Brief Builder",
        "purpose": "Shape a wave or tidal curiosity note from first principles: flutter, vortex, shrimp timing, mantis-shrimp strikes, foils, membranes, reefs, sensors, play and local observation.",
        "filename": "straddie-no-turbine-marine-brief",
        "boundary": "No underwater blades is not a lack of imagination. It opens the field to forms, rhythms, materials and processes that humans have barely mapped.",
        "next_step": "Start with sketches, kids' ideas, maker-space rigs, wave tanks, beach observations, digital simulation and source links before choosing any one device family.",
        "fields": [
            ("edge", "Which coast or water edge is being considered?", "Main Beach, Moreton Bay, ferry channel, Amity edge, reef model, wave tank, or concept only."),
            ("pattern", "Which pattern or movement could inspire it?", "Shrimp appendage timing, mantis-shrimp latch-spring strikes, vortex shedding, oscillating foil, flexible flag, reef lattice, membrane pulse, buoyant hinge, kelp sway, shell geometry or a kid's sketch."),
            ("benefit", "What benefit could be tested?", "Power, sensor trickle-charge, monitoring, reef learning, erosion knowledge, emergency signal, food/habitat co-benefit or public education."),
            ("open_question", "What remains unmapped?", "Geometry, timing, material, scale, anchoring, reversibility, maintenance, community value, learning value or the next experiment."),
        ],
    },
    {
        "id": "perched-lake-boundary",
        "title": "Water-Height Geography Builder",
        "purpose": "Turn water-height curiosity into a local geography note grounded in ocean, bay, sand hills, perched lakes, aquifers, sands and mineral sands.",
        "filename": "straddie-water-height-geography",
        "boundary": "A perched lake can be a teacher without being the battery. Let the first draft map ocean, bay, sand hills, aquifers, wetlands, sands, mineral sands and cultural places.",
        "next_step": "Use a map, digital twin, tank pair, seawater-height model or sandhill elevation model to let real water bodies appear as teachers rather than assumed infrastructure.",
        "fields": [
            ("question", "What is the water-height question?", "Sandhill height, bay/ocean edge, tank pair, seawater reservoir, aquifer model, sandmass model, model only, or educational demo."),
            ("sensitive_place", "What sensitive place could people protect first?", "Perched lake, wetland, spring, national park, cultural place, habitat, aquifer, public access or unknown layer."),
            ("alternative", "What local geography could teach the idea?", "Ocean, bay, sand hill, dune ridge, mineral sands layer, tank pair, sandmass model, aquifer data, virtual model, or no build."),
            ("authority", "Who could be invited in before this becomes real?", "Traditional Owners, park managers, hydrologist, ecologist, council, engineer, emergency services or landholder."),
        ],
    },
    {
        "id": "power-sharing-ledger",
        "title": "Power Sharing And Bill Ledger Builder",
        "purpose": "Turn a local sharing idea into a plain-English bill, battery and governance question.",
        "filename": "straddie-power-sharing-ledger",
        "boundary": "A ledger, token or crypto layer can earn trust by sitting beside clear retail, network, legal, tax, cyber, consent and plain-accounting questions.",
        "next_step": "Start with one load, one storage node, one bill problem and one plain receipt trail alongside any token design.",
        "fields": [
            ("participants", "Who is sharing value?", "Households, renters, shops, club, ferry gateway, maker-space, EV charger, community battery, trust, co-op or concept only."),
            ("surplus", "What surplus or flexible load exists?", "Midday rooftop solar, hot water, cold storage, sand heat, EV charging, e-bike charging, workshop heat, pumps or batteries."),
            ("settlement", "How could value be settled plainly?", "Bill credit, co-op account, mutual reserve, voucher, local ledger, retailer offer, VPP payment, token question or not known."),
            ("review", "What could make money movement trustworthy?", "Retail licence, embedded network rules, network tariff, consumer law, tax, privacy, cyber security, anti-fraud, opt-out, fair-go help path or governance."),
        ],
    },
    {
        "id": "wealth-grant-readiness",
        "title": "Wealth And Grant Readiness Builder",
        "purpose": "Turn an energy option into a local-benefit note that Grants Lab and mutual-care thinking can inspect.",
        "filename": "straddie-energy-wealth-grant-note",
        "boundary": "A community wealth note is not a financial product. Law, governance, consent, anti-fraud checks and human review are part of making the idea inspectable.",
        "next_step": "Separate savings, revenue, risk, ownership, reporting evidence and who can say no.",
        "fields": [
            ("option", "Which energy option is being costed?", "Solar, battery, sand heat, compressed air, marine, wind sensor, demand response, training, or another option."),
            ("benefit", "Who benefits and how?", "Lower bills, local jobs, emergency resilience, training, co-op income, public data, mutual care or shared assets."),
            ("evidence", "What evidence could help a grant?", "Photos, quotes, energy data, letters, risk review, site consent, budgets, milestones or reporting plan."),
            ("governance", "How could value stay local?", "Trust, co-op, community fund, public dashboard, local contracts, training path, mutual reserve or not known."),
        ],
    },
    {
        "id": "boundary-check",
        "title": "Energy Boundary Check Builder",
        "purpose": "Name the consent, evidence and learning questions before an exciting energy idea gathers momentum.",
        "filename": "straddie-energy-boundary-check",
        "boundary": "A clean-energy idea can become clearer when people name what they are curious about, what they are protecting, and what evidence could change their mind.",
        "next_step": "Name the next person to invite in and the evidence that would make the next step wiser.",
        "fields": [
            ("idea", "Which idea is ready for a boundary check?", "Name the option or project."),
            ("people", "Whose consent or authority matters?", "Traditional Owners, residents, landholder, council, business owner, emergency services, marine users, children or workers."),
            ("risk", "What could go wrong?", "Fire, pressure, heat, water, wildlife, culture, data, cost, noise, visual impact, maintenance, false claims or exclusion."),
            ("next_question", "What could change the next step?", "New evidence, no consent, better local knowledge, ecological concern, weak economics, unclear ownership or community refusal."),
        ],
    },
]


def e(value: object) -> str:
    return escape(str(value), quote=True)


def by_id(page_id: str) -> dict:
    return next(page for page in PAGES if page["id"] == page_id)


def hero_image(page_id: str) -> str:
    return HERO_IMAGES.get(page_id, HERO_IMAGES["home"])


def page_hero(page: dict) -> str:
    return (
        '<section class="page-hero"><div class="page-hero-inner">'
        f'<h1>{e(page["title"])}</h1><p class="lede">{e(page["description"])}</p>'
        '</div></section>'
    )


def card_grid(cards: list[dict], klass: str = "card-grid") -> str:
    items = []
    for card in cards:
        tag = "a" if card.get("href") else "article"
        href = f' href="{e(card["href"])}"' if card.get("href") else ""
        action = f'<span class="text-link">{e(card.get("action", "Open"))}</span>' if card.get("href") else ""
        items.append(
            f'<{tag} class="card"{href}><p class="mini-label">{e(card.get("label", "Question"))}</p>'
            f'<h3>{e(card["title"])}</h3><p>{e(card["text"])}</p>{action}</{tag}>'
        )
    return f'<div class="{klass}">' + "".join(items) + "</div>"


def option_grid(cards: list[dict]) -> str:
    items = []
    for card in cards:
        items.append(
            '<article class="option-card">'
            f'<p class="mini-label">{e(card["status"])}</p><h3>{e(card["title"])}</h3>'
            f'<p>{e(card["plain"])}</p>'
            f'<p><strong>First question:</strong> {e(card["question"])}</p>'
            f'<p><strong>Useful lenses:</strong> {e(card["review"])}</p>'
            '</article>'
        )
    return '<div class="option-grid">' + "".join(items) + "</div>"


def repo_grid() -> str:
    cards = []
    for link in COMPANION_LINKS:
        cards.append(
            '<article class="repo-card">'
            f'<p class="mini-label">Source bridge</p><h3>{e(link["title"])}</h3>'
            f'<p>{e(link["summary"])}</p>'
            f'<p><a class="text-link" href="{e(link["site"])}">Live site</a> '
            f'<a class="text-link" href="{e(link["repo"])}">Source repo</a></p>'
            '</article>'
        )
    return '<div class="repo-grid">' + "".join(cards) + "</div>"


def home_body() -> str:
    return """
<section class="hero">
  <div class="hero-body">
    <div class="hero-copy">
      <p class="section-label hero-label">Self-sovereign clean energy atlas</p>
      <h1>Could Straddie become a clean energy superpower?</h1>
      <p class="hero-lede">What if the island did not start with one giant answer, but with a stack of questions people can inspect: roofs first, storage next, marine edges carefully, local wealth clearly, and every bold idea growing through consent, evidence and local authority?</p>
      <div class="hero-actions">
        <a class="button primary" href="options.html">Explore the options</a>
        <a class="button secondary" href="network.html">See the local labs</a>
      </div>
      <p class="micro-note">Questions before claims. Practical tests before scale. People keep the steering wheel.</p>
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">The core move</p>
      <h2>Start with useful energy, not energy theatre.</h2>
      <p class="lede muted">A clean-energy superpower can mean more than a giant industrial build. It could mean roofs that work harder, public buildings that store heat, emergency nodes that stay alive, grants that fund real tests, and local people who can understand the system.</p>
    </div>
""" + card_grid([
        {"label": "Near term", "title": "How much rooftop solar is still untapped?", "text": "Could homes, shops, clubs, halls and shaded car parks become the first power station?"},
        {"label": "Storage", "title": "Can sand hold the evening?", "text": "Could solar heat or spare electricity charge sand, rock or hot-water stores for workshop heat, drying, cooking, water and community backup?"},
        {"label": "Hydrogen", "title": "Could water become a clean-energy loop?", "text": "Could solar, desal, electrolysis, oxygen, heat and brine minerals help the island ask better questions about fuel, water and Moreton Bay repair?"},
        {"label": "Sharing", "title": "Can spare solar be worth more before it leaves?", "text": "Could neighbourhood batteries, EV charging, hot water, cold rooms and plain bill credits beat a weak feed-in tariff without trapping anyone?"},
        {"label": "Pressure", "title": "What can compressed air teach on a sand island?", "text": "Could air storage start with containers, pipes, compressors, heat recovery and aquifer models that map to Straddie's sandmass rather than generic mainland infrastructure?"},
        {"label": "Water", "title": "What can Snowy-scale thinking teach a sand island?", "text": "Could Snowy, Wivenhoe, Kidston, Borumba and pumped-hydro atlases help people ask better Straddie questions about ocean, bay, dune height, perched lakes, aquifers, sands and mineral sands?"},
        {"label": "Marine", "title": "How many wave and tide geometries are still unmapped?", "text": "Could flutter, vortex shedding, shrimp timing, mantis-shrimp strike physics, oscillating foils, membranes, reef lattices, sensors and kids' sketches open more than one marine-energy path?"},
        {"label": "Reefs", "title": "Could sand flows become reef, surf and habitat capability?", "text": "Could Sandworm tunnel volumes, oyster reefs, living shorelines, surf banks, stable dunes and artificial-island questions share one public material ledger?"},
        {"label": "Wealth", "title": "Who owns the upside?", "text": "Could savings, income, training and resilience feed local stewardship instead of leaking away?"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Why a repo?</p>
      <h2>Because the public map can be inspectable.</h2>
      <p class="lede muted">This site is not an energy plan, engineering design or endorsement claim. It is a public workbench for turning big clean-energy imagination into clear questions, source trails, builder forms and next-small-step notes.</p>
      <ol class="pathway">
        <li><p><strong>Ask the plain question.</strong> What problem does this option solve for residents, Country, business, ferry flow, emergency resilience or community wealth?</p></li>
        <li><p><strong>Find the smallest harmless test.</strong> Could a tabletop model, data check, roof audit, workshop bench or digital twin answer the first doubt?</p></li>
        <li><p><strong>Name the open checks.</strong> Who could help inspect culture, ecology, pressure, response systems, water, finance, data and public claims before momentum builds?</p></li>
      </ol>
    </div>
    <div class="quote-panel">If the idea is strong, it can handle plain English, public sources and people saying no.</div>
  </div>
</section>
<section class="section deep-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Linked ecosystem</p>
      <h2>The energy atlas plugs into existing local workbenches.</h2>
      <p class="lede">Maker-space, Sandworm, ferry terminal lab, grants lab, community wealth and Ready S.E.T. Trust Hub already hold the right shape: practical tests, public sources, builders, trust and local benefit.</p>
    </div>
""" + repo_grid() + """
  </div>
</section>
"""


def options_body() -> str:
    return page_hero(by_id("options")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Option stack</p>
      <h2>Which ideas are ready for the front room, and which need the lab?</h2>
      <p class="lede muted">The point is to let each idea show its shape: what it teaches, which part of Straddie's geography it speaks with, what sources can be followed, and how local people could keep improving the question.</p>
    </div>
""" + option_grid([
        {"status": "Start now", "title": "Rooftop solar and batteries", "plain": "The most practical first layer: roofs, shade, small businesses, public buildings, hot water and batteries.", "question": "Which roofs and loads are obvious wins once the owner, electrician and network rules are checked?", "review": "Electrical, fire, roof, cyclone/wind loading, insurance and network export."},
        {"status": "Start small", "title": "Solar thermal and concentration", "plain": "Heat can be easier to store than electricity. Solar concentration might suit a workshop, kitchen, repair yard, hot-water load or sand-heat experiment.", "question": "Where does the island need clean heat, not just clean electrons?", "review": "Heat use, glare, fire access, land use, maintenance and economics."},
        {"status": "Prototype", "title": "Sand batteries", "plain": "A sand battery is thermal storage: heat goes into sand or similar material and comes out as heat, steam, air or sometimes power through another system.", "question": "Could a maker-space bench test show what local heat storage is good for?", "review": "Insulation, hot surfaces, materials, fire, monitoring, output use and public access."},
        {"status": "Water-energy loop", "title": "Green hydrogen, desal and brine mining", "plain": "Green hydrogen asks for clean electricity and water. Straddie can ask it as a transparent loop: desal, electrolysis, oxygen, heat, brine minerals, ferry fuel questions, bay sensors and Moreton Bay repair economics.", "question": "Could a tiny public water-loop lab show what hydrogen, desal and brine recovery teach before a larger pathway takes shape?", "review": "Water source, desal energy, brine concentration, mineral recovery, oxygen use, heat, storage, ferry demand, bay health and economics."},
        {"status": "Sharing layer", "title": "Neighbourhood batteries and power sharing", "plain": "Local solar may be worth more when it is used, stored or shared locally before it is exported at a low feed-in tariff.", "question": "Could a community battery, EV charger or bill-credit ledger keep midday solar value close to residents?", "review": "Retailer, network tariff, metering, consent, privacy, fair-go help paths, tax, consumer law and governance."},
        {"status": "Research lane", "title": "Compressed air", "plain": "Compressed air can be explored through pressure vessels, pipes, heat recovery, control systems, sensor data and sandmass models before the future integrated network gets its own repo.", "question": "Could pressure-air thinking help Straddie understand storage, heat, sensing and resilience as one joyful systems question?", "review": "Pressure behaviour, compressor sound, heat recovery, service access, local skills, geology, emergency knowledge and economics."},
        {"status": "Storage lane", "title": "Flow batteries and salt-gradient ideas", "plain": "Vanadium flow batteries and salt-gradient storage add more storage imagination to the bench. They are different tools with different rhythms, materials and maintenance stories.", "question": "Which storage chemistry fits island loads, repair skills, water context, budget and local stewardship?", "review": "Lifecycle, cost, electrolyte handling, water sensitivity, maintenance, supply chain and end-of-life rules."},
        {"status": "Pumped-hydro lessons", "title": "Sand hills, perched lakes and water height", "plain": "Snowy 2.0, Wivenhoe, Kidston, Borumba and pumped-hydro atlases show that water-height storage is a serious family. Straddie asks it through ocean, bay, dune height, perched lakes, aquifers, wetlands, sands and mineral sands.", "question": "Could a local informal idea learn from those systems and translate the lesson into Straddie's own sand-island geography?", "review": "Snowy Hydro, CleanCo, Genex, Queensland Hydro, ANU atlas, WetlandInfo, local hydrology and community authority."},
        {"status": "Ocean lab", "title": "Wave and tidal without underwater blades", "plain": "Humans have explored only a small part of wave and tide. No underwater blades can open flutter, vortex shedding, shrimp timing, mantis-shrimp strike physics, oscillating foils, membranes, reef lattices, buoys, sensors and maker-space geometry.", "question": "Could kids, fishers, surfers, engineers, artists and marine scientists all sketch different ways motion might become useful energy or knowledge?", "review": "Wave atlas data, marine life, navigation, anchoring, storms, sediment, local observation, repairability and reversibility."},
        {"status": "Coastal abundance", "title": "Reefs, surf banks and sand-media loops", "plain": "Artificial reefs, oyster reefs, living shorelines, surf banks, stable dunes and Sandworm spoil loops can be explored together as material literacy: where does media come from, where could it go, who learns the skills, and what changes over time?", "question": "Could tunnel-volume thinking help a reef plan become a useful local build pathway instead of a stockpile problem?", "review": "Narrowneck, Palm Beach, Tweed sand bypassing, Moreton Bay reefs, Windara Reef, OceanWatch living shorelines, Raine Island, Port of Brisbane and Sandworm spoil-loop data."},
        {"status": "Fractal harvesting", "title": "Bladeless, motionless and flutter wind", "plain": "Wind is not only tower-scale turbines. Vortex masts, rooftop pressure systems, flutter ribbons, piezo flags, triboelectric films and electrostatic converters all ask how motion at different scales could feed island intelligence.", "question": "Could island wind be mapped as many useful edge motions, not just one peak-output machine?", "review": "Roof edges, ferry ramps, dunes, vents, masts, railings, durability, quietness, repair, wildlife, data and output."},
        {"status": "Future repo", "title": "Integrated pressure, carbon and response network", "plain": "This atlas points toward a dedicated repo for the whole pressure, carbon, response and sensing system.", "question": "Could a dedicated map explore compressed air, aquifers, carbon capture, fire response, emergency power, water, ventilation, sensors, data and governance as one living system?", "review": "QYAC, Geoscience Australia, ARENA, Queensland WetlandInfo, emergency-response references and the public source trail."},
    ]) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner split">
    <div>
      <p class="section-label">Self-sovereign posture</p>
      <h2>What does the place reveal when people stay curious?</h2>
      <p class="lede muted">The invitation is not to obey a plan. It is to ask sharper questions: what does Country, water, pressure, fire, cost, data or local wealth reveal when residents can inspect the idea and shape the next test?</p>
    </div>
    <div class="quote-panel">A clean-energy superpower can start as questions people can enter, challenge and improve.</div>
  </div>
</section>
"""


def solar_body() -> str:
    return page_hero(by_id("solar")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">First power station</p>
      <h2>Could every useful roof become part of the island's energy brain?</h2>
      <p class="lede muted">Rooftop solar is the least weird part of the stack. The deeper question is how homes, businesses, clubs and public roofs can act together without taking control away from owners.</p>
      <ul class="question-list">
        <li>Which roofs already produce power, and which are still waiting?</li>
        <li>Which loads matter most: fridges, pumps, workshops, e-bikes, ferries, lights, kiosks or emergency phones?</li>
        <li>Could hot water and thermal storage soak up midday solar before money is spent on complex hardware?</li>
      </ul>
    </div>
    <figure class="visual-panel">
      <img src="assets/img/heroes/home-energy.webp" alt="Coastal island clean energy scene with solar rooftops, sand storage, ferry gateway and a community table.">
    </figure>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Solar heat</p>
      <h2>Could concentration be a workshop question before it is a power-station claim?</h2>
      <p class="lede muted">Concentrated solar thermal can make high-grade heat and store it. On an island, the public first question may be smaller: can clean heat dry, cook, sterilise, warm water, support a workshop or charge a sand store?</p>
    </div>
""" + card_grid([
        {"label": "Question", "title": "What could use heat?", "text": "Food, water, washing, repair, drying, ceramics, glass, community kitchen, disaster response or industrial process heat?"},
        {"label": "Question", "title": "Where does shade already make sense?", "text": "Could car parks, ferry waiting areas, market spaces and workshop yards carry solar shade before they carry big claims?"},
        {"label": "Question", "title": "What is the no-regret test?", "text": "Could one roof audit, load profile, hot-water upgrade or small solar-thermal demo make the next decision clearer?"},
    ]) + """
  </div>
</section>
"""


def storage_body() -> str:
    return page_hero(by_id("storage")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Storage is the island question</p>
      <h2>Can clean power become evening abundance for homes, workshops and ferries?</h2>
      <p class="lede muted">This page opens storage as a joyful responsible abundance question: heat, hot water, sand, rock, compressed air, EVs and demand shifting. The larger pressure, carbon, sensing and fire-response weave is only introduced here, with source links, so a future repo can explore the whole living network properly.</p>
    </div>
    <div class="quote-panel">How much intelligence could a happy clean-energy island power when sunlight, heat, movement and storage begin working together?</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Sand battery", "title": "Could sand store warmth, work and community confidence?", "text": "A sand battery is a heat story first. Could local sand, stone, insulation, sensors and repair skills teach clean heat for water, drying, cooking, workshops or resilience?"},
        {"label": "Flow battery", "title": "Could flow batteries suit the island's daily rhythm?", "text": "Flow batteries invite questions about longer cycling, maintenance, materials, water context, service access, ownership and who learns how to keep them working."},
        {"label": "Salt gradient", "title": "Could blue-energy chemistry add another doorway?", "text": "Salt-gradient systems can begin as a curiosity bench: what can ocean, bay, brine, membranes and chemistry teach before anyone imagines island hardware?"},
        {"label": "Pressure air", "title": "Could compressed air become a transparent pressure-energy question?", "text": "What can containers, pipes, compressors, heat recovery, controls, sensor data and sandmass modelling teach when residents can see the tradeoffs and imagine the next shape themselves?"},
        {"label": "Hydrogen", "title": "Could hydrogen store sunlight as a water loop?", "text": "Could desal, electrolysis, oxygen, heat, hydrogen storage and brine minerals become a public learning loop for transport, backup power and Moreton Bay repair?", "href": "hydrogen.html", "action": "Open hydrogen"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Future repo bridge</p>
      <h2>Where does the bigger pressure-carbon-response map live next?</h2>
      <p class="lede muted">A later repo can hold the whole weave: compressed air, aquifers, carbon capture, fire response, emergency power, water, ventilation, sensors, data, governance and local authority. This first atlas keeps a bridge and gathers the source links that help the deeper map begin well.</p>
    </div>
""" + card_grid([
        {"label": "Future repo", "title": "Integrated pressure, carbon and response network", "text": "A bridge for the deeper repo that can explore the whole systems map in more detail when that room is ready."},
        {"label": "Authority", "title": "Quandamooka Yoolooburrabee Aboriginal Corporation", "text": "Public organisational doorway for Quandamooka Country, land and sea management.", "href": "https://qyac.net.au/", "action": "Open QYAC"},
        {"label": "Reference", "title": "Geoscience Australia carbon capture and storage", "text": "National source trail for capture, transport, compression, storage and monitoring language.", "href": "https://www.ga.gov.au/aecr2024/carbon-capture-and-storage", "action": "Open source"},
        {"label": "Reference", "title": "ARENA advanced compressed air", "text": "Australian source trail for long-duration compressed-air storage.", "href": "https://arena.gov.au/projects/hydrostor-broken-hill-advanced-compressed-air-energy-storage-demonstration/", "action": "Open source"},
        {"label": "Reference", "title": "Aquifer CAES technical paper", "text": "Study material for aquifer-storage questions and the future repo source trail.", "href": "https://www.sandia.gov/files/ess/EESAT/2009_papers/Technical%20Feasibility%20of%20Compressed-Air%20Energy%20Storage%20in%20an%20Aquifer%20Storage%20Vessel.pdf", "action": "Open paper"},
        {"label": "Atlas trail", "title": "Source notes", "text": "The current source trail stays here until the dedicated integrated-systems repo exists.", "href": "sources.html", "action": "Open sources"},
    ]) + """
  </div>
</section>
"""


def hydrogen_body() -> str:
    return page_hero(by_id("hydrogen")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Water-energy loop</p>
      <h2>Could green hydrogen become a loop people can inspect?</h2>
      <p class="lede muted">Green hydrogen starts with renewable electricity and water electrolysis. On a sand island, the richer question is wider: where does the water come from, could desalination be powered cleanly, what does the brine become, how are oxygen and heat used, and could the value make Moreton Bay repair work more resourced and visible over time?</p>
      <ol class="pathway">
        <li><p><strong>Start with water.</strong> Could a public desal bench show litres, energy, membranes, maintenance, brine concentration and water quality in plain English?</p></li>
        <li><p><strong>Split the loop open.</strong> Could electrolysis make hydrogen, oxygen, heat, data and learning visible before a larger fuel pathway takes shape?</p></li>
        <li><p><strong>Let the bay benefit.</strong> Could mineral recovery, sensors, seagrass knowledge, catchment repair and public report-card work sit in the same conversation?</p></li>
      </ol>
    </div>
    <div class="quote-panel">A hydrogen idea gets more interesting when it becomes a water, minerals, oxygen, transport, data and Moreton Bay repair question.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "National strategy", "title": "What does Australia say hydrogen is for?", "text": "Could the national hydrogen strategy help Straddie ask about production, local use, export, skills, infrastructure and community benefit?", "href": "https://www.dcceew.gov.au/energy/publications/australias-national-hydrogen-strategy", "action": "Open source"},
        {"label": "Electrolysis", "title": "What does renewable hydrogen need?", "text": "Could solar, water, electrolysers, oxygen, heat and storage be shown as one transparent public learning loop?", "href": "https://arena.gov.au/renewable-energy/hydrogen/", "action": "Open ARENA"},
        {"label": "Desal", "title": "Could desal be a small visible water question first?", "text": "Could a bench-scale desal loop teach water input, filter care, energy use, brine concentration and maintenance before anyone imagines island-scale supply?"},
        {"label": "Brine mining", "title": "Could brine become a resource-recovery lab?", "text": "Could concentrated brine invite magnesium, lithium, salt, trace-mineral and membrane research while keeping discharge and ecology visible?", "href": "https://gisera.csiro.au/beneficial-reuse-and-disposal-options-for-brine-in-queensland/", "action": "Open source"},
        {"label": "Moreton Bay", "title": "Could clean-energy value help clean the bay?", "text": "Could hydrogen, desal and brine research help fund water-quality sensors, seagrass knowledge, catchment repair, public dashboards and local stewardship?", "href": "https://reportcard.hlw.org.au/", "action": "Open report card"},
        {"label": "Ferries", "title": "Could ferries and service vehicles create a real fuel question?", "text": "Could hydrogen be compared with batteries, shore power, e-fuels and demand shifting for ferries, heavy vehicles, emergency backup and workshop loads?"},
    ]) + """
  </div>
</section>
"""


def sharing_body() -> str:
    return page_hero(by_id("sharing")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Feed-in tariff question</p>
      <h2>Could the island use its own spare solar before selling it cheaply?</h2>
      <p class="lede muted">A feed-in tariff is the rate paid for extra solar exported to the grid. The deeper Straddie question is whether midday power can do more local work first: heat water, chill food, charge EVs, run workshops, fill neighbourhood batteries or support emergency loads.</p>
      <ol class="pathway">
        <li><p><strong>Use first.</strong> What loads can shift into sunny hours without making life harder?</p></li>
        <li><p><strong>Store second.</strong> Which homes, shops, clubs or service nodes need a shared battery, hot-water bank, sand heat store or EV charging window?</p></li>
        <li><p><strong>Settle plainly.</strong> Can savings be shown as bill credits, co-op accounts, vouchers or public receipts alongside any token idea?</p></li>
      </ol>
    </div>
    <div class="quote-panel">The useful question is not "can crypto sell power?" It is "can people see, consent to and benefit from the value their energy creates?"</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Neighbourhood storage</p>
      <h2>What if each village had a small energy commons instead of one giant battery story?</h2>
      <p class="lede muted">Neighbourhood batteries are only one possible storage layer. A local stack could include home batteries, shared network batteries, sand heat, hot water, cool rooms, EV batteries and smart loads, each doing the job it is actually good at.</p>
    </div>
""" + card_grid([
        {"label": "Battery commons", "title": "Where could shared storage reduce waste?", "text": "Could Dunwich, Amity, Point Lookout, the ferry gateway or a public building store rooftop solar close to the loads that use it later?"},
        {"label": "Sand heat node", "title": "Could neighbourhood sand batteries serve heat first?", "text": "Could a small thermal store support hot water, drying, cooking, workshop heat or emergency comfort before pretending to be an electric battery?"},
        {"label": "EV sink", "title": "Can vehicles become flexible loads?", "text": "Could island EVs, e-bikes, service vehicles and visitor chargers soak up midday solar while keeping chargers fair, visible and not grid-stressing?"},
        {"label": "Cold and water", "title": "What loads already want timing?", "text": "Could fridges, cool rooms, pumps, laundry, desalination research, water heating and workshop machines move into the cheap sunny window?"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Transport web</p>
      <h2>Could clean energy planning include ferries, EVs, hydrogen and future tunnels as one transport web?</h2>
      <p class="lede muted">The ferry terminal upgrade makes the gateway a real transport planning node. EV charging, e-shuttles, service vehicles, green-hydrogen fuel questions and future Sandworm-style tunnel ideas can be explored as load-shifting, service and movement questions.</p>
      <ul class="question-list">
        <li>Could ferry arrival peaks tell chargers when not to draw hard from the grid?</li>
        <li>Could EV chargers reward slow, sunny charging instead of expensive evening charging?</li>
        <li>Could hydrogen compare honestly with batteries and shore power for ferries, heavy vehicles or backup fuel?</li>
        <li>Could any future tunnel or utility corridor carry data, air, water and energy services as part of a dedicated Sandworm systems map?</li>
      </ul>
    </div>
    <figure class="visual-panel">
      <img src="assets/img/heroes/ferry-gateway.webp" alt="Dunwich ferry gateway foreshore used as a public transport and clean energy planning reference.">
    </figure>
  </div>
</section>
<section class="section deep-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Plain ledger</p>
      <h2>Could a community ledger make bills easier to trust?</h2>
      <p class="lede">A ledger could start as simple accounting: who generated, who stored, who used, who paid, who received a credit, and who opted out. A token or crypto layer can sit beside plain rules, consumer rights, cyber security and a human-readable fallback.</p>
    </div>
""" + card_grid([
        {"label": "Plain bill", "title": "Could local use beat a feed-in tariff?", "text": "If exported solar earns only a small credit, could it be better to offset a neighbour's load, charge a local EV, run a cold room, heat water or build a mutual reserve?"},
        {"label": "Fair go", "title": "How does everyone keep a fair go?", "text": "Could every household see the rules, join voluntarily, leave easily, protect private load data and find a help path when circumstances change?"},
        {"label": "Retail path", "title": "Which legal wrapper is real?", "text": "Is this a retailer product, embedded network, VPP, community battery subscription, co-op service, grant-funded pilot or only a research note?"},
    ]) + """
  </div>
</section>
"""


def water_body() -> str:
    return page_hero(by_id("water")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Pumped-hydro lessons</p>
      <h2>Could Snowy-scale thinking help a sand island ask better questions?</h2>
      <p class="lede muted">Snowy 2.0, Wivenhoe, Kidston, Borumba and the ANU pumped-hydro atlas prove that water-height storage is a serious human tool. Straddie is a different kind of place: ocean, bay, sand hills, dune ridges, perched lakes, wetlands, aquifers, sands and mineral sands. The informal question starts by learning the logic of height, time, tunnels, tanks, reversible flow, modelling and grid support, then asking what the island's own map reveals.</p>
      <ol class="pathway">
        <li><p><strong>Study real pumped hydro with respect.</strong> What do Snowy, Wivenhoe, Kidston and Borumba teach about scale, duration, reservoirs, tunnels, pumps, reversible generation and public trust?</p></li>
        <li><p><strong>Map Straddie as Straddie.</strong> What do ocean edge, bay edge, dune height, sandmass infiltration, aquifers, perched lakes, wetlands and mineral sands suggest, invite or reshape?</p></li>
        <li><p><strong>Let models become shared capability.</strong> Could tank pairs, digital twins, school rigs and maker-space demos help residents see the physics before any larger informal idea grows legs?</p></li>
      </ol>
    </div>
    <div class="quote-panel">A happy clean-energy island can power more than lights: learning, compute, transport, food, repair, culture and local confidence.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Reference systems and local sketches</p>
      <h2>What could a serious informal water-height idea learn first?</h2>
    </div>
""" + card_grid([
        {"label": "Snowy 2.0", "title": "What does long-duration storage teach?", "text": "Could tunnels, upper and lower reservoirs, reversible generation and grid timing become a plain-English lesson for island-scale imagination?", "href": "https://www.snowyhydro.com.au/snowy-20/about/", "action": "Open source"},
        {"label": "Wivenhoe", "title": "What does Queensland already know?", "text": "Could the Wivenhoe and Splityard Creek relationship teach how stored height can answer peak demand close to home?", "href": "https://cleancoqueensland.com.au/portfolio/owned-and-operated/wivenhoe-pumped-storage-hydro-power-station/", "action": "Open source"},
        {"label": "Kidston", "title": "What can a storage project teach about timing?", "text": "Could the Kidston example help compare solar, evening peaks, long-duration discharge and regional grid value?", "href": "https://genexpower.com.au/250mw-kidston-pumped-storage-hydro-project/", "action": "Open source"},
        {"label": "Borumba", "title": "What does a new Queensland water-height idea need to study?", "text": "Could Borumba show the depth of modelling, consultation, access planning and source trail a serious water-height idea gathers?", "href": "https://qldhydro.com.au/projects/borumba/", "action": "Open source"},
        {"label": "Atlas", "title": "What does topographic screening reveal?", "text": "Could ANU-style pumped-hydro mapping help compare height, distance, water, access and storage duration while translating the lesson to a sand-island setting?", "href": "https://re100.eng.anu.edu.au/global/", "action": "Open atlas"},
        {"label": "Straddie sketch", "title": "What does the island offer on its own terms?", "text": "Could dune height, bay and ocean edges, tank pairs, sandmass infiltration, aquifers, perched lakes, sands and mineral sands shape a different water-height imagination?"},
    ]) + """
  </div>
</section>
"""


def marine_body() -> str:
    return page_hero(by_id("marine")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">First principles ocean lab</p>
      <h2>How many wave and tide geometries are still unmapped?</h2>
      <p class="lede muted">The known wave and tidal options explored by humans are only a small patch of the design space. A no-underwater-blades posture can invite more imagination: flutter cascades, shrimp appendage timing, mantis-shrimp strike physics, vortex shedding, oscillating foils, flexible flags, membranes, reef lattices, buoyant hinges, shell geometries, sensor trickle-power and ideas a kid can sketch in five minutes.</p>
      <ul class="question-list">
        <li>What can waves, tides, fish, swimming shrimp, striking mantis shrimp, kelp, shells, foam lines and sand ripples teach about motion?</li>
        <li>Could maker-space rigs, school models, wave tanks and simulations let people test patterns before choosing a device?</li>
        <li>Could reef-energy ideas also improve monitoring, habitat knowledge, erosion understanding, food systems and public learning?</li>
      </ul>
    </div>
    <figure class="visual-panel">
      <img src="assets/img/heroes/marine-energy.webp" alt="Bright Straddie-style coast with quiet offshore reef-energy structures and clear water.">
    </figure>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Wave atlas", "title": "Where is the movement?", "text": "Could ARENA and CSIRO-style resource mapping show swell, season, direction and energy while leaving the design space open?", "href": "https://arena.gov.au/projects/australian-wave-energy-atlas/", "action": "Open source"},
        {"label": "Flutter", "title": "Could flexible forms harvest tiny repeated motion?", "text": "Could inverted flags, kelp-like strips, soft hinges or piezo surfaces turn small oscillations into useful sensor power or lessons?", "href": "https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/abs/energy-harvesting-by-flowinduced-flutter-in-a-simple-model-of-an-inverted-piezoelectric-flag/37FF699E5B55E238A41F056E4A06DBDB", "action": "Open source"},
        {"label": "Vortex", "title": "Could currents shake useful structures?", "text": "Could vortex-induced vibration, fish-like timing or oscillating bodies offer no-blade current ideas for models and careful field questions?", "href": "https://www.energy.gov/cmei/success-stories/articles/eere-success-story-vortex-hydro-energy-develops-transformational", "action": "Open source"},
        {"label": "Shrimp clue", "title": "Could timing and strike physics teach new geometry?", "text": "Swimming shrimp show cascading appendage timing. Peacock mantis shrimp deliver one of the fastest animal strikes measured: their hammer-like mouthparts can hit 12-23 m/s in water and make cavitation bubbles. Could those clues become sketches, simulations and bench rigs?", "href": "https://pateklab.biology.duke.edu/research/mechanics-of-ultrafast-movement/mechanics-of-movement-mantis-shrimp/", "action": "Open Patek Lab"},
        {"label": "Foils", "title": "Could flapping or oscillating foils stay gentle and useful?", "text": "Could biomimetic foils, fish-fin movement and flexible hydrokinetic forms be compared with standard turbines instead of dismissed?", "href": "https://tethys-engineering.pnnl.gov/publications/analysis-biomimetic-stream-energy-device-based-flapping-foils", "action": "Open source"},
        {"label": "Reef geometry", "title": "Could habitat, surf and sand media share one model?", "text": "Could oyster reefs, living shorelines, surf banks, reef modules and Sandworm material flows become their own public calculator and map?", "href": "reefs.html", "action": "Open reefs"},
        {"label": "Kids and makers", "title": "What would a five-minute sketch reveal?", "text": "Could school groups, surfers, fishers, artists, makers, engineers and marine scientists all add pattern ideas to the same public board?"},
    ]) + """
  </div>
</section>
"""


def reefs_body() -> str:
    examples = [
        {"label": "Gold Coast", "title": "What can Narrowneck and Palm Beach teach?", "text": "Could artificial reefs be read as coastal protection, surf amenity, wave-shape learning and long-term monitoring, not just dumped rock?", "href": "https://www.goldcoast.qld.gov.au/Environment-sustainability/Protecting-our-environment/Managing-our-beaches/Seawalls-artificial-reefs", "action": "Open source"},
        {"label": "Sand bank", "title": "What can Tweed sand bypassing teach?", "text": "Could the Snapper Rocks / southern Gold Coast story help people ask how sand movement, point breaks, nourishment and public value interact?", "href": "https://www.qld.gov.au/environment/coasts-waterways/beach/tweed-river", "action": "Open source"},
        {"label": "Moreton Bay", "title": "What do existing artificial reefs already show?", "text": "Could Moreton Bay reef sites help compare habitat, recreation, placement, access, monitoring and public explanation?", "href": "https://www.qld.gov.au/environment/coasts-waterways/marine-parks/artificial-reefs", "action": "Open source"},
        {"label": "Shellfish", "title": "What can Windara Reef and shellfish restoration teach?", "text": "Could oyster reefs and recycled-shell work show how habitat, water quality, fish life, community labour and coastal care can grow together?", "href": "https://www.natureaustralia.org.au/what-we-do/our-priorities/oceans/ocean-stories/restoring-shellfish-reefs/gulf-st-vincent/", "action": "Open source"},
        {"label": "Living shoreline", "title": "Could oyster shells slow water and grow habitat?", "text": "Could living shorelines turn erosion, shell recovery, saltmarsh, oysters, sediment and community work into a visible coastal repair pathway?", "href": "https://www.oceanwatch.org.au/community/livingshorelines/", "action": "Open source"},
        {"label": "Island shaping", "title": "What can Raine Island teach about shaping with care?", "text": "Could beach re-profiling, habitat outcomes, monitoring and long timeframes sharpen how people talk about any artificial-island or stable-dune idea?", "href": "https://www.qld.gov.au/environment/plants-animals/conservation/raineisland-recovery", "action": "Open source"},
        {"label": "Reclamation", "title": "What can Port of Brisbane teach about staged media placement?", "text": "Could large-scale reclamation help people ask better questions about walls, ground improvement, material logistics, settlement, monitoring and public evidence?", "href": "https://www.portbris.com.au/major-projects/fpe", "action": "Open source"},
        {"label": "Sandworm", "title": "How does the tunnel-spoil loop join this page?", "text": "Could the Sandworm spoil-loop builder supply the material-stream question while this page calculates volume, reef media, skills, equipment and timing?", "href": "https://auraofintelligence.github.io/sandworm-subterranean-systems/builders/spoil-loop-brief.html", "action": "Open builder"},
    ]
    questions = [
        {"label": "Oyster reef", "title": "Could shellfish farming and habitat learn together?", "text": "Where could recycled shell, reef base, spat, water quality, working boats, monitoring and local food knowledge meet without pretending one shape fits every shore?"},
        {"label": "Erosion", "title": "Could living shorelines reduce hard-edge thinking?", "text": "Which bay edges, dune toes, wetlands or ferry-adjacent places invite slower water, more habitat and less panic about sand movement?"},
        {"label": "Surf bank", "title": "Could point-break joy be part of the public value?", "text": "How might reef geometry, sand bypass learning, wave angle, bathymetry, surfer observation and storm recovery become a shared map?"},
        {"label": "Stable dunes", "title": "Could dunes become teachers, not raw material?", "text": "Which stable dunes, mineral sands, vegetation lines and old disturbance stories can help people read what belongs onshore and what belongs offshore?"},
        {"label": "Artificial island", "title": "Could landform imagination stay measurable?", "text": "Could any island, reef shelf, lagoon edge or platform idea carry a simple media ledger: volume, source, placement, monitoring and public learning?"},
        {"label": "Automation", "title": "Could machines become transparent helpers?", "text": "Could conveyors, pumps, screens, geotextile bags, moulds, drones, bathymetry and sensor buoys show what they are doing week by week?"},
    ]
    surface_cards = [
        {"label": "Maker-space", "title": "Could climate-ready blocks be designed as island tools?", "text": "Could quick-fit interlocking blocks be robotically made, assembled, disassembled, serviced and customised for real residents rather than treated as profit-first building products?", "href": "https://auraofintelligence.github.io/straddie-makerspace-lab/sand.html", "action": "Open sand lab"},
        {"label": "Geopolymer yard", "title": "Could surface pieces start as visible recipes?", "text": "Could pavers, tiles, weights, garden edges, service plinths and sample blocks carry recipes, QR material passports, cure dates, repair notes and next-version questions?", "href": "https://auraofintelligence.github.io/straddie-makerspace-lab/concrete.html", "action": "Open concrete lab"},
        {"label": "Ferry gateway", "title": "Could ferry-terminal surfaces become service architecture?", "text": "Could seats, shade bases, low walls, lighting edges, screen plinths and path modules hide power, water, data, sensors and maintenance access while staying movable if sea levels rise?", "href": "https://auraofintelligence.github.io/dunwich-gumpi-ferry-terminal-open-data-lab/community-genai-examples.html", "action": "Open ferry lab"},
        {"label": "Ballow Road", "title": "Could 10-12 Ballow Road test sand sport and screen blocks?", "text": "Could slope-aware blocks become seating, sand-sport boundaries, screen bases, market weights, cable runs, shaded terraces and storage pieces that can be reconfigured instead of locked into one layout?", "href": "https://auraofintelligence.github.io/ballow-road-sand-screen-hub/site.html", "action": "Open Ballow hub"},
        {"label": "Homes", "title": "Could silicate products serve residents first?", "text": "Could glass filters, ceramic membranes, splashbacks, tiles, handles, knobs, jars, repairable appliance parts and custom homeware be made for island usefulness rather than outside-margin logic?", "href": "https://auraofintelligence.github.io/straddie-makerspace-lab/sand.html", "action": "Open home materials"},
        {"label": "Service blocks", "title": "Could blocks hide services without hiding control?", "text": "Could conduits, ducts, micro-drainage, air paths, fibre, sensors, charge points and inspection lids sit inside interlocking blocks that residents can understand, service and move?"},
    ]
    return page_hero(by_id("reefs")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Coastal material literacy</p>
      <h2>Could every metre of tunnel become a reef, dune, surf or habitat question?</h2>
      <p class="lede muted">The Sandworm repo already asks how future tunnel spoil might become blocks, reef modules, dune support, tunnel lining tests or stored heat. This page turns that into a live material ledger: small service tunnels, robot corridors, Loop-style tunnels, weekly advance speed, reef geometry, climate-ready blocks, glass and silicate products, human skills, automation and time.</p>
      <ol class="pathway">
        <li><p><strong>Keep the 100 m unit.</strong> What volume comes from each 100 m section, and how fast could that next 100 m arrive?</p></li>
        <li><p><strong>Choose a pathway.</strong> What share could become reef media, living shoreline, surf-bank base, dune support, service blocks, glass, ceramic or resident-use material?</p></li>
        <li><p><strong>Map the handoff.</strong> Which equipment, skills, testing, automation and storage yards keep up when the tunnel system is advancing quickly?</p></li>
      </ol>
    </div>
    <div class="quote-panel">A reef and block plan can empower the tunnel build when the material stream becomes visible early: not as waste, but as a high-throughput flow of habitat, surf, surface services, homes and learning value.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Australian examples</p>
      <h2>Which real Australian projects can teach the first questions?</h2>
      <p class="lede muted">These are not copy-paste answers for Straddie. They are public examples that help people compare shape, purpose, monitoring, material, public value and the kind of evidence a serious reef or sand-media idea gathers.</p>
    </div>
""" + card_grid(examples) + """
  </div>
</section>
<section class="section" id="reef-calculator">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Interactive tunnel to reef ledger</p>
      <h2>What does 100 m of tunnel become, and how fast can it arrive?</h2>
      <p class="lede muted">Move the sliders to sketch a weekly material flow. The 100 m volume stays as the clean comparison unit; tunnel speed shows whether that material arrives in hours, days or weeks. The scale spans small service and robot tunnels through Loop-style corridors, because the point is to advance the field rather than copy old tunnel pacing or current design-method assumptions.</p>
    </div>
    <div class="reef-calculator" data-reef-calculator>
      <div class="calc-controls">
        <div class="range-field">
          <label for="reef-diameter">Tunnel diameter <output data-calc-out="diameter">3.6 m</output></label>
          <input id="reef-diameter" type="range" min="0.6" max="5" step="0.1" value="3.6" data-calc-input="diameter">
        </div>
        <div class="range-field">
          <label for="reef-speed">Tunnel advance per week <output data-calc-out="weeklyAdvance">1 km/week</output></label>
          <input id="reef-speed" type="range" min="50" max="5000" step="50" value="1000" data-calc-input="weeklyAdvance">
        </div>
        <div class="range-field">
          <label for="reef-weeks">Weeks in this sprint <output data-calc-out="weeks">4</output></label>
          <input id="reef-weeks" type="range" min="1" max="16" step="1" value="4" data-calc-input="weeks">
        </div>
        <div class="range-field">
          <label for="reef-share">Material converted to useful media <output data-calc-out="reefShare">35%</output></label>
          <input id="reef-share" type="range" min="0" max="90" step="5" value="35" data-calc-input="reefShare">
        </div>
        <div class="range-field">
          <label for="reef-bulking">Bulking or formed-media factor <output data-calc-out="bulking">1.15x</output></label>
          <input id="reef-bulking" type="range" min="0.8" max="1.6" step="0.05" value="1.15" data-calc-input="bulking">
        </div>
        <div class="range-field">
          <label for="reef-module">Average reef module or media cell <output data-calc-out="moduleSize">25 m3</output></label>
          <input id="reef-module" type="range" min="5" max="250" step="5" value="25" data-calc-input="moduleSize">
        </div>
      </div>
      <div class="calc-toggle-grid" aria-label="Material pathways">
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="oyster" checked><span>Oyster / shellfish reef</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="living" checked><span>Living shoreline</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="surf" checked><span>Surf bank geometry</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="dune"><span>Stable dune support</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="island"><span>Artificial island / platform</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="surface" checked><span>Quick-fit surface blocks</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="homes"><span>Glass / silicate home products</span></label>
        <label class="toggle-card"><input type="checkbox" data-calc-toggle="automation" checked><span>Automation and sensors</span></label>
      </div>
      <div class="calc-results">
        <article class="calc-metric"><span>Per 100 m tunnel</span><strong data-calc-out="per100">1,018 m3</strong></article>
        <article class="calc-metric"><span>Time to earn 100 m</span><strong data-calc-out="timePer100">16.8 h</strong></article>
        <article class="calc-metric"><span>Weekly tunnel volume</span><strong data-calc-out="weeklySpoil">10,179 m3</strong></article>
        <article class="calc-metric"><span>Weekly useful media</span><strong data-calc-out="weeklyReef">4,097 m3</strong></article>
        <article class="calc-metric"><span>Sprint useful media</span><strong data-calc-out="stageReef">16,389 m3</strong></article>
        <article class="calc-metric"><span>Approx. modules / week</span><strong data-calc-out="weeklyModules">164</strong></article>
        <article class="calc-metric"><span>Stockpile avoided</span><strong data-calc-out="avoided">14,251 m3</strong></article>
      </div>
      <div class="calc-panels">
        <article class="calc-panel">
          <p class="mini-label">Time flow</p>
          <h3>How does the material move over time?</h3>
          <div class="timeline-bars" data-calc-timeline></div>
          <p class="calc-note" data-calc-out="timelineNote"></p>
        </article>
        <article class="calc-panel">
          <p class="mini-label">Work map</p>
          <h3>What equipment, skills and automation appear?</h3>
          <div class="work-map" data-calc-out="workMap"></div>
        </article>
      </div>
      <div class="sandworm-bridge" data-sandworm-bridge>
        <p class="mini-label">Sandworm data bridge</p>
        <h3>Could the Sandworm repo feed the next calculator?</h3>
        <p>The live calculator starts with local inputs here and reads the public Sandworm site data when available. The next useful bridge could pull corridor pages, spoil-loop builder fields and digital-twin layers into one shared material ledger.</p>
        <div class="tag-row" data-sandworm-links></div>
      </div>
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Surface systems and homes</p>
      <h2>Could tunnel media become climate-ready island architecture?</h2>
      <p class="lede muted">Could surface design become an island capability: quick-fit interlocks, robotic placement, hidden services, material passports, repairable home products and movable public surfaces that help the island adapt if sea levels rise?</p>
    </div>
""" + card_grid(surface_cards) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Local questions</p>
      <h2>What else belongs beside wave and tidal energy?</h2>
      <p class="lede muted">Reefs are not only energy structures. They can be oyster habitat, erosion buffers, surf-shaping experiments, stable-dune companions, living shorelines, artificial-island questions, sensor platforms and material-flow teachers.</p>
    </div>
""" + card_grid(questions) + """
  </div>
</section>
<script src="https://auraofintelligence.github.io/sandworm-subterranean-systems/assets/js/site-data.js"></script>
<script src="assets/js/reef-calculator.js"></script>
"""


def wind_body() -> str:
    return page_hero(by_id("wind")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Fractal wind field</p>
      <h2>Could Straddie harvest the wind hiding in edges, flutter and turbulence?</h2>
      <p class="lede muted">Bladeless wind includes vortex-induced vibration, motionless rooftop capture, aeroelastic flutter, piezo flags, triboelectric films, Windbelt-style ribbons and EWICON-style electrostatics. The island question is not only peak commercial output. It is how many small, quiet energy moments could power sensors, signs, radios, lights, weather stations, data loggers, art, learning kits and distributed intelligence.</p>
      <div class="tag-row">
        <span class="tag">Vortex</span>
        <span class="tag">Flutter</span>
        <span class="tag">Roof-edge flow</span>
        <span class="tag">Turbulence</span>
        <span class="tag">Piezo flags</span>
        <span class="tag">TENG films</span>
        <span class="tag">Windbelt ribbons</span>
        <span class="tag">EWICON</span>
        <span class="tag">Aeromine</span>
        <span class="tag">Sensor mesh</span>
      </div>
    </div>
    <div class="quote-panel">Fractal wind asks where motion already lives: roof edges, dune paths, ferry waiting areas, shade structures, vents, signs, masts, railings and workshop rigs.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Vortex", "title": "Could a no-blade mast turn shed vortices into power?", "text": "Vortex Bladeless treats oscillation as the harvest, not a problem to remove.", "href": "https://vortexbladeless.com/", "action": "Open source"},
        {"label": "Roof edge", "title": "Could ferry roofs and sheds read pressure flow?", "text": "Aeromine-style rooftop systems point to roof-edge wind as a designed surface, not a tower.", "href": "https://aerominetechnologies.com/", "action": "Open source"},
        {"label": "Electrostatic", "title": "Could wind move charge without spinning machinery?", "text": "EWICON adds an electrostatic branch to the no-moving-mechanical-parts wind conversation.", "href": "https://www.mecanoo.nl/projects/project/61/ewicon", "action": "Open source"},
        {"label": "Ribbon", "title": "Could Windbelt-style flutter teach low-wind harvesting?", "text": "A ribbon, belt or flag can turn air movement into vibration that a tiny generator can read.", "href": "https://smartshelterfoundation.org/collection/low-wind-energy", "action": "Open source"},
        {"label": "Micro-array", "title": "Could many tiny harvesters act like a wind-reading field?", "text": "VIV micro-harvesters in formation invite sensor-mesh thinking rather than one big machine.", "href": "https://www.nature.com/articles/s41598-019-56786-0", "action": "Open paper"},
        {"label": "Flutter", "title": "Could flags, films and membranes feed island intelligence?", "text": "Piezo and triboelectric flutter research opens low-power pathways for signals, monitoring, art and learning kits.", "href": "https://onlinelibrary.wiley.com/doi/full/10.1002/msd2.12035", "action": "Open paper"},
        {"label": "Island map", "title": "Could kids and makers map wind as patterns?", "text": "Roof edges, dunes, ferry ramps, signs, masts, vents and pathways could become a shared wind-pattern atlas before any one device is chosen."},
    ]) + """
  </div>
</section>
"""


def network_body() -> str:
    research_cards = [
        {"label": "Style guide", "title": item["repo"], "text": item["learning"]}
        for item in STYLE_RESEARCH
    ]
    return page_hero(by_id("network")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Deep references</p>
      <h2>This repo is not alone. It is a clean-energy room in an existing house.</h2>
      <p class="lede muted">The companion sites give the new atlas its shape: practical tests, ferry data, public sources, grants, wealth, mutual care, trust, jobs and careful future imagination.</p>
    </div>
""" + repo_grid() + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Style research carried forward</p>
      <h2>What the recent repos taught this one.</h2>
    </div>
""" + card_grid(research_cards) + """
  </div>
</section>
"""


def wealth_body() -> str:
    return page_hero(by_id("wealth")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Community wealth</p>
      <h2>Could clean energy become shared resilience, not just cheaper bills?</h2>
      <p class="lede muted">The wealth question is simple: who pays, who benefits, who holds the risk, who owns the data, and who gets to say no before the island is locked into a bad deal?</p>
      <ol class="pathway">
        <li><p><strong>Lower bills first.</strong> Household and small-business wins matter.</p></li>
        <li><p><strong>Shared assets second.</strong> Community batteries, thermal stores or emergency nodes need clear ownership and maintenance.</p></li>
        <li><p><strong>Patient wealth grows from trust.</strong> A fund, co-op or mutual reserve can show law, governance, receipts and consent before asking people to believe in it.</p></li>
      </ol>
    </div>
    <div class="quote-panel">A clean-energy superpower is not just a place that makes energy. It is a place that keeps the upside close enough to govern.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Question", "title": "Could Grants Lab fund the first tests?", "text": "Roof audits, data logging, solar shade, maker-space thermal tests and emergency nodes may become clearer grant notes before big capital is needed.", "href": "https://auraofintelligence.github.io/stradbroke-grants-lab/", "action": "Open Grants Lab"},
        {"label": "Question", "title": "Could mutual care reduce risk?", "text": "Prevention, maintenance, fire checks, storm readiness and public dashboards can lower risk before insurance or mutuals are discussed.", "href": "https://auraofintelligence.github.io/moreton-bay-community-wealth-and-mutuals/", "action": "Open mutuals"},
        {"label": "Question", "title": "Could Ready S.E.T. train people into the work?", "text": "Audits, installs, media, maintenance, grant reporting and site checks can become learning pathways if trust is built first.", "href": "https://auraofintelligence.github.io/ready-set-co-op-trust-hub/", "action": "Open Trust Hub"},
        {"label": "Question", "title": "Could a sovereign wealth fund stay plain?", "text": "The draft brief imagines a fund, tokens and dashboards. The plain public version starts with governance, receipts, audit, anti-fraud rules and the right to refuse."},
        {"label": "Question", "title": "Could power sharing feed the mutual?", "text": "If local solar beats a weak feed-in tariff, could part of the upside support maintenance, fair-go support, emergency storage or training alongside any dividend talk?", "href": "sharing.html", "action": "Open power sharing"},
    ]) + """
  </div>
</section>
"""


def boundaries_body() -> str:
    return page_hero(by_id("boundaries")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Guardrails</p>
      <h2>The bolder the energy idea, the simpler the boundary could be.</h2>
      <p class="lede muted">A boundary can be a living question: what is being cared for, who holds authority, what evidence can sharpen the idea, and how could it keep sovereignty, ecology, privacy and trust intact as it grows?</p>
    </div>
""" + card_grid([
        {"label": "Country", "title": "Who holds authority here?", "text": "Public pages can avoid implying approval, representation or cultural authority that has not been granted."},
        {"label": "Water", "title": "Which water could teach before it is used?", "text": "Perched lakes, wetlands, springs and protected water places can begin as teachers of hydrology, culture, ecology and time."},
        {"label": "Marine", "title": "What does sea life need?", "text": "No underwater blades is only one boundary. Noise, anchoring, sediment, navigation and reversibility matter too."},
        {"label": "Pressure", "title": "What could invite engineering review?", "text": "Compressed air, CO2, pressure vessels, heat stores and response systems can bring engineering knowledge, public sources and local skills into the conversation early."},
        {"label": "Finance", "title": "What could stop tokens becoming hype?", "text": "Any token, app, ledger or community dividend idea can show law, cybersecurity, plain accounting, consent and an analog fallback."},
        {"label": "Power bills", "title": "What could keep bill-sharing fair?", "text": "A power-sharing scheme can show clear opt-in rules, fair-go help paths, privacy, dispute handling and a boring non-crypto way to read the bill."},
        {"label": "Data", "title": "What stays private?", "text": "Household loads, bills, vulnerable people, cultural knowledge and business data can stay out of public dashboards unless people choose otherwise."},
    ]) + """
  </div>
</section>
"""


def sources_body() -> str:
    local_cards = [
        {
            "label": "Local draft",
            "title": source["title"],
            "text": f'{source["use"]} Local source name: {source["file"]}',
        }
        for source in LOCAL_DRAFT_INPUTS
    ]
    source_cards = [
        {
            "label": source["publisher"],
            "title": source["title"],
            "text": f'{source["use"]} Source: {source["url"]}',
            "href": source["url"],
            "action": "Open source",
        }
        for source in SOURCE_LINKS
    ]
    return page_hero(by_id("sources")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Source posture</p>
      <h2>Sources help ask better questions. Authority still lives with people and place.</h2>
      <p class="lede muted">This first draft uses official and technical sources to keep the energy conversation grounded. It also links companion repos because style, nav, builders and local framing came from the existing ecosystem.</p>
    </div>
""" + card_grid(local_cards) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Public and technical sources</p>
      <h2>Open sources for the evidence trail.</h2>
    </div>
""" + card_grid(source_cards, "source-grid") + """
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Connected workbenches</p>
      <h2>Repo family references.</h2>
    </div>
""" + repo_grid() + """
  </div>
</section>
"""


def licence_body() -> str:
    return page_hero(by_id("licence")) + """
<section class="section">
  <div class="section-inner readable">
    <p class="section-label">Custom public-interest licence</p>
    <h2>Shared as public infrastructure, not as extractive packaging.</h2>
    <p class="lede muted">This licence follows the Strange But True public-infrastructure pattern and is adapted for Straddie Clean Energy Superpower. It is written in plain English. It is not an open-source licence and it is not a public-domain release.</p>
    <div class="info-panel">
      <p><strong>Short version:</strong> the Straddie Clean Energy Superpower Public Licence welcomes public non-commercial learning, sharing, forking and community adaptation with attribution. Commercial rights, brand assets, generated images, close derivative products and extractive repackaging are reserved.</p>
      <p><a class="text-link" href="https://github.com/auraofintelligence/straddie-clean-energy-superpower/blob/main/LICENCE.md">Read the source licence file</a></p>
    </div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Allowed", "title": "What can people do?", "text": "View, share, clone, fork, study, reference and adapt this repo for personal, educational, community, artistic, documentary, environmental, research, local-planning, regenerative or other non-commercial public-interest purposes."},
        {"label": "Attribution", "title": "What should stay visible?", "text": "Credit Straddie Clean Energy Superpower and Aura of Intelligence where practical, and keep a clear trail to the original project and any changes made in a fork."},
        {"label": "Builder notes", "title": "Who owns local outputs?", "text": "Markdown notes or drafts created by visitors belong to the people or groups who write the answers. Inspect them before sharing, and keep private details private."},
        {"label": "Reserved", "title": "What is not freely granted?", "text": "Commercial use, close repackaging, brand use, generated images, page copy, planning material, calculator patterns and source-note structures are reserved unless written permission is given."},
        {"label": "Authority", "title": "What does the licence not grant?", "text": "It does not grant cultural permission, land access, engineering approval, environmental approval, energy-market rights, safety advice, financial advice or community consent."},
        {"label": "AI use", "title": "How can AI help without flattening it?", "text": "AI can use public pages and builder outputs as draft context, but should keep source limits, human authority, doubt, local consent and the right to disagree visible."},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner readable">
    <p class="section-label">Reality check</p>
    <h2>This is a sincere public workbench.</h2>
    <p>This project is provided as is. Any real clean-energy, water, pressure, hydrogen, reef, tunnel, construction, finance, safety, cultural or environmental pathway still needs the right human review and approval before action.</p>
    <p>Build wisely. Keep the questions visible. Look after the place, the people and the possibility.</p>
  </div>
</section>
"""


def builders_index_body() -> str:
    cards = []
    for builder in BUILDERS:
        cards.append(
            f'<a href="{e(builder["id"])}.html">'
            f'<p class="mini-label">Markdown builder</p><strong>{e(builder["title"])}</strong>'
            f'<p>{e(builder["purpose"])}</p><span class="text-link">Open form</span></a>'
        )
    return page_hero(by_id("builders")) + """
<section class="section">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Browser-only forms</p>
      <h2>Each builder makes a clean Markdown draft.</h2>
      <p class="lede muted">The forms save only in this browser while you type. Copy or download the Markdown when it becomes useful.</p>
    </div>
    <div class="builder-index">
""" + "".join(cards) + """
    </div>
  </div>
</section>
"""


def builder_body(builder: dict) -> str:
    fields = []
    for name, label, hint in builder["fields"]:
        fields.append(
            '<div class="field">'
            f'<label for="{e(name)}">{e(label)}</label>'
            f'<span>{e(hint)}</span>'
            f'<textarea id="{e(name)}" name="{e(name)}"></textarea>'
            '</div>'
        )

    definition = {
        "id": builder["id"],
        "title": builder["title"],
        "purpose": builder["purpose"],
        "filename": builder["filename"],
        "boundary": builder["boundary"],
        "next_step": builder["next_step"],
        "fields": [
            {"name": name, "label": label, "hint": hint}
            for name, label, hint in builder["fields"]
        ],
    }
    definition_json = json.dumps(definition).replace("</", "<\\/")
    page = {"title": builder["title"], "description": builder["purpose"]}

    return page_hero(page) + f"""
<section class="section">
  <div class="section-inner builder-layout">
    <div class="builder-panel">
      <p class="section-label">Working form</p>
      <form class="builder-form" data-builder-form>
        {''.join(fields)}
      </form>
      <div class="button-row">
        <button class="button primary" type="button" data-copy-markdown>Copy Markdown</button>
        <button class="button ghost" type="button" data-download-markdown>Download `.md`</button>
        <button class="button ghost" type="button" data-clear-form>Clear</button>
      </div>
      <p class="status-line" data-builder-status></p>
    </div>
    <div class="builder-panel">
      <p class="section-label">Markdown preview</p>
      <textarea class="markdown-output" data-markdown-output readonly></textarea>
    </div>
  </div>
</section>
<script id="builder-definition" type="application/json">{definition_json}</script>
<script src="../assets/js/form-builder.js"></script>
"""


def site_map_body() -> str:
    page_links = ''.join(
        f'<a class="card" href="{e(page["href"])}"><p class="mini-label">Page</p><h3>{e(page["title"])}</h3><p>{e(page["description"])}</p></a>'
        for page in PAGES
    )
    builder_links = ''.join(
        f'<a class="card" href="builders/{e(builder["id"])}.html"><p class="mini-label">Builder page</p><h3>{e(builder["title"])}</h3><p>{e(builder["purpose"])}</p></a>'
        for builder in BUILDERS
    )
    template_links = ''.join(
        f'<a class="card" href="builders/{e(builder["id"])}.md"><p class="mini-label">Markdown template</p><h3>{e(builder["title"])}</h3><p>{e(builder["filename"])}.md</p></a>'
        for builder in BUILDERS
    )
    return page_hero(by_id("site-map")) + f"""
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Public pages</p><h2>Site pages</h2></div>
    <div class="card-grid">{page_links}</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Builder pages</p><h2>Forms</h2></div>
    <div class="card-grid">{builder_links}</div>
  </div>
</section>
<section class="section">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Markdown templates</p><h2>Downloadable source templates</h2></div>
    <div class="card-grid">{template_links}</div>
  </div>
</section>
<section class="section deep-band">
  <div class="section-inner">
    <div class="section-heading"><p class="section-label">Source bridges</p><h2>Connected workbenches</h2></div>
    {repo_grid()}
  </div>
</section>
"""


BODY_RENDERERS = {
    "home": home_body,
    "options": options_body,
    "solar": solar_body,
    "storage": storage_body,
    "hydrogen": hydrogen_body,
    "sharing": sharing_body,
    "water": water_body,
    "marine": marine_body,
    "reefs": reefs_body,
    "wind": wind_body,
    "network": network_body,
    "wealth": wealth_body,
    "builders": builders_index_body,
    "boundaries": boundaries_body,
    "sources": sources_body,
    "licence": licence_body,
    "site-map": site_map_body,
}


def render_shell(page_id: str, title: str, description: str, body: str, path: str) -> str:
    base = "../" if "/" in path else ""
    canonical = BASE_URL + path
    css = base + f"assets/css/styles.css?v={ASSET_VERSION}"
    favicon = base + f"assets/img/favicon.svg?v={ASSET_VERSION}"
    site_data = base + f"assets/js/site-data.js?v={ASSET_VERSION}"
    site_nav = base + f"assets/js/site-nav.js?v={ASSET_VERSION}"
    image_path = hero_image(page_id)
    preload_image = base + f"{image_path}?v={ASSET_VERSION}"
    image = BASE_URL + image_path
    css_image = "../" + image_path.removeprefix("assets/") + f"?v={ASSET_VERSION}"
    return f"""<!doctype html>
<html lang="en-AU">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(description)}">
  <meta name="theme-color" content="#073337">
  <meta property="og:title" content="{e(title)} | {SITE_TITLE}">
  <meta property="og:description" content="{e(description)}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{e(canonical)}">
  <meta property="og:image" content="{e(image)}">
  <meta property="og:site_name" content="{SITE_TITLE}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{e(title)} | {SITE_TITLE}">
  <meta name="twitter:description" content="{e(description)}">
  <meta name="twitter:image" content="{e(image)}">
  <title>{e(title)} | {SITE_TITLE}</title>
  <link rel="canonical" href="{e(canonical)}">
  <link rel="icon" href="{favicon}" type="image/svg+xml">
  <link rel="preload" as="image" href="{e(preload_image)}" fetchpriority="high">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&family=Nunito+Sans:wght@700;800;900&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{css}">
</head>
<body data-page="{e(page_id)}" data-base="{base}" style="--page-hero-image: url('{e(css_image)}');">
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="site-header" data-site-header></header>
  <main id="main">
{body.strip()}
    <nav class="sequence-nav" data-sequence-nav aria-label="Previous and next pages"></nav>
  </main>
  <footer class="site-footer" data-site-footer></footer>
  <button class="back-to-top" type="button" data-back-to-top aria-label="Back to top">^</button>
  <script src="{site_data}"></script>
  <script src="{site_nav}"></script>
</body>
</html>
"""


def write(path: str, content: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(content, encoding="utf-8", newline="\n")


def builder_template(builder: dict) -> str:
    lines = [
        f"# {builder['title']}",
        "",
        f"Purpose: {builder['purpose']}",
        "",
        "Status: Working note for human review",
        "",
        "## Questions",
        "",
    ]
    for _name, label, hint in builder["fields"]:
        lines.extend([f"### {label}", "", f"Prompt: {hint}", "", "_Not answered yet._", ""])
    lines.extend(["## Boundaries", "", builder["boundary"], "", "## Next small step", "", builder["next_step"], ""])
    return "\n".join(lines)


def write_site_data() -> None:
    sequence = [{"id": page["id"], "label": page["label"], "href": page["href"]} for page in PAGES]
    builder_sequence = [
        {"id": f"builder-{builder['id']}", "label": builder["title"], "href": f"builders/{builder['id']}.html"}
        for builder in BUILDERS
    ]
    final_sequence = []
    for item in sequence:
        final_sequence.append(item)
        if item["id"] == "builders":
            final_sequence.extend(builder_sequence)

    nav = [{"id": page["id"], "label": page["label"], "href": page["href"]} for page in PAGES]
    by_page_id = {item["id"]: item for item in nav}
    nav_groups = [
        {"label": "Energy", "items": [by_page_id[item_id] for item_id in ["solar", "storage", "hydrogen", "sharing", "water", "marine", "reefs", "wind"]]},
        {"label": "Proof", "items": [by_page_id[item_id] for item_id in ["network", "wealth", "boundaries", "sources", "licence", "site-map"]]},
    ]
    nav_order = [
        {"type": "link", "item": by_page_id["home"]},
        {"type": "link", "item": by_page_id["options"]},
        {"type": "group", **nav_groups[0]},
        {"type": "link", "item": by_page_id["builders"]},
        {"type": "group", **nav_groups[1]},
    ]
    payload = {
        "nav": nav,
        "navGroups": nav_groups,
        "navOrder": nav_order,
        "sequence": final_sequence,
    }
    write("assets/js/site-data.js", "window.CLEAN_ENERGY_SITE = " + json.dumps(payload, indent=2) + ";\n")


def write_docs() -> None:
    lines = ["# Straddie Clean Energy Superpower Site Map", "", "## Pages"]
    for page in PAGES:
        lines.append(f"- [{page['title']}](../{page['href']}) - {page['description']}")
    lines.extend(["", "## Builders"])
    for builder in BUILDERS:
        lines.append(f"- [{builder['title']}](../builders/{builder['id']}.html) - {builder['purpose']}")
    lines.extend(["", "## Source Bridges"])
    for link in COMPANION_LINKS:
        lines.append(f"- [{link['title']}]({link['site']}) - [{link['title']} repo]({link['repo']})")
    write("docs/site-map.md", "\n".join(lines) + "\n")

    source_lines = [
        "# Source Notes",
        "",
        "This note records the public sources and nearby repos used for the first clean-energy atlas.",
        "",
        "## Local Working Inputs",
    ]
    for source in LOCAL_DRAFT_INPUTS:
        source_lines.append(f"- `{source['file']}` - {source['use']}")
    source_lines.extend([
        "",
        "## Style And Repo Research",
    ])
    for item in STYLE_RESEARCH:
        source_lines.append(f"- `{item['repo']}` - {item['learning']}")
    source_lines.extend(["", "## Public Sources"])
    for source in SOURCE_LINKS:
        source_lines.append(f"- [{source['title']}]({source['url']}) - {source['publisher']}: {source['use']}")
    source_lines.extend([
        "",
        "## Public Boundary",
        "",
        "This site is not an approval claim, engineering plan, cultural authority statement, legal advice, financial advice, fire-safety design or environmental approval.",
    ])
    write("docs/source-notes.md", "\n".join(source_lines) + "\n")


def write_readme() -> None:
    readme = f"""# {SITE_TITLE}

A public, question-led static site for exploring clean energy options for Minjerribah / North Stradbroke Island.

It covers:

- rooftop solar and batteries
- solar thermal and solar concentration
- sand batteries and other heat storage
- green hydrogen, desalination and brine-mineral recovery questions
- compressed air as a careful research lane
- power sharing, neighbourhood batteries and bill ledgers
- pumped-hydro lessons from Snowy, Wivenhoe, Kidston, Borumba and sand-island geography
- first-principles wave and tidal options without underwater blades
- reef, oyster, surf-bank, artificial-island and Sandworm tunnel-media questions
- fractal no-blade wind across vortex, flutter, rooftop and sensor-scale flows
- future pressure, carbon, sensing and response network questions
- links to maker-space, Sandworm, ferry terminal lab, Grants Lab, community wealth and Ready S.E.T. Trust Hub

## How it works

The source of truth is `tools/build_site.py`.

In simple terms:

1. The Python file stores the page list, builder list, source links and companion repo links.
2. Running it writes the public `.html` pages.
3. The builder pages let a visitor fill in a small form, preview Markdown, copy it, or download a `.md` file.
4. Hero images live in `assets/img/heroes/`.

## Optimise images

```powershell
python tools\\optimise_images.py
```

The script keeps the hero images as WebP and caps oversized files so the site loads faster on phones.

## Local build

```powershell
python tools\\build_site.py
```

Then open `index.html`, or run:

```powershell
python -m http.server 4179 --bind 127.0.0.1
```

## Public posture

This is an exploration workbench. It is not an approval claim, engineering design, cultural authority statement, environmental approval, legal advice, financial advice or fire-safety design.

## Licence

This repo uses the [Straddie Clean Energy Superpower Public Licence](LICENCE.md), a custom public-interest licence adapted from the Strange But True public-infrastructure pattern. Public non-commercial learning, sharing, forking and community adaptation are welcome with attribution. Commercial use, extractive repackaging and false endorsement are reserved.
"""
    write("README.md", readme)


def main() -> None:
    write_site_data()
    for page in PAGES:
        body = BODY_RENDERERS[page["id"]]()
        write(page["href"], render_shell(page["id"], page["title"], page["description"], body, page["href"]))

    for builder in BUILDERS:
        page_id = f"builder-{builder['id']}"
        href = f"builders/{builder['id']}.html"
        write(href, render_shell(page_id, builder["title"], builder["purpose"], builder_body(builder), href))
        write(f"builders/{builder['id']}.md", builder_template(builder))

    write_docs()
    write_readme()
    print(f"Built {len(PAGES)} pages and {len(BUILDERS)} builders.")


if __name__ == "__main__":
    main()
