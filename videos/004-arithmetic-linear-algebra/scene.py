"""
Primes as Basis — a ~3 minute Manim Community Edition short.

Storyline (do not alter the mathematical progression):
    Fundamental Theorem of Arithmetic
        -> primes as "building blocks"
        -> the notion of a basis (R^3 example)
        -> positive integers as an exponent-coordinate space
        -> multiplication becomes addition, exponentiation becomes
           scalar multiplication
        -> "can this be a vector space?" -> no scalars in Z
        -> negative exponents -> positive rationals
        -> Q_{>0} =~ direct sum of Z over the primes
        -> not a vector space, but a free Z-module
        -> closing curiosity hook

Aspect ratio: 9:8 (this animation is meant to sit above/alongside a
9:16 speaker-cam composition, so it must NOT be rendered at 16:9 or 9:16).

Render (low quality preview, fast iteration):
    manim -pql videos/004-arithmetic-linear-algebra/scene.py PrimesAsBasis

Render (final quality):
    manim -pqh videos/004-arithmetic-linear-algebra/scene.py PrimesAsBasis

Both commands will honor the 9:8 pixel_width/pixel_height set below,
regardless of the -q flag (the -q flag only changes render fps/quality
step, not aspect ratio, since we hard-set pixel dimensions explicitly;
manim derives the frame aspect ratio from pixel_width / pixel_height).
"""

from manim import *

# --------------------------------------------------------------------------
# CONFIG — 9:8 aspect ratio, pure black background
# --------------------------------------------------------------------------
config.pixel_width = 1350
config.pixel_height = 1200
config.frame_rate = 30
config.background_color = "#000000"

# --------------------------------------------------------------------------
# PALETTE — restrained accent-color system on black
# --------------------------------------------------------------------------
INK = "#F5F5F5"        # primary text / math, near-white
DIM = "#7A7A7A"         # de-emphasized text
CYAN = "#4FD8E8"        # primes / basis accent
GOLD = "#F2C14E"        # exponents / scalars accent
ROSE = "#F26C6C"        # warnings / negative / "not quite" accent
VIOLET = "#B39CD0"       # module / final structure accent

PRIME_LABELS = ["2", "3", "5", "7", "11", "13"]

# --------------------------------------------------------------------------
# REUSABLE HELPERS
# --------------------------------------------------------------------------


def caption(text, font_size=30):
    """Small bottom-of-frame caption line, kept inside safe margins."""
    cap = Text(text, font_size=font_size, color=DIM)
    cap.to_edge(DOWN, buff=0.55)
    return cap


def title_card(text, font_size=52, color=INK):
    t = Text(text, font_size=font_size, color=color, weight=BOLD)
    return t


def boxed(tex_string, color=INK, font_size=48):
    """A MathTex wrapped in a rounded rectangle, used for the recurring
     'boxed' mathematical statements the script calls for."""
    m = MathTex(tex_string, color=color, font_size=font_size)
    box = SurroundingRectangle(m, color=color, buff=0.35, corner_radius=0.12)
    return VGroup(box, m)


def coordinate_row(values, highlight_indices=None, base_color=INK,
                    highlight_color=GOLD, font_size=40):
    """
    Build a horizontal exponent-coordinate tuple like (2, 1, 1, 0, 0, ...).
    `values` is a list of strings/numbers; the last entry may be "..." to
    suggest the infinite tail without literally drawing it.
    Returns (group, list_of_entry_mobjects) so callers can Transform into it.
    """
    highlight_indices = highlight_indices or set()
    parts = [MathTex("(", color=base_color, font_size=font_size)]
    entries = []
    for i, v in enumerate(values):
        color = highlight_color if i in highlight_indices else base_color
        entry = MathTex(str(v), color=color, font_size=font_size)
        entries.append(entry)
        parts.append(entry)
        if i != len(values) - 1:
            parts.append(MathTex(",", color=base_color, font_size=font_size))
    parts.append(MathTex(")", color=base_color, font_size=font_size))
    group = VGroup(*parts).arrange(RIGHT, buff=0.12)
    return group, entries


def prime_axis_labels(font_size=26, color=DIM):
    """The small 2, 3, 5, 7, 11, 13, ... labels placed under a coordinate
    tuple to remind the viewer which axis is which."""
    labels = [MathTex(p, color=color, font_size=font_size) for p in PRIME_LABELS]
    labels.append(MathTex(r"\cdots", color=color, font_size=font_size))
    row = VGroup(*labels).arrange(RIGHT, buff=0.55)
    return row


