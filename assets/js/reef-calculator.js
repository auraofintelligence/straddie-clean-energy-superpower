(function () {
  const root = document.querySelector("[data-reef-calculator]");
  if (!root) return;

  const number = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 0 });
  const decimal = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 2 });
  const preciseDecimal = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 3 });
  const oneDecimal = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 1 });
  const FORMING_FACTOR = 1.15;
  const SANDMASS_TONNES_PER_M3 = 1.6;
  const BESSER_LENGTH_M = 0.39;
  const BESSER_WIDTH_M = 0.19;
  const BESSER_HEIGHT_M = 0.19;
  const BESSER_ENVELOPE_M3 = BESSER_LENGTH_M * BESSER_WIDTH_M * BESSER_HEIGHT_M;

  const inputs = {
    diameter: root.querySelector('[data-calc-input="diameter"]'),
    weeklyAdvance: root.querySelector('[data-calc-input="weeklyAdvance"]'),
    weeks: root.querySelector('[data-calc-input="weeks"]'),
    reefShare: root.querySelector('[data-calc-input="reefShare"]'),
    modulePreset: root.querySelector('[data-calc-input="modulePreset"]'),
    moduleSize: root.querySelector('[data-calc-input="moduleSize"]'),
    scenarioScale: root.querySelectorAll('[data-calc-input="scenarioScale"]'),
    focus: root.querySelector('[data-calc-input="focus"]'),
    example: root.querySelector('[data-calc-input="example"]'),
  };
  const exportButton = root.querySelector("[data-export-reef-markdown]");
  const markdownPreview = root.querySelector("[data-reef-markdown-preview]");
  let latestState = null;

  const output = (name, value) => {
    const target = root.querySelector(`[data-calc-out="${name}"]`);
    if (target) target.textContent = value;
  };

  const metres3 = (value) => {
    if (Math.abs(value) < 1) return `${preciseDecimal.format(value)} m3`;
    if (Math.abs(value) < 100) return `${decimal.format(value)} m3`;
    return `${number.format(Math.round(value))} m3`;
  };

  const metres2 = (value) => {
    if (Math.abs(value) < 100) return `${decimal.format(value)} m2`;
    return `${number.format(Math.round(value))} m2`;
  };

  const tonnes = (value) => {
    if (Math.abs(value) < 100) return `${decimal.format(value)} t`;
    return `${number.format(Math.round(value))} t`;
  };

  const count = (value) => number.format(Math.max(0, Math.round(value)));
  const count1 = (value) => oneDecimal.format(Math.max(0, value));
  const setCount = (value) => value >= 10 ? count(value) : count1(value);
  const raw = (value, digits = 3) => Number(value.toFixed(digits)).toString();
  const singularUnit = {
    "pieces or cells": "piece or cell",
    "reef cells": "reef cell",
    "shoreline cells": "shoreline cell",
    "geometry cells": "geometry cell",
    "unique blocks": "unique block",
    "civic pieces": "civic piece",
    "home pieces": "home piece",
    "dune pieces": "dune piece",
    "landform cells": "landform cell",
  };
  const unitCount = (value, unit) => {
    const rounded = Math.max(0, Math.round(value));
    const label = rounded === 1 ? (singularUnit[unit] || unit) : unit;
    return `${number.format(rounded)} ${label}`;
  };
  const countLabel = (value, singular, plural) => {
    const rounded = Math.max(0, Math.round(value));
    return `${number.format(rounded)} ${rounded === 1 ? singular : plural}`;
  };

  const formatAdvance = (metresPerWeek) => {
    if (metresPerWeek >= 1000) return `${decimal.format(metresPerWeek / 1000)} km/week`;
    return `${number.format(metresPerWeek)} m/week`;
  };

  const formatDuration = (hours) => {
    if (hours < 24) return `${decimal.format(hours)} h`;
    return `${decimal.format(hours / 24)} days`;
  };

  const volumeScale = (value) => {
    const wheelbarrows = value / 0.1;
    const concreteTrucks = value / 6;
    const containers = value / 33;
    const pools = value / 2500;

    if (value < 0.15) return `about ${count1(wheelbarrows)} wheelbarrow loads`;
    if (value < 3) return `about ${count(wheelbarrows)} wheelbarrow loads`;
    if (value < 8) return `about ${count(wheelbarrows)} wheelbarrow loads or ${countLabel(concreteTrucks, "concrete-truck load", "concrete-truck loads")}`;
    if (value < 33) return `about ${countLabel(concreteTrucks, "concrete-truck load", "concrete-truck loads")}`;
    if (value < 80) return `about ${countLabel(concreteTrucks, "concrete-truck load", "concrete-truck loads")} or ${countLabel(containers, "twenty-foot container", "twenty-foot containers")}`;
    if (value < 1200) return `about ${countLabel(containers, "twenty-foot container", "twenty-foot containers")} or ${countLabel(concreteTrucks, "concrete-truck load", "concrete-truck loads")}`;
    return `about ${countLabel(containers, "twenty-foot container", "twenty-foot containers")}, ${countLabel(concreteTrucks, "concrete-truck load", "concrete-truck loads")} or ${count1(pools)} Olympic pools`;
  };

  const weightScale = (value) => {
    const truckloads = value / 20;
    if (value < 20) return `about ${count1(truckloads)} loaded 20 tonne tip trucks`;
    return `about ${count(truckloads)} loaded 20 tonne tip trucks`;
  };

  const makeList = (label, items) => {
    return `<div><strong>${label}</strong><p>${items.join(", ")}</p></div>`;
  };

  const scaleBands = {
    minimal: {
      label: "Minimal",
      multiplier: 0.55,
      note: "first useful sketch",
    },
    medium: {
      label: "Medium",
      multiplier: 1,
      note: "current middle sketch",
    },
    large: {
      label: "Large",
      multiplier: 2.2,
      note: "fuller public build",
    },
  };

  const constructionScenarios = [
    {
      label: "Bus stop",
      title: "Covered bus stop",
      volume: 8,
      text: "shade bases, seats, battery plinth, cable channels and movable edges",
      parts: [
        { label: "shade bases", volume: 2.2 },
        { label: "bench and waiting seats", volume: 1.4 },
        { label: "battery or service plinth", volume: 1.3 },
        { label: "cable-channel pieces", volume: 1.1 },
        { label: "movable edge pieces", volume: 2 },
      ],
    },
    {
      label: "Jetty",
      title: "Jetty footing set",
      volume: 30,
      text: "footing caps, service runs, spare blocks and inspection lids",
      parts: [
        { label: "footing caps", volume: 12 },
        { label: "service-run blocks", volume: 7 },
        { label: "spare repair blocks", volume: 5 },
        { label: "inspection lids", volume: 6 },
      ],
    },
    {
      label: "School / hall",
      title: "School or community upgrade",
      volume: 45,
      text: "ramps, shade edges, seating, storage and visible service blocks",
      parts: [
        { label: "ramp and access pieces", volume: 10 },
        { label: "shade-edge blocks", volume: 8 },
        { label: "outdoor seating", volume: 10 },
        { label: "storage edges", volume: 7 },
        { label: "visible service blocks", volume: 10 },
      ],
    },
    {
      label: "Home",
      title: "Small housing shell",
      volume: 90,
      text: "raised core, wet-area walls, service spine and modular porch pieces",
      parts: [
        { label: "raised floor or core", volume: 30 },
        { label: "wet-area wall blocks", volume: 18 },
        { label: "service spine", volume: 12 },
        { label: "modular porch pieces", volume: 16 },
        { label: "adaptable spare pieces", volume: 14 },
      ],
    },
    {
      label: "Ballow Road",
      title: "Sand sports clubhouse",
      volume: 120,
      text: "clubhouse walls, shade, counters, storage, screens and robot-readable block IDs",
      parts: [
        { label: "clubhouse wall blocks", volume: 40 },
        { label: "shade structure bases", volume: 22 },
        { label: "counter and kiosk pieces", volume: 12 },
        { label: "storage modules", volume: 16 },
        { label: "screen and media plinths", volume: 18 },
        { label: "robot-readable spare blocks", volume: 12 },
      ],
    },
    {
      label: "Ferry",
      title: "Ferry terminal upgrade",
      volume: 180,
      text: "arrival edges, seats, lighting bases, wayfinding plinths and service corridors",
      parts: [
        { label: "arrival-edge blocks", volume: 40 },
        { label: "public seats", volume: 25 },
        { label: "lighting bases", volume: 18 },
        { label: "wayfinding plinths", volume: 22 },
        { label: "service corridor pieces", volume: 50 },
        { label: "reconfiguration reserve", volume: 25 },
      ],
    },
    {
      label: "Steep seating",
      title: "Stadium seating on slopes",
      volume: 250,
      text: "terraced seating, retaining ribs, handrail bases and drain or service voids",
      parts: [
        { label: "terraced seating blocks", volume: 100 },
        { label: "retaining ribs", volume: 55 },
        { label: "handrail bases", volume: 20 },
        { label: "drain and service void modules", volume: 45 },
        { label: "repair and reconfiguration pieces", volume: 30 },
      ],
    },
    {
      label: "Rock / living edge",
      title: "Rock wall or living edge",
      volume: 320,
      text: "heavy interlocks, toe pieces, planted pockets, access steps and monitoring points",
      parts: [
        { label: "heavy interlock blocks", volume: 100 },
        { label: "toe pieces", volume: 70 },
        { label: "planted pockets", volume: 55 },
        { label: "access steps", volume: 40 },
        { label: "monitoring-point blocks", volume: 20 },
        { label: "future rearrangement reserve", volume: 35 },
      ],
    },
  ];

  const scenarioLibraries = {
    mixed: [
      {
        label: "Oyster reach",
        title: "Oyster nursery reach",
        volume: 36,
        text: "settlement tiles, shell baskets, marker blocks and monitoring ledges",
        parts: [
          { label: "settlement tiles", volume: 8 },
          { label: "shell baskets", volume: 10 },
          { label: "marker blocks", volume: 12 },
          { label: "monitoring ledges", volume: 6 },
        ],
      },
      {
        label: "Living edge",
        title: "Living shoreline pocket",
        volume: 70,
        text: "toe cells, planting pockets, access edges, sensor points and repair reserve",
        parts: [
          { label: "toe cells", volume: 18 },
          { label: "planting pockets", volume: 16 },
          { label: "access edges", volume: 20 },
          { label: "sensor points", volume: 10 },
          { label: "repair reserve", volume: 6 },
        ],
      },
      {
        label: "Surf",
        title: "Surf-bank test patch",
        volume: 120,
        text: "survey marks, adjustable facets, sand-hold ribs, sensor anchors and reset pieces",
        parts: [
          { label: "survey marks", volume: 24 },
          { label: "adjustable facets", volume: 26 },
          { label: "sand-hold ribs", volume: 40 },
          { label: "sensor anchors", volume: 18 },
          { label: "reset pieces", volume: 12 },
        ],
      },
      constructionScenarios[0],
      constructionScenarios[3],
      constructionScenarios[5],
      {
        label: "Civic circle",
        title: "Community meeting circle",
        volume: 32,
        text: "seat arcs, centre markers, shade-footing pieces and movable edges",
        parts: [
          { label: "seat arcs", volume: 8 },
          { label: "centre markers", volume: 10 },
          { label: "shade-footing pieces", volume: 8 },
          { label: "movable edges", volume: 6 },
        ],
      },
      {
        label: "Home run",
        title: "Silicate home-product run",
        volume: 16,
        text: "tiles, pavers, bench pieces, privacy blocks and repair samples",
        parts: [
          { label: "tiles", volume: 4 },
          { label: "pavers", volume: 3 },
          { label: "bench pieces", volume: 4 },
          { label: "privacy blocks", volume: 3 },
          { label: "repair samples", volume: 2 },
        ],
      },
    ],
    oyster: [
      {
        label: "Hatchery edge",
        title: "School oyster nursery trays",
        volume: 6,
        text: "tray bases, shell holders, learning markers and small water-quality mounts",
        parts: [
          { label: "tray bases", volume: 1.5 },
          { label: "shell holders", volume: 2 },
          { label: "learning markers", volume: 1.5 },
          { label: "water-quality mounts", volume: 1 },
        ],
      },
      {
        label: "Community set",
        title: "Community oyster basket set",
        volume: 28,
        text: "basket frames, shell media, edge weights and monitoring tags",
        parts: [
          { label: "basket frames", volume: 8 },
          { label: "shell media", volume: 8 },
          { label: "edge weights", volume: 7 },
          { label: "monitoring tags", volume: 5 },
        ],
      },
      {
        label: "Reef patch",
        title: "Shellfish reef patch",
        volume: 90,
        text: "low reef cells, shell bags, settlement ribs, current gaps and sensor mounts",
        parts: [
          { label: "low reef cells", volume: 20 },
          { label: "shell bags", volume: 24 },
          { label: "settlement ribs", volume: 26 },
          { label: "current gaps", volume: 12 },
          { label: "sensor mounts", volume: 8 },
        ],
      },
      {
        label: "Bay chain",
        title: "Bay habitat chain",
        volume: 220,
        text: "linked reef patches, boat-safe markers, fish refuge and water-quality stations",
        parts: [
          { label: "linked reef patches", volume: 45 },
          { label: "boat-safe markers", volume: 60 },
          { label: "fish refuge", volume: 55 },
          { label: "water-quality stations", volume: 30 },
          { label: "repair reserve", volume: 30 },
        ],
      },
      {
        label: "Clean bay",
        title: "Moreton Bay cleaning trial",
        volume: 420,
        text: "oyster habitat, sampling lanes, community access markers and long-term comparison cells",
        parts: [
          { label: "oyster habitat", volume: 90 },
          { label: "sampling lanes", volume: 110 },
          { label: "access markers", volume: 95 },
          { label: "comparison cells", volume: 65 },
          { label: "repair reserve", volume: 60 },
        ],
      },
      {
        label: "Working water",
        title: "Oyster lease support field",
        volume: 650,
        text: "farm edges, nursery racks, navigation markers, maintenance pads and habitat shoulders",
        parts: [
          { label: "farm edges", volume: 150 },
          { label: "nursery racks", volume: 160 },
          { label: "navigation markers", volume: 140 },
          { label: "maintenance pads", volume: 100 },
          { label: "habitat shoulders", volume: 100 },
        ],
      },
    ],
    living: [
      {
        label: "Path edge",
        title: "Eroded path edge pocket",
        volume: 18,
        text: "toe pieces, planting shelves, access lips and photo markers",
        parts: [
          { label: "toe pieces", volume: 5 },
          { label: "planting shelves", volume: 4 },
          { label: "access lips", volume: 5 },
          { label: "photo markers", volume: 4 },
        ],
      },
      {
        label: "Shore pocket",
        title: "Living shoreline pocket",
        volume: 70,
        text: "low edge cells, planting pockets, wrack catchers, visitor edges and repair pieces",
        parts: [
          { label: "low edge cells", volume: 18 },
          { label: "planting pockets", volume: 12 },
          { label: "wrack catchers", volume: 20 },
          { label: "visitor edges", volume: 10 },
          { label: "repair pieces", volume: 10 },
        ],
      },
      {
        label: "Nursery edge",
        title: "Saltmarsh and mangrove nursery edge",
        volume: 120,
        text: "nursery shelves, tidal gaps, sediment traps, access nodes and monitoring blocks",
        parts: [
          { label: "nursery shelves", volume: 25 },
          { label: "tidal gaps", volume: 22 },
          { label: "sediment traps", volume: 30 },
          { label: "access nodes", volume: 18 },
          { label: "monitoring blocks", volume: 25 },
        ],
      },
      constructionScenarios[7],
      {
        label: "Storm reach",
        title: "Storm-recovery shoreline reach",
        volume: 620,
        text: "living toe, planted pockets, public access, monitoring, reset reserve and learning markers",
        parts: [
          { label: "living toe", volume: 130 },
          { label: "planted pockets", volume: 140 },
          { label: "public access", volume: 120 },
          { label: "monitoring", volume: 90 },
          { label: "reset reserve", volume: 80 },
          { label: "learning markers", volume: 60 },
        ],
      },
    ],
    surf: [
      {
        label: "Tank model",
        title: "Wave tank geometry kit",
        volume: 2.5,
        text: "mini facets, sand trays, flow markers and camera mounts",
        parts: [
          { label: "mini facets", volume: 0.6 },
          { label: "sand trays", volume: 0.5 },
          { label: "flow markers", volume: 0.8 },
          { label: "camera mounts", volume: 0.6 },
        ],
      },
      {
        label: "Point marks",
        title: "Point-break field marker set",
        volume: 15,
        text: "shore markers, removable survey blocks, sand-movement tags and camera points",
        parts: [
          { label: "shore markers", volume: 4 },
          { label: "survey blocks", volume: 3 },
          { label: "sand-movement tags", volume: 5 },
          { label: "camera points", volume: 3 },
        ],
      },
      {
        label: "Trial patch",
        title: "Surf-bank trial patch",
        volume: 120,
        text: "reef facets, toe ribs, sand-hold pockets, sensor anchors and reset modules",
        parts: [
          { label: "reef facets", volume: 25 },
          { label: "toe ribs", volume: 30 },
          { label: "sand-hold pockets", volume: 35 },
          { label: "sensor anchors", volume: 20 },
          { label: "reset modules", volume: 10 },
        ],
      },
      {
        label: "Learning reach",
        title: "Superbank learning reach",
        volume: 480,
        text: "shape cells, current windows, sand feed markers, surf camera bases, reset stock and safety signs",
        parts: [
          { label: "shape cells", volume: 120 },
          { label: "current windows", volume: 90 },
          { label: "sand feed markers", volume: 100 },
          { label: "surf camera bases", volume: 80 },
          { label: "reset stock", volume: 50 },
          { label: "signage bases", volume: 40 },
        ],
      },
      {
        label: "Point field",
        title: "Point-break digital-twin field",
        volume: 1200,
        text: "mapped facets, seasonal variants, marker corridors, storm-reset cells and sensor plinths",
        parts: [
          { label: "mapped facets", volume: 260 },
          { label: "seasonal variants", volume: 240 },
          { label: "marker corridors", volume: 260 },
          { label: "storm-reset cells", volume: 180 },
          { label: "sensor plinths", volume: 160 },
          { label: "learning reserve", volume: 100 },
        ],
      },
    ],
    construction: constructionScenarios,
    meeting: [
      {
        label: "Small circle",
        title: "Small yarn circle",
        volume: 10,
        text: "seat stones, centre marker, shade-footing points and movable edges",
        parts: [
          { label: "seat stones", volume: 3 },
          { label: "centre marker", volume: 2 },
          { label: "shade-footing points", volume: 3 },
          { label: "movable edges", volume: 2 },
        ],
      },
      {
        label: "Meeting place",
        title: "Community meeting circle",
        volume: 32,
        text: "seat arcs, centre pieces, shade bases, story markers and spare movable blocks",
        parts: [
          { label: "seat arcs", volume: 8 },
          { label: "centre pieces", volume: 8 },
          { label: "shade bases", volume: 7 },
          { label: "story markers", volume: 5 },
          { label: "spare movable blocks", volume: 4 },
        ],
      },
      {
        label: "Market ring",
        title: "Market day sitting ring",
        volume: 65,
        text: "stall edges, seats, power-safe plinths, shade feet and gathering markers",
        parts: [
          { label: "stall edges", volume: 16 },
          { label: "seats", volume: 14 },
          { label: "power-safe plinths", volume: 15 },
          { label: "shade feet", volume: 12 },
          { label: "gathering markers", volume: 8 },
        ],
      },
      {
        label: "Listening slope",
        title: "Amphitheatre listening slope",
        volume: 180,
        text: "terrace blocks, step edges, handrail bases, speaker plinths and reconfiguration reserve",
        parts: [
          { label: "terrace blocks", volume: 50 },
          { label: "step edges", volume: 40 },
          { label: "handrail bases", volume: 35 },
          { label: "speaker plinths", volume: 25 },
          { label: "reconfiguration reserve", volume: 30 },
        ],
      },
      {
        label: "Festival field",
        title: "Island festival civic field",
        volume: 360,
        text: "seat fields, shade bases, stage edges, service channels, wayfinding and repair reserve",
        parts: [
          { label: "seat fields", volume: 90 },
          { label: "shade bases", volume: 75 },
          { label: "stage edges", volume: 70 },
          { label: "service channels", volume: 55 },
          { label: "wayfinding", volume: 40 },
          { label: "repair reserve", volume: 30 },
        ],
      },
    ],
    homes: [
      {
        label: "Recipe tray",
        title: "Silicate tile sample run",
        volume: 1.5,
        text: "recipe tiles, finish samples, repair coupons, colour tests and resident notes",
        parts: [
          { label: "recipe tiles", volume: 0.3 },
          { label: "finish samples", volume: 0.3 },
          { label: "repair coupons", volume: 0.4 },
          { label: "colour tests", volume: 0.3 },
          { label: "resident notes", volume: 0.2 },
        ],
      },
      {
        label: "Wet area",
        title: "Bathroom or wet-area tile set",
        volume: 8,
        text: "wall tiles, floor tiles, splashback panels, drain edges and spare repair pieces",
        parts: [
          { label: "wall tiles", volume: 2 },
          { label: "floor tiles", volume: 2 },
          { label: "splashback panels", volume: 1.5 },
          { label: "drain edges", volume: 1.5 },
          { label: "repair pieces", volume: 1 },
        ],
      },
      {
        label: "Home pieces",
        title: "Bench and shelf set",
        volume: 16,
        text: "bench slabs, shelves, sill blocks, garden pavers and repair samples",
        parts: [
          { label: "bench slabs", volume: 4 },
          { label: "shelves", volume: 3 },
          { label: "sill blocks", volume: 3 },
          { label: "garden pavers", volume: 3 },
          { label: "repair samples", volume: 3 },
        ],
      },
      {
        label: "Privacy wall",
        title: "Glass and privacy block upgrade",
        volume: 30,
        text: "privacy blocks, breeze blocks, service trims, edge pieces and spare modules",
        parts: [
          { label: "privacy blocks", volume: 8 },
          { label: "breeze blocks", volume: 6 },
          { label: "service trims", volume: 6 },
          { label: "edge pieces", volume: 5 },
          { label: "spare modules", volume: 5 },
        ],
      },
      {
        label: "House fit-out",
        title: "Small house fit-out kit",
        volume: 70,
        text: "wet-area pieces, porch pavers, service blocks, shade feet, storage and repairs",
        parts: [
          { label: "wet-area pieces", volume: 18 },
          { label: "porch pavers", volume: 14 },
          { label: "service blocks", volume: 12 },
          { label: "shade feet", volume: 10 },
          { label: "storage", volume: 8 },
          { label: "repairs", volume: 8 },
        ],
      },
      {
        label: "Neighbourhood",
        title: "Neighbourhood product library",
        volume: 140,
        text: "tiles, pavers, counters, repair kits, shade pieces and resident-request batches",
        parts: [
          { label: "tiles", volume: 30 },
          { label: "pavers", volume: 25 },
          { label: "counters", volume: 25 },
          { label: "repair kits", volume: 20 },
          { label: "shade pieces", volume: 20 },
          { label: "resident-request batches", volume: 20 },
        ],
      },
    ],
    dune: [
      {
        label: "Access edge",
        title: "Access track sand ladder",
        volume: 20,
        text: "ladder rungs, side lips, vegetation guards, repair pads and photo markers",
        parts: [
          { label: "ladder rungs", volume: 5 },
          { label: "side lips", volume: 4 },
          { label: "vegetation guards", volume: 5 },
          { label: "repair pads", volume: 3 },
          { label: "photo markers", volume: 3 },
        ],
      },
      {
        label: "Dune foot",
        title: "Stable dune foot edge",
        volume: 65,
        text: "soft toe cells, sand catchers, planting pockets, access gaps and monitoring points",
        parts: [
          { label: "soft toe cells", volume: 16 },
          { label: "sand catchers", volume: 12 },
          { label: "planting pockets", volume: 15 },
          { label: "access gaps", volume: 12 },
          { label: "monitoring points", volume: 10 },
        ],
      },
      {
        label: "Lookout toe",
        title: "Viewing platform toe",
        volume: 120,
        text: "platform feet, access steps, planted pockets, service sleeves and repair pieces",
        parts: [
          { label: "platform feet", volume: 30 },
          { label: "access steps", volume: 25 },
          { label: "planted pockets", volume: 25 },
          { label: "service sleeves", volume: 20 },
          { label: "repair pieces", volume: 20 },
        ],
      },
      {
        label: "Storm repair",
        title: "Storm blowout repair kit",
        volume: 240,
        text: "sand-catch cells, walkway edges, vegetation shelves, survey markers, reset stock and access controls",
        parts: [
          { label: "sand-catch cells", volume: 55 },
          { label: "walkway edges", volume: 45 },
          { label: "vegetation shelves", volume: 50 },
          { label: "survey markers", volume: 35 },
          { label: "reset stock", volume: 30 },
          { label: "access controls", volume: 25 },
        ],
      },
      {
        label: "Dune corridor",
        title: "Stable dune and surf-access corridor",
        volume: 520,
        text: "access mats, toe cells, revegetation shelves, public edges, monitoring and repair reserve",
        parts: [
          { label: "access mats", volume: 120 },
          { label: "toe cells", volume: 90 },
          { label: "revegetation shelves", volume: 100 },
          { label: "public edges", volume: 80 },
          { label: "monitoring", volume: 70 },
          { label: "repair reserve", volume: 60 },
        ],
      },
    ],
    island: [
      {
        label: "Model cell",
        title: "Platform model cell",
        volume: 25,
        text: "settlement trays, edge markers, habitat pockets, sensor points and public scale model",
        parts: [
          { label: "settlement trays", volume: 5 },
          { label: "edge markers", volume: 6 },
          { label: "habitat pockets", volume: 6 },
          { label: "sensor points", volume: 4 },
          { label: "public scale model", volume: 4 },
        ],
      },
      {
        label: "Sensor islet",
        title: "Sensor islet or platform question",
        volume: 100,
        text: "platform cells, edge protection, landing points, sensors and reset stock",
        parts: [
          { label: "platform cells", volume: 25 },
          { label: "edge protection", volume: 20 },
          { label: "landing points", volume: 25 },
          { label: "sensors", volume: 15 },
          { label: "reset stock", volume: 15 },
        ],
      },
      {
        label: "Sand cay",
        title: "Artificial sand-cay test field",
        volume: 500,
        text: "core media, edge cells, habitat pockets, access marker lanes, settlement markers and repair reserve",
        parts: [
          { label: "core media", volume: 120 },
          { label: "edge cells", volume: 100 },
          { label: "habitat pockets", volume: 100 },
          { label: "access marker lanes", volume: 80 },
          { label: "settlement markers", volume: 60 },
          { label: "repair reserve", volume: 40 },
        ],
      },
      {
        label: "Edge field",
        title: "Floating or settling edge field",
        volume: 1500,
        text: "settlement cells, current gaps, habitat shelves, service anchors, public monitoring and reserve media",
        parts: [
          { label: "settlement cells", volume: 300 },
          { label: "current gaps", volume: 280 },
          { label: "habitat shelves", volume: 300 },
          { label: "service anchors", volume: 250 },
          { label: "public monitoring", volume: 200 },
          { label: "reserve media", volume: 170 },
        ],
      },
      {
        label: "Archipelago",
        title: "Happy clean-energy archipelago map",
        volume: 5000,
        text: "habitat islands, surf edges, service platforms, oyster water, dune companions and monitoring corridors",
        parts: [
          { label: "habitat islands", volume: 1000 },
          { label: "surf edges", volume: 900 },
          { label: "service platforms", volume: 950 },
          { label: "oyster water", volume: 800 },
          { label: "dune companions", volume: 700 },
          { label: "monitoring corridors", volume: 650 },
        ],
      },
    ],
  };

  const batchComparison = (per100Useful, volume) => {
    if (per100Useful <= 0) return "100 m batch is ready to compare";
    const ratio = per100Useful / volume;
    if (ratio >= 1) return `100 m batch: about ${setCount(ratio)} sets`;
    return `Needs about ${setCount(volume / per100Useful)} x 100 m batches`;
  };

  const blockFormula = (volume, moduleSize, unit = "pieces") => {
    const pieces = moduleSize > 0 ? volume / moduleSize : 0;
    return `${raw(volume)} m3 / ${raw(moduleSize)} m3 = ${unitCount(pieces, unit)}`;
  };

  const matchedComponentSize = (label, focusKey, fallbackSize) => {
    const text = String(label || "").toLowerCase();

    if (focusKey === "mixed") {
      if (/tile|paver|sample|marker|survey|sensor|monitoring/.test(text)) return 0.05;
      if (/service|access|edge|ledge|rib|facet|anchor|privacy|repair|shade|footing/.test(text)) return 0.18;
      if (/seat|arc|bench|plinth|step|pocket|toe|block|storage|porch|core/.test(text)) return 0.35;
      if (/basket|bag|shell/.test(text)) return 1.2;
      if (/reef|habitat|cell|patch|shape|reset/.test(text)) return 5;
      return fallbackSize;
    }

    if (focusKey === "oyster") {
      if (/tile|tray|tag|marker|mount|station/.test(text)) return 0.05;
      if (/basket|bag|shell/.test(text)) return 1.2;
      if (/reef|habitat|refuge|patch/.test(text)) return 5;
      return fallbackSize;
    }

    if (focusKey === "living") {
      if (/plant|monitor|photo/.test(text)) return 0.03;
      if (/access|edge|gap|pocket/.test(text)) return 0.18;
      if (/toe|cell|shelf|catcher|trap/.test(text)) return 0.75;
      if (/reach|storm|reserve/.test(text)) return 2.5;
      return fallbackSize;
    }

    if (focusKey === "surf") {
      if (/mini|model|tray|marker/.test(text)) return 0.02;
      if (/facet|rib|anchor|survey|camera|sensor/.test(text)) return 0.35;
      if (/cell|shape|current|reset|field|corridor/.test(text)) return 5;
      return fallbackSize;
    }

    if (focusKey === "construction") {
      if (/service|cable|corridor|drain|void|inspection/.test(text)) return 0.18;
      if (/seat|bench|shade|footing|plinth|step|handrail|toe|pocket/.test(text)) return 0.35;
      if (/wall|edge|block|spare|repair|storage|porch|core/.test(text)) return 0.08;
      return fallbackSize;
    }

    if (focusKey === "meeting") {
      if (/marker|edge|paver|wayfinding/.test(text)) return 0.05;
      if (/seat|arc|stone|shade|plinth|speaker|stage|terrace/.test(text)) return 0.35;
      if (/field|reserve/.test(text)) return 1.2;
      return fallbackSize;
    }

    if (focusKey === "homes") {
      if (/tile|paver|sample|coupon|colour|recipe|repair/.test(text)) return 0.05;
      if (/panel|sill|bench|shelf|trim|service/.test(text)) return 0.18;
      if (/counter|privacy|breeze|shade|garden|storage/.test(text)) return 0.35;
      return fallbackSize;
    }

    if (focusKey === "dune") {
      if (/vegetation|photo|marker/.test(text)) return 0.03;
      if (/access|edge|rung|lip|step|guard|control/.test(text)) return 0.18;
      if (/ladder|toe|cell|shelf|platform/.test(text)) return 0.75;
      if (/mat|corridor|reserve|storm/.test(text)) return 2.5;
      return fallbackSize;
    }

    if (focusKey === "island") {
      if (/marker|sensor|model/.test(text)) return 0.75;
      if (/settlement|anchor|landing|pocket/.test(text)) return 2.5;
      if (/platform|habitat|edge|shelf|cell/.test(text)) return 5;
      if (/island|field|corridor|reserve|core|service/.test(text)) return 25;
      return fallbackSize;
    }

    return fallbackSize;
  };

  const componentRows = (parts, moduleSize, scaleMultiplier = 1, unit = "pieces", focusKey = "mixed") => parts.map((part) => {
    const volume = part.volume * scaleMultiplier;
    const partSize = Number(part.size || matchedComponentSize(part.label, focusKey, moduleSize));
    const blocks = partSize > 0 ? volume / partSize : 0;
    return {
      ...part,
      baseVolume: part.volume,
      volume,
      blocks,
      size: partSize,
      formula: blockFormula(volume, partSize, unit),
    };
  });

  const componentTotal = (parts) => parts.reduce((sum, part) => sum + part.volume, 0);
  const componentPieceTotal = (parts) => parts.reduce((sum, part) => sum + part.blocks, 0);

  const slug = (value) => value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");

  const focusData = {
    mixed: {
      label: "mixed island portfolio",
      unit: "pieces or cells",
      estimateKicker: "Mixed portfolio sketches",
      estimateTitle: "What could one material stream open up?",
      estimateNote: "This view keeps several doors open at once: reef cells, living edges, surf-bank geometry, public buildings, civic circles and home products.",
      yardstick: "A mixed island portfolio compares several useful futures from the same sand stream, so people can see which path has enough volume, skill, time and local appetite to keep exploring.",
      defaultPreset: "0.056",
      presets: [
        { label: "4x interlock block (0.056 m3)", value: "0.056" },
        { label: "Robotic interlock block (0.08 m3)", value: "0.08" },
        { label: "Stone-circle seat block (0.35 m3)", value: "0.35" },
        { label: "Small shoreline cell (0.75 m3)", value: "0.75" },
        { label: "Reef basket or bag (1.2 m3)", value: "1.2" },
        { label: "Small reef pod (5 m3)", value: "5" },
      ],
      measureNotes: [
        "Good for comparing many pathways before one pathway tries to dominate the whole conversation.",
        "Useful when the maker-space, Sandworm data, ferry lab and grants lab all need the same public volume language.",
      ],
      scenarios: scenarioLibraries.mixed,
      equipment: ["screening train", "batch yard", "moulds", "reef-cell laydown area", "block racks"],
      skills: ["materials testing", "public volume ledger", "reef geometry", "interlock design", "home-product recipes"],
      records: ["batch tags", "photo records", "where the material went", "what changed after placement"],
    },
    oyster: {
      label: "oyster and shellfish reef",
      unit: "reef cells",
      estimateKicker: "Oyster and shellfish reef sketches",
      estimateTitle: "How large could water-cleaning habitat become?",
      estimateNote: "These sketches use baskets, shell bags, low reef cells and water-quality stations instead of construction blocks.",
      yardstick: "Oyster and shellfish reef thinking can start with trays and baskets, then scale into reef patches, habitat chains, water-quality trials and working-water support.",
      defaultPreset: "1.2",
      presets: [
        { label: "Oyster settlement tile (0.012 m3)", value: "0.012" },
        { label: "Shell bag or tray (0.05 m3)", value: "0.05" },
        { label: "Reef basket or bag (1.2 m3)", value: "1.2" },
        { label: "Small reef pod (5 m3)", value: "5" },
        { label: "Reef field cell (25 m3)", value: "25" },
      ],
      measureNotes: [
        "A small school or maker-space trial can be only a few cubic metres.",
        "A bay-facing habitat chain can move into hundreds of cubic metres once monitoring, access and maintenance are included.",
      ],
      scenarios: scenarioLibraries.oyster,
      equipment: ["reef-cell laydown area", "shell handling", "barge or small-vessel placement"],
      skills: ["shell recycling", "oyster restoration knowledge", "water-quality observation"],
      records: ["reef location", "water quality", "shell source", "fish and habitat observations"],
    },
    living: {
      label: "living shoreline",
      unit: "shoreline cells",
      estimateKicker: "Living shoreline sketches",
      estimateTitle: "How much edge, planting and monitoring could appear?",
      estimateNote: "This pathway counts soft toe cells, planting pockets, access edges, sediment catchers and repair pieces.",
      yardstick: "Living shoreline work is not one wall. It can be small edge pockets, nursery shelves, access gaps, monitoring points and resettable storm-recovery reaches.",
      defaultPreset: "0.75",
      presets: [
        { label: "Planting puck (0.03 m3)", value: "0.03" },
        { label: "Toe or service block (0.18 m3)", value: "0.18" },
        { label: "Small shoreline cell (0.75 m3)", value: "0.75" },
        { label: "Coir/sand mattress cell (2.5 m3)", value: "2.5" },
        { label: "Living edge reach (8 m3)", value: "8" },
      ],
      measureNotes: [
        "This can stay legible at footpath scale, beach-access scale or whole shoreline-reach scale.",
        "The size question is as much about access, planting and monitoring as it is about raw volume.",
      ],
      scenarios: scenarioLibraries.living,
      equipment: ["small cells", "planting trays", "low-impact placement tools"],
      skills: ["saltmarsh planting", "sediment reading", "erosion observation"],
      records: ["before and after photos", "tide line notes", "plant survival", "sediment change"],
    },
    surf: {
      label: "surf bank geometry",
      unit: "geometry cells",
      estimateKicker: "Surf-bank geometry sketches",
      estimateTitle: "How large could a wave-shape question become?",
      estimateNote: "This pathway counts flume models, field markers, sand-hold ribs, reef facets, reset modules and sensor bases.",
      yardstick: "Surf-bank work can begin as model geometry and public wave observation, then scale toward point-break learning reaches and seasonal digital-twin fields.",
      defaultPreset: "5",
      presets: [
        { label: "Flume model piece (0.02 m3)", value: "0.02" },
        { label: "Reef facet block (0.35 m3)", value: "0.35" },
        { label: "Survey or sensor frame (0.75 m3)", value: "0.75" },
        { label: "Surf-bank geometry cell (5 m3)", value: "5" },
        { label: "Superbank field cell (25 m3)", value: "25" },
      ],
      measureNotes: [
        "A tabletop or flume question can be tiny and still useful.",
        "A real surf-bank learning reach quickly becomes a field-scale volume because waves, currents and sand movement need room.",
      ],
      scenarios: scenarioLibraries.surf,
      equipment: ["bathymetry tools", "wave cameras", "model tank", "survey markers"],
      skills: ["surfer observation", "wave modelling", "storm-recovery reading"],
      records: ["wave angle", "sand movement", "reef shape versions", "seasonal surf notes"],
    },
    construction: {
      label: "quick-fit construction blocks",
      unit: "unique blocks",
      estimateKicker: "Quick-fit construction sketches",
      estimateTitle: "How many unique blocks could real island works need?",
      estimateNote: "Counts use the selected block envelope and leave room for service holes, conduits, lifting points, repairs, disassembly and sea-level adaptation.",
      yardstick: "Construction block thinking starts near Besser-style envelopes, then opens into robotic interlocks, service-channel pieces, movable public surfaces and climate-ready building kits.",
      defaultPreset: "0.056",
      presets: [
        { label: "2x service block (0.028 m3)", value: "0.028" },
        { label: "4x interlock block (0.056 m3)", value: "0.056" },
        { label: "Robotic interlock block (0.08 m3)", value: "0.08" },
        { label: "Service-channel block (0.18 m3)", value: "0.18" },
        { label: "Seat or footing block (0.35 m3)", value: "0.35" },
      ],
      measureNotes: [
        "Besser-style reference: 390 x 190 x 190 mm is about 0.014 m3 as an outside envelope.",
        "The 2x and 4x presets are not final product rules. They are simple ways to compare service holes, interlocks, handling and robotic installation.",
      ],
      scenarios: scenarioLibraries.construction,
      equipment: ["quick-fit moulds", "robotic block handling", "covered curing racks"],
      skills: ["interlock design", "hidden service channels", "assembly and disassembly planning"],
      records: ["block passports", "service maps", "unlock and repair history", "resident fit notes"],
    },
    meeting: {
      label: "stone circle and civic pieces",
      unit: "civic pieces",
      estimateKicker: "Stone circle and civic sketches",
      estimateTitle: "How much public gathering space could be shaped?",
      estimateNote: "This pathway counts seat arcs, markers, shade bases, speaker plinths, stage edges and movable civic pieces.",
      yardstick: "Civic pieces can be modest: a few seat stones and shade bases. They can also become market rings, listening slopes and festival fields if people want them.",
      defaultPreset: "0.35",
      presets: [
        { label: "Tile or paver batch (0.05 m3)", value: "0.05" },
        { label: "Seat block (0.35 m3)", value: "0.35" },
        { label: "Standing stone or marker (0.75 m3)", value: "0.75" },
        { label: "Circle plinth (1.2 m3)", value: "1.2" },
        { label: "Stage or shade footing (2.5 m3)", value: "2.5" },
      ],
      measureNotes: [
        "This is useful where public-space making, art, wayfinding, shade and community meetings overlap.",
        "The same material stream can become social infrastructure without needing every piece to be structural building work.",
      ],
      scenarios: scenarioLibraries.meeting,
      equipment: ["small moulds", "finish tools", "layout templates"],
      skills: ["public-space geometry", "artistic finishing", "community install planning"],
      records: ["layout story", "finish recipe", "repair notes", "community use notes"],
    },
    homes: {
      label: "glass, silicate and home products",
      unit: "home pieces",
      estimateKicker: "Glass, silicate and home-product sketches",
      estimateTitle: "How much resident-use material could be made?",
      estimateNote: "This pathway counts recipe tests, tiles, pavers, privacy blocks, bench pieces, wet-area kits and repairable home products.",
      yardstick: "Home-product thinking can stay close to residents: tiles, pavers, privacy blocks, bench pieces, garden edges, repair kits and small-batch recipes.",
      defaultPreset: "0.05",
      presets: [
        { label: "Glass or silicate test batch (0.02 m3)", value: "0.02" },
        { label: "Tile or paver batch (0.05 m3)", value: "0.05" },
        { label: "Small panel or block (0.08 m3)", value: "0.08" },
        { label: "Bench or sill piece (0.18 m3)", value: "0.18" },
        { label: "Counter or garden set (0.35 m3)", value: "0.35" },
      ],
      measureNotes: [
        "This pathway is less about one big object and more about many resident-use pieces with recipes people can inspect.",
        "Small volumes matter because repair, custom fit and local design are part of the value.",
      ],
      scenarios: scenarioLibraries.homes,
      equipment: ["glass tests", "ceramic forms", "small kiln or heat tests", "finishing bench"],
      skills: ["recipe testing", "home-fit design", "repairable product thinking"],
      records: ["recipe versions", "resident requests", "repair and return notes", "material passports"],
    },
    dune: {
      label: "stable dune support",
      unit: "dune pieces",
      estimateKicker: "Stable dune support sketches",
      estimateTitle: "How much access, planting and dune care could appear?",
      estimateNote: "This pathway counts sand ladders, toe cells, vegetation shelves, access edges, monitoring points and reset stock.",
      yardstick: "Dune support can be small and adaptive: access ladders, planted shelves, soft toe pieces, viewing-platform feet and storm-reset kits.",
      defaultPreset: "0.35",
      presets: [
        { label: "Vegetation puck (0.03 m3)", value: "0.03" },
        { label: "Access edge block (0.18 m3)", value: "0.18" },
        { label: "Sand ladder segment (0.35 m3)", value: "0.35" },
        { label: "Dune support cell (0.75 m3)", value: "0.75" },
        { label: "Walkway mat cell (2.5 m3)", value: "2.5" },
      ],
      measureNotes: [
        "The important scale is often a human path, a dune foot, a blowout, a lookout or a whole access corridor.",
        "Good records would track sand movement, vegetation, access pressure and storm response over time.",
      ],
      scenarios: scenarioLibraries.dune,
      equipment: ["light placement gear", "sand fencing", "vegetation trays", "monitoring stakes"],
      skills: ["dune ecology", "vegetation care", "sand movement reading"],
      records: ["vegetation line", "sand movement", "storm response", "access impacts"],
    },
    island: {
      label: "artificial island or platform question",
      unit: "landform cells",
      estimateKicker: "Island and platform question sketches",
      estimateTitle: "How large could a landform experiment become?",
      estimateNote: "This pathway counts settlement cells, habitat shelves, platform edges, surf companion geometry, monitoring corridors and reserve media.",
      yardstick: "Artificial island and platform thinking should stay openly exploratory: model cells, sensor islets, sand-cay tests, settling edges and archipelago-scale habitat questions.",
      defaultPreset: "25",
      presets: [
        { label: "Platform model cell (0.75 m3)", value: "0.75" },
        { label: "Settlement cell (2.5 m3)", value: "2.5" },
        { label: "Platform pod (5 m3)", value: "5" },
        { label: "Landform field cell (25 m3)", value: "25" },
        { label: "Large staged cell (100 m3)", value: "100" },
      ],
      measureNotes: [
        "This category is where model scale, settlement monitoring, habitat, navigation, access and public authority all need to be visible.",
        "The calculator keeps the question legible without pretending the first sketch is a final permission pathway.",
      ],
      scenarios: scenarioLibraries.island,
      equipment: ["settlement markers", "staged placement tools", "survey gear"],
      skills: ["staged landform records", "settlement monitoring", "public evidence mapping"],
      records: ["stage volume", "settlement", "edge change", "habitat and access notes"],
    },
  };

  const setPresetOptionsForFocus = (focusKey, options = {}) => {
    if (!inputs.modulePreset || !inputs.moduleSize) return;
    const focus = focusData[focusKey] || focusData.mixed;
    const currentValue = inputs.modulePreset.value;
    const currentCustomSize = inputs.moduleSize.value;
    const selectedValue = options.preserve && focus.presets.some((preset) => preset.value === currentValue)
      ? currentValue
      : focus.defaultPreset;

    inputs.modulePreset.innerHTML = [
      ...focus.presets.map((preset) => `<option value="${preset.value}">${preset.label}</option>`),
      '<option value="custom">Custom size</option>',
    ].join("");

    if (options.preserve && currentValue === "custom") {
      inputs.modulePreset.value = "custom";
      inputs.moduleSize.value = currentCustomSize;
      return;
    }

    inputs.modulePreset.value = selectedValue;
    inputs.moduleSize.value = selectedValue;
  };

  const setExampleOptionsForFocus = (focusKey, options = {}) => {
    if (!inputs.example) return;
    const focus = focusData[focusKey] || focusData.mixed;
    const scenarios = focus.scenarios || scenarioLibraries.mixed;
    const currentValue = inputs.example.value;
    const selectedValue = options.preserve && scenarios[Number(currentValue)]
      ? currentValue
      : "0";

    inputs.example.innerHTML = scenarios
      .map((item, index) => `<option value="${index}">${item.title}</option>`)
      .join("");
    inputs.example.value = selectedValue;
  };

  const updateSandwormBridge = () => {
    const holder = root.querySelector("[data-sandworm-links]");
    if (!holder) return;

    const fallback = [
      { label: "Spoil loop", href: "https://auraofintelligence.github.io/sandworm-subterranean-systems/sandworm-lab.html" },
      { label: "Reefs + power", href: "https://auraofintelligence.github.io/sandworm-subterranean-systems/civilisation-of-sand.html" },
      { label: "Twin layer", href: "https://auraofintelligence.github.io/sandworm-subterranean-systems/digital-twin.html" },
      { label: "Builder", href: "https://auraofintelligence.github.io/sandworm-subterranean-systems/builders/spoil-loop-brief.html" },
    ];

    const nav = window.SANDWORM_SITE && Array.isArray(window.SANDWORM_SITE.nav)
      ? window.SANDWORM_SITE.nav
      : [];
    const byId = Object.fromEntries(nav.map((item) => [item.id, item]));
    const live = ["sandworm-lab", "civilisation", "digital-twin", "makerspace"]
      .map((id) => byId[id])
      .filter(Boolean)
      .map((item) => ({
        label: item.label,
        href: `https://auraofintelligence.github.io/sandworm-subterranean-systems/${item.href}`,
      }));

    const links = live.length ? live : fallback;
    holder.innerHTML = links.map((item) => `<a class="tag" href="${item.href}">${item.label}</a>`).join("");
  };

  const update = () => {
    const diameter = Number(inputs.diameter.value);
    const weeklyAdvance = Number(inputs.weeklyAdvance.value);
    const weeks = Number(inputs.weeks.value);
    const reefShare = Number(inputs.reefShare.value);
    const moduleSize = Number(inputs.moduleSize.value);
    const focusKey = inputs.focus ? inputs.focus.value : "mixed";
    const focus = focusData[focusKey] || focusData.mixed;
    const scenarioSource = focus.scenarios || scenarioLibraries.mixed;
    const unit = focus.unit || "pieces";
    const selectedExampleIndex = inputs.example && scenarioSource[Number(inputs.example.value)]
      ? Number(inputs.example.value)
      : 0;
    const selectedScale = root.querySelector('[data-calc-input="scenarioScale"]:checked')?.value || "medium";
    const scenarioScale = scaleBands[selectedScale] || scaleBands.medium;
    const presetLabel = inputs.modulePreset && inputs.modulePreset.selectedOptions.length
      ? inputs.modulePreset.selectedOptions[0].textContent.replace(/\s+(?:-\s+.*|\(.*\))$/, "")
      : "Custom size";

    const area = Math.PI * (diameter / 2) ** 2;
    const per100 = area * 100;
    const per100Useful = per100 * (reefShare / 100) * FORMING_FACTOR;
    const weeklySpoil = area * weeklyAdvance;
    const weeklyDiverted = weeklySpoil * (reefShare / 100);
    const weeklyReef = weeklyDiverted * FORMING_FACTOR;
    const stageReef = weeklyReef * weeks;
    const stageDiverted = weeklyDiverted * weeks;
    const weeklyPieces = moduleSize > 0 ? weeklyReef / moduleSize : 0;
    const weeklyWeight = weeklySpoil * SANDMASS_TONNES_PER_M3;
    const timePer100Hours = weeklyAdvance > 0 ? (100 / weeklyAdvance) * 7 * 24 : 0;
    const per100Pieces = moduleSize > 0 ? per100Useful / moduleSize : 0;
    const scenarioResults = scenarioSource.map((item) => {
      const itemUnit = item.unit || unit;
      const components = componentRows(item.parts || [], moduleSize, scenarioScale.multiplier, itemUnit, focusKey);
      const volume = components.length ? componentTotal(components) : item.volume * scenarioScale.multiplier;
      const blocks = components.length ? componentPieceTotal(components) : (moduleSize > 0 ? volume / moduleSize : 0);
      const weeklySets = volume > 0 ? weeklyReef / volume : 0;
      return {
        ...item,
        unit: itemUnit,
        baseVolume: item.volume,
        volume,
        blocks,
        weeklySets,
        formula: components.length
          ? `component schedule = ${unitCount(blocks, itemUnit)} across ${metres3(volume)}`
          : blockFormula(volume, moduleSize, itemUnit),
        components,
        componentVolume: componentTotal(components),
        scale: scenarioScale,
        batch: batchComparison(per100Useful, volume),
      };
    });
    const selectedScenario = scenarioResults[selectedExampleIndex] || scenarioResults[0];

    output("diameter", `${decimal.format(diameter)} m`);
    output("weeklyAdvance", formatAdvance(weeklyAdvance));
    output("weeks", number.format(weeks));
    output("reefShare", `${number.format(reefShare)}%`);
    output("modulePreset", presetLabel);
    output("moduleSize", metres3(moduleSize));
    output("scenarioScale", scenarioScale.label);
    output("focusLabel", focus.label);
    output("estimateKicker", focus.estimateKicker || "Transformation sketches");
    output("estimateTitle", focus.estimateTitle || "How large could this batch become?");
    output("estimateNote", focus.estimateNote || "Choose a pathway to swap the example cards and verification note.");
    output("exampleLabel", selectedScenario ? selectedScenario.title : "");
    output("focusYardstick", focus.yardstick || "");
    output("per100", metres3(per100));
    output("per100Scale", volumeScale(per100));
    output("timePer100", formatDuration(timePer100Hours));
    output("weeklySpoil", metres3(weeklySpoil));
    output("weeklySpoilScale", volumeScale(weeklySpoil));
    output("weeklyReef", metres3(weeklyReef));
    output("weeklyReefScale", volumeScale(weeklyReef));
    output("stageReef", metres3(stageReef));
    output("stageReefScale", volumeScale(stageReef));
    output("weeklyUnitLabel", `Approx. ${unit} / week`);
    output("weeklyModules", count(weeklyPieces));
    output("weeklyWeight", tonnes(weeklyWeight));
    output("weeklyWeightScale", weightScale(weeklyWeight));
    output("avoided", metres3(stageDiverted));
    output("avoidedScale", volumeScale(stageDiverted));

    const focusMeasures = root.querySelector("[data-calc-out=\"focusMeasures\"]");
    if (focusMeasures) {
      const measureCards = [
        `<div><span>Selected unit</span><strong>${metres3(moduleSize)}</strong><em>${volumeScale(moduleSize)}</em></div>`,
        `<div><span>100 m batch</span><strong>${unitCount(per100Pieces, unit)}</strong><em>${metres3(per100Useful)} useful media</em></div>`,
        `<div><span>Current week</span><strong>${unitCount(weeklyPieces, unit)}</strong><em>${metres3(weeklyReef)} useful media</em></div>`,
      ];
      const notes = (focus.measureNotes || []).map((note) => `<p>${note}</p>`);
      focusMeasures.innerHTML = [...measureCards, ...notes].join("");
    }

    const timeline = root.querySelector("[data-calc-timeline]");
    if (timeline) {
      const bars = Array.from({ length: weeks }, (_, index) => {
        const label = `Week ${index + 1}`;
        const width = Math.max(8, Math.min(100, (weeklyReef / Math.max(weeklySpoil, 1)) * 100));
        return `<div class="timeline-row"><span>${label}</span><b style="width:${width}%"></b><em>${metres3(weeklyReef)}</em></div>`;
      });
      timeline.innerHTML = bars.join("");
    }

    output(
      "timelineNote",
      `Across ${number.format(weeks)} week${weeks === 1 ? "" : "s"}, ${metres3(stageDiverted)} of raw material could become ${metres3(stageReef)} of formed media for ${focus.label}. That is ${volumeScale(stageReef)}. At ${formatAdvance(weeklyAdvance)}, the next 100 m arrives in about ${formatDuration(timePer100Hours)}.`
    );

    const equipment = weeklySpoil < 250
      ? ["micro-borer or service robot", "small carts", "maker-space test bays"]
      : weeklySpoil < 1500
        ? ["compact TBM", "robot carts", "mobile screener", "small batch mixer"]
        : weeklySpoil < 10000
          ? ["Loop-scale TBM", "conveyors", "screening train", "batch yard"]
          : ["multi-shift boring system", "automated spoil routing", "dedicated material yard", "continuous batching"];

    const skills = ["survey and measurement", "materials testing", "batch records", "site logistics", "community explanation"];
    const records = ["volume dashboard", "QR or RFID batch tags", "photo records", "weight or load records"];

    const workMap = root.querySelector("[data-calc-out=\"workMap\"]");
    if (workMap) {
      workMap.innerHTML = [
        makeList("Equipment that could appear", [...new Set([...equipment, ...focus.equipment])]),
        makeList("Human skills that could grow", [...new Set([...skills, ...focus.skills])]),
        makeList("Records people could inspect", [...new Set([...records, ...focus.records])]),
      ].join("");
    }

    const selectedExample = root.querySelector("[data-calc-out=\"selectedExample\"]");
    if (selectedExample && selectedScenario) {
      selectedExample.innerHTML = `<article class="selected-example-card">
        <div>
          <p class="mini-label">Selected example</p>
          <h4>${selectedScenario.title}</h4>
          <strong>${metres3(selectedScenario.volume)} sketch -> ${unitCount(selectedScenario.blocks, selectedScenario.unit)}</strong>
          <p>${selectedScenario.scale.label} scale. Medium reference was ${metres3(selectedScenario.baseVolume)}. Includes ${selectedScenario.text}.</p>
        </div>
        <div class="component-schedule">
          ${selectedScenario.components.map((part) => `<div>
            <span>${part.label}</span>
            <strong>${metres3(part.volume)} -> ${unitCount(part.blocks, selectedScenario.unit)}</strong>
            <em>${raw(part.size)} m3 each</em>
          </div>`).join("")}
        </div>
        <details class="component-formula-details">
          <summary>Show component formulas</summary>
          <div class="component-formula-list">
            ${selectedScenario.components.map((part) => `<code>${part.label}: ${part.formula}</code>`).join("")}
          </div>
        </details>
        <p class="calc-note">${selectedScenario.batch}; current week: about ${setCount(selectedScenario.weeklySets)} sets.</p>
      </article>`;
    }

    const blockEstimates = root.querySelector("[data-calc-out=\"blockEstimates\"]");
    if (blockEstimates) {
      blockEstimates.innerHTML = scenarioResults.map((item, index) => {
        const current = index === selectedExampleIndex ? " is-current" : "";
        return `<article class="block-estimate-card compact${current}">
          <p class="mini-label">${item.label}</p>
          <h4>${item.title}</h4>
          <strong>${metres3(item.volume)}</strong>
          <p>${unitCount(item.blocks, item.unit)} by matched component sizes.</p>
        </article>`;
      }).join("");
    }

    latestState = {
      diameter,
      weeklyAdvance,
      weeks,
      reefShare,
      moduleSize,
      scenarioScale,
      focus,
      focusKey,
      unit,
      selectedExampleIndex,
      selectedScenario,
      presetLabel,
      area,
      per100,
      per100Useful,
      per100Pieces,
      weeklySpoil,
      weeklyDiverted,
      weeklyReef,
      stageReef,
      stageDiverted,
      weeklyPieces,
      weeklyWeight,
      timePer100Hours,
      scenarioResults,
      generatedAt: new Date(),
    };
    if (markdownPreview) markdownPreview.value = markdownFromState(latestState);
  };

  const markdownFromState = (state) => {
    const generated = state.generatedAt.toLocaleString("en-AU");
    const lines = [
      "# Straddie Reef, Tunnel Media And Quick-Block Verification Note",
      "",
      `Generated: ${generated}`,
      `Source page: ${window.location.href.split("#")[0]}`,
      "",
      "This is a public calculation note, not an engineering sign-off. It captures the viewer's current calculator settings so a builder, engineer, maker-space, council team, neighbour group or grant lab can check the assumptions.",
      "",
      "## Current Calculator Settings",
      "",
      `- Tunnel diameter: ${decimal.format(state.diameter)} m`,
      `- Tunnel advance: ${formatAdvance(state.weeklyAdvance)}`,
      `- Sprint length: ${number.format(state.weeks)} week${state.weeks === 1 ? "" : "s"}`,
      `- Material converted to useful media: ${number.format(state.reefShare)}%`,
      `- Media preset: ${state.presetLabel}`,
      `- Global comparison unit: ${metres3(state.moduleSize)}`,
      `- Build-example scale: ${state.scenarioScale.label} (${state.scenarioScale.note}, ${raw(state.scenarioScale.multiplier, 2)}x the medium sketch)`,
      `- Material story: ${state.focus.label}`,
      `- Selected example: ${state.selectedScenario ? state.selectedScenario.title : "Not selected"}`,
      `- Counting unit: ${state.unit}`,
      "",
      "## Shared Assumptions",
      "",
      `- Forming factor: ${FORMING_FACTOR}x useful formed media from diverted raw material.`,
      `- Rough damp sandmass: ${SANDMASS_TONNES_PER_M3} tonnes per m3.`,
      "- Everyday volume yardsticks: wheelbarrow 0.1 m3, concrete truck 6 m3, twenty-foot container 33 m3, Olympic pool 2,500 m3.",
      `- Besser-style reference envelope: ${BESSER_LENGTH_M} m x ${BESSER_WIDTH_M} m x ${BESSER_HEIGHT_M} m = ${raw(BESSER_ENVELOPE_M3, 6)} m3.`,
      `- 2x Besser-style envelope: ${raw(BESSER_ENVELOPE_M3 * 2, 3)} m3.`,
      `- 4x Besser-style envelope: ${raw(BESSER_ENVELOPE_M3 * 4, 3)} m3.`,
      "- Example scales are adjustable guesses: minimal = 0.55x medium, medium = 1x, large = 2.2x. The point is to expose the range, not pretend one early number is final.",
      "- Service holes, lifting points, conduits, drainage, interlocks, habitat gaps, monitoring mounts and material recipes can change the final mass and method. This note counts selected piece or cell envelopes for early verification.",
      "",
      "## Pathway Yardstick",
      "",
      state.focus.yardstick,
      "",
      ...((state.focus.measureNotes || []).map((note) => `- ${note}`)),
      "",
      "## Core Formulas",
      "",
      `- Tunnel cross-section area = pi x (${decimal.format(state.diameter)} / 2)^2 = ${metres2(state.area)}.`,
      `- 100 m tunnel volume = ${metres2(state.area)} x 100 m = ${metres3(state.per100)} (${volumeScale(state.per100)}).`,
      `- Useful media per 100 m = ${metres3(state.per100)} x ${number.format(state.reefShare)}% x ${FORMING_FACTOR} = ${metres3(state.per100Useful)}.`,
      `- Weekly tunnel volume = ${metres2(state.area)} x ${number.format(state.weeklyAdvance)} m/week = ${metres3(state.weeklySpoil)} (${volumeScale(state.weeklySpoil)}).`,
      `- Weekly useful media = ${metres3(state.weeklySpoil)} x ${number.format(state.reefShare)}% x ${FORMING_FACTOR} = ${metres3(state.weeklyReef)} (${volumeScale(state.weeklyReef)}).`,
      `- Sprint useful media = ${metres3(state.weeklyReef)} x ${number.format(state.weeks)} = ${metres3(state.stageReef)} (${volumeScale(state.stageReef)}).`,
      `- ${state.unit} per 100 m = ${metres3(state.per100Useful)} / ${metres3(state.moduleSize)} = ${unitCount(state.per100Pieces, state.unit)}.`,
      `- ${state.unit} per week = ${metres3(state.weeklyReef)} / ${metres3(state.moduleSize)} = ${unitCount(state.weeklyPieces, state.unit)}.`,
      `- Rough weekly weight = ${metres3(state.weeklySpoil)} x ${SANDMASS_TONNES_PER_M3} t/m3 = ${tonnes(state.weeklyWeight)} (${weightScale(state.weeklyWeight)}).`,
      "",
      "## Selected Example Component Schedule",
      "",
      state.selectedScenario
        ? `${state.selectedScenario.title}: ${metres3(state.selectedScenario.volume)} sketch, counted as ${unitCount(state.selectedScenario.blocks, state.selectedScenario.unit)} across matched component sizes.`
        : "No selected example was available.",
      "",
      ...(state.selectedScenario ? state.selectedScenario.components.map((part) => `- ${part.label}: ${part.formula} (${raw(part.size)} m3 each)`) : []),
      "",
      `## ${state.focus.estimateTitle}`,
      "",
      state.focus.estimateNote,
      "",
      `Each example uses its own matched component sizes. The global comparison unit remains visible above so people can compare it with the component schedule.`,
      "",
      `| Example | Scale | Medium reference | Sketch volume | Formula | Approx. ${state.unit} | 100 m batch comparison | Current week |`,
      "| --- | --- | ---: | ---: | --- | ---: | --- | --- |",
      ...state.scenarioResults.map((item) => `| ${item.title} | ${item.scale.label} | ${metres3(item.baseVolume)} | ${metres3(item.volume)} | ${item.formula} | ${unitCount(item.blocks, item.unit)} | ${item.batch} | about ${setCount(item.weeklySets)} sets |`),
      "",
      "## Example Component Split Formulas",
      "",
      "These are editable sketch allocations. They show how the headline count could be built from parts, while leaving room for better site survey, robotics, service holes, habitat gaps, monitoring, repair and community design.",
      "",
      ...state.scenarioResults.flatMap((item) => [
        `### ${item.title}`,
        "",
        `Scale: ${item.scale.label} (${raw(item.scale.multiplier, 2)}x medium). Medium reference was ${metres3(item.baseVolume)}.`,
        "",
        `Total check: component sketch adds to ${metres3(item.componentVolume)}; total block formula is ${item.formula}.`,
        "",
        ...item.components.map((part) => `- ${part.label}: ${part.formula}`),
        "",
      ]),
      "## Verification Questions",
      "",
      "- Which parts are structural, non-structural, landscape, service, seating, reef, footing or temporary public-space pieces?",
      "- Which blocks need service holes, conduits, drainage, lifting points, RFID or QR passports, interlocks, inspection lids or custom geometry?",
      "- What material recipe, curing path, testing protocol and durability target would make each block family inspectable?",
      "- Which dimensions should be changed after site survey, access, robotics, maintenance, storm, sea-level, corrosion and community-use checks?",
      "- What data should be exported back into the Sandworm subterranean systems repo or a local digital twin?",
      "",
      "## Related Public Context",
      "",
      "- Straddie Clean Energy Superpower reef calculator",
      "- Sandworm Subterranean Systems spoil-loop and digital-twin work",
      "- Straddie Maker-Space Lab material recipe work",
      "- Dunwich / Gumpi Ferry Terminal Open Data Lab",
      "- Ballow Road Sand & Screen Hub",
    ];

    return `${lines.join("\n")}\n`;
  };

  const downloadMarkdown = () => {
    update();
    if (!latestState) return;

    const blob = new Blob([markdownFromState(latestState)], { type: "text/markdown;charset=utf-8" });
    const link = document.createElement("a");
    const focusLabel = slug(latestState.focus.label) || "material";
    link.href = URL.createObjectURL(blob);
    link.download = `straddie-reef-block-verification-${focusLabel}.md`;
    document.body.appendChild(link);
    link.click();
    URL.revokeObjectURL(link.href);
    link.remove();
    output("exportStatus", "Markdown verification note downloaded.");
  };

  Object.entries(inputs).forEach(([name, input]) => {
    if (!input || name === "modulePreset" || name === "focus") return;
    const controls = input.addEventListener ? [input] : Array.from(input);
    controls.forEach((control) => {
      control.addEventListener("input", () => {
        if (name === "moduleSize" && inputs.modulePreset) inputs.modulePreset.value = "custom";
        update();
      });
      control.addEventListener("change", update);
    });
  });

  if (inputs.focus) {
    inputs.focus.addEventListener("change", () => {
      setPresetOptionsForFocus(inputs.focus.value);
      setExampleOptionsForFocus(inputs.focus.value);
      update();
    });
  }

  if (inputs.modulePreset) {
    inputs.modulePreset.addEventListener("change", () => {
      if (inputs.modulePreset.value !== "custom") inputs.moduleSize.value = inputs.modulePreset.value;
      update();
    });
  }

  root.querySelectorAll(".segmented-control label").forEach((label) => {
    label.addEventListener("click", () => {
      const radio = label.querySelector('[data-calc-input="scenarioScale"]');
      if (!radio || radio.checked) return;
      radio.checked = true;
      update();
    });
  });

  if (exportButton) exportButton.addEventListener("click", downloadMarkdown);

  updateSandwormBridge();
  const initialFocus = inputs.focus ? inputs.focus.value : "mixed";
  setPresetOptionsForFocus(initialFocus);
  setExampleOptionsForFocus(initialFocus);
  update();
})();
