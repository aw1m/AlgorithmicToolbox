# Uses python3
import sys

def lcm(a, b):
    temp_a, temp_b = a,b
    while b:
        r = b
        b =  a % b
        a = r
        #print(a, b)
    #return (a, b, temp_a,  temp_b, (temp_a)*(temp_b/a) )
    return ((temp_a)*(temp_b//a))
if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
