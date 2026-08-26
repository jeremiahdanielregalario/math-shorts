import numpy as np
from manim import *

# ── Vertical 9:16 configuration ──────────────────────────────────────────────
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080

# ── Colors ────────────────────────────────────────────────────────────────────
MATH_COL = "#58C4DD"
HIGHLIGHT = "#FFFF00"
APOthem_COL = "#83C167"
TRIANGLE_COL = "#FF8C00"
RED_COL = "#FC6255"

# ── Layout ────────────────────────────────────────────────────────────────────
# Math content center: x = -1.0 (left 70% of 9-wide frame)
MATH_CX = -1.0


class LimitSecretlyGeometry(Scene):
    """A Limit That Is Secretly Geometry.

    lim_{n→∞} n·tan(π/n) = π is the area of a regular n-gon
    with apothem 1, approaching the unit circle area.
    """

    def construct(self):
        self.camera.background_color = BLACK
        self.hook()
        self.scene_2_polygon()
        self.scene_3_apothem()
        self.scene_4_triangle()
        self.scene_5_tangent()
        self.scene_6_area()
        self.scene_7_polygon_progression()
        self.scene_8_circle()
        self.scene_9_limit()
        self.ending()

    # ── Helpers ───────────────────────────────────────────────────────────────

    def show_boxed(self, tex_str, color=MATH_COL, font_size=40):
        mob = MathTex(tex_str, color=color, font_size=font_size)
        box = SurroundingRectangle(
            mob, color=color, buff=0.25, corner_radius=0.1
        )
        return VGroup(mob, box)

    def make_title(self, text, color=WHITE, font_size=42):
        return Text(text, font_size=font_size, color=color).move_to(
            UP * 6.5 + LEFT * 1.0
        )

    def clear_scene(self, *mobs):
        if mobs:
            self.play(*[FadeOut(m) for m in mobs])
        else:
            self.play(*[FadeOut(m) for m in self.mobjects])

    def make_polygon(self, n, apothem=1.0):
        R = apothem / np.cos(np.pi / n)
        poly = RegularPolygon(
            n, radius=R, color=WHITE, stroke_width=2
        )
        poly.rotate(-PI / 2, about_point=ORIGIN)
        return poly, R

    @staticmethod
    def vertex(angle, R):
        return R * np.array([np.cos(angle), np.sin(angle), 0])

    # ── SCENE 1 — The Mysterious Limit ────────────────────────────────────────

    def hook(self):
        limit_expr = MathTex(
            r"\lim_{n\to\infty}", r"n\tan\left(\frac{\pi}{n}\right)",
            font_size=52, color=MATH_COL,
        ).arrange(RIGHT, buff=0.3).move_to(MATH_CX * RIGHT)

        box = SurroundingRectangle(
            limit_expr, color=MATH_COL, buff=0.3, corner_radius=0.1
        )
        boxed_limit = VGroup(limit_expr, box)

        self.play(FadeIn(boxed_limit), run_time=2.0)
        self.wait(1.0)

        question = MathTex("?", font_size=52, color=WHITE).next_to(
            boxed_limit, DOWN, buff=1.0
        )
        self.play(FadeIn(question), run_time=0.5)
        self.wait(1.5)

        self.play(FadeOut(question), run_time=0.3)
        self.wait(0.5)
        self.clear_scene(boxed_limit)

    # ── SCENE 2 — A Regular Polygon Appears ───────────────────────────────────

    def scene_2_polygon(self):
        title = self.make_title("A Regular Polygon")
        self.play(Write(title), run_time=0.6)

        limit_small = MathTex(
            r"n\tan\left(\frac{\pi}{n}\right)",
            font_size=32, color=MATH_COL,
        ).move_to(UP * 5.5 + LEFT * 2.5)
        self.play(FadeIn(limit_small), run_time=0.4)

        hexagon, R = self.make_polygon(6)
        self.play(Create(hexagon), run_time=1.5)
        self.wait(0.5)

        center = Dot(ORIGIN, color=WHITE, radius=0.08)
        self.play(FadeIn(center), run_time=0.3)

        n = 6
        angles = [-PI / 2 + k * 2 * PI / n for k in range(n)]
        center_lines = VGroup()
        for angle in angles:
            end = R * np.array([np.cos(angle), np.sin(angle), 0])
            center_lines.add(Line(ORIGIN, end, color=WHITE, stroke_width=1.5))
        self.play(
            LaggedStart(*[Create(cl) for cl in center_lines], lag_ratio=0.1),
            run_time=1.5,
        )
        self.wait(0.5)

        idx = 0
        v0 = self.vertex(angles[idx], R)
        v1 = self.vertex(angles[idx + 1], R)
        tri = VGroup(
            Line(ORIGIN, v0, color=HIGHLIGHT, stroke_width=3),
            Line(ORIGIN, v1, color=HIGHLIGHT, stroke_width=3),
            Line(v1, v0, color=HIGHLIGHT, stroke_width=3),
        )
        self.play(Create(tri), run_time=0.8)
        self.wait(1.0)
        self.clear_scene()

    # ── SCENE 3 — What Is an Apothem? ─────────────────────────────────────────

    def scene_3_apothem(self):
        n = 6
        hexagon, R = self.make_polygon(n)
        self.add(hexagon)

        center = Dot(ORIGIN, color=WHITE, radius=0.08)
        self.add(center)

        angles = [-PI / 2 + k * 2 * PI / n for k in range(n)]
        center_lines = VGroup()
        for angle in angles:
            end = R * np.array([np.cos(angle), np.sin(angle), 0])
            center_lines.add(Line(ORIGIN, end, color=WHITE, stroke_width=1.5))
        self.add(center_lines)

        idx = 0
        v0 = self.vertex(angles[idx], R)
        v1 = self.vertex(angles[idx + 1], R)
        tri = VGroup(
            Line(ORIGIN, v0, color=HIGHLIGHT, stroke_width=3),
            Line(ORIGIN, v1, color=HIGHLIGHT, stroke_width=3),
            Line(v1, v0, color=HIGHLIGHT, stroke_width=3),
        )
        self.add(tri)

        mid = np.array([R * np.sin(PI / n), -1, 0])
        apothem_line = Line(ORIGIN, mid, color=APOthem_COL, stroke_width=3)
        self.play(Create(apothem_line), run_time=0.8)

        ra_size = 0.25
        ra = VGroup(
            Line(mid + UP * ra_size, mid + UP * ra_size + LEFT * ra_size,
                 color=APOthem_COL, stroke_width=2),
            Line(mid + LEFT * ra_size, mid + UP * ra_size + LEFT * ra_size,
                 color=APOthem_COL, stroke_width=2),
        )
        self.play(Create(ra), run_time=0.4)

        one_label = MathTex("1", font_size=40, color=APOthem_COL).next_to(
            apothem_line, RIGHT, buff=0.15
        )
        self.play(Write(one_label), run_time=0.4)

        apothem_label = MathTex(
            r"\text{apothem}", font_size=30, color=APOthem_COL,
        ).next_to(one_label, RIGHT, buff=0.3)
        self.play(Write(apothem_label), run_time=0.6)
        self.wait(1.5)
        self.clear_scene()

    # ── SCENE 4 — The Triangle Hiding Inside the Polygon ──────────────────────

    def scene_4_triangle(self):
        n = 6
        hexagon, R = self.make_polygon(n)
        self.add(hexagon)

        center = Dot(ORIGIN, color=WHITE, radius=0.08)
        self.add(center)

        angles = [-PI / 2 + k * 2 * PI / n for k in range(n)]
        center_lines = VGroup()
        for angle in angles:
            end = R * np.array([np.cos(angle), np.sin(angle), 0])
            center_lines.add(Line(ORIGIN, end, color=WHITE, stroke_width=1.5))
        self.add(center_lines)

        idx = 0
        v0 = self.vertex(angles[idx], R)
        v1 = self.vertex(angles[idx + 1], R)
        tri = VGroup(
            Line(ORIGIN, v0, color=HIGHLIGHT, stroke_width=3),
            Line(ORIGIN, v1, color=HIGHLIGHT, stroke_width=3),
            Line(v1, v0, color=HIGHLIGHT, stroke_width=3),
        )
        self.add(tri)

        mid = np.array([R * np.sin(PI / n), -1, 0])
        apothem_line = Line(ORIGIN, mid, color=APOthem_COL, stroke_width=3)
        self.add(apothem_line)

        half_tri = VGroup(
            Line(ORIGIN, mid, color=TRIANGLE_COL, stroke_width=3),
            Line(mid, v1, color=TRIANGLE_COL, stroke_width=3),
            Line(ORIGIN, v1, color=TRIANGLE_COL, stroke_width=3),
        )
        self.play(Create(half_tri), run_time=0.8)
        self.wait(0.5)

        central_angle = MathTex(
            r"\frac{2\pi}{n}", font_size=36, color=MATH_COL,
        ).move_to(UP * 1.5 + LEFT * 0.4)
        self.play(Write(central_angle), run_time=0.6)
        self.wait(0.5)

        half_angle = MathTex(
            r"\frac{\pi}{n}", font_size=40, color=TRIANGLE_COL,
        ).move_to(UP * 1.0 + LEFT * 0.4)
        self.play(Write(half_angle), run_time=0.6)
        self.wait(1.5)
        self.clear_scene()

    # ── SCENE 5 — The Tangent Appears ─────────────────────────────────────────

    def scene_5_tangent(self):
        apothem_line = Line(ORIGIN, DOWN * 2.5, color=APOthem_COL, stroke_width=3)
        self.play(Create(apothem_line), run_time=0.5)

        one_label = MathTex("1", font_size=44, color=APOthem_COL).next_to(
            apothem_line, LEFT, buff=0.2
        )
        self.play(Write(one_label), run_time=0.4)

        side_start = DOWN * 2.5
        side_end = DOWN * 2.5 + RIGHT * 1.8
        side_line = Line(
            side_start, side_end, color=WHITE, stroke_width=2
        )
        self.play(Create(side_line), run_time=0.5)

        x_label = MathTex("x", font_size=44, color=TRIANGLE_COL).next_to(
            side_line, DOWN, buff=0.2
        )
        self.play(Write(x_label), run_time=0.4)
        self.wait(0.5)

        angle_arc = Arc(
            radius=0.7, start_angle=-PI / 2, angle=PI / 6,
            color=WHITE, stroke_width=2,
        ).move_arc_center_to(ORIGIN)
        self.play(Create(angle_arc), run_time=0.4)

        angle_label = MathTex(
            r"\frac{\pi}{n}", font_size=36, color=WHITE,
        ).move_to(UP * 0.5 + LEFT * 0.8)
        self.play(Write(angle_label), run_time=0.4)

        hyp_end = DOWN * 2.5 + RIGHT * 1.8
        hyp = Line(
            ORIGIN, hyp_end, color=WHITE, stroke_width=2
        )
        self.play(Create(hyp), run_time=0.5)
        self.wait(0.5)

        tan_eq = MathTex(
            r"\tan\left(\frac{\pi}{n}\right)", r"=", r"\frac{x}{1}",
            font_size=44, color=MATH_COL,
        ).shift(UP * 2.5)
        self.play(Write(tan_eq), run_time=0.8)
        self.wait(0.5)

        result = MathTex(
            r"x", r"=", r"\tan\left(\frac{\pi}{n}\right)",
            font_size=44, color=TRIANGLE_COL,
        ).shift(UP * 1.0)
        box = SurroundingRectangle(
            result, color=TRIANGLE_COL, buff=0.25, corner_radius=0.1,
        )
        self.play(Write(result), Create(box), run_time=0.8)
        self.wait(1.5)
        self.clear_scene()

    # ── SCENE 6 — Find the Area ───────────────────────────────────────────────

    def scene_6_area(self):
        n = 6
        hexagon, R = self.make_polygon(n)
        self.play(Create(hexagon), run_time=1.0)

        center = Dot(ORIGIN, color=WHITE, radius=0.08)
        self.play(FadeIn(center), run_time=0.3)

        mid = np.array([R * np.sin(PI / n), -1, 0])
        half_side = MathTex(
            r"\tan\!\left(\frac{\pi}{n}\right)",
            font_size=28, color=TRIANGLE_COL,
        ).next_to(mid, DOWN, buff=0.15)
        self.play(Write(half_side), run_time=0.5)

        full_side = MathTex(
            r"2\tan\!\left(\frac{\pi}{n}\right)",
            font_size=36, color=TRIANGLE_COL,
        ).to_edge(LEFT, buff=0.5).shift(DOWN * 1.0)
        self.play(Write(full_side), run_time=0.6)
        self.wait(0.5)

        perimeter = MathTex(
            r"P", r"=", r"2n\tan\!\left(\frac{\pi}{n}\right)",
            font_size=40, color=MATH_COL,
        ).next_to(full_side, DOWN, buff=0.5)
        self.play(Write(perimeter), run_time=0.7)
        self.wait(0.5)

        area_formula = MathTex(
            r"A", r"=", r"\frac{1}{2}", r"P", r"\cdot", r"a",
            font_size=40, color=WHITE,
        ).next_to(perimeter, DOWN, buff=0.6)
        self.play(Write(area_formula), run_time=0.7)

        substitution = MathTex(
            r"A", r"=", r"\frac{1}{2}",
            r"\left[2n\tan\!\left(\frac{\pi}{n}\right)\right]",
            r"\cdot", r"1",
            font_size=36, color=MATH_COL,
        ).next_to(area_formula, DOWN, buff=0.5)
        self.play(Write(substitution), run_time=0.8)
        self.wait(0.5)

        result = self.show_boxed(
            r"A_n=n\tan\left(\frac{\pi}{n}\right)",
            color=TRIANGLE_COL, font_size=44,
        )
        result.next_to(substitution, DOWN, buff=0.6)
        self.play(Write(result), run_time=0.8)
        self.wait(1.0)

        pause_text = Text(
            "Wait.", font_size=48, color=HIGHLIGHT,
        ).to_edge(DOWN, buff=2.0)
        self.play(Write(pause_text), run_time=0.5)
        self.wait(1.0)
        self.clear_scene()

    # ── SCENE 7 — The Limit Has a Geometric Meaning ───────────────────────────

    def scene_7_polygon_progression(self):
        title = self.make_title("The Limit Has a Geometric Meaning")
        self.play(Write(title), run_time=0.6)

        expr = MathTex(
            r"n\tan\left(\frac{\pi}{n}\right)",
            font_size=44, color=MATH_COL,
        ).move_to(UP * 5.5 + LEFT * 2.5)
        self.play(FadeIn(expr), run_time=0.4)

        arrow = MathTex(r"\longrightarrow", font_size=36, color=HIGHLIGHT).next_to(
            expr, DOWN, buff=0.3
        )
        an = MathTex(r"A_n", font_size=44, color=TRIANGLE_COL).next_to(
            arrow, DOWN, buff=0.3
        )
        self.play(Write(arrow), Write(an), run_time=0.6)
        self.wait(0.5)

        ns = [3, 6, 12, 24, 48, 96]
        scale_factor = 2.0

        first_poly, _ = self.make_polygon(ns[0])
        first_poly.scale(scale_factor)
        self.play(Create(first_poly), run_time=0.8)

        n_label = MathTex(
            r"n=3", font_size=36, color=WHITE,
        ).next_to(first_poly, DOWN, buff=0.4)
        self.play(Write(n_label), run_time=0.4)
        self.wait(0.3)

        prev_poly = first_poly
        prev_label = n_label

        for ni in ns[1:]:
            new_poly, _ = self.make_polygon(ni)
            new_poly.scale(scale_factor)
            new_label = MathTex(
                rf"n={ni}", font_size=36, color=WHITE,
            ).next_to(new_poly, DOWN, buff=0.4)

            self.play(
                Transform(prev_poly, new_poly),
                Transform(prev_label, new_label),
                run_time=0.7,
            )
            self.wait(0.3)

        self.wait(1.0)
        self.clear_scene()

    # ── SCENE 8 — The Circle ──────────────────────────────────────────────────

    def scene_8_circle(self):
        title = self.make_title("The Circle")
        self.play(Write(title), run_time=0.6)

        circle = Circle(radius=2.0, color=WHITE, stroke_width=2)
        self.play(Create(circle), run_time=2.0)
        self.wait(0.5)

        r_label = MathTex(
            r"r=1", font_size=40, color=APOthem_COL,
        ).move_to(UP * 1.0 + LEFT * 2.5)
        self.play(Write(r_label), run_time=0.5)
        self.wait(0.5)

        area_result = MathTex(
            r"A", r"=", r"\pi r^2", r"=", r"\pi",
            font_size=52, color=MATH_COL,
        ).shift(DOWN * 2.0)
        self.play(Write(area_result), run_time=1.0)
        self.wait(1.5)
        self.clear_scene()

    # ── SCENE 9 — Return to the Original Limit ────────────────────────────────

    def scene_9_limit(self):
        limit_expr = MathTex(
            r"\lim_{n\to\infty}", r"n\tan\left(\frac{\pi}{n}\right)",
            font_size=48, color=MATH_COL,
        ).arrange(RIGHT, buff=0.3).shift(UP * 2.0)
        self.play(Write(limit_expr), run_time=1.0)
        self.wait(0.5)

        equals = MathTex("=", font_size=48, color=WHITE).next_to(
            limit_expr, DOWN, buff=0.5
        )
        lim_an = MathTex(
            r"\lim_{n\to\infty} A_n",
            font_size=44, color=TRIANGLE_COL,
        ).next_to(equals, DOWN, buff=0.5)
        self.play(Write(equals), Write(lim_an), run_time=0.8)
        self.wait(0.5)

        self.clear_scene(limit_expr, equals, lim_an)

        first_poly, _ = self.make_polygon(3)
        first_poly.scale(2.0)
        self.play(Create(first_poly), run_time=0.6)

        ns = [6, 12, 24, 48, 96]
        prev = first_poly
        for ni in ns:
            new_poly, _ = self.make_polygon(ni)
            new_poly.scale(2.0)
            self.play(Transform(prev, new_poly), run_time=0.5)

        circle = Circle(radius=2.0, color=WHITE, stroke_width=2)
        self.play(Transform(prev, circle), run_time=1.0)
        self.wait(0.5)

        pi_box = self.show_boxed(r"\pi", color=MATH_COL, font_size=72)
        pi_box.shift(DOWN * 2.5)
        self.play(Write(pi_box), run_time=0.8)
        self.wait(1.5)
        self.clear_scene()

    # ── ENDING — The Curiosity ────────────────────────────────────────────────

    def ending(self):
        final = self.show_boxed(
            r"\lim_{n\to\infty}n\tan\left(\frac{\pi}{n}\right)=\pi",
            color=MATH_COL, font_size=48,
        )
        final.shift(UP * 1.0)
        self.play(Write(final), run_time=1.5)
        self.wait(1.0)

        because = Text(
            "because it was geometry all along.",
            font_size=36, color=WHITE,
        ).next_to(final, DOWN, buff=1.0)
        self.play(Write(because), run_time=1.0)
        self.wait(2.0)
        self.clear_scene()
