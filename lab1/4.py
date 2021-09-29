values = [60, 100, 120]
wt = [10, 20, 30]
W = 50
length = len(values)


def knapSack(W, wt, val, length):
    K = [[0 for x in range(W + 1)] for x in range(length + 1)]
    for i in range(length + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(values[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
  
    return K[length][W]

print(knapSack(W, wt, values, length))