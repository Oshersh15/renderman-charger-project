from geometry.charger_body import draw_main_body
from geometry.pins import draw_pins
from geometry.plug_block import draw_plug_block


def draw_charger(ri, cfg):
    """Draw the complete charger assembly."""

    ri.TransformBegin()
    ri.Rotate(25, 0, 1, 0)

    draw_main_body(ri)
    draw_plug_block(ri, cfg)
    draw_pins(ri)

    ri.TransformEnd()
