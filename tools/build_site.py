from __future__ import annotations

import json
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE_TITLE = "Straddie Clean Energy Superpower"
BASE_URL = "https://auraofintelligence.github.io/straddie-clean-energy-superpower/"
ASSET_VERSION = "20260614-energy-superpower-v1"
DESCRIPTION = (
    "A self-sovereign public atlas for exploring clean energy options on Minjerribah / "
    "North Stradbroke Island: rooftop solar, solar thermal, sand batteries, compressed air, "
    "careful water-height storage, quiet marine energy, non-turbine wind and community wealth."
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
        "description": "A plain-English map of which energy options look near-term, which need bench tests, and which should stay as careful questions.",
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
        "description": "Could sand batteries, thermal stores and carefully reviewed compressed-air ideas turn local solar into useful hours after sunset?",
    },
    {
        "id": "water",
        "label": "Water height",
        "href": "water-height.html",
        "title": "Perched Lakes And Pumped-Hydro Questions",
        "description": "How could water-height storage be modelled without touching sensitive perched lakes, wetlands or cultural places?",
    },
    {
        "id": "marine",
        "label": "Marine",
        "href": "marine.html",
        "title": "Wave And Tidal Without Underwater Blades",
        "description": "Could wave pressure, tidal movement and reef-edge monitoring be explored without spinning underwater turbines?",
    },
    {
        "id": "wind",
        "label": "No-blade wind",
        "href": "wind.html",
        "title": "Non-Turbine Wind As A Small Test",
        "description": "Where could bladeless or vibration-based wind ideas help sensors, signs or small loads without becoming another visual or wildlife problem?",
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
        "description": "Consent, Country, safety, engineering review, marine life, pressure systems, fire systems and public/private data boundaries.",
    },
    {
        "id": "sources",
        "label": "Sources",
        "href": "sources.html",
        "title": "Source Trail",
        "description": "Official sources, connected repos and research notes used to scaffold this first clean energy atlas.",
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
    "options": "assets/img/heroes/home-energy.webp",
    "solar": "assets/img/heroes/home-energy.webp",
    "storage": "assets/img/heroes/makerspace-lab.webp",
    "water": "assets/img/heroes/ferry-gateway.webp",
    "marine": "assets/img/heroes/marine-energy.webp",
    "wind": "assets/img/heroes/community-wealth.webp",
    "network": "assets/img/heroes/ferry-gateway.webp",
    "wealth": "assets/img/heroes/wealth-hours.webp",
    "builders": "assets/img/heroes/builders.webp",
    "boundaries": "assets/img/heroes/sources.webp",
    "sources": "assets/img/heroes/sources.webp",
    "site-map": "assets/img/heroes/sources.webp",
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
        "use": "Keeps home solar and battery guidance tied to practical household questions and safety.",
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
        "title": "Broken Hill Advanced Compressed Air Energy Storage Demonstration",
        "url": "https://arena.gov.au/projects/hydrostor-broken-hill-advanced-compressed-air-energy-storage-demonstration/",
        "publisher": "ARENA",
        "use": "Shows compressed air as a serious long-duration storage pathway when geology, safety and economics line up.",
    },
    {
        "title": "Technical feasibility of CAES in an aquifer storage vessel",
        "url": "https://www.sandia.gov/files/ess/EESAT/2009_papers/Technical%20Feasibility%20of%20Compressed-Air%20Energy%20Storage%20in%20an%20Aquifer%20Storage%20Vessel.pdf",
        "publisher": "Sandia / Lawrence Berkeley National Laboratory authors",
        "use": "Keeps aquifer compressed-air language cautious because natural aquifer storage is difficult and unproven commercially.",
    },
    {
        "title": "Pumped Hydro Energy Storage",
        "url": "https://arena.gov.au/renewable-energy/pumped-hydro-energy-storage/",
        "publisher": "ARENA",
        "use": "Clarifies pumped hydro as water-height storage that normally uses turbines, reservoirs and careful siting.",
    },
    {
        "title": "Ocean energy",
        "url": "https://arena.gov.au/renewable-energy/ocean/",
        "publisher": "ARENA",
        "use": "Grounds wave and tidal energy as a broad family of technologies, not one settled device type.",
    },
    {
        "title": "Australian Wave Energy Atlas",
        "url": "https://arena.gov.au/projects/australian-wave-energy-atlas/",
        "publisher": "ARENA / CSIRO",
        "use": "Supports wave-resource mapping before any marine device or reef-edge idea gets proposed.",
    },
    {
        "title": "Review of wave energy converter power take-off systems",
        "url": "https://www.nrel.gov/docs/fy23osti/82807.pdf",
        "publisher": "NREL",
        "use": "Adds a research trail for non-standard wave power take-off concepts, including non-air-turbine pathways.",
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
        "use": "Keeps CO2 fire-suppression ideas behind strong life-safety controls and occupied-space warnings.",
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
        "use": "Draft concept fuel only. Adds wave and tidal options, solar resource framing, sand batteries, vanadium flow batteries, salt-gradient questions, oyster-crete reefs, sovereign wealth fund architecture, token risks and a risk-register habit.",
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
        "learning": "Keep trust, training, media and voluntary pathways clear. Do not treat people as labour inventory.",
    },
]


