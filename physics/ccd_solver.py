"""第 58 批：子弹速度调到 600 米每秒，打薄墙直接穿过去，打斜板又停在半空..."""

def swept_distance(velocity, dt):
    """返回扫掠距离。"""
    raise NotImplementedError("TODO: swept_distance")

def expanded_extents(half_extents, velocity, dt):
    """扩展扫掠包围盒。"""
    raise NotImplementedError("TODO: expanded_extents")

def adaptive_substeps(distance, thickness):
    """按厚度返回子步数。"""
    raise NotImplementedError("TODO: adaptive_substeps")

def angular_sweep(angular_velocity, dt):
    """返回角扫掠角度。"""
    raise NotImplementedError("TODO: angular_sweep")

def is_trigger(layer, trigger_mask):
    """判断是否触发器。"""
    raise NotImplementedError("TODO: is_trigger")

def refresh_mask(mask, new_layer):
    """刷新分层掩码。"""
    raise NotImplementedError("TODO: refresh_mask")

def kinematic_push(platform_velocity, dt):
    """返回平台位移。"""
    raise NotImplementedError("TODO: kinematic_push")

def contact_normal(front, back):
    """返回一维接触法线。"""
    raise NotImplementedError("TODO: contact_normal")

def safe_position(start, normal, penetration):
    """回退到安全位置。"""
    raise NotImplementedError("TODO: safe_position")

def deterministic_order(shapes):
    """返回确定性形状顺序。"""
    raise NotImplementedError("TODO: deterministic_order")
