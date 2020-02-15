import numpy as np


def points():
    point_list = []
    val = -1 * np.sqrt(2)
    while val < np.sqrt(2):
        point_list.append([val, lower(val)])
        val += 0.0005
    return point_list


def lower(x):
    output = -1 * np.sqrt(2-(x*x)) + np.sqrt(abs(x))
    if np.isnan(output):
        return 0
    else:
        return output


def distance(point1, point2):
    diff = np.subtract(point1, point2)
    square_diff = np.square(diff)
    return np.sqrt(square_diff[0] + square_diff[1])


# 10328th position is the correct one
def circle_radius():
    centers = np.arange(-1 * np.sqrt(2), np.sqrt(2), 0.0001)
    centers = centers[::-1]
    heart_points = points()

    for ind, val in enumerate(centers):
        radius = distance([0, np.sqrt(2)], [0, val])
        print("Radius#: " + str(ind))
        for point in heart_points:
            if distance(point, [0, val]) < radius:
                return [0, centers[ind-1]]


rad = distance(circle_radius(), [0, np.sqrt(2)])
print(np.pi * rad**2)
