# 003 — Primes as the Basis of Arithmetic

## Video title
Primes Are the Basis of Arithmetic (And It's Linear Algebra)

## Mathematical concept
The Fundamental Theorem of Arithmetic gives every positive integer a unique prime factorization. This is analogous to representing vectors in terms of a basis. By mapping integers to exponent vectors over the primes, multiplication becomes vector addition and exponentiation becomes scalar multiplication. Extending exponents to all integers captures the positive rationals. The resulting structure is not a vector space (scalars would leave Q>0) but a free Z-module with the primes as basis: Q>0 ≅ ⊕_p Z.

## Intended duration
~2 minutes (approx 1:53 rendered at 60fps)

## Target audience
Math-curious viewers on TikTok, Instagram Reels, YouTube Shorts.

## Aspect ratio
9:8 (1080×960) — designed to sit alongside speaker footage in a 9:16 composition.

## Scene breakdown

### Scene 1 — Hook / FTA (0:00–0:12)
60 appears, factorizes into 2²·3·5. Introduce the Fundamental Theorem of Arithmetic.

### Scene 2 — Primes as building blocks (0:12–0:22)
Show that primes are the "atoms" of integers. Multiple numbers factorized. The primes are highlighted.

### Scene 3 — What is a basis? (0:22–0:38)
Introduce R³ with standard basis e₁, e₂, e₃. Show (a,b,c) = ae₁ + be₂ + ce₃. Basis elements generate the space.

### Scene 4 — The prime coordinate system (0:38–0:55)
Map 60 = 2²·3·5 to exponent vector (2,1,1,0,0,…). The "aha" moment: exponents as coordinates.

### Scene 5 — Multiplication becomes addition (0:55–1:20)
12·18 = 216. Show (2,1,0,…) + (1,2,0,…) = (3,3,0,…) corresponding to 2³·3³. Includes:
- exponent coordinate morph from factorizations (2²·3 → (2,1,0,…))
- the vector addition of coordinates
- a progressive comparison table reveal (addition↔multiplication, scalar mult↔exponentiation, basis↔primes)

### Scene 6 — Negative exponents (1:20–1:35)
Allow negative exponents → fractions appear. 12/25 = 2²·3·5⁻² → (2,1,-2,0,…). Q>0 ↔ Z^(N).

### Scene 7 — The scalar problem (1:35–1:45)
Can this be a vector space? Exponents restricted to Z. Z is not a field → not a vector space.

### Scene 8 — The module (1:45–1:55)
Free Z-module. Q>0 ≅ ⊕_p Z. Primes as basis elements of the module.

### Scene 9 — The logarithm twist (1:55–2:05)
ln(ab) = ln(a) + ln(b). ln turns multiplication into addition. ln(primes) as independent directions.

### Scene 10 — Final isomorphism & hook (2:05–2:20)
Q>0 ≅ ⊕_p Z. "Primes are a basis of Q>0 as a free Z-module." Hook: what about all real exponents?
Timings are approximate; approximated scene boundaries from the render.

## Rendering
```bash
# Preview (fast)
manim -pql videos/003-primes-as-basis/scene.py PrimesAsBasis

# Final quality
manim -pqh videos/003-primes-as-basis/scene.py PrimesAsBasis
```

Rendered output (media/ is gitignored):
- Preview: `media/videos/scene/960p15/PrimesAsBasis.mp4` — 1080×960, 15fps
- Final: `media/videos/scene/960p60/PrimesAsBasis.mp4` — 1080×960 (9:8), 60fps, ~1:53

## Production status
- [x] Implementation
- [x] Preview render reviewed
- [x] Final render
- [ ] Published
