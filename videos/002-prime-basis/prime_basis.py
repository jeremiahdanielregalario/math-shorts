from manim import *

# ── Vertical 9:16 configuration (1080x1920) ───────────────────────────────────
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080
config.background_color = BLACK

# ── Palette ───────────────────────────────────────────────────────────────────
C_PRIME = "#58C4DD"   # Blue : basis / prime elements
C_TUPLE = "#A6E22E"   # Green: coordinates / tuples
C_ACCENT = "#FFE64D"  # Yellow: key insights / highlights
C_ERR = "#FF5555"     # Red   : failure cases / errors

# ── Layout guardrails ─────────────────────────────────────────────────────────
# Frame runs y in [-8, 8]. The bottom speaker overlay occupies y in [-8, -3.5]
# and MUST stay empty. All content is kept within y in (-3.5, 7.5) via
# CONTENT_MAX_Y and CONTENT_MIN_Y.
CONTENT_MAX_Y = 7.5
CONTENT_MIN_Y = -3.5


def _clamp_y(mob, top):
    """Raise ``mob`` so its lowest point never dips below the speaker overlay."""
    low = mob.get_bottom()[1]
    if low < CONTENT_MIN_Y:
        mob.shift(UP * (CONTENT_MIN_Y - low))
    if mob.get_top()[1] > CONTENT_MAX_Y:
        mob.shift(DOWN * (mob.get_top()[1] - CONTENT_MAX_Y))
    return mob


