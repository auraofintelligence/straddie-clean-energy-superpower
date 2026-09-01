# Straddie Clean Energy Superpower

<!-- github-organisation:start -->

## Project links and history

- First substantive build: 14 June 2026.
- GitHub repository: [straddie-clean-energy-superpower](https://github.com/auraofintelligence/straddie-clean-energy-superpower).
- Public site: [visit the public site](https://auraofintelligence.github.io/straddie-clean-energy-superpower/).

## Related public projects

Each link below reflects an evidenced family, lineage or direct connection. This project has 7 relevant public connections.

### Aura Systems Image Atlas source projects

- [aura-systems-image-atlas](https://github.com/auraofintelligence/aura-systems-image-atlas) - [public page](https://auraofintelligence.github.io/aura-systems-image-atlas/) - source project represented in this visual atlas.
- [civilisation-of-sand](https://github.com/auraofintelligence/civilisation-of-sand) - [public page](https://auraofintelligence.github.io/civilisation-of-sand/) - shared community programme.
- [Sandworm-subterranean-systems](https://github.com/auraofintelligence/sandworm-subterranean-systems) - [public page](https://auraofintelligence.github.io/sandworm-subterranean-systems/) - explicit cross-reference, shared community programme.
- [shared-table-initiative](https://github.com/auraofintelligence/shared-table-initiative) - [public page](https://auraofintelligence.github.io/shared-table-initiative/) - shared community programme.
- [straddie-makerspace-lab](https://github.com/auraofintelligence/straddie-makerspace-lab) - [public page](https://auraofintelligence.github.io/straddie-makerspace-lab/) - explicit cross-reference, shared community programme.

### Circular making and local infrastructure

- [grain-by-grain](https://github.com/auraofintelligence/grain-by-grain) - [public page](https://auraofintelligence.github.io/grain-by-grain/) - shared community programme.
- [straddie-tip-loop-lab](https://github.com/auraofintelligence/straddie-tip-loop-lab) - [public page](https://auraofintelligence.github.io/straddie-tip-loop-lab/) - explicit cross-reference, shared community programme.

<!-- github-organisation:end -->

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
- links to maker-space, Sandworm, ferry terminal lab, Grants Lab, community wealth, Legal Memory Workbench and Ready S.E.T. Trust Hub

## How it works

The source of truth is `tools/build_site.py`.

In simple terms:

1. The Python file stores the page list, builder list, source links and companion repo links.
2. Running it writes the public `.html` pages.
3. The builder pages let a visitor fill in a small form, preview Markdown, copy it, or download a `.md` file.
4. Hero images live in `assets/img/heroes/`.

## Optimise images

```powershell
python tools\optimise_images.py
```

The script keeps the hero images as WebP and caps oversized files so the site loads faster on phones.

## Local build

```powershell
python tools\build_site.py
```

Then open `index.html`, or run:

```powershell
python -m http.server 4179 --bind 127.0.0.1
```

## Public posture

This is an exploration workbench. It is not an approval claim, engineering design, cultural authority statement, environmental approval, legal advice, financial advice or fire-safety design.

## Licence

This repo uses the [Straddie Clean Energy Superpower Public Licence](LICENCE.md), a custom public-interest licence adapted from the Strange But True public-infrastructure pattern. Public non-commercial learning, sharing, forking and community adaptation are welcome with attribution. Commercial use, extractive repackaging and false endorsement are reserved.
