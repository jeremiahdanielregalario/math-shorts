from manim import *

config.frame_height = 8
config.frame_width = 9
config.pixel_height = 960
config.pixel_width = 1080

ACCENT = "#58C4DD"
HIGHLIGHT = "#FFE64D"
RED = "#FF5555"
GREEN = "#A6E22E"
PURPLE = "#9A72AC"
SUBTLE = "#888888"
ORANGE = "#FF8C00"

CONTENT_MAX_Y = 3.2
CONTENT_MIN_Y = -3.2


def clamp(mob):
    if mob.get_top()[1] > CONTENT_MAX_Y:
        mob.shift(DOWN * (mob.get_top()[1] - CONTENT_MAX_Y))
    if mob.get_bottom()[1] < CONTENT_MIN_Y:
        mob.shift(UP * (CONTENT_MIN_Y - mob.get_bottom()[1]))
    return mob


class PrimesAsBasis(Scene):
    """Primes as the basis of arithmetic.

    A ~2.5 minute 9:8 short exploring prime factorization as the
    analogue of a basis, culminating in Q>0 as a free Z-module.
    """

    def construct(self):
        self.camera.background_color = BLACK
        self.scene_1_hook_fta()
        self.scene_2_building_blocks()
        self.scene_3_what_is_a_basis()
        self.scene_4_prime_coordinates()
        self.scene_5_multiplication_adds()
        self.scene_6_negative_exponents()
        self.scene_7_is_it_a_vector_space()
        self.scene_8_the_module()
        self.scene_9_logarithm()
        self.scene_10_finale()

    # ── Small helpers ────────────────────────────────────────────────────────

    def place(self, mob, y):
        mob.move_to(y * UP)
        clamp(mob)
        return mob

    def reveal(self, mobs, lag=0.15, run=1.0):
        if not isinstance(mobs, list):
            mobs = [mobs]
        self.play(
            LaggedStart(*[FadeIn(m, shift=UP * 0.25) for m in mobs], lag_ratio=lag),
            run_time=run,
        )

    def box(self, mob, color=HIGHLIGHT, buff=0.25):
        return SurroundingRectangle(mob, color=color, buff=buff, corner_radius=0.12)

    def clear(self, *mobs):
        if mobs:
            self.play(*[FadeOut(m) for m in mobs])
        else:
            self.clear_scene()

    # ── Scene 1: Hook / Fundamental Theorem of Arithmetic ────────────────────

    def scene_1_hook_fta(self):
        sixty = MathTex("60", font_size=80, color=WHITE)
        self.place(sixty, 1.2)
        self.play(Write(sixty), run_time=0.7)
        self.wait(0.4)

        fact = MathTex(
            "60", "=", "2^2", "\\cdot", "3", "\\cdot", "5",
            font_size=56,
        )
        fact[2].set_color(ACCENT)
        fact[4].set_color(ACCENT)
        fact[6].set_color(ACCENT)
        self.place(fact, 1.2)
        self.play(TransformMatchingTex(sixty, fact), run_time=1.3)
        self.wait(0.6)

        primes = VGroup(
            MathTex("2", font_size=72, color=ACCENT),
            MathTex("3", font_size=72, color=ACCENT),
            MathTex("5", font_size=72, color=ACCENT),
        ).arrange(RIGHT, buff=2.0)
        self.place(primes, -0.5)
        self.play(FadeOut(fact), run_time=0.3)
        self.reveal([p for p in primes], lag=0.2)
        self.wait(0.4)

        fta_text = MathTex(
            "\\text{Fundamental Theorem of Arithmetic:}",
            font_size=30,
        )
        self.place(fta_text, 1.8)
        self.play(Write(fta_text), run_time=0.6)

        every = MathTex(
            "\\text{every } n \\in \\mathbb{Z}_{>0}", "\\ = \\prod_p p^{v_p(n)}",
            font_size=30,
        )
        every[1].set_color(ACCENT)
        self.place(every, -1.8)
        self.play(Write(every), run_time=0.9)
        self.wait(1.2)

        hook_text = VGroup(
            MathTex("\\text{What if primes are }", font_size=34),
            MathTex("\\text{basis vectors?}", font_size=34, color=HIGHLIGHT),
        ).arrange(RIGHT, buff=0.2)
        self.place(hook_text, -0.5)
        self.play(
            FadeOut(primes), FadeOut(fta_text), FadeOut(every),
            run_time=0.3,
        )
        self.play(Write(hook_text), run_time=0.8)
        self.wait(1.0)

        foundation = MathTex(
            "\\text{so every integer is a unique}",
            font_size=26,
        )
        self.place(foundation, 0.8)
        self.play(FadeOut(hook_text), run_time=0.3)
        self.play(Write(foundation), run_time=0.6)

        combo = MathTex(
            "\\text{combination of primes}",
            font_size=30, color=HIGHLIGHT,
        )
        self.place(combo, -0.6)
        self.play(FadeIn(combo, shift=UP), run_time=0.5)
        self.wait(1.0)
        self.clear(*self.mobjects)

    # ── Scene 2: Primes as building blocks ───────────────────────────────────

    def scene_2_building_blocks(self):
        title = MathTex(
            "\\text{Primes: the building blocks}",
            font_size=34, color=HIGHLIGHT,
        )
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.6)

        intro = MathTex(
            "\\text{every integer is built from primes}",
            font_size=26,
        )
        self.place(intro, 0.8)
        self.play(Write(intro), run_time=0.6)
        self.wait(0.3)

        nums = [
            MathTex("12", "=", "2^2 \\cdot 3", font_size=26),
            MathTex("18", "=", "2 \\cdot 3^2", font_size=26),
            MathTex("20", "=", "2^2 \\cdot 5", font_size=26),
            MathTex("45", "=", "3^2 \\cdot 5", font_size=26),
            MathTex("100", "=", "2^2 \\cdot 5^2", font_size=26),
        ]
        for n in nums:
            n[2].set_color(ACCENT)
        grid = VGroup(*nums).arrange(DOWN, buff=0.65)
        scaled = grid
        if grid.width > 6.5:
            scaled = grid.copy().scale(6.5 / grid.width)
        self.place(scaled, -0.8)
        self.reveal([m for m in scaled], lag=0.15, run=1.4)
        self.wait(1.0)

        per_nums = MathTex("12", "\\cdot", "18", "=", "216", font_size=34)
        per_nums[4].set_color(WHITE)
        self.place(per_nums, -2.4)
        self.play(Write(per_nums), run_time=0.7)
        self.wait(0.5)

        insight = MathTex(
            "\\text{The exponents are the coordinates}",
            font_size=28, color=GREEN,
        )
        self.place(insight, 1.2)
        self.play(
            FadeOut(scaled), FadeOut(intro), FadeOut(per_nums),
            run_time=0.4,
        )
        self.play(Write(insight), run_time=0.6)
        self.wait(1.0)
        self.clear(*self.mobjects)

    # ── Scene 3: What is a basis? ────────────────────────────────────────────

    def scene_3_what_is_a_basis(self):
        title = VGroup(
            MathTex("\\text{Now: what is a }", font_size=32),
            MathTex("\\text{basis?}", font_size=32, color=ACCENT),
        ).arrange(RIGHT, buff=0.2)
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.6)

        r3 = MathTex(
            "\\mathbb{R}^3", "\\text{ over }", "\\mathbb{R}",
            font_size=36,
        )
        r3[0].set_color(ACCENT)
        self.place(r3, 1.2)
        self.play(Write(r3), run_time=0.7)
        self.wait(0.4)

        basis = VGroup(
            MathTex("\\mathbf{e}_1 = (1,0,0)", font_size=26),
            MathTex("\\mathbf{e}_2 = (0,1,0)", font_size=26),
            MathTex("\\mathbf{e}_3 = (0,0,1)", font_size=26),
        ).arrange(RIGHT, buff=1.4)
        basis[0].set_color(GREEN)
        basis[1].set_color(GREEN)
        basis[2].set_color(GREEN)
        self.place(basis, 0.0)
        self.reveal([basis[0], basis[1], basis[2]], lag=0.2)
        self.wait(0.5)

        aha = MathTex(
            "(a,b,c)", "=", "a", "\\mathbf{e}_1",
            "+", "b", "\\mathbf{e}_2", "+", "c", "\\mathbf{e}_3",
            font_size=30,
        )
        aha[1].set_color(WHITE)
        aha[0].set_color(HIGHLIGHT)
        self.place(aha, -2.4)
        self.play(Write(aha), run_time=1.0)
        self.wait(0.8)

        example = MathTex(
            "(2,5,7)", "=", "2\\mathbf{e}_1 + 5\\mathbf{e}_2 + 7\\mathbf{e}_3",
            font_size=26,
        )
        example[0].set_color(GREEN)
        self.place(example, -0.6)
        self.play(
            FadeOut(aha),
            run_time=0.3,
        )
        self.reveal([example[0], example[1], example[2]], lag=0.2)
        self.wait(0.8)

        label = MathTex(
            "\\underbrace{\\text{basis elements}}_{\\text{generate the space}}",
            font_size=24,
        )
        self.place(label, 1.0)
        self.play(
            FadeOut(basis),
            run_time=0.3,
        )
        self.play(FadeIn(label), run_time=0.5)
        self.wait(1.2)
        self.clear(*self.mobjects)

    # ── Scene 4: The prime coordinate system ─────────────────────────────────

    def scene_4_prime_coordinates(self):
        title = MathTex(
            "\\text{Primes as a basis?}",
            font_size=32, color=HIGHLIGHT,
        )
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.6)

        intro = MathTex(
            "\\text{Index coordinates by the primes:}",
            font_size=26,
        )
        self.place(intro, 1.2)
        self.play(Write(intro), run_time=0.6)

        primes = VGroup(
            MathTex("2", font_size=40, color=ACCENT),
            MathTex("3", font_size=40, color=ACCENT),
            MathTex("5", font_size=40, color=ACCENT),
            MathTex("7", font_size=40, color=ACCENT),
            MathTex("11", font_size=40, color=ACCENT),
            MathTex("13", font_size=40, color=ACCENT),
            MathTex("\\cdots", font_size=40, color=ACCENT),
        ).arrange(RIGHT, buff=0.9)
        self.place(primes, 0.0)
        self.reveal([p for p in primes], lag=0.1, run=1.2)
        self.wait(0.6)

        example = MathTex(
            "60", "\\longleftrightarrow", "(2,1,1,0,0,\\ldots)",
            font_size=30,
        )
        example[2].set_color(GREEN)
        self.place(example, -2.0)
        self.play(Write(example), run_time=0.9)
        self.wait(0.6)

        annot = MathTex(
            "\\underbrace{(2,\\ 1,\\ 1,\\ 0,\\ 0,\\ldots)}_{\\text{exponent vector}}",
            font_size=24,
        )
        self.place(annot, 1.0)
        self.play(
            FadeOut(primes), FadeOut(intro),
            run_time=0.3,
        )
        self.play(FadeIn(annot), run_time=0.5)
        self.wait(0.8)

        independence = MathTex(
            "\\text{primes = independent directions}",
            font_size=26, color=HIGHLIGHT,
        )
        self.place(independence, -1.4)
        self.play(FadeIn(independence, shift=UP), run_time=0.5)
        self.wait(1.2)
        self.clear(*self.mobjects)

    # ── Scene 5: Multiplication becomes addition ─────────────────────────────

    def scene_5_multiplication_adds(self):
        title = VGroup(
            MathTex("\\text{Multiplication }", font_size=32, color=ACCENT),
            MathTex("\\leftrightarrow", font_size=32),
            MathTex("\\text{ addition}", font_size=32, color=HIGHLIGHT),
        ).arrange(RIGHT, buff=0.2)
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.7)

        twelve = MathTex(
            "12", "=", "2^2", "\\cdot", "3",
            font_size=26,
        )
        eighteen = MathTex(
            "18", "=", "2", "\\cdot", "3^2",
            font_size=26,
        )
        eqs = VGroup(twelve, eighteen).arrange(DOWN, buff=0.5)
        self.place(eqs, 0.8)
        self.reveal([twelve, eighteen], lag=0.3)
        self.wait(0.8)

        # Morph factorization into exponent coordinates
        seventy = MathTex(
            "12", "=", "2^2", "\\cdot", "3",
            "\\;\\longrightarrow\\;", "(2,1,0,\\ldots)",
            font_size=26,
        )
        seventy[-1].set_color(GREEN)
        self.play(TransformMatchingTex(twelve, seventy), run_time=1.2)
        self.wait(0.8)

        overflow = MathTex(
            "18", "=", "2", "\\cdot", "3^2",
            "\\;\\longrightarrow\\;", "(1,2,0,\\ldots)",
            font_size=26,
        )
        overflow[-1].set_color(GREEN)
        self.play(TransformMatchingTex(eighteen, overflow), run_time=1.2)
        self.wait(1.0)
        self.play(FadeOut(seventy), FadeOut(overflow), run_time=0.3)

        # Now multiply 12 x 18
        mult = VGroup(
            MathTex("12", font_size=30),
            MathTex("\\times", font_size=30),
            MathTex("18", font_size=30),
            MathTex("=", font_size=30),
            MathTex("216", font_size=30, color=HIGHLIGHT),
        ).arrange(RIGHT, buff=0.35)
        self.place(mult, 1.2)
        self.play(Write(mult), run_time=0.7)
        self.wait(0.8)

        # Factor 216
        fact216 = MathTex(
            "216", "=", "2^3", "\\cdot", "3^3",
            font_size=30,
        )
        fact216[2].set_color(ACCENT)
        fact216[4].set_color(ACCENT)
        self.place(fact216, -0.2)
        self.play(Write(fact216), run_time=0.8)
        self.wait(0.5)

        # The key morph: turn the prime factors into exponent coordinates
        self.play(
            FadeOut(mult), FadeOut(fact216), FadeOut(eqs),
            run_time=0.4,
        )

        vec12 = MathTex("(2,1,0,\\ldots)", font_size=28, color=GREEN)
        plus = MathTex("+", font_size=32)
        vec18 = MathTex("(1,2,0,\\ldots)", font_size=28, color=GREEN)
        eq = MathTex("=", font_size=32)
        vec36 = MathTex("(3,3,0,\\ldots)", font_size=28, color=GREEN)
        add_line = VGroup(vec12, plus, vec18, eq, vec36).arrange(RIGHT, buff=0.3)
        self.place(add_line, 0.6)
        self.play(Write(vec12), run_time=0.5)
        self.play(Write(plus), run_time=0.3)
        self.play(Write(vec18), run_time=0.5)
        self.play(Write(eq), run_time=0.3)
        self.play(Write(vec36), run_time=0.6)
        self.wait(0.8)

        # Corresponds back to 216
        back = MathTex(
            "\\longleftrightarrow", "216", "=", "2^3 \\cdot 3^3",
            font_size=26,
        )
        back[0].set_color(WHITE)
        back[2].set_color(WHITE)
        self.place(back, -1.6)
        self.play(Write(back), run_time=0.8)
        self.wait(0.8)
        self.clear(*self.mobjects)

        # Progressive comparison reveal
        table_ops = VGroup(
            MathTex("\\text{addition}", font_size=28),
            MathTex("\\leftrightarrow", font_size=28, color=HIGHLIGHT),
            MathTex("\\text{multiplication}", font_size=28),
        ).arrange(RIGHT, buff=0.3)
        self.place(table_ops, 0.8)
        self.reveal([table_ops[0], table_ops[1], table_ops[2]], lag=0.3)
        self.wait(0.8)

        table_sclar = VGroup(
            MathTex("\\text{scalar mult.}", font_size=28),
            MathTex("\\leftrightarrow", font_size=28, color=HIGHLIGHT),
            MathTex("\\text{exponentiation}", font_size=28),
        ).arrange(RIGHT, buff=0.3)
        self.place(table_sclar, -0.2)
        self.reveal([table_sclar[0], table_sclar[1], table_sclar[2]], lag=0.3)
        self.wait(0.8)

        table_basis = VGroup(
            MathTex("\\text{basis}", font_size=28),
            MathTex("\\leftrightarrow", font_size=28, color=HIGHLIGHT),
            MathTex("\\text{primes}", font_size=28),
        ).arrange(RIGHT, buff=0.3)
        self.place(table_basis, -1.2)
        self.reveal([table_basis[0], table_basis[1], table_basis[2]], lag=0.3)

        box = self.box(VGroup(table_ops, table_sclar, table_basis), color=HIGHLIGHT)
        self.play(Create(box), run_time=0.6)
        self.wait(1.6)
        self.clear(*self.mobjects)

    # ── Scene 6: Negative exponents → positive rationals ─────────────────────

    def scene_6_negative_exponents(self):
        title = MathTex(
            "\\text{What about fractions?}",
            font_size=32, color=HIGHLIGHT,
        )
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.6)

        claim = MathTex(
            "\\text{exponents so far: } 0, 1, 2, 3, \\ldots",
            font_size=26,
        )
        self.place(claim, 1.2)
        self.play(Write(claim), run_time=0.6)

        neg = MathTex("2^{-1}", "=", "\\frac{1}{2}", font_size=40)
        neg[0].set_color(RED)
        self.place(neg, -0.4)
        self.play(
            FadeOut(claim), run_time=0.3,
        )
        self.play(Write(neg), run_time=0.7)
        self.wait(0.5)

        neg2 = MathTex("2^{-2}", "=", "\\frac{1}{4}", font_size=32)
        neg2[0].set_color(RED)
        self.place(neg2, -1.8)
        self.play(Write(neg2), run_time=0.6)
        self.wait(0.5)

        rational = MathTex(
            "\\frac{12}{25}", "=", "2^2 \\cdot 3^1 \\cdot 5^{-2}",
            "\\longleftrightarrow", "(2,1,-2,0,\\ldots)",
            font_size=30,
        )
        rational[4].set_color(GREEN)
        self.place(rational, -2.7)
        self.play(
            FadeOut(neg), FadeOut(neg2),
            run_time=0.4,
        )
        self.play(Write(rational), run_time=1.1)
        self.wait(1.0)

        outcome = MathTex(
            "\\text{Hence: } \\mathbb{Q}_{>0}",
            font_size=28, color=GREEN,
        )
        self.place(outcome, -0.4)
        self.play(FadeIn(outcome, shift=UP), run_time=0.5)
        self.wait(0.8)
        self.clear(*self.mobjects)

    # ── Scene 7: Is this a vector space? ─────────────────────────────────────

    def scene_7_is_it_a_vector_space(self):
        question = VGroup(
            MathTex("\\mathbb{Q}_{>0}", font_size=40),
            MathTex("\\text{? a }", font_size=36),
            MathTex("\\text{vector space}", font_size=36, color=HIGHLIGHT),
        ).arrange(RIGHT, buff=0.2)
        self.place(question, 1.2)
        box = self.box(question, color=HIGHLIGHT)
        self.play(Write(question), run_time=0.8)
        self.play(Create(box), run_time=0.5)
        self.wait(0.8)

        # Operations correspond
        op1 = MathTex("\\text{add} \\leftrightarrow \\text{multiply}", font_size=26)
        op1[0].set_color(GREEN)
        self.place(op1, -0.6)
        self.play(Write(op1), run_time=0.6)

        op2 = MathTex(
            "\\text{scalar mult.} \\leftrightarrow \\text{exponentiation}",
            font_size=26,
        )
        op2[0].set_color(GREEN)
        self.place(op2, -1.8)
        self.play(Write(op2), run_time=0.6)
        self.wait(0.8)

        but = MathTex(
            "\\text{...but exponents live in }",
            font_size=26,
        )
        z = MathTex("\\mathbb{Z}", font_size=32)
        but_grp = VGroup(but, z).arrange(RIGHT, buff=0.2)
        self.place(but_grp, -0.8)
        self.play(
            FadeOut(question), FadeOut(box), FadeOut(op1), FadeOut(op2),
            run_time=0.3,
        )
        self.play(Write(but), Write(z), run_time=0.7)
        self.wait(0.6)

        z_not_field = MathTex(
            "\\mathbb{Z}", "\\text{ is not a field}",
            font_size=30,
        )
        z_not_field[0].set_color(RED)
        self.place(z_not_field, -2.0)
        self.play(FadeOut(but_grp), run_time=0.3)
        self.play(Write(z_not_field), run_time=0.6)
        self.wait(0.8)

        conclusion = MathTex(
            "\\text{not a vector space,}",
            font_size=30, color=RED,
        )
        self.place(conclusion, -0.8)
        self.play(FadeIn(conclusion, shift=UP), run_time=0.5)
        self.wait(1.0)
        self.clear(*self.mobjects)

    # ── Scene 8: The module ──────────────────────────────────────────────────

    def scene_8_the_module(self):
        title = MathTex(
            "\\text{A free } \\mathbb{Z} \\text{-module}",
            font_size=34, color=GREEN,
        )
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.7)
        self.wait(0.4)

        iso = MathTex(
            "\\mathbb{Q}_{>0}", "\\cong", "\\bigoplus_p \\mathbb{Z}",
            font_size=36,
        )
        iso[1].set_color(WHITE)
        iso[0].set_color(ACCENT)
        iso[2].set_color(GREEN)
        self.place(iso, 0.8)
        self.play(Write(iso), run_time=1.1)
        self.wait(0.5)

        basis = MathTex(
            "\\text{primes} \\longleftrightarrow \\text{basis elements}",
            font_size=28, color=HIGHLIGHT,
        )
        self.place(basis, -0.6)
        self.play(Write(basis), run_time=0.7)
        self.wait(0.6)

        module = MathTex(
            "\\text{free } \\mathbb{Z} \\text{-module under multiplication}",
            font_size=26,
        )
        self.place(module, -2.0)
        self.play(Write(module), run_time=0.7)
        self.wait(0.8)

        abelian = MathTex(
            "\\text{= free abelian group}",
            font_size=26,
        )
        abelian.set_color(GREEN)
        self.place(abelian, -2.6)
        self.play(FadeIn(abelian, shift=UP), run_time=0.5)
        self.wait(1.0)
        self.clear(*self.mobjects)

    # ── Scene 9: The logarithm twist ─────────────────────────────────────────

    def scene_9_logarithm(self):
        title = MathTex(
            "\\text{One more beautiful angle}",
            font_size=32,
        )
        self.place(title, 2.2)
        self.play(Write(title), run_time=0.6)

        log_rule = MathTex(
            "\\ln(ab)", "=", "\\ln a", "+", "\\ln b",
            font_size=34,
        )
        log_rule[4].set_color(HIGHLIGHT)
        self.place(log_rule, 0.6)
        self.play(Write(log_rule), run_time=0.8)
        self.wait(0.5)

        expand = MathTex(
            "\\ln\\left(2^{a_1}3^{a_2}5^{a_3}\\cdots\\right)",
            "=",
            "a_1\\ln2 + a_2\\ln3 + a_3\\ln5 + \\cdots",
            font_size=28,
        )
        expand[2].set_color(GREEN)
        self.place(expand, -0.6)
        self.play(Write(expand), run_time=1.1)
        self.wait(0.6)

        insight = MathTex(
            "\\text{multiplication} \\rightarrow \\text{addition}",
            font_size=28, color=ACCENT,
        )
        self.place(insight, -2.0)
        self.play(FadeIn(insight, shift=UP), run_time=0.5)
        self.wait(1.2)
        self.clear(*self.mobjects)

    # ── Scene 10: Finale ─────────────────────────────────────────────────────

    def scene_10_finale(self):
        boxed_iso = MathTex(
            "\\mathbb{Q}_{>0}", "\\cong", "\\bigoplus_{p\\ \\text{prime}} \\mathbb{Z}",
            font_size=38,
        )
        boxed_iso[0].set_color(ACCENT)
        boxed_iso[1].set_color(WHITE)
        boxed_iso[2].set_color(GREEN)
        self.place(boxed_iso, 1.8)
        box = self.box(boxed_iso, color=HIGHLIGHT)
        self.play(Write(boxed_iso), run_time=1.0)
        self.play(Create(box), run_time=0.5)
        self.wait(0.8)

        primes = VGroup(
            MathTex("2", font_size=40, color=ACCENT),
            MathTex("3", font_size=40, color=ACCENT),
            MathTex("5", font_size=40, color=ACCENT),
            MathTex("7", font_size=40, color=ACCENT),
            MathTex("\\cdots", font_size=40, color=ACCENT),
        ).arrange(RIGHT, buff=0.6)
        self.place(primes, 0.2)
        self.reveal([p for p in primes], lag=0.1)

        punch = MathTex(
            "\\text{Primes are a basis of } \\mathbb{Q}_{>0}",
            font_size=28,
        )
        punch[0].set_color(WHITE)
        self.place(punch, -1.4)
        self.play(Write(punch), run_time=0.8)
        self.wait(1.0)

        not_vs = MathTex(
            "\\text{... as a free } \\mathbb{Z} \\text{-module.}",
            font_size=30, color=HIGHLIGHT,
        )
        self.place(not_vs, -2.6)
        self.play(FadeIn(not_vs, shift=UP), run_time=0.6)
        self.wait(1.6)

        # Part 2 hook
        self.play(
            *[FadeOut(m) for m in (boxed_iso, box, primes, punch, not_vs)],
            run_time=0.4,
        )

        hook = MathTex(
            "\\text{What if we allow }", "\\text{all real exponents?}",
            font_size=34,
        )
        hook[1].set_color(HIGHLIGHT)
        self.place(hook, 1.0)
        self.play(Write(hook), run_time=0.8)
        self.wait(0.6)

        examples = VGroup(
            MathTex("2^{\\sqrt{2}}", font_size=36),
            MathTex("3^{\\pi}", font_size=36),
            MathTex("5^{e}", font_size=36),
            MathTex("\\cdots", font_size=36),
        ).arrange(RIGHT, buff=0.7)
        examples.set_color(ACCENT)
        self.place(examples, -0.8)
        self.reveal([e for e in examples], lag=0.15)
        self.wait(1.0)

        closing = MathTex(
            "\\text{That is linear algebra!}",
            font_size=30,
        )
        self.place(closing, -1.8)
        self.play(
            FadeOut(examples),
            run_time=0.4,
        )
        self.play(Write(closing), run_time=0.7)
        self.wait(1.2)

        final_box = self.box(closing, color=HIGHLIGHT)
        self.play(Create(final_box), run_time=0.5)
        self.wait(1.5)
        self.clear(*self.mobjects)
