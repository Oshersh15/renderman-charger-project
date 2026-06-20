def create_lighting(ri, cfg):
    # Dome light
    ri.AttributeBegin()
    ri.Light(
        'PxrDomeLight',
        'studioHDRI',
        {
            'string lightColorMap': [cfg.HDRI_TEXTURE],
            'float intensity': [0.15],
            'float diffuse': [1],
            'float specular': [0.7],
        },
    )
    ri.AttributeEnd()

    # Rectangular window/key light
    ri.AttributeBegin()
    ri.Translate(-20, 8, -4)
    ri.Scale(10, 10, 10)
    ri.Rotate(50, 0, 1, 0)
    ri.Light(
        'PxrRectLight',
        'keyLight',
        {
            'float intensity': [25],
            'color lightColor': [1.0, 0.88, 0.68],
            'float exposure': [0],
        },
    )
    ri.AttributeEnd()
    
    