class PrimeBasisShort(Scene):
    """Primes as Basis Vectors — a ~90s vertical short.

    Five scenes: FTA & the basis concept, infinite prime coordinates,
    negative exponents & Q_{>0}, vector space vs. free Z-module, and the
    finale isomorphism. Ends with the punchline that prime factorization
    is linear algebra over the integers.
    """

    def construct(self):
        self.scene_1_basis_concept()
        self.scene_2_infinite_coordinates()
        self.scene_3_negative_exponents()
        self.scene_4_vector_space_vs_free_module()
        self.scene_5_isomorphism_conclusion()

    # ── SCENE 1: FTA & the Basis Concept ──────────────────────────────────────

    def scene_1_basis_concept(self):
        # --- Intro: the Fundamental Theorem of Arithmetic --------------------
        title = MathTex(
            "\\text{The Fundamental Theorem of Arithmetic}", font_size=30,
        )
        title[0].set_weight(BOLD)
        title.to_edge(UP, buff=1.0)
        _clamp_y(title, 7.5)
        self.play(Write(title))

        context = MathTex(
            "\\text{You met it in number theory:}",
            font_size=26,
        )
        context.move_to(UP * 5.2)
        _clamp_y(context, 7.5)
        self.play(Write(context))

        fta_statement = MathTex(
            "\\text{every } n > 1 \\text{ factors }",
            "\\text{uniquely}", "\\text{ into primes.}",
            font_size=26,
        )
        fta_statement[1].set_color(C_ACCENT)
        fta_statement.move_to(UP * 4.2)
        _clamp_y(fta_statement, 7.5)
        self.play(Write(fta_statement))
        self.wait(0.8)

        fta_eq = MathTex(
            "60", "=", "2^2", "\\cdot", "3^1", "\\cdot", "5^1",
            font_size=38,
        )
        fta_eq.move_to(UP * 2.8)
        _clamp_y(fta_eq, 7.5)
        self.play(FadeIn(fta_eq))
        self.wait(1.0)

        self.play(
            FadeOut(context), FadeOut(fta_statement), FadeOut(fta_eq),
        )

        # --- Pivot: a concrete vector space, R^3 over R ----------------------
        pivot = MathTex(
            "\\text{Now, a vector space you know:}", font_size=26,
        )
        pivot.move_to(UP * 5.2)
        _clamp_y(pivot, 7.5)
        self.play(Write(pivot))

        r3 = MathTex("\\mathbb{R}^3", "\\text{ over }", "\\mathbb{R}",
                     font_size=32, color=C_PRIME)
        r3.move_to(UP * 4.0)
        _clamp_y(r3, 7.5)
        self.play(Write(r3))
        self.wait(0.5)

        basis_vecs = VGroup(
            MathTex("\\mathbf{i} = (1,0,0)", font_size=26),
            MathTex("\\mathbf{j} = (0,1,0)", font_size=26),
            MathTex("\\mathbf{k} = (0,0,1)", font_size=26),
        ).arrange(DOWN, buff=0.4).move_to(UP * 1.2)
        _clamp_y(basis_vecs, 7.5)
        self.play(
            LaggedStart(*[Write(v) for v in basis_vecs], lag_ratio=0.2),
            run_time=1.0,
        )
        self.wait(0.5)

        basis_def = MathTex(
            "\\text{every }", "\\mathbf{v}", "= c_1 ",
            "\\mathbf{i}", "+ c_2 ", "\\mathbf{j}", "+ c_3 ",
            "\\mathbf{k}", ",  \\quad c_i \\in \\mathbb{R}",
            font_size=26,
        )
        basis_def.move_to(DOWN * 1.0)
        _clamp_y(basis_def, 7.5)

        box = SurroundingRectangle(
            basis_def, color=C_ACCENT, buff=0.35, corner_radius=0.15
        )
        label = MathTex(
            "\\text{same idea: a basis } \\{ \\mathbf{i}, \\mathbf{j}, \\mathbf{k} \\}",
            font_size=26, color=C_ACCENT,
        )
        label.next_to(box, UP, buff=0.3)
        grp = VGroup(basis_def, box, label)
        _clamp_y(grp, 7.5)

        self.play(Write(basis_def), Create(box), FadeIn(label))
        self.wait(2.0)

        self.play(
            FadeOut(title), FadeOut(pivot), FadeOut(r3),
            FadeOut(basis_vecs), FadeOut(grp),
        )

    # ── SCENE 2: Infinite Prime Coordinates & Operations ──────────────────────

    def scene_2_infinite_coordinates(self):
        header = MathTex(
            "\\text{Basis Directions: } p_1, p_2, p_3, \\dots = 2, 3, 5, 7, \\dots",
            font_size=26, color=C_PRIME,
        )
        header.move_to(UP * 5.5)
        _clamp_y(header, 7.5)
        self.play(Write(header))

        num_12 = MathTex(
            "12", "=", "2^2", "\\cdot", "3^1", "\\cdot", "5^0", "\\cdots",
            "\\longleftrightarrow", "(2, 1, 0, 0, \\dots)",
            font_size=26,
        )
        num_12[-1].set_color(C_TUPLE)
        num_12.move_to(UP * 3.2)
        _clamp_y(num_12, 7.5)
        self.play(Write(num_12))
        self.wait(1.0)

        ops_title = MathTex(
            "\\text{Operation Duality}", font_size=28, color=C_ACCENT,
        )
        ops_title.move_to(UP * 0.7)
        _clamp_y(ops_title, 7.5)

        op_mult = MathTex(
            "\\text{Multiplication } (\\times)", "\\iff",
            "\\text{Vector Addition } (+)",
            font_size=24,
        )
        op_mult.move_to(DOWN * 0.4)
        _clamp_y(op_mult, 7.5)

        op_example = MathTex("12", "\\times", "18", "=", "216", font_size=26)
        op_example.move_to(DOWN * 1.3)
        _clamp_y(op_example, 7.5)

        op_vec = MathTex(
            "(2,1,0,\\dots)", "+", "(1,2,0,\\dots)", "=", "(3,3,0,\\dots)",
            font_size=22, color=C_TUPLE,
        )
        op_vec.move_to(DOWN * 2.2)
        _clamp_y(op_vec, 7.5)

        self.play(Write(ops_title))
        self.play(Write(op_mult))
        self.play(Write(op_example))
        self.play(Write(op_vec))
        self.wait(2.5)

        self.play(
            FadeOut(header), FadeOut(num_12), FadeOut(ops_title),
            FadeOut(op_mult), FadeOut(op_example), FadeOut(op_vec),
        )

    # ── SCENE 3: Negative Exponents & Positive Rationals (Q_{>0}) ─────────────

    def scene_3_negative_exponents(self):
        hook = MathTex(
            "\\text{What if exponent }", "\\in", "\\mathbb{Z}?",
            font_size=30, color=C_ACCENT,
        )
        hook.move_to(UP * 4.5)
        _clamp_y(hook, 7.5)
        self.play(Write(hook))

        frac_eq = MathTex(
            "\\frac{12}{25}", "=", "2^2", "\\cdot", "3^1", "\\cdot", "5^{-2}",
            "\\longleftrightarrow", "(2, 1, -2, 0, \\dots)",
            font_size=26,
        )
        frac_eq[-1].set_color(C_TUPLE)
        frac_eq.move_to(UP * 2.5)
        _clamp_y(frac_eq, 7.5)
        self.play(Write(frac_eq))
        self.wait(2.0)

        outcome = MathTex(
            "\\text{Captures ALL Positive Rationals } \\mathbb{Q}_{>0}!",
            font_size=28, color="#83C167",
        )
        outcome.move_to(UP * 0.5)
        _clamp_y(outcome, 7.5)
        self.play(FadeIn(outcome, shift=UP))
        self.wait(2.0)

        self.play(FadeOut(hook), FadeOut(frac_eq), FadeOut(outcome))

    # ── SCENE 4: Vector Space vs. Free Z-Module ───────────────────────────────

    def scene_4_vector_space_vs_free_module(self):
        question = MathTex(
            "\\mathbb{Q}_{>0}", "\\text{ a Vector Space?}",
            font_size=30, color=C_ERR,
        )
        question.move_to(UP * 4.5)
        _clamp_y(question, 7.5)
        self.play(Write(question))

        fail_case = MathTex(
            "2^{1/2}", "=", "\\sqrt{2}", "\\notin", "\\mathbb{Q}_{>0}",
            font_size=30,
        )
        fail_case.move_to(UP * 2.5)
        _clamp_y(fail_case, 7.5)
        self.play(Write(fail_case))

        cross = Cross(fail_case, stroke_color=C_ERR, stroke_width=6)
        self.play(Create(cross))
        self.wait(1.5)

        reason = MathTex(
            "\\text{Scalars are restricted to integers (}", "\\mathbb{Z}",
            "\\text{)}",
            font_size=24,
        )
        reason.move_to(UP * 0.5)
        _clamp_y(reason, 7.5)
        self.play(Write(reason))

        conclusion = MathTex(
            "\\mathbb{Q}_{>0}", "\\text{ is a Free }", "\\mathbb{Z}",
            "\\text{-Module!}",
            font_size=28, color=C_ACCENT,
        )
        conclusion.move_to(DOWN * 0.8)
        _clamp_y(conclusion, 7.5)
        self.play(Write(conclusion))
        self.wait(2.0)

        self.play(
            FadeOut(question), FadeOut(fail_case), FadeOut(cross),
            FadeOut(reason), FadeOut(conclusion),
        )

    # ── SCENE 5: Isomorphism & Conclusion ─────────────────────────────────────

    def scene_5_isomorphism_conclusion(self):
        iso_eq = MathTex(
            "(\\mathbb{Q}_{>0}, \\times)", "\\cong",
            "\\bigoplus_{p \\text{ prime}} \\mathbb{Z}",
            font_size=32,
        )
        iso_eq.move_to(UP * 2.0)
        iso_eq[1].set_color(C_ACCENT)
        _clamp_y(iso_eq, 7.5)

        box = SurroundingRectangle(
            iso_eq, color=C_ACCENT, buff=0.3, corner_radius=0.1,
        )
        _clamp_y(VGroup(iso_eq, box), 7.5)

        summary = MathTex(
            "\\text{Prime Factorization IS }", "\\text{Linear Algebra}",
            "\\\\", "\\text{(Over the }", "\\text{Integers)}",
            font_size=26,
        )
        summary[1].set_color(C_PRIME)
        summary[4].set_color(C_ACCENT)
        summary.move_to(DOWN * 1.5)
        _clamp_y(summary, 7.5)

        self.play(Write(iso_eq), Create(box))
        self.play(FadeIn(summary, shift=UP))
        self.wait(3.0)
