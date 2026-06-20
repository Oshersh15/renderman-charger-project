import math

from shaders.materials import create_label_material, create_matte_grey_plastic


def draw_plug_block(ri, cfg):
    plug_outline = [
        (-0.45, 1.00),
        (0.45, 1.00),
        (0.47, 0.98),
        (0.49, 0.96),
        (0.73, 0.19),
        (0.75, 0.0),
        (0.73, -0.19),
        (0.49, -0.96),
        (0.47, -0.98),
        (0.45, -1.00),
        (-0.45, -1.00),
        (-0.47, -0.98),
        (-0.49, -0.96),
        (-0.73, -0.19),
        (-0.75, 0.0),
        (-0.73, 0.2),
        (-0.49, 0.96),
        (-0.47, 0.98),
    ]

    plug_count = len(plug_outline)

    plug_side_points = []
    plug_side_normals = []

    for z in [-1, 1]:
        for x, y in plug_outline:
            plug_side_points.extend([x, y, z])
            length = math.sqrt(x * x + y * y)
            nx = x / length
            ny = y / length
            plug_side_normals.extend([nx, ny, 0])

    plug_side_npolys = [4] * plug_count
    plug_side_indices = []

    for i in range(plug_count):
        j = (i + 1) % plug_count
        plug_side_indices.extend([i, i + plug_count, j + plug_count, j])

    plug_back_points = []
    for x, y in plug_outline:
        plug_back_points.extend([x, y, -1])
    plug_back_indices = list(range(plug_count))

    plug_front_points = []
    label_st = []

    min_x = min(p[0] for p in plug_outline)
    max_x = max(p[0] for p in plug_outline)
    min_y = min(p[1] for p in plug_outline)
    max_y = max(p[1] for p in plug_outline)

    for x, y in plug_outline:
        plug_front_points.extend([x, y, 1])

        s = (x - min_x) / (max_x - min_x)
        t = (y - min_y) / (max_y - min_y)
        t = 1.0 - t
        s = 1.0 - s
        t = (t - 0.5) * 0.4 + 0.5
        label_st.extend([s, t])

    plug_front_indices = list(range(plug_count - 1, -1, -1))

    ri.TransformBegin()
    ri.Translate(0, 0, -1.67)
    ri.Scale(1.32, 0.33, 0.57)

    create_label_material(ri, cfg)
    ri.PointsPolygons(
        [plug_count],
        plug_back_indices,
        {
            ri.P: plug_back_points,
            'facevarying float[2] st': label_st,
        },
    )

    create_matte_grey_plastic(ri, name='matteGreyPlastic', base=(0.68, 0.67, 0.64))
    ri.PointsPolygons(
        plug_side_npolys,
        plug_side_indices,
        {
            ri.P: plug_side_points,
            'vertex normal N': plug_side_normals,
        },
    )
    ri.PointsPolygons([plug_count], plug_front_indices, {ri.P: plug_front_points})

    ri.TransformEnd()