def setup_camera(ri, cfg):
    target_x, target_y, target_z = cfg.CAMERA_TARGET

    ri.Translate(0, 0, cfg.CAMERA_DISTANCE)
    ri.Rotate(cfg.CAMERA_HEIGHT_ANGLE, 1, 0, 0)
    ri.Rotate(cfg.CAMERA_SIDE_ANGLE, 0, 1, 0)
    ri.Rotate(cfg.CAMERA_ROLL_ANGLE, 0, 0, 1)
    ri.Translate(-target_x, -target_y, -target_z)
