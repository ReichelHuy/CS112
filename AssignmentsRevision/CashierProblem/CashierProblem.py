
def min_ignore_none(a,b):
    if a is None:
        return b
    if b is None:
        return a
    return min(a,b)

def minimum_coins(m, coins):
    memo = {}
    memo[0]= 0
    for i in range(1,m+1):
        memo[i] = float('inf')
        for coin in coins:
            subproblem = i-coin 
            if subproblem <0:
                continue
            memo[i]= min_ignore_none(memo.get(i), (memo.get(subproblem) + 1))
    if memo[m] == float('inf'):
        return "-1"
    return memo[m]

K = int(input()) 
coins = list(map(int, input().split()))
Target = int(input())
print(minimum_coins(Target,coins))