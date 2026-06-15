# Straddie Clean Energy Superpower

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
