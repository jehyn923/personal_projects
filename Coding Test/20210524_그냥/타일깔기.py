def tiling(n):
    memo = [-1 for i in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    memo[2] = 3 
    memo[3] = 6

    for i in range(4, n+1):
        memo[i] = memo[i-1] + memo[i-2]*2 + memo[i-3]

    return memo[n]


print(tiling(5))
print(tiling(8))
print(tiling(10))