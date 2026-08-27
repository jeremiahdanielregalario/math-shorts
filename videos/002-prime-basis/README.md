# 002 — Are Prime Numbers the Basis Vectors of Arithmetic?

## Video title
Are Prime Numbers the Basis Vectors of Arithmetic?

## Mathematical concept
Prime factorization as a coordinate system. The Fundamental Theorem of Arithmetic implies every positive integer maps to an exponent vector over the primes. Multiplication becomes vector addition. Extending to negative exponents gives Q>0 ↔ Z^(N), making Q>0 a free Z-module with primes as basis — not a vector space, because scalar multiplication by non-integer rationals leaves Q>0.

## Intended duration
~90 seconds

## Target audience
Math-curious viewers on TikTok, Instagram Reels, YouTube Shorts.

## Visual storyboard

### Hook
60 appears → breaks into 2²·3·5 → primes float separately.
"What if primes are basis vectors?"

### Scene 1 — Every number has coordinates
Show 12, 18, 20, 45, 100 with factorizations → exponent vectors.

### Scene 2 — Multiplication becomes addition
12·18 = 216. Exponent vectors add: (2,1,0) + (1,2,0) = (3,3,0).

### Scene 3 — But something is missing
Powers of 2 → allow negative exponents → fractions appear.

### Scene 4 — Enter the positive rationals
12/25 = 2²·3·5⁻² → vector (2,1,-2,0,…). Q>0 ↔ Z^(N).

### Scene 5 — So is this a vector space?
The operations look right, but something is off.

### Scene 6 — The scalar problem
2^(1/2) = √2 ∉ Q. 2^π leaves Q entirely.

### Scene 7 — Enter the module
Vector space → Module. Z^(N) is a free Z-module. Primes = basis.

### Scene 8 — The logarithm twist
ln turns multiplication into addition. ln(primes) are independent directions.

### Scene 9 — Still not quite
Real span of ln(primes) is bigger than ln(Q>0). Free abelian group, not R-vector space.

### Ending
Q>0 ≅ ⊕_p Z. Primes are basis directions of multiplication.
"Prime factorization is linear algebra if multiplication is addition."
Part 2 hook: What if we allowed ALL real exponents?

## Rendering
```bash
# Preview (fast)
manim -pql videos/002-prime-basis/scene.py PrimesAsBasis

# Final quality
manim -pqh videos/002-prime-basis/scene.py PrimesAsBasis
```

## Production status
- [x] Implementation
- [ ] Preview render reviewed
- [ ] Final render
- [ ] Published
