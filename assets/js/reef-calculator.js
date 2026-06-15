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
    focus: root.querySelector('[data-calc-input="focus"]'),
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
    if (value < 80) return `about ${count(concreteTrucks)} concrete-truck loads or ${count(containers)} twenty-foot containers`;
    if (value < 1200) return `about ${count(containers)} twenty-foot containers or ${count(concreteTrucks)} concrete-truck loads`;
    return `about ${count(containers)} twenty-foot containers, ${count(concreteTrucks)} concrete-truck loads or ${count1(pools)} Olympic pools`;
  };

  const weightScale = (value) => {
    const truckloads = value / 20;
    if (value < 20) return `about ${count1(truckloads)} loaded 20 tonne tip trucks`;
    return `about ${count(truckloads)} loaded 20 tonne tip trucks`;
  };

  const makeList = (label, items) => {
    return `<div><strong>${label}</strong><p>${items.join(", ")}</p></div>`;
  };

  const blockScenarios = [
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

  const batchComparison = (per100Useful, volume) => {
    if (per100Useful <= 0) return "100 m batch is ready to compare";
    const ratio = per100Useful / volume;
    if (ratio >= 1) return `100 m batch: about ${setCount(ratio)} sets`;
    return `Needs about ${setCount(volume / per100Useful)} x 100 m batches`;
  };

  const blockFormula = (volume, moduleSize) => {
    const blocks = moduleSize > 0 ? volume / moduleSize : 0;
    return `${raw(volume)} m3 / ${raw(moduleSize)} m3 = ${count(blocks)} blocks`;
  };

  const componentRows = (parts, moduleSize) => parts.map((part) => {
    const blocks = moduleSize > 0 ? part.volume / moduleSize : 0;
    return {
      ...part,
      blocks,
      formula: blockFormula(part.volume, moduleSize),
    };
  });

  const componentTotal = (parts) => parts.reduce((sum, part) => sum + part.volume, 0);

  const slug = (value) => value.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/(^-|-$)/g, "");

  const focusData = {
    mixed: {
      label: "mixed island portfolio",
      equipment: ["screening train", "batch yard", "moulds", "reef-cell laydown area", "block racks"],
      skills: ["materials testing", "public volume ledger", "reef geometry", "interlock design", "home-product recipes"],
      records: ["batch tags", "photo records", "where the material went", "what changed after placement"],
    },
    oyster: {
      label: "oyster and shellfish reef",
      equipment: ["reef-cell laydown area", "shell handling", "barge or small-vessel placement"],
      skills: ["shell recycling", "oyster restoration knowledge", "water-quality observation"],
      records: ["reef location", "water quality", "shell source", "fish and habitat observations"],
    },
    living: {
      label: "living shoreline",
      equipment: ["small cells", "planting trays", "low-impact placement tools"],
      skills: ["saltmarsh planting", "sediment reading", "erosion observation"],
      records: ["before and after photos", "tide line notes", "plant survival", "sediment change"],
    },
    surf: {
      label: "surf bank geometry",
      equipment: ["bathymetry tools", "wave cameras", "model tank", "survey markers"],
      skills: ["surfer observation", "wave modelling", "storm-recovery reading"],
      records: ["wave angle", "sand movement", "reef shape versions", "seasonal surf notes"],
    },
    construction: {
      label: "quick-fit construction blocks",
      equipment: ["quick-fit moulds", "robotic block handling", "covered curing racks"],
      skills: ["interlock design", "hidden service channels", "assembly and disassembly planning"],
      records: ["block passports", "service maps", "unlock and repair history", "resident fit notes"],
    },
    meeting: {
      label: "stone circle and civic pieces",
      equipment: ["small moulds", "finish tools", "layout templates"],
      skills: ["public-space geometry", "artistic finishing", "community install planning"],
      records: ["layout story", "finish recipe", "repair notes", "community use notes"],
    },
    homes: {
      label: "glass, silicate and home products",
      equipment: ["glass tests", "ceramic forms", "small kiln or heat tests", "finishing bench"],
      skills: ["recipe testing", "home-fit design", "repairable product thinking"],
      records: ["recipe versions", "resident requests", "repair and return notes", "material passports"],
    },
    dune: {
      label: "stable dune support",
      equipment: ["light placement gear", "sand fencing", "vegetation trays", "monitoring stakes"],
      skills: ["dune ecology", "vegetation care", "sand movement reading"],
      records: ["vegetation line", "sand movement", "storm response", "access impacts"],
    },
    island: {
      label: "artificial island or platform question",
      equipment: ["settlement markers", "staged placement tools", "survey gear"],
      skills: ["staged landform records", "settlement monitoring", "public evidence mapping"],
      records: ["stage volume", "settlement", "edge change", "habitat and access notes"],
    },
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
    const focus = focusData[inputs.focus.value] || focusData.mixed;
    const presetLabel = inputs.modulePreset && inputs.modulePreset.selectedOptions.length
      ? inputs.modulePreset.selectedOptions[0].textContent.replace(/\s+-\s+.*$/, "")
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
    const scenarioResults = blockScenarios.map((item) => {
      const blocks = moduleSize > 0 ? item.volume / moduleSize : 0;
      const weeklySets = item.volume > 0 ? weeklyReef / item.volume : 0;
      return {
        ...item,
        blocks,
        weeklySets,
        formula: blockFormula(item.volume, moduleSize),
        components: componentRows(item.parts || [], moduleSize),
        componentVolume: componentTotal(item.parts || []),
        batch: batchComparison(per100Useful, item.volume),
      };
    });

    output("diameter", `${decimal.format(diameter)} m`);
    output("weeklyAdvance", formatAdvance(weeklyAdvance));
    output("weeks", number.format(weeks));
    output("reefShare", `${number.format(reefShare)}%`);
    output("modulePreset", presetLabel);
    output("moduleSize", metres3(moduleSize));
    output("focusLabel", focus.label);
    output("per100", metres3(per100));
    output("per100Scale", volumeScale(per100));
    output("timePer100", formatDuration(timePer100Hours));
    output("weeklySpoil", metres3(weeklySpoil));
    output("weeklySpoilScale", volumeScale(weeklySpoil));
    output("weeklyReef", metres3(weeklyReef));
    output("weeklyReefScale", volumeScale(weeklyReef));
    output("stageReef", metres3(stageReef));
    output("stageReefScale", volumeScale(stageReef));
    output("weeklyModules", count(weeklyPieces));
    output("weeklyWeight", tonnes(weeklyWeight));
    output("weeklyWeightScale", weightScale(weeklyWeight));
    output("avoided", metres3(stageDiverted));
    output("avoidedScale", volumeScale(stageDiverted));

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

    const blockEstimates = root.querySelector("[data-calc-out=\"blockEstimates\"]");
    if (blockEstimates) {
      blockEstimates.innerHTML = scenarioResults.map((item) => {
        const componentList = item.components.length ? `<details class="component-split">
          <summary>Show example component split</summary>
          <ul>
            ${item.components.map((part) => `<li><span>${part.label}: ${metres3(part.volume)} -> ${count(part.blocks)} blocks</span><code>${part.formula}</code></li>`).join("")}
          </ul>
        </details>` : "";
        return `<article class="block-estimate-card">
          <p class="mini-label">${item.label}</p>
          <h4>${item.title}</h4>
          <strong>${count(item.blocks)} unique blocks</strong>
          <p>${metres3(item.volume)} sketch: ${item.text}.</p>
          <code>Formula: ${item.formula}</code>
          ${componentList}
          <em>${item.batch}; current week: about ${setCount(item.weeklySets)} sets.</em>
        </article>`;
      }).join("");
    }

    latestState = {
      diameter,
      weeklyAdvance,
      weeks,
      reefShare,
      moduleSize,
      focus,
      presetLabel,
      area,
      per100,
      per100Useful,
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
      `- Selected piece or media cell: ${metres3(state.moduleSize)}`,
      `- Material story: ${state.focus.label}`,
      "",
      "## Shared Assumptions",
      "",
      `- Forming factor: ${FORMING_FACTOR}x useful formed media from diverted raw material.`,
      `- Rough damp sandmass: ${SANDMASS_TONNES_PER_M3} tonnes per m3.`,
      "- Everyday volume yardsticks: wheelbarrow 0.1 m3, concrete truck 6 m3, twenty-foot container 33 m3, Olympic pool 2,500 m3.",
      `- Besser-style reference envelope: ${BESSER_LENGTH_M} m x ${BESSER_WIDTH_M} m x ${BESSER_HEIGHT_M} m = ${raw(BESSER_ENVELOPE_M3, 6)} m3.`,
      `- 2x Besser-style envelope: ${raw(BESSER_ENVELOPE_M3 * 2, 3)} m3.`,
      `- 4x Besser-style envelope: ${raw(BESSER_ENVELOPE_M3 * 4, 3)} m3.`,
      "- Service holes, lifting points, conduits, drainage, interlocks and material recipes can change the final mass and engineering method. This note counts block envelopes for early verification.",
      "",
      "## Core Formulas",
      "",
      `- Tunnel cross-section area = pi x (${decimal.format(state.diameter)} / 2)^2 = ${metres2(state.area)}.`,
      `- 100 m tunnel volume = ${metres2(state.area)} x 100 m = ${metres3(state.per100)} (${volumeScale(state.per100)}).`,
      `- Useful media per 100 m = ${metres3(state.per100)} x ${number.format(state.reefShare)}% x ${FORMING_FACTOR} = ${metres3(state.per100Useful)}.`,
      `- Weekly tunnel volume = ${metres2(state.area)} x ${number.format(state.weeklyAdvance)} m/week = ${metres3(state.weeklySpoil)} (${volumeScale(state.weeklySpoil)}).`,
      `- Weekly useful media = ${metres3(state.weeklySpoil)} x ${number.format(state.reefShare)}% x ${FORMING_FACTOR} = ${metres3(state.weeklyReef)} (${volumeScale(state.weeklyReef)}).`,
      `- Sprint useful media = ${metres3(state.weeklyReef)} x ${number.format(state.weeks)} = ${metres3(state.stageReef)} (${volumeScale(state.stageReef)}).`,
      `- Pieces per week = ${metres3(state.weeklyReef)} / ${metres3(state.moduleSize)} = ${count(state.weeklyPieces)} pieces.`,
      `- Rough weekly weight = ${metres3(state.weeklySpoil)} x ${SANDMASS_TONNES_PER_M3} t/m3 = ${tonnes(state.weeklyWeight)} (${weightScale(state.weeklyWeight)}).`,
      "",
      "## Quick Interlock Building Sketches",
      "",
      "Each example uses: sketch volume / selected block envelope = approximate unique blocks.",
      "",
      "| Example | Sketch volume | Formula | Approx. blocks | 100 m batch comparison | Current week |",
      "| --- | ---: | --- | ---: | --- | --- |",
      ...state.scenarioResults.map((item) => `| ${item.title} | ${metres3(item.volume)} | ${item.formula} | ${count(item.blocks)} | ${item.batch} | about ${setCount(item.weeklySets)} sets |`),
      "",
      "## Example Component Split Formulas",
      "",
      "These are editable sketch allocations. They show how the headline block count could be built from parts, while leaving room for better site survey, robotics, service holes and community design.",
      "",
      ...state.scenarioResults.flatMap((item) => [
        `### ${item.title}`,
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
    if (!input || name === "modulePreset") return;
    input.addEventListener("input", () => {
      if (name === "moduleSize" && inputs.modulePreset) inputs.modulePreset.value = "custom";
      update();
    });
    input.addEventListener("change", update);
  });

  if (inputs.modulePreset) {
    inputs.modulePreset.addEventListener("change", () => {
      if (inputs.modulePreset.value !== "custom") inputs.moduleSize.value = inputs.modulePreset.value;
      update();
    });
  }

  if (exportButton) exportButton.addEventListener("click", downloadMarkdown);

  updateSandwormBridge();
  update();
})();
