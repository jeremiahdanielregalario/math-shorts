from manim import *

# Configure vertical 9:16 format
config.frame_height = 16
config.frame_width = 9
config.pixel_height = 1920
config.pixel_width = 1080


class CircleToSquare(Scene):
    """A circle smoothly morphs into a square.

    This is a minimal smoke-test scene to verify the project
    setup and vertical rendering pipeline.
    """

    def construct(self):
        circle = Circle(radius=2, color=BLUE)
        square = Square(side_length=4, color=GREEN)

        title = Text("Morphing Shapes", font_size=48)
        title.to_edge(UP, buff=1.5)

        self.play(Write(title))
        self.play(Create(circle))
        self.wait(0.5)

        self.play(Transform(circle, square), run_time=2)
        self.wait(0.5)

        self.play(FadeOut(circle), FadeOut(title))