# --------------------------------------------------------------------------
# MAIN SCENE
# --------------------------------------------------------------------------


class PrimesAsBasis(Scene):
    def construct(self):
        self.scene_1_fundamental_theorem()
        self.scene_2_building_blocks()
        self.scene_3_basis_in_r3()
        self.scene_4_prime_coordinates()
        self.scene_5_multiplication_to_addition()
        self.scene_6_correspondence_table()
        self.scene_7_vector_space_question()
        self.scene_8_positive_rationals()
        self.scene_9_module_conclusion()
        self.scene_10_closing_curiosity()

    # ----------------------------------------------------------------
    # Scene 1 (0:00-0:20) — Fundamental Theorem of Arithmetic
    # ----------------------------------------------------------------
    def scene_1_fundamental_theorem(self):
        n = MathTex("60", color=INK, font_size=90)
        self.play(FadeIn(n, scale=0.6), run_time=0.8)
        self.wait(0.4)

        factored = MathTex("60", "=", "2^2", r"\cdot", "3", r"\cdot", "5",
                            color=INK, font_size=90)
        factored[2].set_color(CYAN)
        factored[4].set_color(CYAN)
        factored[6].set_color(CYAN)

        self.play(TransformMatchingShapes(n, factored[0]), run_time=0.6)
        self.play(
            Write(factored[1:]),
            run_time=1.4,
        )
        self.wait(0.5)

        subtitle = Text(
            "Every positive integer factors uniquely into primes.",
            font_size=32, color=DIM,
        ).next_to(factored, DOWN, buff=0.9)
        theorem_name = Text(
            "The Fundamental Theorem of Arithmetic",
            font_size=30, color=GOLD,
        ).next_to(subtitle, DOWN, buff=0.35)

        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(theorem_name, shift=UP * 0.2), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(factored, subtitle, theorem_name)), run_time=0.7)

    # ----------------------------------------------------------------
    # Scene 2 (0:20-0:45) — primes as building blocks; the stray question
    # ----------------------------------------------------------------
    def scene_2_building_blocks(self):
        line = Text(
            "So primes are the building blocks of every integer.",
            font_size=34, color=INK,
        )
        self.play(FadeIn(line, shift=UP * 0.2), run_time=0.9)
        self.wait(1.0)

        # quick flurry of a few factorizations to sell "building blocks"
        examples = VGroup(
            MathTex("12 = 2^2\\cdot 3", color=DIM, font_size=34),
            MathTex("18 = 2\\cdot 3^2", color=DIM, font_size=34),
            MathTex("100 = 2^2\\cdot 5^2", color=DIM, font_size=34),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        examples.next_to(line, DOWN, buff=0.7)

        self.play(LaggedStart(*[FadeIn(e, shift=RIGHT * 0.2) for e in examples],
                               lag_ratio=0.35), run_time=1.4)
        self.wait(0.8)

        self.play(FadeOut(VGroup(line, examples)), run_time=0.6)

        # the curiosity, then it's set aside
        curious = Text(
            "I've always wondered: what if the exponents could be\n"
            "any integer — would this extend to all positive rationals?",
            font_size=30, color=INK, line_spacing=1.2,
        )
        self.play(FadeIn(curious, shift=UP * 0.15), run_time=1.0)
        self.wait(1.8)

        aside = Text("Let's set that aside for a moment...", font_size=28, color=DIM)
        aside.next_to(curious, DOWN, buff=0.6)
        self.play(FadeIn(aside), run_time=0.7)
        self.wait(1.0)
        self.play(FadeOut(VGroup(curious, aside)), run_time=0.6)

    # ----------------------------------------------------------------
    # Scene 3 (0:45-1:15) — basis, illustrated with R^3
    # ----------------------------------------------------------------
    def scene_3_basis_in_r3(self):
        heading = title_card("What is a basis?", font_size=42, color=INK)
        heading.to_edge(UP, buff=0.9)
        self.play(FadeIn(heading, shift=DOWN * 0.2), run_time=0.8)

        sub = Text(
            "Basis elements can generate every element of a space.",
            font_size=28, color=DIM,
        ).next_to(heading, DOWN, buff=0.35)
        self.play(FadeIn(sub), run_time=0.7)
        self.wait(0.6)

        # A light isometric-style origin with three axis arrows, standing
        # in for R^3 without invoking a literal 3D camera.
        origin = ORIGIN + DOWN * 0.6
        dir_e1 = np.array([-2.1, -1.1, 0])
        dir_e2 = np.array([2.3, -0.9, 0])
        dir_e3 = np.array([0, 2.1, 0])

        o_dot = Dot(origin, color=INK, radius=0.05)
        arrow1 = Arrow(origin, origin + dir_e1, color=CYAN, buff=0, stroke_width=5)
        arrow2 = Arrow(origin, origin + dir_e2, color=CYAN, buff=0, stroke_width=5)
        arrow3 = Arrow(origin, origin + dir_e3, color=CYAN, buff=0, stroke_width=5)

        label1 = MathTex(r"\mathbf{e}_1=(1,0,0)", color=CYAN, font_size=30)
        label1.next_to(arrow1.get_end(), DOWN + LEFT, buff=0.15)
        label2 = MathTex(r"\mathbf{e}_2=(0,1,0)", color=CYAN, font_size=30)
        label2.next_to(arrow2.get_end(), DOWN + RIGHT, buff=0.15)
        label3 = MathTex(r"\mathbf{e}_3=(0,0,1)", color=CYAN, font_size=30)
        label3.next_to(arrow3.get_end(), UP, buff=0.15)

        self.play(FadeIn(o_dot), run_time=0.3)
        self.play(
            LaggedStart(
                AnimationGroup(GrowArrow(arrow1), FadeIn(label1)),
                AnimationGroup(GrowArrow(arrow2), FadeIn(label2)),
                AnimationGroup(GrowArrow(arrow3), FadeIn(label3)),
                lag_ratio=0.4,
            ),
            run_time=1.8,
        )
        self.wait(0.6)

        # combine into a generic vector (a,b,c)
        combo = MathTex(
            "(a,b,c)", "=", "a", r"\,\mathbf{e}_1",
            "+", "b", r"\,\mathbf{e}_2", "+", "c", r"\,\mathbf{e}_3",
            color=INK, font_size=34,
        ).to_edge(DOWN, buff=0.8)
        combo[2].set_color(GOLD)  # a
        self.play(FadeIn(combo, shift=UP * 0.2), run_time=1.0)
        self.wait(1.6)

        self.play(
            FadeOut(VGroup(heading, sub, o_dot, arrow1, arrow2, arrow3,
                            label1, label2, label3, combo)),
            run_time=0.7,
        )

    # ----------------------------------------------------------------
    # Scene 4 (1:15-1:45) — the integers as a "space" of primes; the
    # exponent-coordinate system, using 60 as the running example
    # ----------------------------------------------------------------
    def scene_4_prime_coordinates(self):
        prompt = Text(
            "Now look at the positive integers as a space —\n"
            "with the primes as its elements.",
            font_size=30, color=INK, line_spacing=1.2,
        )
        self.play(FadeIn(prompt, shift=UP * 0.15), run_time=1.0)
        self.wait(1.2)
        self.play(FadeOut(prompt), run_time=0.6)

        n60 = MathTex("60", "=", "2^2", "\\cdot", "3^1", "\\cdot", "5^1",
                       color=INK, font_size=64)
        n60.move_to(UP * 2.0)
        n60[2].set_color(CYAN)
        n60[4].set_color(CYAN)
        n60[6].set_color(CYAN)
        self.play(Write(n60), run_time=1.2)
        self.wait(0.5)

        # extract the exponent digits visually. To avoid orphaning any
        # transform copies on screen, we animate transient copies but keep
        # references to them and fade EVERYTHING created here out together.
        tail = Text("(exponents extracted)", font_size=24, color=DIM)
        tail.next_to(n60, DOWN, buff=0.5)
        self.play(FadeIn(tail), run_time=0.5)
        self.wait(0.4)

        digits = VGroup(
            MathTex("2", color=GOLD, font_size=42),
            MathTex("1", color=GOLD, font_size=42),
            MathTex("1", color=GOLD, font_size=42),
        )
        digits.arrange(RIGHT, buff=0.35)
        digits.move_to(DOWN * 0.6)

        self.play(FadeOut(tail), run_time=0.3)
        # fly the exponent digits down into the extraction row using copies;
        # the copies are kept and removed together with everything else
        sources = [n60[2], n60[4], n60[6]]
        ghosts = [src.copy() for src in sources]
        self.play(
            *[Transform(ghosts[i], digits[i]) for i in range(3)],
            run_time=1.1,
        )
        self.play(FadeIn(digits), run_time=0.5)
        self.wait(0.3)

        # the coordinate vector extends the extracted digits with trailing zeros
        vec, _ = coordinate_row(["2", "1", "1", "0", "0", "\\cdots"],
                                highlight_indices={0, 1, 2}, font_size=42)
        vec.move_to(digits.get_center())
        under = prime_axis_labels()
        under.next_to(vec, DOWN, buff=0.35)

        self.play(FadeOut(digits), FadeIn(vec), run_time=0.6)
        self.play(FadeIn(under), run_time=0.5)
        self.wait(0.5)
        self.remove(*ghosts)

        arrow = MathTex(r"\longleftrightarrow", color=DIM, font_size=40)
        arrow.next_to(n60, RIGHT, buff=0.6)

        self.play(n60.animate.shift(LEFT * 1.6), FadeIn(arrow.shift(LEFT * 1.6)),
                   vec.animate.shift(RIGHT * 0.4), under.animate.shift(RIGHT * 0.4),
                   run_time=0.9)
        self.wait(1.6)

        self.play(FadeOut(VGroup(n60, arrow, vec, under)), run_time=0.7)

    # ----------------------------------------------------------------
    # Scene 5 (1:45-2:10) — multiplication becomes addition
    # ----------------------------------------------------------------
    def scene_5_multiplication_to_addition(self):
        heading = Text("Watch what happens when we multiply.", font_size=30, color=INK)
        heading.to_edge(UP, buff=0.9)
        self.play(FadeIn(heading, shift=DOWN * 0.2), run_time=0.8)

        left = MathTex("12", "=", "2^2", "\\cdot", "3", color=INK, font_size=44)
        right = MathTex("18", "=", "2", "\\cdot", "3^2", color=INK, font_size=44)
        left[2].set_color(CYAN)
        left[4].set_color(CYAN)
        right[2].set_color(CYAN)
        right[4].set_color(CYAN)

        pair = VGroup(left, right).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        pair.next_to(heading, DOWN, buff=0.8)
        self.play(Write(left), run_time=0.9)
        self.play(Write(right), run_time=0.9)
        self.wait(0.5)

        vec12, _ = coordinate_row(["2", "1", "0", "\\cdots"], font_size=36)
        vec18, _ = coordinate_row(["1", "2", "0", "\\cdots"], font_size=36)
        vec12.next_to(left, RIGHT, buff=0.7)
        vec18.next_to(right, RIGHT, buff=0.7)

        self.play(FadeIn(vec12, shift=LEFT * 0.2), run_time=0.7)
        self.play(FadeIn(vec18, shift=LEFT * 0.2), run_time=0.7)
        self.wait(0.6)

        self.play(FadeOut(heading), run_time=0.4)

        mult_line = MathTex("12", "\\times", "18", "=", "216", color=INK, font_size=50)
        mult_line.move_to(UP * 2.0)

        self.play(
            FadeOut(pair),
            run_time=0.4,
        )
        self.play(
            vec12.animate.move_to(UP * 0.2 + LEFT * 2.6),
            vec18.animate.move_to(UP * 0.2 + RIGHT * 2.6),
            run_time=0.8,
        )
        self.play(FadeIn(mult_line, shift=DOWN * 0.2), run_time=0.9)
        self.wait(0.8)

        plus = MathTex("+", color=DIM, font_size=40)
        plus.move_to((vec12.get_center() + vec18.get_center()) / 2)
        self.play(FadeIn(plus), run_time=0.5)
        self.wait(0.3)

        sum_vec, _ = coordinate_row(["3", "3", "0", "\\cdots"],
                                         highlight_indices={0, 1}, font_size=40)
        sum_vec.move_to(DOWN * 1.4)

        self.play(
            ReplacementTransform(
                VGroup(vec12.copy(), vec18.copy()), sum_vec
            ),
            run_time=1.1,
        )
        self.wait(0.4)

        factored_216 = MathTex("216", "=", "2^3", "\\cdot", "3^3", color=GOLD,
                                font_size=40)
        factored_216.next_to(sum_vec, DOWN, buff=0.5)
        self.play(FadeIn(factored_216, shift=UP * 0.15), run_time=0.9)
        self.wait(0.4)

        aha = Text("Multiplication became addition.", font_size=30, color=GOLD)
        aha.next_to(factored_216, DOWN, buff=0.5)
        self.play(FadeIn(aha, shift=UP * 0.15), run_time=0.8)
        self.wait(1.4)

        self.play(
            FadeOut(VGroup(vec12, vec18, mult_line, plus, sum_vec,
                            factored_216, aha)),
            run_time=0.7,
        )

    # ----------------------------------------------------------------
    # Scene 6 — progressive reveal of the vector-space / arithmetic
    # correspondence table
    # ----------------------------------------------------------------
    def scene_6_correspondence_table(self):
        heading = Text("A pattern is forming...", font_size=32, color=INK)
        self.play(FadeIn(heading), run_time=0.7)
        self.wait(0.6)
        self.play(heading.animate.to_edge(UP, buff=0.9), run_time=0.5)

        row1 = MathTex(r"\text{addition} \;\longleftrightarrow\; \text{multiplication}",
                        color=INK, font_size=32)
        row2 = MathTex(
            r"\text{scalar multiplication} \;\longleftrightarrow\; \text{exponentiation}",
            color=INK, font_size=32)
        row3 = MathTex(r"\text{basis} \;\longleftrightarrow\; \text{primes}",
                        color=CYAN, font_size=32)

        rows = VGroup(row1, row2, row3).arrange(DOWN, buff=0.55)
        rows.next_to(heading, DOWN, buff=0.9)

        for r in rows:
            self.play(FadeIn(r, shift=UP * 0.15), run_time=0.9)
            self.wait(0.7)

        self.wait(1.0)
        self.play(FadeOut(VGroup(heading, rows)), run_time=0.7)

    # ----------------------------------------------------------------
    # Scene 7 (2:10-2:35) — is this actually a vector space?
    # ----------------------------------------------------------------
    def scene_7_vector_space_question(self):
        q = title_card("Can this actually be a vector space?", font_size=36,
                        color=INK)
        q.move_to(UP * 0.3)
        self.play(FadeIn(q, scale=0.9), run_time=1.0)
        self.wait(1.8)  # deliberate pause before the reveal

        exps = MathTex("0,\\;1,\\;2,\\;3,\\;\\ldots", color=DIM, font_size=36)
        exps.next_to(q, DOWN, buff=0.7)
        note = Text("...the exponents only ever grow.", font_size=26, color=DIM)
        note.next_to(exps, DOWN, buff=0.35)
        self.play(FadeIn(exps, shift=UP * 0.15), FadeIn(note), run_time=0.9)
        self.wait(1.0)

        neg = MathTex(r"2^{-1} = \frac{1}{2}", color=ROSE, font_size=44)
        neg.next_to(note, DOWN, buff=0.6)
        self.play(FadeIn(neg, shift=UP * 0.2), run_time=0.9)
        self.wait(1.2)

        push = Text("Negative exponents push us out of the integers...",
                     font_size=26, color=ROSE)
        push.next_to(neg, DOWN, buff=0.4)
        self.play(FadeIn(push), run_time=0.8)
        self.wait(1.4)

        self.play(FadeOut(VGroup(q, exps, note, neg, push)), run_time=0.7)

    # ----------------------------------------------------------------
    # Scene 8 (2:10-2:35 cont'd / 2:35-2:55) — positive rationals
    # ----------------------------------------------------------------
    def scene_8_positive_rationals(self):
        frac = MathTex(r"\frac{12}{25}", color=INK, font_size=64)
        self.play(FadeIn(frac, scale=0.7), run_time=0.8)
        self.wait(0.7)

        factored = MathTex(r"\frac{12}{25}", "=", "2^2", "\\cdot", "3^1", "\\cdot",
                            "5^{-2}", color=INK, font_size=54)
        factored.move_to(UP * 1.6)
        factored[2].set_color(CYAN)
        factored[4].set_color(CYAN)
        factored[6].set_color(ROSE)

        self.play(ReplacementTransform(frac, factored[0]), run_time=0.6)
        self.play(Write(factored[1:]), run_time=1.2)
        self.wait(0.7)

        vec, _ = coordinate_row(["2", "1", "-2", "0", "\\cdots"],
                                       highlight_indices={2}, base_color=INK,
                                       highlight_color=ROSE, font_size=42)
        vec.next_to(factored, DOWN, buff=0.8)
        under = prime_axis_labels()
        under.next_to(vec, DOWN, buff=0.35)

        self.play(FadeIn(vec, shift=UP * 0.2), FadeIn(under), run_time=1.0)
        self.wait(1.4)

        self.play(FadeOut(VGroup(factored, vec, under)), run_time=0.6)

        explain = Text(
            "Every positive rational is a finitely-supported\n"
            "sequence of integer exponents over the primes.",
            font_size=28, color=INK, line_spacing=1.2,
        )
        self.play(FadeIn(explain, shift=UP * 0.15), run_time=1.0)
        self.wait(1.3)
        self.play(explain.animate.to_edge(UP, buff=0.9).scale(0.85), run_time=0.6)

        iso = boxed(r"\mathbb{Q}_{>0} \;\cong\; \bigoplus_{p\ \text{prime}} \mathbb{Z}",
                    color=GOLD, font_size=46)
        iso.next_to(explain, DOWN, buff=0.9)
        self.play(FadeIn(iso[1], shift=UP * 0.2), run_time=1.0)
        self.wait(0.5)
        self.play(Create(iso[0]), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(explain, iso)), run_time=0.7)

    # ----------------------------------------------------------------
    # Scene 9 (2:55-3:15) — the module: Z is not a field
    # ----------------------------------------------------------------
    def scene_9_module_conclusion(self):
        coord = MathTex(r"\mathbb{Z}^{(\mathbb{N})} \;=\; \bigoplus_{p} \mathbb{Z}",
                         color=INK, font_size=44)
        coord.move_to(UP * 1.8)
        self.play(FadeIn(coord, shift=DOWN * 0.2), run_time=0.9)
        self.wait(1.0)

        not_field = Text("But Z is not a field.", font_size=30, color=ROSE)
        not_field.next_to(coord, DOWN, buff=0.6)
        self.play(FadeIn(not_field), run_time=0.8)
        self.wait(1.0)

        not_vs = boxed("\\text{Not quite a vector space.}", color=ROSE, font_size=34)
        not_vs.next_to(not_field, DOWN, buff=0.6)
        self.play(FadeIn(not_vs[1], shift=UP * 0.15), Create(not_vs[0]), run_time=0.9)
        self.wait(1.4)

        self.play(FadeOut(VGroup(coord, not_field, not_vs)), run_time=0.7)

        module_box = boxed(r"\text{A free } \mathbb{Z}\text{-module.}",
                            color=VIOLET, font_size=40)
        module_box.move_to(UP * 1.4)
        self.play(FadeIn(module_box[1], shift=UP * 0.2), Create(module_box[0]),
                   run_time=1.0)
        self.wait(1.2)

        final_iso = boxed(
            r"\mathbb{Q}_{>0} \;\cong\; \bigoplus_{p\ \text{prime}} \mathbb{Z}",
            color=GOLD, font_size=46,
        )
        final_iso.next_to(module_box, DOWN, buff=0.7)
        self.play(FadeIn(final_iso[1], shift=UP * 0.2), run_time=1.0)
        self.play(Create(final_iso[0]), run_time=0.7)
        self.wait(1.0)

        statement = VGroup(
            Text("Primes are a basis of ", font_size=27, color=CYAN),
            MathTex(r"\mathbb{Q}_{>0}", font_size=30, color=CYAN),
            Text(" as a free Z-module,\nunder multiplication.",
                 font_size=27, color=CYAN, line_spacing=1.25),
        ).arrange(RIGHT, buff=0.15)
        statement.next_to(final_iso, DOWN, buff=0.7)
        self.play(FadeIn(statement, shift=UP * 0.15), run_time=1.0)
        self.wait(2.0)

        self.play(FadeOut(VGroup(module_box, final_iso, statement)), run_time=0.8)

    # ----------------------------------------------------------------
    # Scene 10 — closing curiosity hook
    # ----------------------------------------------------------------
    def scene_10_closing_curiosity(self):
        closing = Text(
            "And now I'm wondering...\nwhat happens if we change the scalars?",
            font_size=32, color=INK, line_spacing=1.3,
        )
        self.play(FadeIn(closing, shift=UP * 0.2), run_time=1.0)
        self.wait(2.2)
        self.play(FadeOut(closing), run_time=0.9)
        self.wait(0.3)