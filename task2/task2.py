import sys
from fractions import Fraction


ellipse_path, points_path = sys.argv[1:]

with open(ellipse_path, encoding="utf-8-sig") as ellipse_file:
    center_x, center_y, radius_x, radius_y = map(
        Fraction, ellipse_file.read().split()
    )

with open(points_path, encoding="utf-8-sig") as points_file:
    for line in points_file:
        if not line.strip():
            continue

        x, y = map(Fraction, line.split())

        horizontal = (x - center_x) / radius_x
        vertical = (y - center_y) / radius_y
        score = horizontal ** 2 + vertical ** 2

        if score == 1:
            print(0)
        elif score < 1:
            print(1)
        else:
            print(2)
