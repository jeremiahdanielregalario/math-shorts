# Math Shorts

Short-form mathematical videos created with [Manim Community Edition](https://www.manim.community/).

## Target platforms

- TikTok
- Instagram Reels
- YouTube Shorts

## Technology

- Python 3.11+
- Manim Community Edition

## Repository structure

```
math-shorts/
├── README.md
├── AGENTS.md
├── pyproject.toml
├── .gitignore
├── videos/           # Each video lives in its own numbered directory
│   └── 001-example/
├── shared/           # Reusable styles and helpers
│   ├── styles.py
│   └── helpers.py
└── tests/
```

## Setup

```bash
# Clone the repository
git clone <repo-url>
cd math-shorts

# Create a virtual environment
python -m venv .venv

# Activate it
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS / Linux:
source .venv/bin/activate

# Install dependencies
pip install -e .

# (Optional) Install dev tools
pip install -e ".[dev]"
```

### Requirements

- Python 3.11+
- [FFmpeg](https://ffmpeg.org/) installed and on your PATH
- A LaTeX distribution (e.g. MiKTeX, TeX Live) for math text rendering

## Rendering

Every video directory contains a `scene.py` with one or more Manim `Scene` classes.

### Preview render (fast, low quality)

```bash
manim -pql videos/001-example/scene.py CircleToSquare
```

### Final render (high quality)

```bash
manim -pqh videos/001-example/scene.py CircleToSquare
```

The `-p` flag opens the video after rendering. Remove it for headless rendering.

Rendered output goes to `media/` which is gitignored.

## Development workflow

```
Idea
→ Mathematical storyboard
→ Manim implementation
→ Preview render
→ Review
→ Iterate
→ Final render
→ Publish
```

## Adding a new video

1. Create a directory under `videos/` with the pattern `NNN-short-name/`:

   ```
   mkdir videos/002-pythagorean-theorem
   ```

2. Add a `scene.py` with your Manim scene class(es).

3. Add a `README.md` documenting the video concept and status.

4. If the video needs external assets (fonts, images, etc.), put them in an `assets/` subdirectory.

5. Import shared styles from `shared/` if useful, but keep the video self-contained.

## Rendered output

Rendered videos are placed in `media/` and are **not** committed to Git. The repository tracks source code and assets needed to reproduce a video, not the output files.
