import math
import sys


def read_circle(file_path):
    with open(file_path, 'r') as file:
        x_center, y_center = map(float, file.readline().split())
        radius = float(file.readline().strip())
    return x_center, y_center, radius


def read_points(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            points.append((x, y))
    return points


def solve(x_center, y_center, radius, x, y):
    distance = math.sqrt((x - x_center) ** 2 + (y - y_center) ** 2)
    
    if distance < radius:
        return 1
    elif distance == radius:
        return 0
    else:
        return 2


def main():
    if len(sys.argv) != 3:
        print("Use,please: taks2.py <circle_file> <points_file>")
        sys.exit(1)

    circle_file = sys.argv[1]
    points_file = sys.argv[2]

    x_center, y_center, radius = read_circle(circle_file)
    points = read_points(points_file)
    for _, (x, y) in enumerate(points):
        print(solve(x_center, y_center, radius, x, y))


if __name__ == "__main__":
    main()
