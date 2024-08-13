# k는 k-1, k+1과 겹친다.
# 최대한 많은 수의 회의를 참여하는 것이 좋으므로 순서대로 확인
import sys
input = sys.stdin.readline

n = int(input())
meeting = []
for i in range(n):
    meeting.append(list(map(int, input().split())))

# 시작 시간으로 정렬
meeting.sort()

dp = [0 for _ in range(n)]
dp[0] = meeting[0][2]

for i in range(1, n): 
    # 이전 회의 선택했을 경우 vs 이전이전 회의+현재회의 선택했을 경우
    dp[i] = max(dp[i-1], dp[i-2] + meeting[i][2])
print(dp[n-1])