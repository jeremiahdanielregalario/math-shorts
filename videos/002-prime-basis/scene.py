from manim import *

# ── Vertical 9:16 configuration ──────────────────────────────────────────────
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

# ── Colors ────────────────────────────────────────────────────────────────────
MATH_COL = "#58C4DD"
HIGHLIGHT = "#FFFF00"
GREEN_COL = "#83C167"
RED_COL = "#FC6255"
PURPLE_COL = "#9A72AC"
ORANGE_COL = "#FF8C00"
SUBTITLE_COL = "#AAAAAA"

# ── Layout (vertical 9×16 frame, top ~4 units reserved for facecam) ──────────
# Frame y-range: -8 to +8. Facecam occupies roughly y=3.5 to y=8.
# All content lives below y=3.
CONTENT_TOP = 2.5


class PrimesAsBasis(Scene):
    """Are Prime Numbers the Basis Vectors of Arithmetic?

    A ~90-second vertical video exploring the analogy between
    prime factorization and basis vectors, leading to the
    conclusion that Q_>0 is a free Z-module with primes as basis.
    """

    def construct(self):
        self.camera.background_color = BLACK
        self.hook()
        self.scene_1_every_number_has_coordinates()
        self.scene_2_multiplication_becomes_addition()
        self.scene_3_but_something_is_missing()
        self.scene_4_enter_positive_rationals()
        self.scene_5_so_is_this_a_vector_space()
        self.scene_6_the_scalar_problem()
        self.scene_7_enter_the_module()
        self.scene_8_the_logarithm_twist()
        self.scene_9_still_not_quite()
        self.ending()

    # ── Utility helpers ───────────────────────────────────────────────────────

    def make_title(self, text, color=WHITE, font_size=42):
        return Text(text, font_size=font_size, color=color).to_edge(
            UP, buff=4.5
        )

    def make_subtitle(self, text, color=SUBTITLE_COL, font_size=28):
        return Text(text, font_size=font_size, color=color).to_edge(
            DOWN, buff=1.5
        )

    def clear_scene(self, *mobs):
        if mobs:
            self.play(*[FadeOut(m) for m in mobs])
        else:
            self.play(*[FadeOut(m) for m in self.mobjects])

    def show_boxed(self, tex_str, color=MATH_COL, font_size=40):
        mob = MathTex(tex_str, color=color, font_size=font_size)
        box = SurroundingRectangle(
            mob, color=color, buff=0.25, corner_radius=0.1
        )
        return VGroup(mob, box)

    # ── HOOK ──────────────────────────────────────────────────────────────────

    def hook(self):
        number = MathTex("60", font_size=96, color=WHITE)
        self.play(Write(number), run_time=0.8)
        self.wait(0.5)

        factorization = MathTex(
            "60", "=", "2^2", "\\cdot", "3", "\\cdot", "5",
            font_size=60, color=MATH_COL,
        )
        self.play(TransformMatchingTex(number, factorization), run_time=1.2)
        self.wait(0.5)

        primes = VGroup(
            MathTex("2", font_size=72, color=GREEN_COL),
            MathTex("3", font_size=72, color=GREEN_COL),
            MathTex("5", font_size=72, color=GREEN_COL),
        ).arrange(RIGHT, buff=2.0).shift(DOWN * 2.5)

        self.play(
            FadeOut(factorization),
            LaggedStart(
                *[FadeIn(p, shift=UP * 0.3) for p in primes],
                lag_ratio=0.2,
            ),
            run_time=1.0,
        )
        self.wait(0.4)

        hook_text = Text(
            "What if primes are\nbasis vectors?",
            font_size=38,
            color=HIGHLIGHT,
        ).to_edge(DOWN, buff=2.0)
        self.play(Write(hook_text), run_time=1.0)
        self.wait(1.2)

        not_literal = Text(
            "Not literally.\nBut the analogy is deep.",
            font_size=30,
            color=SUBTITLE_COL,
        ).to_edge(DOWN, buff=2.0)
        self.play(
            FadeOut(hook_text),
            FadeIn(not_literal),
            run_time=0.8,
        )
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 1 — Every number has coordinates ───────────────────────────────

    def scene_1_every_number_has_coordinates(self):
        title = self.make_title("Every number has coordinates")
        self.play(Write(title), run_time=0.6)

        # Show integers
        nums = VGroup(
            MathTex("12", font_size=52, color=WHITE),
            MathTex("18", font_size=52, color=WHITE),
            MathTex("20", font_size=52, color=WHITE),
            MathTex("45", font_size=52, color=WHITE),
            MathTex("100", font_size=52, color=WHITE),
        ).arrange(RIGHT, buff=1.2).shift(UP * 0.5)
        self.play(LaggedStart(*[Write(n) for n in nums], lag_ratio=0.12), run_time=1.0)

        # Show factorizations below each
        facts = VGroup(
            MathTex("2^2 \\cdot 3", font_size=30, color=MATH_COL),
            MathTex("2 \\cdot 3^2", font_size=30, color=MATH_COL),
            MathTex("2^2 \\cdot 5", font_size=30, color=MATH_COL),
            MathTex("3^2 \\cdot 5", font_size=30, color=MATH_COL),
            MathTex("2^2 \\cdot 5^2", font_size=30, color=MATH_COL),
        )
        for i, f in enumerate(facts):
            f.next_to(nums[i], DOWN, buff=0.3)
        self.play(
            LaggedStart(*[FadeIn(f, shift=UP * 0.2) for f in facts], lag_ratio=0.15),
            run_time=1.2,
        )
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

        # FTA statement
        fta = MathTex(
            "\\text{Every } n \\in \\mathbb{Z}_{>0}",
            font_size=40, color=WHITE,
        )
        fta2 = MathTex(
            "= p_1^{a_1} \\cdot p_2^{a_2} \\cdots",
            font_size=40, color=MATH_COL,
        )
        fta_group = VGroup(fta, fta2).arrange(RIGHT, buff=0.3).shift(UP * 1.5)
        self.play(Write(fta), run_time=0.8)
        self.play(Write(fta2), run_time=0.8)
        self.wait(1.0)

        # Show 12 → 2^2·3 → (2,1,0,…)
        twelve = MathTex("12", font_size=52, color=WHITE).shift(ORIGIN)
        self.play(Write(twelve), run_time=0.5)

        twofact = MathTex(
            "= 2^2 \\cdot 3", font_size=44, color=MATH_COL,
        ).next_to(twelve, RIGHT, buff=0.3)
        self.play(Write(twofact), run_time=0.6)
        self.wait(0.8)

        # Transform into vector
        arrow = MathTex("\\longleftrightarrow", font_size=40, color=WHITE)
        vec_label = MathTex(
            "(2,1,0,0,\\ldots)", font_size=44, color=GREEN_COL,
        )
        vec_row = VGroup(twelve, twofact, arrow, vec_label).arrange(
            RIGHT, buff=0.4
        ).shift(ORIGIN)
        self.play(
            FadeOut(twelve), FadeOut(twofact),
            run_time=0.3,
        )
        self.play(vec_row.animate.move_to(DOWN * 1.0), run_time=0.5)

        coord_label = MathTex(
            "\\text{coordinates: } 2, 3, 5, 7, \\ldots",
            font_size=30, color=SUBTITLE_COL,
        ).next_to(vec_row, DOWN, buff=0.8)
        self.play(FadeIn(coord_label), run_time=0.6)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 2 — Multiplication becomes addition ────────────────────────────

    def scene_2_multiplication_becomes_addition(self):
        title = self.make_title("Multiplication → Addition")
        self.play(Write(title), run_time=0.6)

        # 12 and 18 with factorizations
        twelve = MathTex("12", "=", "2^2", "\\cdot", "3", font_size=44, color=MATH_COL)
        eighteen = MathTex(
            "18", "=", "2", "\\cdot", "3^2", font_size=44, color=MATH_COL,
        )
        eqs = VGroup(twelve, eighteen).arrange(DOWN, buff=0.6).shift(UP * 0.5)
        self.play(FadeIn(eqs), run_time=1.0)
        self.wait(0.5)

        # Exponent vectors — placed clearly below the factorizations
        vec12 = MathTex("(2,1,0,\\ldots)", font_size=38, color=GREEN_COL)
        vec18 = MathTex("(1,2,0,\\ldots)", font_size=38, color=GREEN_COL)
        vecs = VGroup(vec12, vec18).arrange(DOWN, buff=0.4).shift(DOWN * 2.5)
        self.play(FadeIn(vec12), FadeIn(vec18), run_time=0.6)
        self.wait(0.8)

        # Multiplication result — placed below the vectors
        mult_result = MathTex(
            "12 \\cdot 18 = 216", font_size=44, color=WHITE,
        ).shift(DOWN * 4.5)
        self.play(Write(mult_result), run_time=0.7)
        self.wait(0.5)

        result_factor = MathTex(
            "= 2^3 \\cdot 3^3", font_size=40, color=MATH_COL,
        ).next_to(mult_result, DOWN, buff=0.3)
        self.play(Write(result_factor), run_time=0.6)
        self.wait(0.5)

        # Vector addition — replace everything with the clean equation
        self.play(
            FadeOut(eqs), FadeOut(vec12), FadeOut(vec18),
            FadeOut(mult_result), FadeOut(result_factor),
            run_time=0.3,
        )

        plus = MathTex("+", font_size=44, color=WHITE)
        equals = MathTex("=", font_size=44, color=WHITE)
        vec_sum = MathTex("(3,3,0,\\ldots)", font_size=40, color=GREEN_COL)
        vec_eq = VGroup(
            MathTex("(2,1,0,\\ldots)", font_size=38, color=GREEN_COL),
            plus,
            MathTex("(1,2,0,\\ldots)", font_size=38, color=GREEN_COL),
            equals,
            vec_sum,
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 1.5)
        self.play(FadeIn(vec_eq), run_time=0.6)
        self.wait(1.0)

        # Key insight
        insight = VGroup(
            MathTex("\\text{multiplication}", font_size=36, color=WHITE),
            MathTex("\\longleftrightarrow", font_size=36, color=HIGHLIGHT),
            MathTex("\\text{addition}", font_size=36, color=WHITE),
        ).arrange(RIGHT, buff=0.4).shift(DOWN * 3.5)
        box = SurroundingRectangle(
            insight, color=HIGHLIGHT, buff=0.25, corner_radius=0.1
        )
        self.play(Write(insight), Create(box), run_time=1.0)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 3 — But something is missing ───────────────────────────────────

    def scene_3_but_something_is_missing(self):
        title = self.make_title("But something is missing...", color=RED_COL)
        self.play(Write(title), run_time=0.6)

        # Show powers of 2
        powers = VGroup(
            MathTex("2^1", font_size=40, color=MATH_COL),
            MathTex("2^2", font_size=40, color=MATH_COL),
            MathTex("2^3", font_size=40, color=MATH_COL),
            MathTex("2^4", font_size=40, color=MATH_COL),
            MathTex("2^5", font_size=40, color=MATH_COL),
        ).arrange(RIGHT, buff=0.8).shift(UP * 0.0)
        self.play(
            LaggedStart(*[Write(p) for p in powers], lag_ratio=0.12),
            run_time=1.0,
        )
        self.wait(0.5)

        # Highlight the exponents
        exp_label = MathTex(
            "\\text{exponents: } 1, 2, 3, 4, 5",
            font_size=30, color=HIGHLIGHT,
        ).next_to(powers, DOWN, buff=0.5)
        self.play(FadeIn(exp_label), run_time=0.5)
        self.wait(1.0)
        self.clear_scene(*self.mobjects)

        # The problem: we need negative exponents
        problem = MathTex(
            "2^3", font_size=52, color=MATH_COL,
        ).shift(UP * 1.0)
        self.play(Write(problem), run_time=0.5)
        self.wait(0.5)

        neg_exp = MathTex(
            "2^{-1} = \\frac{1}{2}", font_size=48, color=GREEN_COL,
        ).next_to(problem, DOWN, buff=1.0)
        self.play(Write(neg_exp), run_time=0.8)
        self.wait(0.8)

        # Show more negative exponents
        more_neg = VGroup(
            MathTex("2^{-2} = \\frac{1}{4}", font_size=36, color=GREEN_COL),
            MathTex("2^{-3} = \\frac{1}{8}", font_size=36, color=GREEN_COL),
        ).arrange(DOWN, buff=0.4).next_to(neg_exp, DOWN, buff=0.6)
        self.play(
            LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in more_neg], lag_ratio=0.2),
            run_time=0.8,
        )
        self.wait(1.0)

        insight = Text(
            "Allow negative exponents\n→ fractions appear!",
            font_size=32, color=HIGHLIGHT,
        ).to_edge(DOWN, buff=2.0)
        self.play(Write(insight), run_time=0.8)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 4 — Enter the positive rationals ───────────────────────────────

    def scene_4_enter_positive_rationals(self):
        title = self.make_title("Enter the positive rationals")
        self.play(Write(title), run_time=0.6)

        # Factor 12/25
        frac = MathTex(
            "\\frac{12}{25}", font_size=52, color=WHITE,
        ).shift(UP * 0.5)
        self.play(Write(frac), run_time=0.6)

        step1 = MathTex(
            "= \\frac{2^2 \\cdot 3}{5^2}", font_size=44, color=MATH_COL,
        ).next_to(frac, DOWN, buff=0.5)
        self.play(Write(step1), run_time=0.7)
        self.wait(0.5)

        step2 = MathTex(
            "= 2^2 \\cdot 3^1 \\cdot 5^{-2}",
            font_size=44, color=MATH_COL,
        ).next_to(step1, DOWN, buff=0.5)
        self.play(Write(step2), run_time=0.7)
        self.wait(0.5)

        # Vector form
        vec = MathTex(
            "\\longleftrightarrow (2, 1, -2, 0, \\ldots)",
            font_size=40, color=GREEN_COL,
        ).next_to(step2, DOWN, buff=0.7)
        self.play(Write(vec), run_time=0.8)
        self.wait(1.0)
        self.clear_scene(*self.mobjects)

        # The big picture
        big = MathTex(
            "\\mathbb{Q}_{>0}",
            font_size=52, color=WHITE,
        ).shift(UP * 1.0)
        self.play(Write(big), run_time=0.6)

        iso = MathTex(
            "\\longleftrightarrow",
            font_size=44, color=HIGHLIGHT,
        ).next_to(big, DOWN, buff=0.6)
        self.play(Write(iso), run_time=0.4)

        coords = MathTex(
            "\\mathbb{Z}^{(\\mathbb{N})}",
            font_size=52, color=GREEN_COL,
        ).next_to(iso, DOWN, buff=0.6)
        self.play(Write(coords), run_time=0.6)
        self.wait(0.5)

        explanation = MathTex(
            "\\text{primes = basis directions}",
            font_size=36, color=PURPLE_COL,
        ).next_to(coords, DOWN, buff=0.8)
        box = SurroundingRectangle(
            explanation, color=PURPLE_COL, buff=0.2, corner_radius=0.1
        )
        self.play(Write(explanation), Create(box), run_time=0.8)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 5 — So is this a vector space? ─────────────────────────────────

    def scene_5_so_is_this_a_vector_space(self):
        question = self.show_boxed(
            "\\mathbb{Q}_{>0}\\ ?\\ \\text{Vector Space}",
            color=HIGHLIGHT,
            font_size=48,
        )
        question.shift(UP * 0.5)
        self.play(Write(question), run_time=0.8)
        self.wait(1.0)

        # Show the correspondence
        ops = VGroup(
            MathTex(
                "\\times \\longleftrightarrow +",
                font_size=40, color=MATH_COL,
            ),
            MathTex(
                "\\text{exponentiation} \\longleftrightarrow \\text{scalar mult.}",
                font_size=36, color=MATH_COL,
            ),
        ).arrange(DOWN, buff=0.6).shift(DOWN * 2.0)
        self.play(
            LaggedStart(*[Write(o) for o in ops], lag_ratio=0.3),
            run_time=1.2,
        )
        self.wait(1.0)

        # The answer
        answer = Text(
            "Almost...\nBut not quite.",
            font_size=40, color=RED_COL,
        ).shift(DOWN * 4.5)
        self.play(Write(answer), run_time=0.8)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 6 — The scalar problem ─────────────────────────────────────────

    def scene_6_the_scalar_problem(self):
        title = self.make_title("The scalar problem", color=RED_COL)
        self.play(Write(title), run_time=0.6)

        # Show basis element
        basis = MathTex("2", font_size=60, color=MATH_COL).shift(UP * 0.5)
        self.play(Write(basis), run_time=0.5)
        self.wait(0.5)

        # Attempt sqrt(2)
        attempt1 = MathTex(
            "2^{1/2} = \\sqrt{2}", font_size=48, color=WHITE,
        ).next_to(basis, DOWN, buff=0.8)
        self.play(Write(attempt1), run_time=0.7)

        warning1 = MathTex(
            "\\sqrt{2} \\notin \\mathbb{Q}_{>0}",
            font_size=40, color=RED_COL,
        ).next_to(attempt1, DOWN, buff=0.5)
        warning_box = SurroundingRectangle(
            warning1, color=RED_COL, buff=0.2, corner_radius=0.1
        )
        self.play(Write(warning1), Create(warning_box), run_time=0.7)
        self.wait(1.0)

        # Attempt 2^pi
        attempt2 = MathTex(
            "2^{\\pi}", font_size=48, color=WHITE,
        ).shift(DOWN * 3.0)
        self.play(Write(attempt2), run_time=0.6)

        warning2 = MathTex(
            "2^{\\pi} \\notin \\mathbb{Q}",
            font_size=40, color=RED_COL,
        ).next_to(attempt2, DOWN, buff=0.5)
        warning_box2 = SurroundingRectangle(
            warning2, color=RED_COL, buff=0.2, corner_radius=0.1
        )
        self.play(Write(warning2), Create(warning_box2), run_time=0.7)
        self.wait(1.0)

        # The problem
        problem_text = MathTex(
            "\\text{Scalar mult. leaves } \\mathbb{Q}_{>0}",
            font_size=36, color=SUBTITLE_COL,
        ).to_edge(DOWN, buff=1.5)
        self.play(FadeIn(problem_text), run_time=0.6)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 7 — Enter the module ───────────────────────────────────────────

    def scene_7_enter_the_module(self):
        # "VECTOR SPACE" transforms into "MODULE"
        vs_text = Text(
            "VECTOR SPACE", font_size=56, color=RED_COL,
        ).shift(UP * 0.5)
        self.play(Write(vs_text), run_time=0.6)
        self.wait(0.8)

        mod_text = Text(
            "MODULE", font_size=56, color=GREEN_COL,
        ).shift(UP * 0.5)
        self.play(Transform(vs_text, mod_text), run_time=0.8)
        self.wait(0.5)

        # Show Z^(N)
        zn = MathTex(
            "\\mathbb{Z}^{(\\mathbb{N})}",
            font_size=52, color=GREEN_COL,
        ).next_to(vs_text, DOWN, buff=1.0)
        self.play(Write(zn), run_time=0.6)
        self.wait(0.5)

        # The isomorphism
        iso = self.show_boxed(
            "\\mathbb{Q}_{>0} \\cong \\bigoplus_{p} \\mathbb{Z}",
            color=HIGHLIGHT,
            font_size=40,
        )
        iso.shift(DOWN * 2.5)
        self.play(Write(iso), run_time=0.8)
        self.wait(0.5)

        # Comparison table
        table = VGroup(
            MathTex(
                "\\text{Vector space}", font_size=34, color=SUBTITLE_COL,
            ),
            MathTex("\\leftrightarrow", font_size=34, color=HIGHLIGHT),
            MathTex(
                "\\text{Module}", font_size=34, color=SUBTITLE_COL,
            ),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 4.5)
        table2 = VGroup(
            MathTex(
                "\\mathbb{R}^n", font_size=38, color=MATH_COL,
            ),
            MathTex("\\leftrightarrow", font_size=34, color=HIGHLIGHT),
            MathTex(
                "\\mathbb{Z}^{(\\mathbb{N})}",
                font_size=38, color=GREEN_COL,
            ),
        ).arrange(RIGHT, buff=0.3).shift(DOWN * 5.5)

        table_box = SurroundingRectangle(
            VGroup(table, table2), color=PURPLE_COL, buff=0.3,
            corner_radius=0.1,
        )
        self.play(
            FadeIn(table), FadeIn(table2), Create(table_box),
            run_time=1.0,
        )
        self.wait(0.5)

        # Primes = basis
        primes_basis = MathTex(
            "\\text{primes} \\longleftrightarrow \\text{basis vectors}",
            font_size=36, color=HIGHLIGHT,
        ).to_edge(DOWN, buff=1.5)
        self.play(Write(primes_basis), run_time=0.7)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 8 — The logarithm twist ────────────────────────────────────────

    def scene_8_the_logarithm_twist(self):
        title = self.make_title("The logarithm twist")
        self.play(Write(title), run_time=0.6)

        # ln of a product
        ln_product = MathTex(
            "\\ln\\!\\left(2^{a_1} 3^{a_2} 5^{a_3} \\cdots\\right)",
            font_size=44, color=WHITE,
        ).shift(UP * 0.5)
        self.play(Write(ln_product), run_time=0.8)

        arrow = MathTex(
            "\\longrightarrow", font_size=40, color=HIGHLIGHT,
        ).next_to(ln_product, DOWN, buff=0.5)
        self.play(Write(arrow), run_time=0.4)

        expanded = MathTex(
            "a_1 \\ln 2 + a_2 \\ln 3 + a_3 \\ln 5 + \\cdots",
            font_size=40, color=MATH_COL,
        ).next_to(arrow, DOWN, buff=0.5)
        self.play(Write(expanded), run_time=0.8)
        self.wait(1.0)
        self.clear_scene(*self.mobjects)

        # ln(ab) = ln(a) + ln(b)
        log_rule = MathTex(
            "\\ln(ab) = \\ln a + \\ln b",
            font_size=44, color=WHITE,
        ).shift(UP * 0.5)
        self.play(Write(log_rule), run_time=0.6)
        self.wait(0.5)

        mult_to_add = VGroup(
            MathTex("\\text{multiplication}", font_size=36, color=MATH_COL),
            MathTex("\\longrightarrow", font_size=36, color=HIGHLIGHT),
            MathTex("\\text{addition}", font_size=36, color=MATH_COL),
        ).arrange(RIGHT, buff=0.3).next_to(log_rule, DOWN, buff=0.6)
        self.play(
            LaggedStart(*[Write(m) for m in mult_to_add], lag_ratio=0.2),
            run_time=1.0,
        )
        self.wait(1.0)
        self.clear_scene(*self.mobjects)

        # Show ln primes as coordinate directions
        ln_primes = VGroup(
            MathTex("\\ln 2", font_size=40, color=GREEN_COL),
            MathTex("\\ln 3", font_size=40, color=GREEN_COL),
            MathTex("\\ln 5", font_size=40, color=GREEN_COL),
            MathTex("\\ln 7", font_size=40, color=GREEN_COL),
            MathTex("\\ldots", font_size=40, color=GREEN_COL),
        ).arrange(RIGHT, buff=0.8).shift(DOWN * 1.5)

        dir_label = MathTex(
            "\\text{independent directions}",
            font_size=32, color=HIGHLIGHT,
        ).next_to(ln_primes, DOWN, buff=0.6)

        self.play(
            LaggedStart(*[Write(lp) for lp in ln_primes], lag_ratio=0.12),
            run_time=1.0,
        )
        self.play(FadeIn(dir_label), run_time=0.6)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── SCENE 9 — Still not quite a real vector space ────────────────────────

    def scene_9_still_not_quite(self):
        title = self.make_title("Still not quite...", color=RED_COL)
        self.play(Write(title), run_time=0.6)

        # Real span
        span = MathTex(
            "\\operatorname{span}_{\\mathbb{R}} \\{\\ln 2, \\ln 3, \\ln 5, \\ldots\\}",
            font_size=40, color=WHITE,
        ).shift(UP * 0.5)
        self.play(Write(span), run_time=0.8)

        vs = MathTex(
            "\\neq \\ln \\mathbb{Q}_{>0}",
            font_size=40, color=RED_COL,
        ).next_to(span, DOWN, buff=0.5)
        self.play(Write(vs), run_time=0.6)
        self.wait(0.5)

        # Counterexample
        counter = MathTex(
            "\\frac{1}{2} \\ln 2 = \\ln \\sqrt{2}",
            font_size=44, color=WHITE,
        ).shift(DOWN * 1.5)
        self.play(Write(counter), run_time=0.7)
        self.wait(0.5)

        not_rational = MathTex(
            "\\sqrt{2} \\notin \\mathbb{Q}",
            font_size=40, color=RED_COL,
        ).next_to(counter, DOWN, buff=0.5)
        self.play(Write(not_rational), run_time=0.6)
        self.wait(1.0)

        # The conclusion
        conclusion = VGroup(
            MathTex(
                "\\ln \\mathbb{Q}_{>0}", font_size=40, color=MATH_COL,
            ),
            MathTex(
                "\\text{ is a }", font_size=36, color=WHITE,
            ),
            MathTex(
                "\\text{free abelian group}", font_size=40, color=GREEN_COL,
            ),
        ).arrange(RIGHT, buff=0.2).shift(DOWN * 4.0)
        box = SurroundingRectangle(
            conclusion, color=GREEN_COL, buff=0.25, corner_radius=0.1
        )
        self.play(Write(conclusion), Create(box), run_time=1.0)
        self.wait(1.5)
        self.clear_scene(*self.mobjects)

    # ── ENDING — The punchline ───────────────────────────────────────────────

    def ending(self):
        # The big isomorphism
        big_iso = self.show_boxed(
            "\\mathbb{Q}_{>0} \\cong \\bigoplus_{p\\ \\text{prime}} \\mathbb{Z}",
            color=HIGHLIGHT,
            font_size=44,
        )
        big_iso.shift(UP * 0.5)
        self.play(Write(big_iso), run_time=1.0)
        self.wait(1.0)

        # Primes as basis
        primes = VGroup(
            MathTex("2", font_size=48, color=GREEN_COL),
            MathTex("3", font_size=48, color=GREEN_COL),
            MathTex("5", font_size=48, color=GREEN_COL),
            MathTex("7", font_size=48, color=GREEN_COL),
            MathTex("11", font_size=48, color=GREEN_COL),
            MathTex("\\ldots", font_size=48, color=GREEN_COL),
        ).arrange(RIGHT, buff=0.7).next_to(big_iso, DOWN, buff=1.0)
        self.play(
            LaggedStart(*[FadeIn(p, shift=UP * 0.2) for p in primes], lag_ratio=0.1),
            run_time=1.0,
        )
        self.wait(1.0)

        # The punchline
        punchline = MathTex(
            "\\text{Primes are basis-like}",
            font_size=44, color=HIGHLIGHT,
        ).shift(DOWN * 3.0)
        punchline2 = MathTex(
            "\\text{directions of multiplication.}",
            font_size=44, color=HIGHLIGHT,
        ).next_to(punchline, DOWN, buff=0.3)
        box = SurroundingRectangle(
            VGroup(punchline, punchline2),
            color=HIGHLIGHT, buff=0.3, corner_radius=0.1,
        )
        self.play(Write(punchline), Write(punchline2), Create(box), run_time=1.2)
        self.wait(2.0)
        self.clear_scene(*self.mobjects)

        # Final screen
        final1 = MathTex(
            "\\text{Prime factorization is}",
            font_size=40, color=WHITE,
        ).shift(UP * 1.0)
        final2 = MathTex(
            "\\text{linear algebra}",
            font_size=44, color=HIGHLIGHT,
        ).next_to(final1, DOWN, buff=0.3)
        self.play(Write(final1), Write(final2), run_time=0.8)
        self.wait(1.0)

        final3 = MathTex(
            "\\text{if multiplication is addition.}",
            font_size=40, color=MATH_COL,
        ).next_to(final2, DOWN, buff=0.6)
        self.play(Write(final3), run_time=0.8)
        self.wait(2.0)
        self.clear_scene(*self.mobjects)

        # Part 2 hook
        hook_question = MathTex(
            "\\text{What if we allowed}",
            font_size=40, color=SUBTITLE_COL,
        ).shift(UP * 1.0)
        hook_big = MathTex(
            "\\text{ALL real exponents?}",
            font_size=48, color=HIGHLIGHT,
        ).next_to(hook_question, DOWN, buff=0.4)
        self.play(Write(hook_question), Write(hook_big), run_time=1.0)
        self.wait(0.5)

        examples = VGroup(
            MathTex("2^{\\sqrt{2}}", font_size=44, color=MATH_COL),
            MathTex("3^{\\pi}", font_size=44, color=MATH_COL),
            MathTex("5^{e}", font_size=44, color=MATH_COL),
            MathTex("\\ldots", font_size=44, color=MATH_COL),
        ).arrange(RIGHT, buff=0.6).shift(DOWN * 1.5)
        self.play(
            LaggedStart(*[FadeIn(e, shift=UP * 0.2) for e in examples], lag_ratio=0.15),
            run_time=1.0,
        )
        self.wait(2.0)
