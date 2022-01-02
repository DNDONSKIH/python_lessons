#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint


def get_distance(x1, y1, x2, y2):
    return (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** .5


# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

msk_x = sites["Moscow"][0]
msk_y = sites["Moscow"][1]
lnd_x = sites["London"][0]
lnd_y = sites["London"][1]
prs_x = sites["Paris"][0]
prs_y = sites["Paris"][1]

distance_Moscow_London = get_distance(msk_x, msk_y, lnd_x, lnd_y)
distance_Moscow_Paris = get_distance(msk_x, msk_y, prs_x, prs_y)

distance_London_Paris = get_distance(lnd_x, lnd_y, prs_x, prs_y)
distance_London_Moscow = distance_Moscow_London

distance_Paris_Moscow = distance_Moscow_Paris
distance_Paris_London = distance_London_Paris

distances = {
    "Moscow": {"London": distance_Moscow_London, "Paris": distance_Moscow_Paris},
    "London": {"Paris": distance_London_Paris, "Moscow": distance_London_Moscow},
    "Paris": {"Moscow": distance_Paris_Moscow, "London": distance_Paris_London},
}

pprint(distances)
