# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    x = [(values[i]/weights[i], values[i], weights[i]) for i in range(n)]
    x.sort(reverse = True)
    for vw, v, w in x:
        if w <= capacity:
            value += v
            capacity = capacity - w
        else:
            value += vw*capacity
            capacity = 0
            break



    return value


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
