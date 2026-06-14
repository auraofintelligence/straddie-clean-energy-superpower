from __future__ import annotations

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
HERO_DIR = ROOT / "assets" / "img" / "heroes"

MAX_WIDTHS = {
    "ferry-gateway.webp": 1800,
}
DEFAULT_MAX_WIDTH = 1600
QUALITY = 76


def target_width(path: Path) -> int:
    return MAX_WIDTHS.get(path.name, DEFAULT_MAX_WIDTH)


def resize_for_web(image: Image.Image, max_width: int) -> Image.Image:
    image = image.convert("RGB")
    if image.width <= max_width:
        return image
    height = round(image.height * (max_width / image.width))
    return image.resize((max_width, height), Image.Resampling.LANCZOS)


def optimise(path: Path) -> Path:
    output = path.with_suffix(".webp")
    max_width = target_width(output)
    if path.suffix.lower() == ".webp":
        with Image.open(path) as image:
            if image.width <= max_width:
                return path

    temp_output = output.with_suffix(".tmp.webp")
    with Image.open(path) as image:
        web_image = resize_for_web(image, max_width)
        web_image.save(temp_output, "WEBP", quality=QUALITY, method=6)
    temp_output.replace(output)
    if path.suffix.lower() != ".webp":
        path.unlink()
    return output


def main() -> None:
    outputs = []
    for path in sorted(HERO_DIR.iterdir()):
        if path.suffix.lower() not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        output = optimise(path)
        outputs.append(output)

    for path in outputs:
        with Image.open(path) as image:
            print(f"{path.relative_to(ROOT)}\t{path.stat().st_size:,} bytes\t{image.width}x{image.height}")


if __name__ == "__main__":
    main()
