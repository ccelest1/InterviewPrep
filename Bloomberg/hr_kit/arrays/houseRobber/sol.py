def rob_top_down(self, nums: list[int]) -> int:
    # store values for later lookups
    max_accum = {}

    # recursive helper
    def solve(max_accum, nums, i):
        if i == 0:
            return nums[0]
        if i == 1:
            return max(nums[0], nums[1])
        if i in max_accum:
            return max_accum[i]
        take = solve(max_accum, nums, i - 2) + nums[i]
        notTake = solve(max_accum, nums, i - 1)
        max_accum[i] = max(take, notTake)
        return max_accum[i]

    ans = solve(max_accum, nums, len(nums) - 1)
    return ans


def rob_bottom_up(self, nums: list[int]) -> int:
    # edge case of empty array case
    if len(nums) == 0:
        return 0

    # base cases
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])
        # dynamic programming cases
        # build up the table with the max_accum value at each position
    max_accum = [0] * len(nums)
    max_accum[0] = nums[0]
    max_accum[1] = max(nums[1], nums[0])

    for i in range(2, len(nums)):
        max_accum[i] = max(max_accum[i - 2] + nums[i], max_accum[i - 1])

    return max_accum[-1]
