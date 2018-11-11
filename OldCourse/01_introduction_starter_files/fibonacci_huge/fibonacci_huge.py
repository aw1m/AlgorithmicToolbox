# Uses python3
import sys
import math

def get_fibonacci_huge_naive(n, m):
    if n<=1:
        return n
    else:
        fib = [0,1]
        for i in range(n-1):
            fib.append((fib[-2]+fib[-1])%m)
            if fib[-2:] == [0,1]:
                del fib[-2:]
                break
    #print(fib)
    cyc = len(fib)
    if m>2:
        k = (n%cyc)
    else:
        k = 0
    #print(f"n = {n}, cyc = {cyc}, m = {m}, k = {k} , fib[k] = {fib[k]}")
    #return
    return fib[k]

# n, m =99999999999999,2
# print(get_fibonacci_huge_naive(n, m))
#
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
