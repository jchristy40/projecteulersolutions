
def twosum(nums, target):
	for x in range(len(nums)):
		targetcheck = target - nums[x]
		if targetcheck in nums and nums.index(targetcheck) != x:
			return [x,nums.index(targetcheck)]
	return

print(twosum([2,2,7,11,13], 4))
