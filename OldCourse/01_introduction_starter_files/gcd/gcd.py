# Uses python3
def gcd(a, b):
    while b:
        #print(a, b)
        r = b
        b =  a % b
        a = r
    return a

if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
