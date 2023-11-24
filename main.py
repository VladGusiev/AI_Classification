import copy

import matplotlib.pyplot as plt
import random

POINTS_ARRAY = []
ALL_COLORS = ["red", "green", "blue", "violet"]

class Point:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


def initial_point_generation():
        # RED POINTS
        POINTS_ARRAY.append(Point("red", -4500, -4400))
        POINTS_ARRAY.append(Point("red", -4100, -3000))
        POINTS_ARRAY.append(Point("red", -2500, -3400))
        POINTS_ARRAY.append(Point("red", -2000, -1400))
        # GREEN POINTS
        POINTS_ARRAY.append(Point("green", 4500, -4400))
        POINTS_ARRAY.append(Point("green", 4100, -3000))
        POINTS_ARRAY.append(Point("green", 1800, -2400))
        POINTS_ARRAY.append(Point("green", 2500, -3400))
        POINTS_ARRAY.append(Point("green", 2000, -1400))
        # BLUE POINTS
        POINTS_ARRAY.append(Point("blue", -4500, 4400))
        POINTS_ARRAY.append(Point("blue", -4100, 3000))
        POINTS_ARRAY.append(Point("blue", -1800, 2400))
        POINTS_ARRAY.append(Point("blue", -2500, 3400))
        POINTS_ARRAY.append(Point("blue", -2000, 1400))
        # VIOLET POINTS
        POINTS_ARRAY.append(Point("violet", 4500, 4400))
        POINTS_ARRAY.append(Point("violet", 4100, 3000))
        POINTS_ARRAY.append(Point("violet", 1800, 2400))
        POINTS_ARRAY.append(Point("violet", 2500, 3400))
        POINTS_ARRAY.append(Point("violet", 2000, 1400))


def distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** (1 / 2)


def find_nearest_point(point):
    min_distance = 10
    nearest_point = None
    for p in POINTS_ARRAY:
        if p != point:
            if distance(point, p) < min_distance:
                min_distance = distance(point, p)
                nearest_point = p
    return nearest_point


def generate_test_environment():
    last_color = ""
    for i in range(0, 4000):

        new_point_color = ALL_COLORS[random.randint(0, 3)]
        while new_point_color == last_color:
            new_point_color = ALL_COLORS[random.randint(0, 3)]
        new_coords = False

        if random.randint(1, 100) != 1:
            if new_point_color == "red":
                x = random.randint(-5000, 500)
                y = random.randint(-5000, 500)
            elif new_point_color == "green":
                x = random.randint(-500, 5000)
                y = random.randint(-5000, 500)
            elif new_point_color == "blue":
                x = random.randint(-5000, 500)
                y = random.randint(-500, 5000)
            elif new_point_color == "violet":
                x = random.randint(-500, 5000)
                y = random.randint(-500, 5000)
            # check if point with same coordinates already exists, repeat until new coordinates are found
            while not new_coords:
                for point in POINTS_ARRAY:
                    if point.x == x and point.y == y:
                        if new_point_color == "red":
                            x = random.randint(-5000, 500)
                            y = random.randint(-5000, 500)
                        elif new_point_color == "green":
                            x = random.randint(-500, 5000)
                            y = random.randint(-5000, 500)
                        elif new_point_color == "blue":
                            x = random.randint(-5000, 500)
                            y = random.randint(-500, 5000)
                        elif new_point_color == "violet":
                            x = random.randint(-500, 5000)
                            y = random.randint(-500, 5000)
                        break
                    new_coords = True
        else:
            # generate random coordinates
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
            # check if point with same coordinates already exists, repeat until new coordinates are found
            while not new_coords:
                for point in POINTS_ARRAY:
                    if point.x == x and point.y == y:
                        x = random.randint(-5000, 5000)
                        y = random.randint(-5000, 5000)
                        break
                    new_coords = True

        POINTS_ARRAY.append(Point(new_point_color, x, y))
        last_color = copy.deepcopy(new_point_color)
        print("new point color", new_point_color)


def main():

    initial_point_generation()
    generate_test_environment()

    for point in POINTS_ARRAY:
        plt.scatter(point.x, point.y, marker='o', color=point.color)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Classification')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