BUILDERS = [
    {
        "id": "entry-trail",
        "title": "Energy Entry Trail Builder",
        "purpose": "Choose a clean-energy doorway without needing to accept the whole atlas.",
        "filename": "straddie-energy-entry-trail",
        "boundary": "The note is an invitation, not an approval claim. People can use one part, reject another, or ask for better evidence.",
        "next_step": "Name one small thing that would make the option easier to test, explain or dismiss.",
        "fields": [
            ("doorway", "Which doorway feels alive?", "Rooftop solar, sand battery, compressed air, wave pressure, no-blade wind, pumped hydro model, grants, wealth, or another doorway."),
            ("question", "What is the plain question?", "Write it as a real question, not a conclusion."),
            ("useful_output", "What would be useful to leave with?", "A map, source list, cost question, safety review, workshop test, grant note or public explainer."),
        ],
    },
    {
        "id": "solar-rooftop-note",
        "title": "Rooftop Solar And Shade Note Builder",
        "purpose": "Turn a roof, car park, shade structure or public building into a first clean-energy question.",
        "filename": "straddie-rooftop-solar-note",
        "boundary": "A solar note still needs owner consent, electrical review, cyclone/wind loading, heritage and visual checks, fire access and network rules.",
        "next_step": "Check the roof or site, the owner pathway, the load profile and the public data trail before promising savings.",
        "fields": [
            ("site", "Which site or roof is being imagined?", "Home, business, school, club, ferry gateway, car park shade, community hall or concept only."),
            ("load", "What load should it help?", "Household bills, EV charging, kiosk, fridge, workshop, lighting, water pumping, battery charging or emergency backup."),
            ("storage", "Does storage matter here?", "Home battery, community battery, sand heat store, hot water, EV battery, no storage, or not sure."),
            ("checks", "What needs checking first?", "Owner, electrician, roof, fire access, insurance, network export, grant path, shading, public benefit or maintenance."),
        ],
    },
    {
        "id": "sand-air-storage",
        "title": "Sand And Air Storage Brief Builder",
        "purpose": "Compare sand-battery heat storage with compressed-air storage without mixing up their risks.",
        "filename": "straddie-sand-air-storage-brief",
        "boundary": "Thermal sand storage, compressed air, CO2, pressure vessels and fire systems are different systems. They need different safety reviews.",
        "next_step": "Choose one storage path and one harmless test before connecting it to a bigger network.",
        "fields": [
            ("need", "What energy problem is being solved?", "Evening power, heat, workshop process heat, emergency backup, ferry gateway load, water pumping, or seasonal resilience."),
            ("medium", "Which storage medium is in play?", "Hot sand, rock, hot water, compressed air vessel, mine/cavern idea, aquifer question, battery, or hybrid."),
            ("place", "Where could it live safely?", "Maker-space yard, service zone, ferry lab, existing industrial site, digital model, or not known."),
            ("review", "What is the review gate?", "Pressure safety, fire engineering, electrical, geology, heat insulation, public access, noise, permissions or economics."),
        ],
    },
    {
        "id": "marine-no-turbine",
        "title": "No-Underwater-Blades Marine Brief Builder",
        "purpose": "Draft a wave or tidal question that avoids underwater turbines and starts with marine life.",
        "filename": "straddie-no-turbine-marine-brief",
        "boundary": "Marine energy needs cultural authority, ecology review, navigation checks, fishers, sediment, storm survival and reversibility before physical testing.",
        "next_step": "Separate resource mapping, tabletop testing, digital simulation and any real-world marine activity.",
        "fields": [
            ("edge", "Which coast or water edge is being considered?", "Main Beach, Moreton Bay, ferry channel, Amity edge, reef model, wave tank, or concept only."),
            ("device", "What non-blade idea is being explored?", "Pressure bladder, oscillating body, pump to shore, membrane, sensor buoy, reef monitoring frame, or no device yet."),
            ("benefit", "What benefit should be tested?", "Power, desalination pressure, monitoring, reef learning, erosion knowledge, emergency signal, or public education."),
            ("avoid", "What should it avoid?", "Spinning blades, animal strike risk, noise, navigation conflict, permanent anchoring, cultural harm, sediment harm or visual clutter."),
        ],
    },
    {
        "id": "perched-lake-boundary",
        "title": "Perched Lake Boundary Builder",
        "purpose": "Keep pumped-hydro curiosity away from sensitive lakes until evidence and authority are clear.",
        "filename": "straddie-perched-lake-boundary",
        "boundary": "A perched lake is not a spare battery. Treat lakes, wetlands, springs and cultural places as boundaries first, not infrastructure sites.",
        "next_step": "Use a map, digital twin or off-river closed-loop model before naming any real water body.",
        "fields": [
            ("question", "What is the water-height question?", "Height difference, closed-loop reservoir, stormwater tank, seawater reservoir, model only, or educational demo."),
            ("sensitive_place", "What sensitive place must be protected?", "Perched lake, wetland, spring, national park, cultural place, habitat, public access or unknown layer."),
            ("alternative", "What alternative could be safer?", "Tank pair, quarry/mine void elsewhere, hilltop reservoir outside sensitive area, virtual model, or no build."),
            ("authority", "Who must be involved before this becomes real?", "Traditional Owners, park managers, hydrologist, ecologist, council, engineer, public safety or landholder."),
        ],
    },
    {
        "id": "wealth-grant-readiness",
        "title": "Wealth And Grant Readiness Builder",
        "purpose": "Turn an energy option into a local-benefit note that Grants Lab and mutual-care thinking can inspect.",
        "filename": "straddie-energy-wealth-grant-note",
        "boundary": "A community wealth note is not a financial product. It needs law, governance, consent, anti-fraud checks and human review.",
        "next_step": "Separate savings, revenue, risk, ownership, reporting evidence and who can say no.",
        "fields": [
            ("option", "Which energy option is being costed?", "Solar, battery, sand heat, compressed air, marine, wind sensor, demand response, training, or another option."),
            ("benefit", "Who benefits and how?", "Lower bills, local jobs, emergency resilience, training, co-op income, public data, mutual care or shared assets."),
            ("evidence", "What evidence would a grant need?", "Photos, quotes, energy data, letters, risk review, site consent, budgets, milestones or reporting plan."),
            ("governance", "How could value stay local?", "Trust, co-op, community fund, public dashboard, local contracts, training path, mutual reserve or not known."),
        ],
    },
    {
        "id": "boundary-check",
        "title": "Energy Boundary Check Builder",
        "purpose": "Name the safety, consent and evidence gates before an exciting energy idea gets loud.",
        "filename": "straddie-energy-boundary-check",
        "boundary": "If a boundary is unclear, slow down. A good clean-energy idea should survive review, correction and refusal.",
        "next_step": "Name the next reviewer and the stop rule.",
        "fields": [
            ("idea", "Which idea needs a boundary check?", "Name the option or project."),
            ("people", "Whose consent or authority matters?", "Traditional Owners, residents, landholder, council, business owner, emergency services, marine users, children or workers."),
            ("risk", "What could go wrong?", "Fire, pressure, heat, water, wildlife, culture, data, cost, noise, visual impact, maintenance, false claims or exclusion."),
            ("stop_rule", "What would make the idea pause?", "A safety concern, no consent, poor data, ecological risk, bad economics, unclear ownership or community refusal."),
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
            f'<p><strong>Review gate:</strong> {e(card["review"])}</p>'
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
      <p class="hero-lede">What if the island did not start with one giant answer, but with a stack of questions people can inspect: roofs first, storage next, marine edges carefully, local wealth clearly, and every bold idea held behind consent, safety and evidence?</p>
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
      <p class="lede muted">A clean-energy superpower does not need to mean a giant industrial build. It could mean roofs that work harder, public buildings that store heat, emergency nodes that stay alive, grants that fund real tests, and local people who can understand the system.</p>
    </div>
""" + card_grid([
        {"label": "Near term", "title": "How much rooftop solar is still untapped?", "text": "Could homes, shops, clubs, halls and shaded car parks become the first power station?"},
        {"label": "Storage", "title": "Can sand hold the evening?", "text": "Could solar heat or spare electricity charge sand, rock or hot-water stores for workshop heat, drying, cooking, water and community backup?"},
        {"label": "Pressure", "title": "Can compressed air stay safe and boring?", "text": "Could pressure storage be tested as a small engineering question before anyone talks about aquifers, networks or public tanks?"},
        {"label": "Water", "title": "Can pumped hydro stay on the map without touching sacred or fragile water?", "text": "Could only closed-loop, off-river or model-first options survive the first boundary check?"},
        {"label": "Marine", "title": "Can wave and tide work without underwater blades?", "text": "Could pressure, buoyancy, membranes, monitoring and simulation be explored before any ocean hardware gets wet?"},
        {"label": "Wealth", "title": "Who owns the upside?", "text": "Could savings, income, training and resilience feed local stewardship instead of leaking away?"},
    ]) + """
  </div>
</section>
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Why a repo?</p>
      <h2>Because the public map should be inspectable.</h2>
      <p class="lede muted">This site is not an energy plan, engineering design or endorsement claim. It is a public workbench for turning big clean-energy imagination into clear questions, source trails, builder forms and next-small-step notes.</p>
      <ol class="pathway">
        <li><p><strong>Ask the plain question.</strong> What problem does this option solve for residents, Country, business, ferry flow, emergency resilience or community wealth?</p></li>
        <li><p><strong>Find the smallest harmless test.</strong> Could a tabletop model, data check, roof audit, workshop bench or digital twin answer the first doubt?</p></li>
        <li><p><strong>Name the review gate.</strong> Who must check culture, ecology, pressure, fire, water, finance, safety and public claims before momentum builds?</p></li>
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
      <p class="lede muted">The point is not to rank dreams by glamour. The point is to sort them by testability, safety, consent, cost, local benefit and how quickly they can teach the next thing.</p>
    </div>
""" + option_grid([
        {"status": "Start now", "title": "Rooftop solar and batteries", "plain": "The most practical first layer: roofs, shade, small businesses, public buildings, hot water and batteries.", "question": "Which roofs and loads are obvious wins once the owner, electrician and network rules are checked?", "review": "Electrical, fire, roof, cyclone/wind loading, insurance and network export."},
        {"status": "Start small", "title": "Solar thermal and concentration", "plain": "Heat can be easier to store than electricity. Solar concentration might suit a workshop or industrial heat test before any big claim.", "question": "Where does the island need clean heat, not just clean electrons?", "review": "Heat safety, glare, fire risk, land use, maintenance and economics."},
        {"status": "Prototype", "title": "Sand batteries", "plain": "A sand battery is thermal storage: heat goes into sand or similar material and comes out as heat, steam, air or sometimes power through another system.", "question": "Could a maker-space bench test show what local heat storage is good for?", "review": "Insulation, hot surfaces, materials, fire, monitoring, output use and public access."},
        {"status": "Research lane", "title": "Compressed air", "plain": "Compressed air can store energy, but tanks, caverns, mines and aquifers are very different risk profiles.", "question": "Could container-scale pressure tests teach enough before anyone says aquifer?", "review": "Pressure-vessel law, compressor noise, heat, rupture risk, geology, emergency services and economics."},
        {"status": "Storage lane", "title": "Flow batteries and salt-gradient ideas", "plain": "The draft research brief names vanadium flow batteries and salt-gradient storage. They are useful to compare, but not the same as sand or air.", "question": "Which storage chemistry is safest, serviceable and most useful for island loads?", "review": "Lifecycle, cost, electrolyte safety, water sensitivity, maintenance, supply chain and end-of-life rules."},
        {"status": "Boundary first", "title": "Perched lake pumped hydro", "plain": "Pumped hydro uses height. Perched lakes, wetlands and cultural places should be treated as boundaries, not spare infrastructure.", "question": "Can the energy model be tested with tanks, maps or closed-loop alternatives instead?", "review": "Traditional Owner authority, hydrology, national park, ecology, water quality and public trust."},
        {"status": "Ocean lab", "title": "Wave and tidal without underwater blades", "plain": "If no underwater turbines is a hard boundary, the first lane is resource mapping, pressure devices, buoyancy, membranes and simulation.", "question": "What can wave and tide teach without adding animal-strike machinery?", "review": "Marine life, noise, navigation, anchoring, storms, sediment, fishers, visual impact and reversibility."},
        {"status": "Micro test", "title": "Non-turbine wind", "plain": "Bladeless or vibration-based wind is not a main power promise yet. It might still be useful for sensors, signs or education.", "question": "Where is wind useful enough for a tiny load without becoming clutter?", "review": "Noise, vibration, wildlife, visual impact, durability and real output."},
        {"status": "Systems question", "title": "Carbon capture and fire networks", "plain": "CO2 capture, compressed gas and fire suppression are not one simple network. The public page should keep them separate and safety-led.", "question": "What shared sensors, data, water, air or emergency-power layers are useful before CO2 enters the story?", "review": "Life safety, asphyxiation risk, confined spaces, standards, alarms, storage, access and liability."},
    ]) + """
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner split">
    <div>
      <p class="section-label">Simple rule</p>
      <h2>If it touches people, Country, water, pressure or fire, slow down.</h2>
      <p class="lede muted">Self-sovereign does not mean everyone builds whatever they want. It means people can inspect the idea, understand the tradeoffs, refuse bad terms, and help shape the next test.</p>
    </div>
    <div class="quote-panel">A clean-energy superpower starts as clean choices people can trust.</div>
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
      <p class="lede muted">Concentrated solar thermal can make high-grade heat and store it. On an island, the public-safe first question may be smaller: can clean heat dry, cook, sterilise, warm water, support a workshop or charge a sand store?</p>
    </div>
""" + card_grid([
        {"label": "Question", "title": "What needs heat?", "text": "Food, water, washing, repair, drying, ceramics, glass, community kitchen, disaster response or industrial process heat?"},
        {"label": "Question", "title": "Where does shade already make sense?", "text": "Could car parks, ferry waiting areas, market spaces and workshop yards carry solar shade before they carry big claims?"},
        {"label": "Question", "title": "What is the no-regret test?", "text": "Could one roof audit, load profile, hot-water upgrade or small solar-thermal demo make the next decision clearer?"},
        {"label": "Builder", "title": "Draft a rooftop note", "text": "Turn a roof or shade idea into a clean Markdown brief.", "href": "builders/solar-rooftop-note.html", "action": "Open builder"},
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
      <h2>Can clean power stay useful after sunset, storms and ferry peaks?</h2>
      <p class="lede muted">Batteries are only one answer. Heat, hot water, sand, rock, compressed air, EVs and demand shifting can all be part of the conversation if each one stays in its own safety lane.</p>
    </div>
    <div class="quote-panel">Do not merge systems just because they all feel futuristic. Hot sand, compressed air, CO2 and fire suppression each need their own rules.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Sand battery", "title": "Could sand store useful heat?", "text": "A sand battery is best understood as a heat store. It may suit water, drying, workshop heat, cooking or process heat before electric export."},
        {"label": "Flow battery", "title": "Would a vanadium flow battery be boring in the good way?", "text": "Flow batteries may suit longer daily cycling if the site, cost, maintenance and electrolyte supply chain make sense."},
        {"label": "Salt gradient", "title": "Should blue-energy ideas stay in the research drawer?", "text": "Salinity-gradient systems are interesting, but the first public step may be a source note, not hardware."},
        {"label": "Compressed air", "title": "Could pressure storage be container-scale first?", "text": "Compressed air can be serious storage, but vessels, mines, caverns and aquifers are not interchangeable."},
        {"label": "Aquifer caution", "title": "Should aquifers stay as research notes?", "text": "Natural aquifer CAES is difficult and site-specific. It belongs behind geology, water and safety review, not on a public promise board."},
        {"label": "CO2 boundary", "title": "Where does carbon capture actually belong?", "text": "Carbon capture means capture, compression, transport and durable storage or use. It should not be casually joined to emergency air or fire systems."},
        {"label": "Fire boundary", "title": "Could fire suppression be a separate safety layer?", "text": "CO2 fire systems can create asphyxiation hazards. Water, mist, detection, alarms and emergency power may be safer first topics."},
        {"label": "Builder", "title": "Draft a storage brief", "text": "Compare sand and air without blurring their safety cases.", "href": "builders/sand-air-storage.html", "action": "Open builder"},
    ]) + """
  </div>
</section>
"""


def water_body() -> str:
    return page_hero(by_id("water")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Water is not spare hardware</p>
      <h2>Could pumped-hydro curiosity protect the lakes by staying digital first?</h2>
      <p class="lede muted">Pumped hydro normally stores energy by moving water between high and low reservoirs and generating through turbines. Straddie's perched lakes, wetlands, springs and protected areas should be treated as boundaries first.</p>
      <ol class="pathway">
        <li><p><strong>Model height, do not name a lake.</strong> Start with maps, tanks, digital twins or off-river closed loops.</p></li>
        <li><p><strong>Protect water quality and Country.</strong> Sensitive lakes are not blank assets waiting for a clever use.</p></li>
        <li><p><strong>Ask what else gives the same benefit.</strong> Sand heat, batteries, demand shifting or mainland-linked storage may answer the need with less risk.</p></li>
      </ol>
    </div>
    <div class="quote-panel">The best pumped-hydro page might be the one that proves which places should never be touched.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
    <div class="section-heading">
      <p class="section-label">Safer first tests</p>
      <h2>How can water-height thinking teach without becoming a proposal?</h2>
    </div>
""" + card_grid([
        {"label": "Model", "title": "Tank-pair education rig", "text": "Could a small maker-space rig teach gravity storage without naming any real water body?"},
        {"label": "Digital twin", "title": "Height and sensitivity overlay", "text": "Could a public map show elevation, protected areas, water sensitivity and no-go zones together?"},
        {"label": "Alternative", "title": "Closed-loop elsewhere", "text": "If water-height storage ever matters, could non-sensitive closed-loop sites outside fragile areas be the only live branch?"},
        {"label": "Builder", "title": "Draft a lake boundary", "text": "Keep a water-height question from turning into a lake claim.", "href": "builders/perched-lake-boundary.html", "action": "Open builder"},
    ]) + """
  </div>
</section>
"""


def marine_body() -> str:
    return page_hero(by_id("marine")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">No underwater blades</p>
      <h2>Can wave and tidal energy be explored as pressure, movement and knowledge first?</h2>
      <p class="lede muted">If turbines are off the table, the first useful work is not a device sale. It is wave-resource mapping, marine-life review, tabletop models, pressure-to-shore questions and reversible sensor buoys.</p>
      <ul class="question-list">
        <li>What can be learned from waves before anything is installed?</li>
        <li>Could a device pump fluid or air to shore without placing spinning blades in animal pathways?</li>
        <li>Could reef-energy ideas also improve monitoring, habitat knowledge or erosion understanding?</li>
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
        {"label": "Question", "title": "What does the wave atlas say?", "text": "Could CSIRO and ARENA-style wave-resource mapping guide where to look and where not to look?"},
        {"label": "Question", "title": "Could pressure do the work?", "text": "Could wave motion pressurise air, water or a membrane, with conversion happening safely onshore or in a service zone?"},
        {"label": "Question", "title": "Could living breakwaters be habitat first?", "text": "Oyster-crete, reef modules and seagrass edges belong first as ecology and coastal-process questions, with energy only as a secondary possibility."},
        {"label": "Question", "title": "What does marine life need?", "text": "How do whales, dolphins, turtles, dugongs, fish, birds, currents, sediment and navigation shape the stop rules?"},
        {"label": "Builder", "title": "Draft a marine brief", "text": "Write a no-underwater-blades marine-energy question.", "href": "builders/marine-no-turbine.html", "action": "Open builder"},
    ]) + """
  </div>
</section>
"""


def wind_body() -> str:
    return page_hero(by_id("wind")) + """
<section class="section">
  <div class="section-inner split">
    <div>
      <p class="section-label">Small loads first</p>
      <h2>Could non-turbine wind be useful without pretending it is the main game?</h2>
      <p class="lede muted">Bladeless or vibration-based wind generators are interesting, but they should be treated as micro-generation experiments until real output, durability, noise and maintenance are clear.</p>
      <div class="tag-row">
        <span class="tag">Sensors</span>
        <span class="tag">Signs</span>
        <span class="tag">Education</span>
        <span class="tag">Remote trickle loads</span>
        <span class="tag">Wind-data logging</span>
      </div>
    </div>
    <div class="quote-panel">If solar can do the job quietly, the no-blade wind test needs a better reason than novelty.</div>
  </div>
</section>
<section class="section soft-band">
  <div class="section-inner">
""" + card_grid([
        {"label": "Question", "title": "Where is wind actually strong and useful?", "text": "Could one year of wind data tell us where a small device is worth testing?"},
        {"label": "Question", "title": "What load is tiny enough?", "text": "Could it power a sensor, sign, low-power radio, environmental monitor or learning kit?"},
        {"label": "Question", "title": "What would make it stop?", "text": "Poor output, noise, vibration, wildlife concern, visual clutter, storm damage or easier solar options."},
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
        <li><p><strong>Patient wealth only after trust.</strong> A fund, co-op or mutual reserve needs law, governance, receipts and consent.</p></li>
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
        {"label": "Question", "title": "Could Ready S.E.T. train people into the work?", "text": "Audits, installs, media, maintenance, grant reporting and safety checks can become learning pathways if trust is built first.", "href": "https://auraofintelligence.github.io/ready-set-co-op-trust-hub/", "action": "Open Trust Hub"},
        {"label": "Question", "title": "Could a sovereign wealth fund stay plain?", "text": "The draft brief imagines a fund, tokens and dashboards. The public-safe version starts with governance, receipts, audit, anti-fraud rules and the right to refuse."},
        {"label": "Builder", "title": "Draft a wealth and grant note", "text": "Turn an energy option into a local-benefit and grant-readiness question.", "href": "builders/wealth-grant-readiness.html", "action": "Open builder"},
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
      <h2>The bolder the energy idea, the simpler the boundary should be.</h2>
      <p class="lede muted">Boundaries do not kill imagination. They stop imagination from becoming extraction, unsafe pressure, false endorsement, private-data capture or ecological harm.</p>
    </div>
""" + card_grid([
        {"label": "Country", "title": "Who holds authority here?", "text": "Public pages should not imply approval, representation or cultural authority that has not been granted."},
        {"label": "Water", "title": "What water must not be treated as infrastructure?", "text": "Perched lakes, wetlands, springs and protected water places begin as no-go questions."},
        {"label": "Marine", "title": "What does sea life need?", "text": "No underwater blades is only one boundary. Noise, anchoring, sediment, navigation and reversibility matter too."},
        {"label": "Pressure", "title": "What belongs behind engineering review?", "text": "Compressed air, CO2, pressure vessels, heat stores and fire systems need formal safety logic before public build talk."},
        {"label": "Finance", "title": "What stops tokens becoming hype?", "text": "Any token, app, ledger or community dividend idea needs law, cybersecurity, plain accounting, consent and an analog fallback."},
        {"label": "Data", "title": "What stays private?", "text": "Household loads, bills, vulnerable people, cultural knowledge and business data should not become public dashboards by accident."},
        {"label": "Builder", "title": "Run a boundary check", "text": "Name the consent, safety and evidence gates before the idea gets loud.", "href": "builders/boundary-check.html", "action": "Open builder"},
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
      <h2>Sources help ask better questions. They do not create permission.</h2>
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
      <p class="section-label">Draft form</p>
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
    "water": water_body,
    "marine": marine_body,
    "wind": wind_body,
    "network": network_body,
    "wealth": wealth_body,
    "builders": builders_index_body,
    "boundaries": boundaries_body,
    "sources": sources_body,
    "site-map": site_map_body,
}


def render_shell(page_id: str, title: str, description: str, body: str, path: str) -> str:
    base = "../" if "/" in path else ""
    canonical = BASE_URL + path
    css = base + f"assets/css/styles.css?v={ASSET_VERSION}"
    favicon = base + "assets/img/favicon.svg"
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
        "Status: Draft for human review",
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
        {"label": "Energy", "items": [by_page_id[item_id] for item_id in ["solar", "storage", "water", "marine", "wind"]]},
        {"label": "Proof", "items": [by_page_id[item_id] for item_id in ["network", "wealth", "boundaries", "sources", "site-map"]]},
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
        "## Local Draft Inputs",
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
- compressed air as a careful research lane
- perched-lake pumped-hydro boundaries
- wave and tidal options without underwater blades
- non-turbine wind as a small-load experiment
- carbon capture and fire-suppression boundaries
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
