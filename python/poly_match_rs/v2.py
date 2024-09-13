from typing import List, Tuple
import numpy as np
from .core import v2
import time

Point = np.array


class Polygon(v2.Polygon):
    _area: float = None

    def area(self) -> float:
        if self._area is None:
            self._area = 0.5 * np.abs(
                np.dot(self.x, np.roll(self.y, 1)) - np.dot(self.y, np.roll(self.x, 1))
            )
        return self._area


def generate_one_polygon() -> Polygon:
    x = np.arange(0.0, 1.0, 0.1)
    y = np.sqrt(1.0 - x**2)
    return Polygon(x=x, y=y)


def generate_example() -> Tuple[List[Polygon], List[np.array]]:
    rng = np.random.RandomState(6)
    xs = np.arange(0.0, 100.0, 1.0)
    rng.shuffle(xs)

    ys = np.arange(0.0, 100.0, 1.0)
    rng.shuffle(ys)

    points = np.array([np.array([x, y]) for x, y in zip(xs, ys)])

    ex_poly = generate_one_polygon()
    polygons = [
        Polygon(
            x=ex_poly.x + rng.randint(0.0, 100.0),
            y=ex_poly.y + rng.randint(0.0, 100.0),
        )
        for _ in range(1000)
    ]

    return polygons, points


def select_best_polygon(
    polygon_sets: List[Tuple[Point, List[Polygon]]]
) -> List[Tuple[Point, Polygon]]:
    best_polygons = []
    for point, polygons in polygon_sets:
        best_polygon = polygons[0]

        for poly in polygons:
            if poly.area() < best_polygon.area():
                best_polygon = poly

        best_polygons.append((point, best_polygon))

    return best_polygons


def main() -> float:
    polygons, points = generate_example()
    max_dist = 10.0
    start = time.perf_counter()
    for i in range(500):
        polygon_sets = v2.find_all_close_polygons(polygons, points, max_dist)
        _ = select_best_polygon(polygon_sets)
        if i >= 5 and time.perf_counter() - start > 3.0:
            break
    end = time.perf_counter()
    num_iter = i + 1
    took = (end - start) / num_iter
    return took