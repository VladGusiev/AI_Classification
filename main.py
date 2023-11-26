import copy

import matplotlib.pyplot as plt
import heapq
import random
import time
from progress.bar import Bar


CLASSIFIED_CORRECTLY = [0, 0, 0, 0]
CLASSIFIED_INCORRECTLY = [0, 0, 0, 0]


POINTS_ARRAY = set()
CLASSIFIED_1K_POINTS_ARRAY = set()
CLASSIFIED_3K_POINTS_ARRAY = set()
CLASSIFIED_7K_POINTS_ARRAY = set()
CLASSIFIED_15K_POINTS_ARRAY = set()

ALL_COLORS = ["red", "green", "blue", "violet"]


class Point:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y


def initial_point_generation():
        # RED POINTS
        POINTS_ARRAY.add(Point("red", -4500, -4400))
        POINTS_ARRAY.add(Point("red", -4100, -3000))
        POINTS_ARRAY.add(Point("red", -2500, -3400))
        POINTS_ARRAY.add(Point("red", -2000, -1400))

        # GREEN POINTS
        POINTS_ARRAY.add(Point("green", 4500, -4400))
        POINTS_ARRAY.add(Point("green", 4100, -3000))
        POINTS_ARRAY.add(Point("green", 1800, -2400))
        POINTS_ARRAY.add(Point("green", 2500, -3400))
        POINTS_ARRAY.add(Point("green", 2000, -1400))

        # BLUE POINTS
        POINTS_ARRAY.add(Point("blue", -4500, 4400))
        POINTS_ARRAY.add(Point("blue", -4100, 3000))
        POINTS_ARRAY.add(Point("blue", -1800, 2400))
        POINTS_ARRAY.add(Point("blue", -2500, 3400))
        POINTS_ARRAY.add(Point("blue", -2000, 1400))

        # VIOLET POINTS
        POINTS_ARRAY.add(Point("violet", 4500, 4400))
        POINTS_ARRAY.add(Point("violet", 4100, 3000))
        POINTS_ARRAY.add(Point("violet", 1800, 2400))
        POINTS_ARRAY.add(Point("violet", 2500, 3400))
        POINTS_ARRAY.add(Point("violet", 2000, 1400))

        for point in POINTS_ARRAY:
            CLASSIFIED_1K_POINTS_ARRAY.add(Point(point.color, point.x, point.y))
            CLASSIFIED_3K_POINTS_ARRAY.add(Point(point.color, point.x, point.y))
            CLASSIFIED_7K_POINTS_ARRAY.add(Point(point.color, point.x, point.y))
            CLASSIFIED_15K_POINTS_ARRAY.add(Point(point.color, point.x, point.y))


