# Uses python3

def get_change(m):
    coins = [10,5,1]
    total = 0
    for x in coins:
        if m//x>0:
            count = m//x
            m = m - count*x
            total +=count
    return total

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
