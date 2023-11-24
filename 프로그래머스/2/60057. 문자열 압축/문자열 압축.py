def solution(s):
    answer = len(s)
    # 압축 단위를 1에서부터 len(s) // 2 까지 늘려가며 검사.
    half_len = len(s) // 2
    for step in range(1, half_len + 1):
        compressed = ""
        count = 1
        prev = s[0:step]
        for i in range(step, len(s), step):
            if prev == s[i:i+step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[i:i+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer