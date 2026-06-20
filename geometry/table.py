import math


def draw_table(ri):
    table_points = [
        -30, 0, -30,
         30, 0, -30,
         30, 0,  30,
        -30, 0,  30,
    ]

    u_offset = -0.2
    v_offset = -0.2
    angle = math.radians(30)
    cx = 0.5
    cy = 0.5

    uvs = [(0, 0), (1, 0), (1, 1), (0, 1)]
    table_st = []

    for u, v in uvs:
        u -= cx
        v -= cy

        ru = u * math.cos(angle) - v * math.sin(angle)
        rv = u * math.sin(angle) + v * math.cos(angle)

        ru += cx + u_offset
        rv += cy + v_offset

        table_st.extend([ru, rv])

    ri.TransformBegin()
    ri.Translate(0, -0.61, -1)
    
    table_s = table_st[0::2]
    table_t = table_st[1::2]
    
    ri.PointsPolygons(
        [4],
        [0, 3, 2, 1],
        {
            ri.P: table_points,
            'facevarying float[2] st': table_st,
            'facevarying float sCoord': table_s,
            'facevarying float tCoord': table_t,
        }
    )
    
    ri.TransformEnd()
