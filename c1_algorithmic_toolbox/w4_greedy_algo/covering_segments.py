# Uses python3
import sys
from collections import namedtuple


Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    points = []
    # sorting the segments according to their end points
    sorted_segments = sorted(
        segments,
        key=lambda s: s.end,
    )
    # print(sorted_segments)
    points.append(sorted_segments[0].end)
    for s in sorted_segments:
        if s.start <= points[-1]:
            continue
        else:
            points.append(s.end)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]),
                    zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')

    # Debug
    # with open('input.txt') as f:
    #     input = f.read()
    #     n, *data = map(int, input.split())
    #     segments = list(map(lambda x: Segment(x[0], x[1]),
    #                     zip(data[::2], data[1::2])))
    # points = optimal_points(segments)
    # print(points)
