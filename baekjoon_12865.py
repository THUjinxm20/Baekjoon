#knapsack algorithm


N, K = map(int, input().split())
knapsack = [[0] * (K+1) for i in range(N+1)]

for i in range(1, N+1):  # 행
    weight, value = map(int,input().split())
    for j in range(1, K+1): #열
        if weight > j:
            knapsack[i][j] = knapsack[i-1][j] # 전 행의 값 그대로
        else:
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][j-weight]+value)


print(knapsack[N][K])








