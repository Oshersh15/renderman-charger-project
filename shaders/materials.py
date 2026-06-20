def create_table_material(ri, cfg):
    ri.Pattern(
        "PxrTexture",
        "woodTexture",
        {
            "string filename": [cfg.WOOD_TEXTURE],
        },
    )

    ri.Pattern(
        "PxrColorCorrect",
        "warmWoodTexture",
        {
            "reference color inputRGB": ["woodTexture:resultRGB"],
            "color rgbGain": [1.25, 0.85, 0.55],
        },
    )

    ri.Pattern(
        "wood_bump",
        "woodBumpOSL",
        {
            "float grainAngle": [60.0],
            "float grainScale": [1.2],
            "float lineDensity": [18.0],
            "float warpStrength": [0.35],
            "float contrast": [1.8],
            "float grainStrength": [0.008],
        },
    )

    ri.Pattern(
        "PxrBump",
        "woodBump",
        {
            "reference float inputBump": ["woodBumpOSL:resultF"],
            "float scale": [3.0],
        },
    )

    ri.Bxdf(
        "PxrDisney",
        "simpleWoodTable",
        {
            "reference color baseColor": ["warmWoodTexture:resultRGB"],
            "reference normal bumpNormal": ["woodBump:resultN"],
            "float metallic": [0],
            "float specular": [0.05],
            "float roughness": [0.8],
            "float clearcoat": [0.0],
            "float clearcoatGloss": [0.5],
            "float presence": [1],
        },
    )


def create_glossy_white_plastic(ri):
    ri.Pattern(
        "plastic_wear",
        "plasticWear",
        {
            "color cleanColor": [
                0.82,
                0.80,
                0.76,
            ],  # Base white/plastic colour before dents.
            "float spotScale": [
                2.0
            ],  # Overall pattern scale. Lower = fewer possible dents. Higher = more dents.
            "float spotThreshold": [
                0.7
            ],  # How many dents survive. Higher = fewer dents. Lower = more dents.
            "float spotRadius": [
                0.001
            ],  # Size of each dent/spot. Higher = bigger marks.
            "float spotSoftness": [
                0.02
            ],  # Edge softness. Higher = blurrier/softer dents.
            "float shapeNoise": [
                0.035
            ],  # Irregularity of the circle shape. Higher = less perfect circles.
            "float patternSeed": [3.0],  # Changes the random dent layout.
            "float patternOffsetX": [0.0],  # Slides the whole dent pattern in X.
            "float patternOffsetY": [
                0.0
            ],  # Slides the whole dent pattern in Y/Z direction.
            "float patternAngle": [-10.0],  # Rotates the whole dent pattern.
            "float spotDarkness": [
                0.14
            ],  # How visible/dark the dents are in the colour.
            "float roughnessBase": [0.16],  # Normal plastic roughness outside dents.
            "float roughnessBoost": [0.35],  # Extra roughness inside dents.
        },
    )

    ri.Pattern(
        "PxrBump",
        "plasticDentBump",
        {
            "reference float inputBump": ["plasticWear:bumpOut"],
            "float scale": [0.25],
        },
    )

    ri.Bxdf(
        "PxrDisney",
        "glossyWhitePlastic",
        {
            "reference color baseColor": ["plasticWear:baseColorOut"],
            "color emitColor": [0, 0, 0],
            "float subsurface": [0],
            "color subsurfaceColor": [0, 0, 0],
            "float metallic": [0],
            "float specular": [0.75],
            "float specularTint": [0],
            "reference float roughness": ["plasticWear:roughnessOut"],
            "float anisotropic": [0],
            "float sheen": [0],
            "float sheenTint": [0.5],
            "float clearcoat": [0.45],
            "float clearcoatGloss": [0.8],
            "float presence": [1],
            "reference normal bumpNormal": ["plasticDentBump:resultN"],
        },
    )


def create_matte_grey_inset(ri):
    ri.Bxdf(
        "PxrDisney",
        "matteGreyInset",
        {
            "color baseColor": [0.68, 0.67, 0.64],
            "color emitColor": [0, 0, 0],
            "float subsurface": [0],
            "color subsurfaceColor": [0, 0, 0],
            "float metallic": [0],
            "float specular": [0.2],
            "float specularTint": [0],
            "float roughness": [0.65],
            "float anisotropic": [0],
            "float sheen": [0],
            "float sheenTint": [0.5],
            "float clearcoat": [0.0],
            "float clearcoatGloss": [0.5],
            "float presence": [1],
        },
    )


def create_matte_grey_plastic(ri, name="matteGreyPlastic", base=(0.68, 0.67, 0.64)):
    ri.Bxdf(
        "PxrDisney",
        name,
        {
            "color baseColor": list(base),
            "float metallic": [0],
            "float specular": [0.2],
            "float roughness": [0.65],
            "float clearcoat": [0],
            "float presence": [1],
        },
    )


def create_label_material(ri, cfg):
    ri.Pattern(
        "PxrTexture",
        "labelTexture",
        {
            "string filename": [cfg.LABEL_TEXTURE],
        },
    )

    ri.Bxdf(
        "PxrDisney",
        "labelFaceMaterial",
        {
            "reference color baseColor": ["labelTexture:resultRGB"],
            "float metallic": [0],
            "float specular": [0.2],
            "float roughness": [0.65],
            "float clearcoat": [0],
            "float presence": [1],
        },
    )


def create_pin_grey_plastic(ri):
    create_matte_grey_plastic(ri, name="pinGreyPlastic", base=(0.68, 0.67, 0.64))


def create_metal_pins(ri):
    ri.Bxdf(
        "PxrDisney",
        "metalPins",
        {
            "color baseColor": [0.7, 0.7, 0.7],
            "float metallic": [1],
            "float specular": [1],
            "float roughness": [0.15],
            "float clearcoat": [0],
            "float presence": [1],
        },
    )