def distance(point1, point2):
    return (point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2


def calculate_distance_to_all_points(point, array_of_points):
    distances = [(distance(point, p), p) for p in array_of_points]
    return distances


def nearest_k_points(point, k, array_of_points):
    distances = calculate_distance_to_all_points(point, array_of_points)
    nearest_points = heapq.nsmallest(k, distances, key=lambda x: x[0])
    return nearest_points


def classify_point(point, k, array_of_points, color):
    nearest_points = nearest_k_points(point, k, array_of_points)
    red_points = 0
    green_points = 0
    blue_points = 0
    violet_points = 0

    for p in nearest_points:
        if p[1].color == "red":
            red_points += 1
        elif p[1].color == "green":
            green_points += 1
        elif p[1].color == "blue":
            blue_points += 1
        elif p[1].color == "violet":
            violet_points += 1

    all_colors = [[red_points, "red"], [green_points, "green"], [blue_points, "blue"], [violet_points, "violet"]]
    all_colors.sort(key=lambda x: x[0])

    # CLASSIFIED_POINTS_ARRAY.append(Point(all_colors[-1][1], point.x, point.y))
    # return all_colors[-1][1]
    if all_colors[-1][1] == color:
        if k == 1:
            CLASSIFIED_CORRECTLY[0] += 1
        elif k == 3:
            CLASSIFIED_CORRECTLY[1] += 1
        elif k == 7:
            CLASSIFIED_CORRECTLY[2] += 1
        elif k == 15:
            CLASSIFIED_CORRECTLY[3] += 1
    else:
        if k == 1:
            CLASSIFIED_INCORRECTLY[0] += 1
        elif k == 3:
            CLASSIFIED_INCORRECTLY[1] += 1
        elif k == 7:
            CLASSIFIED_INCORRECTLY[2] += 1
        elif k == 15:
            CLASSIFIED_INCORRECTLY[3] += 1
    return Point(all_colors[-1][1], point.x, point.y)


def generate_test_environment():
    bar = Bar('Generating points and classify them', max=40000)

    last_color = ""
    for i in range(0, 40000):

        new_point_color = ALL_COLORS[random.randint(0, 3)]
        while new_point_color == last_color:
            new_point_color = ALL_COLORS[random.randint(0, 3)]
        new_coords = False

        if random.randint(1, 100) != 1:
            x, y = generate_x_and_y(new_point_color)
            # check if point with same coordinates already exists, repeat until new coordinates are found
            while not new_coords:
                if (x, y) in POINTS_ARRAY:
                    x, y = generate_x_and_y(new_point_color)
                    break
                new_coords = True
        else:
            # generate random coordinates
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
            # check if point with same coordinates already exists, repeat until new coordinates are found
            while not new_coords:
                if (x, y) in POINTS_ARRAY:
                    x = random.randint(-5000, 5000)
                    y = random.randint(-5000, 5000)
                    break
                new_coords = True

        POINTS_ARRAY.add((x, y))
        CLASSIFIED_1K_POINTS_ARRAY.add(classify_point(Point(new_point_color, x, y), 1, CLASSIFIED_1K_POINTS_ARRAY, new_point_color))
        CLASSIFIED_3K_POINTS_ARRAY.add(classify_point(Point(new_point_color, x, y), 3, CLASSIFIED_3K_POINTS_ARRAY, new_point_color))
        CLASSIFIED_7K_POINTS_ARRAY.add(classify_point(Point(new_point_color, x, y), 7, CLASSIFIED_7K_POINTS_ARRAY, new_point_color))
        CLASSIFIED_15K_POINTS_ARRAY.add(classify_point(Point(new_point_color, x, y), 15, CLASSIFIED_15K_POINTS_ARRAY, new_point_color))

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


def batch_plot(ax, points):
    x_values = [point.x for point in points]
    y_values = [point.y for point in points]
    ax.scatter(x_values, y_values, marker='.', color=[point.color for point in points])


def plot_multiple_graphs(points_lists, start_time):

    fig, ax = plt.subplots(2, 2)

    batch_plot(ax[0, 0], points_lists[0])
    batch_plot(ax[0, 1], points_lists[1])
    batch_plot(ax[1, 0], points_lists[2])
    batch_plot(ax[1, 1], points_lists[3])

    ax[0, 0].set_xlabel('X')
    ax[0, 0].set_ylabel('Y')
    ax[0, 0].set_title('k-nn = 1 | success: ' + str(int(CLASSIFIED_CORRECTLY[0] / (CLASSIFIED_CORRECTLY[2] + CLASSIFIED_INCORRECTLY[0]) * 100)) + '%')
    ax[0,0].margins(0)

    ax[0, 1].set_xlabel('X')
    ax[0, 1].set_ylabel('Y')
    ax[0, 1].set_title('k-nn = 3 | success: ' + str(int(CLASSIFIED_CORRECTLY[1] / (CLASSIFIED_CORRECTLY[2] + CLASSIFIED_INCORRECTLY[1]) * 100)) + '%')
    ax[0, 1].margins(0)

    ax[1, 0].set_xlabel('X')
    ax[1, 0].set_ylabel('Y')
    ax[1, 0].set_title('k-nn = 7 | success: ' + str(int(CLASSIFIED_CORRECTLY[2] / (CLASSIFIED_CORRECTLY[2] + CLASSIFIED_INCORRECTLY[2]) * 100)) + '%')
    ax[1, 0].margins(0)

    ax[1, 1].set_xlabel('X')
    ax[1, 1].set_ylabel('Y')
    ax[1, 1].set_title('k-nn = 15 | success: ' + str(int(CLASSIFIED_CORRECTLY[3] / (CLASSIFIED_CORRECTLY[2] + CLASSIFIED_INCORRECTLY[3]) * 100)) + '%')
    ax[1, 1].margins(0)

    for a in ax.flat:
        a.label_outer()

    fig.suptitle('Classification of 40k points')
    end_time = time.time()
    print("Time elapsed: " + str(int(end_time - start_time)) + " seconds")

    plt.show()


def main():
    start_time = time.time()
    initial_point_generation()
    generate_test_environment()

    plot_multiple_graphs([CLASSIFIED_1K_POINTS_ARRAY, CLASSIFIED_3K_POINTS_ARRAY, CLASSIFIED_7K_POINTS_ARRAY, CLASSIFIED_15K_POINTS_ARRAY], start_time)



if __name__ == '__main__':
    main()
