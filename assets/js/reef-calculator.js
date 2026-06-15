(function () {
  const root = document.querySelector("[data-reef-calculator]");
  if (!root) return;

  const number = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 0 });
  const decimal = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 2 });
  const FORMING_FACTOR = 1.15;
  const SANDMASS_TONNES_PER_M3 = 1.6;

  const inputs = {
    diameter: root.querySelector('[data-calc-input="diameter"]'),
    weeklyAdvance: root.querySelector('[data-calc-input="weeklyAdvance"]'),
    weeks: root.querySelector('[data-calc-input="weeks"]'),
    reefShare: root.querySelector('[data-calc-input="reefShare"]'),
    modulePreset: root.querySelector('[data-calc-input="modulePreset"]'),
    moduleSize: root.querySelector('[data-calc-input="moduleSize"]'),
    focus: root.querySelector('[data-calc-input="focus"]'),
  };

  const output = (name, value) => {
    const target = root.querySelector(`[data-calc-out="${name}"]`);
    if (target) target.textContent = value;
  };

  const metres3 = (value) => {
    if (Math.abs(value) < 100) return `${decimal.format(value)} m3`;
    return `${number.format(Math.round(value))} m3`;
  };

  const tonnes = (value) => {
    if (Math.abs(value) < 100) return `${decimal.format(value)} t`;
    return `${number.format(Math.round(value))} t`;
  };

  const count = (value) => number.format(Math.max(0, Math.round(value)));
  const count1 = (value) => decimal.format(Math.max(0, value));

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
    const weeklySpoil = area * weeklyAdvance;
    const weeklyDiverted = weeklySpoil * (reefShare / 100);
    const weeklyReef = weeklyDiverted * FORMING_FACTOR;
    const stageReef = weeklyReef * weeks;
    const stageDiverted = weeklyDiverted * weeks;
    const weeklyPieces = moduleSize > 0 ? weeklyReef / moduleSize : 0;
    const weeklyWeight = weeklySpoil * SANDMASS_TONNES_PER_M3;
    const timePer100Hours = weeklyAdvance > 0 ? (100 / weeklyAdvance) * 7 * 24 : 0;

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

  updateSandwormBridge();
  update();
})();
