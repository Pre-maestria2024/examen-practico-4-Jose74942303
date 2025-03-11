
import sys

def min_damage(m, n, H, D):
    sum_h = sum(H)
    sum_d = sum(D)
    
    if sum_h < n:
        return 0
    
    INF = float('inf')
    max_sum = sum_h
    dp = [INF] * (max_sum + 1)
    dp[0] = 0
    
    for hi, di in zip(H, D):
        for w in range(max_sum, -1, -1):
            if dp[w] != INF:
                new_w = min(max_sum, w + hi)
                dp[new_w] = min(dp[new_w], dp[w] + di)
    
    minimal = min(dp[w] for w in range(n, max_sum + 1))
    return sum_d - minimal

def main():
    m, n = map(int, input().split())
    H = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    print(min_damage(m, n, H, D))
    
if __name__ == '__main__':
    main()
