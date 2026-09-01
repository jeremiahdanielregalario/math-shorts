# 004 — Arithmetic as Linear Algebra (Primes as Basis)

## Video title
Primes Are Basis Vectors — Arithmetic as Linear Algebra

## Mathematical concept
Prime factorization is the arithmetic analogue of a basis. The Fundamental
Theorem of Arithmetic turns every positive integer into a unique list of
prime exponents — an exponent-coordinate vector. Multiplication becomes
coordinate-wise addition, and exponentiation becomes scalar multiplication.
Extending exponents to all of Z captures every positive rational, making
Q>0 isomorphic to the direct sum of Z over the primes. Since Z is not a
field, this is not a vector space — it is a free Z-module (equivalently, a
free abelian group) with the primes as its basis.

## Intended duration
~1:45 (approx 104s rendered at 30fps; authored as a ~3 minute storyline)

## Target audience
Math-curious viewers on TikTok, Instagram Reels, YouTube Shorts.

## Aspect ratio
9:8 (1350×1200) — designed to sit above/alongside speaker footage in a
9:16 composition. This is the *claude-authored* alternate implementation
of the same storyline as `003-primes-as-basis` (distinct visual language:
isometric R³ arrows, exponent-extraction morph, ROSE negative-exponent
accents).

## Scene breakdown

1. **Fundamental Theorem of Arithmetic (0:00–0:20)** — 60 factorizes into
   2²·3·5; uniqueness is stated.
2. **Primes as building blocks (0:20–0:45)** — a flurry of factorizations
   (12, 18, 100); the curiosity about arbitrary integer exponents is raised,
   then set aside.
3. **What is a basis? (0:45–1:15)** — isometric-style R³ with e₁, e₂, e₃
   arrows; (a,b,c) = ae₁ + be₂ + ce₃.
4. **The prime coordinate system (1:15–1:45)** — 60 = 2²·3¹·5¹; exponents
   are extracted and dropped into coordinate slots (2,1,1,0,0,…) indexed by
   the primes.
5. **Multiplication becomes addition (1:45–2:10)** — 12 and 18 as vectors;
   12×18=216 becomes (2,1,0,…)+(1,2,0,…)=(3,3,0,…) with 216 = 2³·3³.
6. **Correspondence table (progressive reveal)** — addition↔multiplication,
   scalar multiplication↔exponentiation, basis↔primes.
7. **Can this be a vector space? (2:10–2:35)** — exponents only grow; 2⁻¹=½
   pushes out of the integers.
8. **Positive rationals (2:35–2:55)** — 12/25 = 2²·3¹·5⁻² ↔ (2,1,-2,0,…);
   Q>0 ≅ ⊕_p Z.
9. **Module conclusion (2:55–3:15)** — Z^(N) = ⊕_p Z, "Z is not a field",
   not a vector space but a free Z-module; primes are a basis of Q>0.
10. **Closing curiosity** — what happens if we change the scalars?

## Rendering
```bash
# Preview (fast)
manim -pql videos/004-arithmetic-linear-algebra/scene.py PrimesAsBasis

# Final quality
manim -pqh videos/004-arithmetic-linear-algebra/scene.py PrimesAsBasis
```

The frame aspect ratio is derived automatically from pixel_width/pixel_height
(1350×1200 = 9:8), so aspect ratio is preserved at any -q quality.

## Production status
- [x] Implementation
- [x] Preview render reviewed
- [x] Final render
- [ ] Published