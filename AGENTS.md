# AGENTS.md — Math Shorts

This file is the persistent instruction manual for AI coding agents working on this repository.

## Project overview

**Math Shorts** is a collection of short-form mathematical video projects. Each video is an animation built with [Manim Community Edition](https://www.manim.community/) targeting vertical phone-screen platforms:

- TikTok
- Instagram Reels
- YouTube Shorts

The project owner is a mathematics graduate who provides mathematical ideas, storyboards, and creative direction. The coding agent's role is to implement those ideas as clean Manim code.

## Repository structure

```
math-shorts/
├── pyproject.toml          # Project config and dependencies
├── .gitignore
├── README.md               # Setup and usage instructions
├── AGENTS.md               # This file
├── shared/                 # Reusable styles and helpers
│   ├── __init__.py
│   ├── styles.py           # Colors, sizing, visual constants
│   └── helpers.py          # Reusable Manim helper functions
├── videos/                 # One directory per video
│   └── NNN-short-name/
│       ├── README.md       # Video concept, storyboard, status
│       ├── scene.py        # Manim scene class(es)
│       └── assets/         # External assets (only if needed)
└── tests/
```

## Vertical 9:16 format

All videos target **vertical 9:16** (1080×1920 pixels). This is the primary format.

Every scene must be configured for vertical rendering:

```python
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
```

Key rules for vertical layout:
- Keep important content away from edges (use `SAFE_MARGIN` from `shared/styles.py`).
- Avoid small text — it must be readable on a phone screen.
- Default `MATH_FONT_SIZE` is 48; adjust as needed but stay legible.
- Do **not** assume 16:9 horizontal format.

## Mathematical correctness

This is a priority. Rules:

- Never silently change mathematical statements.
- Never simplify an argument in a way that makes it mathematically false.
- Never invent mathematical claims.
- Preserve notation provided by the project owner.
- Prefer mathematically meaningful animations over decorative ones.
- If a requested statement appears incorrect or ambiguous, point it out before modifying it.

The project owner owns the mathematical creative direction. The agent implements it faithfully.

## Animation philosophy

Animations should prioritize **mathematical understanding**. Prefer:

- Transformations, geometric motion, graphs, number lines
- Coordinate systems, vector fields, function transformations
- Equation transformations, morphing mathematical objects
- Highlighting relationships, parameter changes
- Limits and convergence, geometric interpretations

Avoid:
- Random camera movement, flashy transitions
- Particle effects, decorative animations
- Bouncing objects, visual noise

A viewer should understand something mathematical from the visual structure alone.

## Coding conventions

### Naming

Use clear, mathematically meaningful names:

```python
circle          # a circle
number_line     # a number line
theta_label     # a label for theta
function_graph  # a plotted function
initial_point   # starting point
final_point     # ending point
```

Avoid vague names like `thing`, `obj1`, `stuff`.

### Code structure

- Keep scenes readable.
- Break large scenes into helper methods within the scene class.
- Only extract reusable functions into `shared/` when a pattern is genuinely reused across videos.
- Do **not** prematurely abstract. Keep it simple.

### Style

- Follow standard Python conventions.
- Line length: 88 characters (Ruff default).
- Import from `manim` directly: `from manim import *`.

## Rendering

### Preview (fast)

```bash
manim -pql videos/NNN-name/scene.py SceneName
```

### Final (high quality)

```bash
manim -pqh videos/NNN-name/scene.py SceneName
```

Output goes to `media/` which is gitignored.

## Shared utilities (`shared/`)

Currently minimal by design. Will grow as repeated patterns emerge across videos.

- `styles.py` — visual constants (colors, font sizes, margins, frame config)
- `helpers.py` — reusable Manim helper functions

Do not add to these until there is a clear, demonstrated need.

## Generated files

- `media/` — all rendered output, **never** commit
- `__pycache__/` — Python cache, **never** commit
- `.env` files — **never** commit

The repository tracks source code and assets, not generated output.

## When creating a new video

1. Read this file (you're reading it now).
2. Inspect existing shared utilities in `shared/`.
3. Inspect similar existing videos for patterns.
4. Understand the mathematical storyboard provided.
5. Implement incrementally.
6. Test with a preview render.
7. Fix any errors.
8. Keep the implementation consistent with existing visual language.

Do not modify unrelated videos or rewrite working infrastructure without reason.
