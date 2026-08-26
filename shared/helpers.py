from manim import config


def set_vertical_frame(
    pixel_width: int = 1080,
    pixel_height: int = 1920,
) -> None:
    """Configure Manim for vertical 9:16 rendering.

    Call this at the top of a scene file before creating the scene class,
    or pass these as command-line arguments when rendering.

    Usage in a scene file:
        from shared.helpers import set_vertical_frame
        set_vertical_frame()
    """
    config.frame_height = 16
    config.frame_width = 9
    config.pixel_height = pixel_height
    config.pixel_width = pixel_width
