import simple_draw as sd


def draw_roof(x, y):
    point = sd.get_point(x, y)
    v1 = sd.get_vector(start_point=point, angle=0, length=400, width=3)
    v2 = sd.get_vector(start_point=v1.start_point, angle=30, length=230, width=3)
    v3 = sd.get_vector(start_point=v1.end_point, angle=150, length=230, width=3)
    v1.draw()
    v2.draw()
    v3.draw()
