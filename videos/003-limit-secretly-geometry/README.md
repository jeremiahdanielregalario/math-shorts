# 003 — A Limit That Is Secretly Geometry

## Video title
A Limit That Is Secretly Geometry

## Mathematical concept
The limit `lim_{n→∞} n·tan(π/n) = π` is the area of a regular n-gon with apothem 1, approaching the area of the unit circle.

## Intended duration
~60–90 seconds

## Target audience
Math-curious viewers on TikTok, Instagram Reels, YouTube Shorts.

## Visual storyboard
1. The mysterious limit is revealed with no explanation
2. A regular hexagon appears with center lines drawn
3. The apothem is introduced and labeled
4. A single triangle slice is analyzed (central angle π/n)
5. Tangent appears from the right triangle
6. The polygon area formula derives A_n = n·tan(π/n)
7. The polygon morphs through n = 3 → 6 → 12 → 24 → 48 → 96
8. The limiting unit circle appears with area π
9. The original limit is resolved

## Rendering
```bash
# Preview (fast)
manim -pql videos/003-limit-secretly-geometry/scene.py LimitSecretlyGeometry

# Final quality (60fps)
manim -pqh --fps 60 videos/003-limit-secretly-geometry/scene.py LimitSecretlyGeometry
```

## Production status
- [x] Implemented
- [ ] Reviewed
- [ ] Final render
- [ ] Published
