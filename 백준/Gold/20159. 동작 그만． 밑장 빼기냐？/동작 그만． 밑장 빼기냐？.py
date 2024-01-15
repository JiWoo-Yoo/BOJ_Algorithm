# 삽질: 밑장빼기 최대 1번
# 참고: https://dalseoin.tistory.com/entry/%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC-20159-%EB%8F%99%EC%9E%91-%EA%B7%B8%EB%A7%8C-%EB%B0%91%EC%9E%A5-%EB%B9%BC%EA%B8%B0%EB%83%90
n = int(input())
cards = list(map(int, input().split()))
jh_o_sum = 0

for i in range(0, len(cards), 2):
    jh_o_sum += cards[i]
    
ans = jh_o_sum
jh_sum = jh_o_sum
# 정훈이 차례 밑장빼기
for i in range(n-1, 0, -2):
    jh_sum += cards[i]
    jh_sum -= cards[i - 1]
    ans = max(ans, jh_sum)
    
jh_sum = jh_o_sum
# 상대 차례 밑장빼기
for i in range(n-2, 1, -2):
    jh_sum -= cards[i]
    jh_sum += cards[i - 1]
    ans = max(ans, jh_sum)

print(ans)
