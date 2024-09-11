from .core import v0
from .baseline import generate_example, select_best_polygon
import time


def main():
    polygons, points = generate_example()
    max_dist = 10.0
    start = time.perf_counter()
    for i in range(500):
        polygon_sets = []
        for point in points:
            close_polygons = v0.find_close_polygons(polygons, point, max_dist)
            if len(close_polygons) == 0:
                continue
            polygon_sets.append((point, close_polygons))
        _ = select_best_polygon(polygon_sets)
        if i >= 5 and time.perf_counter() - start > 3.0:
            break
    end = time.perf_counter()
    num_iter = i + 1
    took = (end - start) / num_iter
    return took
