# 0과 1이 각각 몇 번 출력되는지 구하는 프로그램
# 피보나치를 직접 구하는게 아님.
# 0은 0:1번출력, 1:0번출력
# 1은 0:0번출력, 1:1번출력 
# 2는 0의 0,1출력수 + 1의 0,1출력수 -> 0:1번출력, 1:1번출력
# 3은 1의 0,1출력수 + 2의 0,1출력수 -> 0:1번출력, 1:2번출력 

# 즉, dp[i][0] = dp[i-1][0] + dp[i-2][0],
#     dp[i][1] = dp[i-1][1] + dp[i-2][1]

t = int(input())

dp = [[0, 0] for _ in range(40 + 1)]

dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]
    dp[i][1] = dp[i-1][1] + dp[i-2][1]

for _ in range(t):
    n = int(input())
    print(dp[n][0], dp[n][1])
    
    
