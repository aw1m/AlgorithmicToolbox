# Uses python3
import sys

def lcm(a, b):
    x = a
    y = b
    z = 0

    while (True):
        if y == 0:
            gcd =  x
        else:
            z = x % y
            x = y
            y = z

    return (a*b)//gcd

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

