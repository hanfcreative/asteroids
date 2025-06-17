SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS
ASTEROID_VELOCITY_MULT = 1.2

PLAYER_RADIUS = 20
PLAYER_TURN_SPEED = 300
PLAYER_SPEED = 200
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

SHOT_RADIUS = 5
SHOT_DURATION = 3

STAR_COLOR = (255, 255, 255)
# smaller = deeper = slower
STAR_PARALLAX_MIN = 0.05
STAR_PARALLAX_MAX = 0.3

NIGHTSKY_NUM_STARS = 100
# for 60 FPS: 1 = very slow change, 60 = instant jump tp target
# NIGHTSKY_PARALLAX_EASE <= 1 / dt ≈ 60
NIGHTSKY_PARALLAX_EASE = 5
# multiplier currently only used in hybrid mode. add to other modes?
# currently screen wrap can not keep up with. consider changing wrap math 
NIGHTSKY_PARALLAX_MOVE_MULTIPLIER = 2.0
# options: "arcade", "realistic", "smooth", "hybrid"
NIGHTSKY_PARALLAX_MODE = "hybrid"
NIGHTSKY_PARALLAX_BEHAVIOR = {
    "arcade": {
        "retain_velocity_on_stop": True,
    },
    "realistic": {
        "retain_velocity_on_stop": False,
    },
    "smooth": {
        "retain_velocity_on_stop": False,
    },
    "hybrid": {
        "retain_velocity_on_stop": True,
    },
}
