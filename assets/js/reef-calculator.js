(function () {
  const root = document.querySelector("[data-reef-calculator]");
  if (!root) return;

  const number = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 0 });
  const decimal = new Intl.NumberFormat("en-AU", { maximumFractionDigits: 2 });

  const inputs = {
    diameter: root.querySelector('[data-calc-input="diameter"]'),
    weeklyAdvance: root.querySelector('[data-calc-input="weeklyAdvance"]'),
    weeks: root.querySelector('[data-calc-input="weeks"]'),
    reefShare: root.querySelector('[data-calc-input="reefShare"]'),
    bulking: root.querySelector('[data-calc-input="bulking"]'),
    modulePreset: root.querySelector('[data-calc-input="modulePreset"]'),
    moduleSize: root.querySelector('[data-calc-input="moduleSize"]'),
  };

  const output = (name, value) => {
    const target = root.querySelector(`[data-calc-out="${name}"]`);
    if (target) target.textContent = value;
  };

  const checked = (name) => {
    const toggle = root.querySelector(`[data-calc-toggle="${name}"]`);
    return Boolean(toggle && toggle.checked);
  };

  const metres3 = (value) => {
    if (Math.abs(value) < 100) return `${decimal.format(value)} m3`;
    return `${number.format(Math.round(value))} m3`;
  };
  const count = (value) => number.format(Math.max(0, Math.round(value)));

  const formatAdvance = (metresPerWeek) => {
    if (metresPerWeek >= 1000) return `${decimal.format(metresPerWeek / 1000)} km/week`;
    return `${number.format(metresPerWeek)} m/week`;
  };

  const formatDuration = (hours) => {
    if (hours < 24) return `${decimal.format(hours)} h`;
    return `${decimal.format(hours / 24)} days`;
  };

  const makeList = (label, items) => {
    return `<div><strong>${label}</strong><p>${items.join(", ")}</p></div>`;
  };

  const pathwayNames = {
    oyster: "oyster reef",
    living: "living shoreline",
    surf: "surf bank",
    dune: "stable dune support",
    island: "artificial island / platform",
    surface: "quick-fit surface blocks",
    construction: "construction interlock blocks",
    meeting: "stone circle and community meeting pieces",
    homes: "glass and silicate home products",
    automation: "automation and sensing",
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
    const bulking = Number(inputs.bulking.value);
    const moduleSize = Number(inputs.moduleSize.value);
    const presetLabel = inputs.modulePreset && inputs.modulePreset.selectedOptions.length
      ? inputs.modulePreset.selectedOptions[0].textContent.replace(/\s+-\s+.*$/, "")
      : "Custom size";

    const area = Math.PI * (diameter / 2) ** 2;
    const per100 = area * 100;
    const weeklySpoil = area * weeklyAdvance;
    const weeklyDiverted = weeklySpoil * (reefShare / 100);
    const weeklyReef = weeklyDiverted * bulking;
    const stageReef = weeklyReef * weeks;
    const stageDiverted = weeklyDiverted * weeks;
    const weeklyModules = moduleSize > 0 ? weeklyReef / moduleSize : 0;
    const timePer100Hours = weeklyAdvance > 0 ? (100 / weeklyAdvance) * 7 * 24 : 0;

    output("diameter", `${decimal.format(diameter)} m`);
    output("weeklyAdvance", formatAdvance(weeklyAdvance));
    output("weeks", number.format(weeks));
    output("reefShare", `${number.format(reefShare)}%`);
    output("bulking", `${decimal.format(bulking)}x`);
    output("modulePreset", presetLabel);
    output("moduleSize", metres3(moduleSize));
    output("per100", metres3(per100));
    output("timePer100", formatDuration(timePer100Hours));
    output("weeklySpoil", metres3(weeklySpoil));
    output("weeklyReef", metres3(weeklyReef));
    output("stageReef", metres3(stageReef));
    output("weeklyModules", count(weeklyModules));
    output("avoided", metres3(stageDiverted));

    const active = Object.keys(pathwayNames).filter((key) => checked(key));
    const activeNames = active.map((key) => pathwayNames[key]);
    const stageText = activeNames.length ? activeNames.join(", ") : "open material questions";

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
      `Could ${metres3(stageDiverted)} of raw tunnel material become ${metres3(stageReef)} of formed media across ${number.format(weeks)} week${weeks === 1 ? "" : "s"} for ${stageText}? At ${formatAdvance(weeklyAdvance)}, the next 100 m arrives in about ${formatDuration(timePer100Hours)}.`
    );

    const equipment = weeklySpoil < 250
      ? ["micro-borer or service robot", "small carts", "maker-space test bays", "desktop moulds", "material jars"]
      : weeklySpoil < 1500
        ? ["compact TBM", "robot carts", "mobile screener", "small batch mixer", "quick-fit moulds", "covered laydown racks"]
        : weeklySpoil < 10000
          ? ["Loop-scale TBM", "conveyors", "screening train", "batch yard", "robotic block handling", "barge or truck scheduling"]
          : ["multi-shift boring system", "automated spoil routing", "dedicated material yard", "continuous batching", "robotic placement fleet", "public dashboard"];

    const skills = ["survey and measurement", "materials testing", "batch records", "site logistics", "community explanation"];
    if (checked("oyster")) skills.push("shell recycling", "oyster restoration knowledge");
    if (checked("living")) skills.push("living-shoreline planting", "sediment observation");
    if (checked("surf")) skills.push("bathymetry reading", "surfer observation", "wave modelling");
    if (checked("dune")) skills.push("dune ecology", "sand fencing and vegetation care");
    if (checked("island")) skills.push("settlement monitoring", "staged landform records");
    if (checked("surface")) skills.push("interlock design", "service-channel layout", "robotic assembly", "move-and-repair planning");
    if (checked("construction")) skills.push("quick-fit construction blocks", "assembly and disassembly planning", "hidden services layout");
    if (checked("meeting")) skills.push("stone-circle layout", "public meeting geometry", "artistic finishing");
    if (checked("homes")) skills.push("glass tests", "ceramic forming", "home-fit design", "resident product passports");

    const automation = ["volume dashboard", "QR or RFID batch tags", "photo records", "load-cell or weighbridge feed"];
    if (checked("automation")) {
      automation.push("drone photogrammetry", "bathymetry passes", "sensor buoys", "weather and turbidity logs", "robotic pick-and-place logs");
    }
    if (checked("surf")) automation.push("wave-camera review");
    if (checked("oyster") || checked("living")) automation.push("water-quality sensors");
    if (checked("surface")) automation.push("service-map records", "block unlock history", "inspection-lid register");
    if (checked("construction")) automation.push("robotic placement logs", "block passport records", "service-void scan records");
    if (checked("meeting")) automation.push("layout templates", "community install records", "finish and repair notes");
    if (checked("homes")) automation.push("resident request queue", "recipe version records", "repair and return logs");

    const workMap = root.querySelector("[data-calc-out=\"workMap\"]");
    if (workMap) {
      workMap.innerHTML = [
        makeList("Equipment that could appear", equipment),
        makeList("Human skills that could grow", skills),
        makeList("Automation that could keep the story visible", automation),
      ].join("");
    }
  };

  Object.entries(inputs).forEach(([name, input]) => {
    if (!input || name === "modulePreset") return;
    input.addEventListener("input", () => {
      if (name === "moduleSize" && inputs.modulePreset) inputs.modulePreset.value = "custom";
      update();
    });
  });
  if (inputs.modulePreset) {
    inputs.modulePreset.addEventListener("change", () => {
      if (inputs.modulePreset.value !== "custom") inputs.moduleSize.value = inputs.modulePreset.value;
      update();
    });
  }
  root.querySelectorAll("[data-calc-toggle]").forEach((toggle) => toggle.addEventListener("change", update));
  updateSandwormBridge();
  update();
})();
