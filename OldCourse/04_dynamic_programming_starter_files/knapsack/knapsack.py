# Uses python3
import sys

def optimal_weight(W,n,w):
    # write your code here
   
    table = [[0 for _ in range(W+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1,W+1):
            last_i = i-1
            bar_wt = w[i-1]
            r_cap =j-bar_wt
            last_j = j-1
            var = [["i", "j", "last_i", "last_j", "bar_wt", "r_cap"],[i, j, last_i, last_j, bar_wt, r_cap]]
            #[print("{}: {}".format(var[0][i], var[1][i])) for i in range(6)]            
            if bar_wt > j:
                table[i][j] = table[last_i][j]
            else:
                if table[last_i][j]>= table[last_i][r_cap] + bar_wt:
                    table[i][j] = table[last_i][j]
                else:
                        table[i][j] = table[last_i][r_cap] + bar_wt
            #print(table[i])
    return table[-1][-1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, n, w))

