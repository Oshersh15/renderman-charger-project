# Charger RenderMan Project

This project recreates an Apple USB-C power adapter using the RenderMan Python API. The scene includes custom geometry generation, physically based materials, image textures, custom OSL shaders, HDRI lighting and depth of field.

## Running the Project

Run from the project root:

```bash
python3 render.py
```

## Required Textures

The following texture files should be placed in the `textures` directory:

- `brown_photostudio_05_4k.tx`
- `wood_image.tx`
- `label2.tx`

## OSL Shaders

The project uses the following compiled OSL shaders:

- `plastic_wear.oso`
- `wood_bump.oso`

If modifications are made to the source `.osl` files, they must be recompiled using `oslc`.

## Output

The rendered image will be written to the path specified by `RENDER_OUTPUT` in `config.py`.
