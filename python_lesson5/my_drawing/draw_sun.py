import simple_draw as sd
import random as r


def draw_sun():
    point = sd.get_point(200, 500)
    sd.circle(point, 50, sd.COLOR_YELLOW, 100)
