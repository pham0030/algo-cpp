# Uses python3
import sys
import random
import time


def fast_count_segments(starts, ends, points):
    cnt = {}
    num_segments = 0
    list_points = [(i, 'left') for i in starts]
    list_points += [(i, 'point') for i in points]
    list_points += [(i, 'right') for i in ends]
    list_points.sort()
    for point, kind in list_points:
        if kind == 'left':
            num_segments += 1
        elif kind == 'right':
            num_segments -= 1
        else:
            cnt[point] = num_segments
    return [cnt[p] for p in points]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input_ = sys.stdin.read()
    data = list(map(int, input_.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    # use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')

    # Simple debug
    # with open('input.txt') as f:
    #     input_ = f.read()
    #     data = list(map(int, input_.split()))
    #     n = data[0]
    #     m = data[1]
    #     starts = data[2:2 * n + 2:2]
    #     ends = data[3:2 * n + 2:2]
    #     points = data[2 * n + 2:]
    #     # use fast_count_segments
    #     cnt = fast_count_segments(starts, ends, points)
    #     for x in cnt:
    #         print(x, end=' ')

    # Stress test
    # i = 1
    # random.seed(2)
    # while(i <= 10000):
    #     print('Test :{}'.format(i))
    #     i += 1
    #     v = 1e2
    #     n = 1e1
    #     s = random.randint(1, n)
    #     p = random.randint(1, n)
    #     starts = [random.randint(-v//2, v//2) for _ in range(s)]
    #     ends = [starts[i] + random.randint(0, v//2) for i in range(s)]
    #     points = [random.randint(-v, v) for _ in range(p)]
    #     t0 = time.time()
    #     fast = fast_count_segments(starts, ends, points)
    #     t0 = time.time() - t0
    #     print('fast running time: {}'.format(t0))
    #     t1 = time.time()
    #     naive = naive_count_segments(starts, ends, points)
    #     t1 = time.time() - t1
    #     print('naive running time: {}'.format(t1))
    #     print('improvement: {}'.format(t1/t0))
    #     if fast != naive:
    #         print('Wrong')
    #         seg = [(starts[i], ends[i]) for i in range(len(starts))]
    #         sorted_segments = sorted(
    #             seg,
    #             key=lambda s: s[0],
    #         )
    #         for j in range(len(fast)):
    #             if fast[j] != naive[j]:
    #                 print('j:{}'.format(j))
    #                 print(fast[j])
    #                 print(naive[j])
    #             break
    #     else:
    #         print('Ok')
