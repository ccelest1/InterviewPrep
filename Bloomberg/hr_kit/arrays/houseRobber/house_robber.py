class Solution:
    def rob(self, nums: list[int]) -> int:
        sums = []
        l = 0
        """
        for i in range(0,len(nums),2):
            for j in range(i+2,len(nums),2):
                new_sum = nums[i] + nums[j]
                print(new_sum)
                if(new_sum>max_sum):
                    max_sum = new_sum
        return max_sum
        """
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        while l < len(nums):
            new_sum = nums[l]
            for i in range(l + 2, len(nums), 2):
                print(nums[i])
                new_sum += nums[i]
            sums.append(new_sum)
            l += 1
        if len(nums) > 3:
            sums.append(nums[0] + nums[-1])

        return max(sums)


# worked
print(Solution.rob([2, 7, 9, 3, 1]))

print(Solution.rob([1, 2, 3, 1]))

print(Solution.rob([1, 2]))

# did not work
print(Solution.rob([2, 1, 1, 2]))
# largest solution occurs with first and last element summed

print(Solution.rob([1, 3, 1, 3, 100]))
