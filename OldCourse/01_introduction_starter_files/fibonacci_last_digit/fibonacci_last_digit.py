# Uses python3
import math

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n
    else:
        fib=[0,1]
        half_list = 0
        while fib[:half_list]!=fib[half_list:]:
            x=(fib[-1]+fib[-2])% 10
            fib.append(x)
            half_list = math.floor(len(fib)/2)
    cycle_index = n % half_list
    return fib[cycle_index]


if __name__ == '__main__':
    n = int(input())
    #m = int(input())
    print(get_fibonacci_last_digit_naive(n))
