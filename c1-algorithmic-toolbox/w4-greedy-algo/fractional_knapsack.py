# Uses python3
import sys
import random


def get_optimal_value_naive(capacity, weights, values):
    value = 0.
    weights = weights[:]
    values = values[:]
    ratio = [v/w for w, v in zip(weights, values)]
    A = [0.] * len(ratio)
    for iterat in range(len(ratio)):
        if capacity == 0:
            return value

        ratio_max = 0.
        for i in range(len(ratio)):
            if weights[i] > 0 and ratio[i] > ratio_max:
                ratio_max = ratio[i]
                chosen_i = i
        a = min(weights[chosen_i], capacity)
        value += a*ratio[chosen_i]
        weights[chosen_i] -= a
        A[chosen_i] += a
        capacity -= a
    return value


def get_optimal_value(capacity, weights, values):
    value = 0.
    vw = sorted(
        [(v, w) for v, w in zip(values, weights)],
        key=lambda i: i[0]/i[1],
        reverse=True
    )
    for item in vw:
        if capacity - item[1] >= 0:
            value += item[0]  # value index = 0
            capacity -= item[1]  # weight index = 1
        else:
            value += (item[0]/item[1]) * capacity
            capacity = 0
        if not capacity:
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

    # Debug
    # opt_value = get_optimal_value_naive(50, [], [])
    # print("{:.4f}".format(opt_value))
    # opt_value = get_optimal_value(50, [], [])
    # print("{:.4f}".format(opt_value))

    # Stress Test
    # random.seed(1)
    # i = 1
    # while(True):
    #     print('Test: {}'.format(i))
    #     capacity = random.randint(0, 2e6+1)
    #     weights = [random.randint(1, 2e6+1) for
    #                _ in range(random.randint(0, 1e3+1))]
    #     values = [random.randint(1, 2e6+1) for _ in range(len(weights))]

    #     naive = get_optimal_value_naive(capacity, weights, values)
    #     res = get_optimal_value(capacity, weights, values)
    #     if (naive - res >= 1e-3):
    #         print('Miss match, naive: {}, res: {}'.format(naive, res))
    #         print('capacity: {}'.format(capacity))
    #         print('weights: {}'.format(weights))
    #         print('value: {}'.format(values))
    #         break
    #     else:
    #         print('Ok!')
    #     i += 1
