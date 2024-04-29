def solution(nums):
    answer = 0
    no_jb = set(nums)
    mons = {}
    for n in no_jb:
        mons[n] = 0
    for n in nums:
        mons[n] += 1
    if len(mons) > len(nums) // 2:
        answer = len(nums) // 2
    else:
        answer = len(mons)
        
    return answer