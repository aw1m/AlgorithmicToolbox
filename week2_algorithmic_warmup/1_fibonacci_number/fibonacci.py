# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    fib = [0, 1]
    for i in range(n - 1):
        fib.append(fib[-2] + fib[-1])
        fib.remove(fib[0])
    return fib[-1]

n = int(input())
print(calc_fib(n))
