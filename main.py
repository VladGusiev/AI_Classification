import copy

import matplotlib.pyplot as plt
import random
import time
from progress.bar import ChargingBar


CLASSIFIED_CORRECTLY = 0
CLASSIFIED_INCORRECTLY = 0

POINTS_ARRAY = []
ALL_COLORS = ["red", "green", "blue", "violet"]
CLASSIFIED_POINTS_ARRAY = []


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

        CLASSIFIED_POINTS_ARRAY.append(Point("red", -4500, -4400))
        CLASSIFIED_POINTS_ARRAY.append(Point("red", -4100, -3000))
        CLASSIFIED_POINTS_ARRAY.append(Point("red", -2500, -3400))
        CLASSIFIED_POINTS_ARRAY.append(Point("red", -2000, -1400))
        # GREEN POINTS
        POINTS_ARRAY.append(Point("green", 4500, -4400))
        POINTS_ARRAY.append(Point("green", 4100, -3000))
        POINTS_ARRAY.append(Point("green", 1800, -2400))
        POINTS_ARRAY.append(Point("green", 2500, -3400))
        POINTS_ARRAY.append(Point("green", 2000, -1400))

        CLASSIFIED_POINTS_ARRAY.append(Point("green", 4500, -4400))
        CLASSIFIED_POINTS_ARRAY.append(Point("green", 4100, -3000))
        CLASSIFIED_POINTS_ARRAY.append(Point("green", 1800, -2400))
        CLASSIFIED_POINTS_ARRAY.append(Point("green", 2500, -3400))
        CLASSIFIED_POINTS_ARRAY.append(Point("green", 2000, -1400))
        # BLUE POINTS
        POINTS_ARRAY.append(Point("blue", -4500, 4400))
        POINTS_ARRAY.append(Point("blue", -4100, 3000))
        POINTS_ARRAY.append(Point("blue", -1800, 2400))
        POINTS_ARRAY.append(Point("blue", -2500, 3400))
        POINTS_ARRAY.append(Point("blue", -2000, 1400))

        CLASSIFIED_POINTS_ARRAY.append(Point("blue", -4500, 4400))
        CLASSIFIED_POINTS_ARRAY.append(Point("blue", -4100, 3000))
        CLASSIFIED_POINTS_ARRAY.append(Point("blue", -1800, 2400))
        CLASSIFIED_POINTS_ARRAY.append(Point("blue", -2500, 3400))
        CLASSIFIED_POINTS_ARRAY.append(Point("blue", -2000, 1400))
        # VIOLET POINTS
        POINTS_ARRAY.append(Point("violet", 4500, 4400))
        POINTS_ARRAY.append(Point("violet", 4100, 3000))
        POINTS_ARRAY.append(Point("violet", 1800, 2400))
        POINTS_ARRAY.append(Point("violet", 2500, 3400))
        POINTS_ARRAY.append(Point("violet", 2000, 1400))

        CLASSIFIED_POINTS_ARRAY.append(Point("violet", 4500, 4400))
        CLASSIFIED_POINTS_ARRAY.append(Point("violet", 4100, 3000))
        CLASSIFIED_POINTS_ARRAY.append(Point("violet", 1800, 2400))
        CLASSIFIED_POINTS_ARRAY.append(Point("violet", 2500, 3400))
        CLASSIFIED_POINTS_ARRAY.append(Point("violet", 2000, 1400))


def distance(point1, point2):
    return ((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2) ** (1 / 2)


def classify_point(point, k):
    nearest_points = nearest_k_points(point, k)
    red_points = 0
    green_points = 0
    blue_points = 0
    violet_points = 0

    for p in nearest_points:
        if p.color == "red":
            red_points += 1
        elif p.color == "green":
            green_points += 1
        elif p.color == "blue":
            blue_points += 1
        elif p.color == "violet":
            violet_points += 1

    all_colors = [[red_points, "red"], [green_points, "green"], [blue_points, "blue"], [violet_points, "violet"]]
    all_colors.sort(key=lambda x: x[0])

    CLASSIFIED_POINTS_ARRAY.append(Point(all_colors[-1][1], point.x, point.y))
    return all_colors[-1][1]


def calculate_distance_to_all_points(point):
    distances = [(distance(point, p), p) for p in CLASSIFIED_POINTS_ARRAY]
    return distances


def nearest_k_points(point, k):
    distances = calculate_distance_to_all_points(point)
    distances.sort(key=lambda x: x[0])
    nearest_points = [point[1] for point in distances[:k]]
    return nearest_points


def generate_test_environment():
    bar = ChargingBar('Generating test environment', max=4000)

    last_color = ""
    for i in range(0, 4000):

        new_point_color = ALL_COLORS[random.randint(0, 3)]
        while new_point_color == last_color:
            new_point_color = ALL_COLORS[random.randint(0, 3)]
        new_coords = False

        if random.randint(1, 100) != 1:
            x, y = generate_x_and_y(new_point_color)
            # check if point with same coordinates already exists, repeat until new coordinates are found
            while not new_coords:
                for point in POINTS_ARRAY:
                    if point.x == x and point.y == y:
                        x, y = generate_x_and_y(new_point_color)
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

        if classify_point(Point(new_point_color, x, y), 1) == new_point_color:
            global CLASSIFIED_CORRECTLY
            CLASSIFIED_CORRECTLY += 1
        else:
            global CLASSIFIED_INCORRECTLY
            CLASSIFIED_INCORRECTLY += 1

        POINTS_ARRAY.append(Point(new_point_color, x, y))
        last_color = copy.deepcopy(new_point_color)
        bar.next()
    bar.finish()


def generate_x_and_y(new_point_color):
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
    return x, y


# classify all remaining points on the grid
def classify_remaining_points():

    bar = ChargingBar('Classifying all remaining coordinates')
    for x in range(-5000, 5000):
        for y in range(-5000, 5000):
            # check if point with same coordinates already exists, repeat until new coordinates are found
            for point in CLASSIFIED_POINTS_ARRAY:
                if point.x != x and point.y != y:
                    classify_point(Point("unknown", x, y), 1)
                    bar.next()
    bar.finish()


def main():
    start_time = time.time()
    initial_point_generation()
    generate_test_environment()

    plot_bar = ChargingBar('Plotting classified result', max=4000)
    for point in CLASSIFIED_POINTS_ARRAY:
        plt.scatter(point.x, point.y, marker='.', s=1, color=point.color)
        plot_bar.next()
    plot_bar.finish()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Classification Classified Points')
    plt.grid(True)
    plt.show()

    plot_bar = ChargingBar('Plotting test environment', max=4000)
    for point in POINTS_ARRAY:
        plt.scatter(point.x, point.y, marker='.', s=1, color=point.color)
        plot_bar.next()
    plot_bar.finish()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Classification Test Environment')
    plt.grid(True)
    plt.show()

    print("Correctly classified points: " + str(CLASSIFIED_CORRECTLY))
    print("Incorrectly classified points: " + str(CLASSIFIED_INCORRECTLY))

    classify_remaining_points()

    plot_bar = ChargingBar('Plotting final result')
    for point in CLASSIFIED_POINTS_ARRAY:
        plt.scatter(point.x, point.y, marker='.', s=1, color=point.color)
        plot_bar.next()
    plot_bar.finish()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Classification Fully Classified Environment')
    plt.grid(True)
    plt.show()

    end_time = time.time()
    print("Time elapsed: " + str(end_time - start_time))


if __name__ == '__main__':
    main()
