import math

from shaders.materials import create_glossy_white_plastic, create_matte_grey_inset


def build_charger_outline(arc_segments=120):
    """Build the rounded outline used for the main charger body."""

    outline = []

    outline.append((-0.75, 1.0))
    outline.append((0.75, 1.0))

    for i in range(1, arc_segments):
        t = i / float(arc_segments)
        angle = math.radians(90 - t * 180)
        x = 0.75 + 0.43 * math.cos(angle)
        y = 1.0 * math.sin(angle)
        outline.append((x, y))

    outline.append((0.75, -1.0))
    outline.append((-0.75, -1.0))

    for i in range(1, arc_segments):
        t = i / float(arc_segments)
        angle = math.radians(-90 - t * 180)
        x = -0.75 + 0.43 * math.cos(angle)
        y = 1.0 * math.sin(angle)
        outline.append((x, y))

    return outline


def draw_main_body(ri):
    """Draw the white outer body and the grey recessed front inset."""

    outline = build_charger_outline()
    count = len(outline)

    inner_x_scale = 0.95
    inner_y_scale = 0.85
    inner_outline = [(x * inner_x_scale, y * inner_y_scale) for x, y in outline]

    white_points = []
    for x, y in outline:
        white_points.extend([x, y, -1])
    for x, y in outline:
        white_points.extend([x, y, 1])
    for x, y in inner_outline:
        white_points.extend([x, y, -1])
    for x, y in inner_outline:
        white_points.extend([x, y, 1])

    outer_front = 0
    outer_back = count
    inner_front = count * 2
    inner_back = count * 3

    white_npolys = []
    white_indices = []

    for i in range(count):
        j = (i + 1) % count
        white_npolys.append(4)
        white_indices.extend(
            [outer_front + i, outer_back + i, outer_back + j, outer_front + j]
        )

    for i in range(count):
        j = (i + 1) % count
        white_npolys.append(4)
        white_indices.extend(
            [outer_front + i, outer_front + j, inner_front + j, inner_front + i]
        )

    for i in range(count):
        j = (i + 1) % count
        white_npolys.append(4)
        white_indices.extend(
            [outer_back + j, outer_back + i, inner_back + i, inner_back + j]
        )

    create_glossy_white_plastic(ri)
    ri.TransformBegin()
    ri.Scale(1.0, 0.6, 1.15)
    ri.PointsPolygons(white_npolys, white_indices, {ri.P: white_points})
    ri.TransformEnd()

    grey_points = []
    for x, y in inner_outline:
        grey_points.extend([x, y, -1])

    create_matte_grey_inset(ri)
    ri.TransformBegin()
    ri.Scale(1.0, 0.6, 1.15)
    ri.PointsPolygons([count], list(range(count)), {ri.P: grey_points})
    ri.TransformEnd()
