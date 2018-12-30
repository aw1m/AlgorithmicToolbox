# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    fib = [0, 1]
    for i in range(n - 1):
        fib.append((fib[-2] + fib[-1]) % 10)
        fib.remove(fib[0])
    return fib[-1]

if __name__ == '__main__':
    n = int(input())
    print(get_fibonacci_last_digit_naive(n))
