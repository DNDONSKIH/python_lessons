import simple_draw as sd
import random as r


def draw_snow():
    for i in range(50):
        x, y = r.randint(0, 400), r.randint(0, 50)
        point = sd.get_point(x, y)
        sd.snowflake(center=point, length=r.randint(5, 20))
