# ATM 앞에 N명 한줄서기(1~N)
# i번사람의 돈 인출 시간 Pi분
# 돈 인출 필요시간의 합의 최솟값

n = int(input())
p = list(map(int, input().split()))

# 가장 시간이 적게 걸리는 녀석을 앞에 놔야 함
p.sort()

# 누적하기
for i in range(1, n):
    p[i] += p[i-1]
    
print(sum(p))
