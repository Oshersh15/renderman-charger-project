from shaders.materials import create_metal_pins, create_pin_grey_plastic


def draw_pins(ri):
    pin_radius = 0.09
    pin_start = -1.95
    pin_split = -2.9
    pin_end = -3.35
    pin_spacing = 0.55

    create_pin_grey_plastic(ri)
    for x in [-pin_spacing, pin_spacing]:
        ri.TransformBegin()
        ri.Translate(x, 0, 0)
        ri.Cylinder(pin_radius, pin_start, pin_split, 360)
        ri.TransformEnd()

    create_metal_pins(ri)
    for x in [-pin_spacing, pin_spacing]:
        ri.TransformBegin()
        ri.Translate(x, 0, 0)
        ri.Cylinder(pin_radius, pin_split, pin_end, 360)

        ri.TransformBegin()
        ri.Translate(0, 0, pin_end)
        ri.Sphere(pin_radius, -pin_radius, pin_radius, 360)
        ri.TransformEnd()

        ri.TransformEnd()
