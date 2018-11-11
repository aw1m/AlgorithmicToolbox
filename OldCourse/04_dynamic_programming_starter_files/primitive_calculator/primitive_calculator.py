# Uses python3
import sys

def optimal_sequence(n):
    v = [0 for i in range(n+1)]
    v[0]=1
    #forward
    for i in range(1,n+1):
        v[i] = v[i-1]+1
        if i%2==0 and v[i//2] < v[i]:
            v[i] = v[i//2]+1
        if i%3==0 and v[i//3] < v[i]:
            v[i] = v[i//3] +1
    #back
    results = []
    while n>1:
        #print(n)
        results.append(n)
        if v[n-1] ==v[n]-1:
            n = n-1
        elif n%2 == 0 and v[n//2]==v[n]-1:
            n = n//2
        elif n%3== 0 and v[n//3]==v[n]-1:
            n = n//3

        print(results)

    results.append(1)
    return sorted(results)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
