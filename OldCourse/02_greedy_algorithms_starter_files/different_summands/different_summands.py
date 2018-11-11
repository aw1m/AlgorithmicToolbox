# Uses python3
import sys

def optimal_summands(n):
    summands = []
    
    return summands


def algorithm(value):
	n, k= value, 1
	operands = []
	while True:
		
		if ( n <= 2*k):
			operands.append(n)
			break
			
		else:
			operands.append(k)
			n = n - k
			k+= 1
	
	return k, operands
value = 8
print(algorithm(value))

##if __name__ == '__main__':
##    input = sys.stdin.read()
##    n = int(input)
##    summands = optimal_summands(n)
##    print(len(summands))
##    for x in summands:
##        print(x, end=' ')
