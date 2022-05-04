# Uses python3
import sys
import math
import time
import random


def dist(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def brute(points):
    num_points = len(points)
    point1 = points[0]
    if num_points == 1:
        return 0
    point2 = points[1]
    min_dis = dist(point1, point2)
    if num_points == 2:
        return min_dis
    for i in range(num_points - 1):
        for j in range(i + 1, num_points):
            d = dist(points[i], points[j])
            if d < min_dis:
                min_dis = d
    return min_dis


def minimum_distance(points):
    points_x_sorted = sorted(points, key=lambda i: i[0])  # Presorting x-wise
    points_y_sorted = sorted(points, key=lambda i: i[1])  # Presorting y-wise
    min_dis = closest_pair(points_x_sorted, points_y_sorted)
    return min_dis


def closest_pair(points_x_sorted, points_y_sorted):
    num_points_x = len(points_x_sorted)
    if num_points_x <= 3:
        return brute(points_x_sorted)
    mid = num_points_x // 2
    # Split the points_x_sorted
    Lx = points_x_sorted[:mid]
    Rx = points_x_sorted[mid:]
    mid_point_x = points_x_sorted[mid][0]

    # Split the points_y_sorted
    Lx_set = set(Lx)
    Ly = []
    Ry = []
    for point in points_y_sorted:
        if point in Lx_set:
            Ly.append(point)
        else:
            Ry.append(point)

    # Recursively call
    min_L = closest_pair(Lx, Ly)
    min_R = closest_pair(Rx, Ry)

    # Choose the small distances
    if min_L <= min_R:
        d = min_L
    else:
        d = min_R
    min_dis = d

    # Search for minimum for points on the boundary mid
    # Create a subarray of points not further than delta from midpoint
    # of x-wise sorted array from y-wise sorted array
    strip_y = [point for point in points_y_sorted if
               abs(mid_point_x - point[0]) < d]

    num_points_strip_y = len(strip_y)
    if num_points_strip_y > 1:
        for i in range(num_points_strip_y - 1):
            for j in range(i + 1, min(i + 5, num_points_strip_y)):
                point1, point2 = strip_y[i], strip_y[j]
                dst = dist(point1, point2)
                if dst < min_dis:
                    min_dis = dst
    return min_dis


def minimum_distance2(points):

    if len(points) <= 1:
        return 0
    # We use first two points as our initial guess.
    best = [dist(points[0], points[1]), (points[0], points[1])]

    # check whetherpair forms a closer pair than existing
    def testpair(point1, point2):
        dst = dist(point1, point2)
        if dst < best[0]:
            best[0] = dst
            best[1] = point1, point2

    # merge two sorted lists by y-coordinate
    def merge_y_wise(L, R):
        i = 0
        j = 0
        while i < len(L) or j < len(R):
            if j >= len(R) or (i < len(L) and L[i][1] <= R[j][1]):
                yield L[i]
                i += 1
            else:
                yield R[j]
                j += 1

    # Find closest pair recursively; returns all points sorted by y coordinate
    def closest_pair2(points):
        if len(points) < 2:
            return points
        mid = len(points) // 2
        mid_x = points[mid][0]
        # Resorting recursively y-wise the result
        points = list(merge_y_wise(closest_pair2(points[:mid]),
                                   closest_pair2(points[mid:])))

        # Search for minimum for points on the boundary mid
        # Create a subarray of points not further than the best from midpoint
        E = [p for p in points if abs(p[0] - mid_x) < best[0]]
        for i in range(len(E)):
            for j in range(1, 6):
                if i + j < len(E):
                    testpair(E[i], E[i + j])
        return points

    points.sort()
    closest_pair2(points)
    return best


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    min_dis = minimum_distance(points)
    print("{0:.9f}".format(min_dis))

    # with open('input.txt') as f:
    #     input_ = f.read()
    #     data = list(map(int, input_.split()))
    #     n = data[0]
    #     x = data[1::2]
    #     y = data[2::2]
    #     assert(n == len(x) and n == len(y))
    #     points = list(zip(x, y))
    #     point1, point2, min_dis = brute(points)
    #     print("{0:.9f}".format(min_dis))
    #     print("({}, {})".format(point1[0], point1[1]))
    #     print("({}, {})".format(point2[0], point2[1]))

    # with open('input.txt') as f:
    #     input_ = f.read()
    #     data = list(map(int, input_.split()))
    #     n = data[0]
    #     x = data[1::2]
    #     y = data[2::2]
    #     assert(n == len(x) and n == len(y))
    #     points = list(zip(x, y))
    #     point1, point2, min_dis = minimum_distance(points)
    #     print("{0:.9f}".format(min_dis))
    #     print("({}, {})".format(point1[0], point1[1]))
    #     print("({}, {})".format(point2[0], point2[1]))

    # Stress test
    # i = 1
    # random.seed(1)
    # while(i <= 100):
    #     print('-'*20)
    #     print('Test: {}'.format(i))
    #     i += 1
    #     v = 1e9
    #     # n = random.randint(1, 1e5)
    #     n = int(1e3)
    #     x = [random.randint(-v, v) for _ in range(n)]
    #     y = [random.randint(-v, v) for _ in range(n)]
    #     points = list(zip(x, y))
    #     # print(points)
    #     t1 = time.time()
    #     min_dis1 = minimum_distance(points)
    #     t1 = time.time() - t1
    #     print('Fast search running time: {}'.format(t1))
    #     t2 = time.time()
    #     min_dis2 = brute(points)
    #     t2 = time.time() - t2
    #     print('Brute search running time: {}'.format(t2))
    #     print('Improvement: {:.0f}%'.format(t2/t1*100))
    #     if min_dis1 != min_dis2:
    #         print('Wrong! Fast search: {}, Brute search: {}'.format(
    #               min_dis1, min_dis2))
    #         break
    #     else:
    #         print('Ok!')

    # Stress test2
    # i = 1
    # random.seed(1)
    # while(i <= 100):
    #     print('-'*20)
    #     print('Test: {}'.format(i))
    #     i += 1
    #     v = 1e9
    #     # n = random.randint(1, 1e5)
    #     n = int(1e5)
    #     # x = [random.randint(-v, v) for _ in range(n)]
    #     x = [v for _ in range(n)]
    #     y = [random.randint(-v, v) for _ in range(n)]
    #     # y = [2 for _ in range(n)]
    #     points = list(zip(x, y))
    #     # print(points)
    #     t1 = time.time()
    #     min_dis1 = minimum_distance(points)
    #     t1 = time.time() - t1
    #     print('Fast search running time: {}'.format(t1))
    #     t2 = time.time()
    #     min_dis2, p = minimum_distance2(points)
    #     t2 = time.time() - t2
    #     print('Faster search 2 running time: {}'.format(t2))
    #     print('Improvement: {:.0f}%'.format(t2/t1*100))
    #     if min_dis1 != min_dis2:
    #         print('Wrong! Fast search: {}, Fast search: {}'.format(
    #               min_dis1, min_dis2))
    #         break
    #     else:
    #         print('Ok!')
