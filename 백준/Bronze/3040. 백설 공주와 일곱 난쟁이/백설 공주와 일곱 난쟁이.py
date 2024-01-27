nums = []
for _ in range(9):
    nums.append(int(input()))
total = sum(nums)
go_out = False

for l in range(len(nums)-1):
    for r in range(l+1, len(nums)):
        if total - (nums[l] + nums[r]) == 100:
            nums[l] = 0
            nums[r] = 0
            go_out = True
            break
    if go_out == True:
        break

for num in nums:
    if num == 0:
        continue
    else:
        print(num)
