#!/usr/bin/python3
import prman

import config as cfg
from geometry.charger import draw_charger
from geometry.table import draw_table
from scene.camera import setup_camera
from scene.lighting import create_lighting
from shaders.materials import create_table_material


def render():
    ri = prman.Ri()
    ri.Option("rib", {"string asciistyle": "indented"})

    ri.Begin("__render")
    ri.Display(cfg.RENDER_OUTPUT, "it", "rgba")
    ri.Display(cfg.RENDER_OUTPUT, "openexr", "rgba")
    ri.Format(cfg.RENDER_WIDTH, cfg.RENDER_HEIGHT, 1)
    ri.PixelVariance(0.001)
    ri.Projection(ri.PERSPECTIVE, {ri.FOV: cfg.FOV})

    setup_camera(ri, cfg)

    # for render 1:
    # ri.DepthOfField(
    #     5.6,   # f-stop: lower = stronger blur, higher = subtler blur
    #     1.0,   # focal length
    #     15.0   # focal distance: distance from camera to the charger
    # )

    # for render 2:
    # ri.DepthOfField(
    #     12.0,   # f-stop: lower = stronger blur, higher = subtler blur
    #     1.0,   # focal length
    #     6.0   # focal distance: distance from camera to the charger
    # )

    ri.Option("searchpath", {"string shader": [cfg.WOOD_OSL]})

    ri.Integrator("PxrPathTracer", "integrator", {})
    ri.WorldBegin()

    create_lighting(ri, cfg)

    create_table_material(ri, cfg)
    draw_table(ri)

    draw_charger(ri, cfg)

    ri.WorldEnd()
    ri.End()


if __name__ == "__main__":
    render()
