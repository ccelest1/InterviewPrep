# [DP Solution](https://levelup.gitconnected.com/solving-the-house-robber-leetcode-problem-1d34df04ea20)

## Dynamic Programming Problem
- Structured way to solve dynamic programming problems: `IDEAL`
    * I: Id dynamic programming problem
    * D: Define state w/ few parameters
    * E: Express recurrence relation, base cases
    * A: Adopt implementation approach - top down v bottom up
    * L: Look @ time, space complexity

## Id Dynamic Programming Problem
- Via the house robber description, it is an optimization problem as you are finding the max amount of money one can rob -> deals w/ a sequence represented by list[int]
    * 2 properties: overlapping sub-problems, optimal substructure
        1. overlapping sub-problems
            - As one progresses along x houses row, current decision is based on prior decisions made at houses prior
                * houses are eliminated depending on starting and chosen houses
        2. optimal substructure
            - max amt robbed up to current house is built on max amounts accumulated from prior houses

## Define state w/ fewest parameters
- i = array index/house position on street
- max_accum[i] = max accumulated amt robbed (up to and including) house i

## Express recurrence relation, base cases
- Form relation between previous states to reach current state
    * @ each house, can decide to rob house or not rob house:
        * Rob house:
            - at house i, if I decide to rob it then previous house @ pos `i-1` can't be robbed, else police will be alerted
            - if I take max_accum value for house 2 doors down @ i-2 and add to sum, being nums[i] -> `max_accum[i-2] + nums[i]`
        * Don't rob house:
            - @ house i, if I decide not to rob it then I possess max_accum val for prev house @ position `i-1` being `max_accum[i-1]`
        * thus it is the max of these 2 possible choices
            * `max_accum[i] = max(max_accum[i-2] + nums[i], max_accum[i-1])`
- Base Cases
    * @ 1st house, max amt by robbing it is `max_accum[0] = nums[0]`
    * @ 2nd house, max amt accumulated is max of robbing it or 1st house `max_accum[1] = max(nums[1], nums[0])`

## Adopt implementation approach
* __Top Down - recursive utilizing memoization__
    - start w/ original problem -> break down by taking out last house -> find max_accum values for prev house + house 2 doors away: based on recurrence relation : `max_accum[i] = max(max_accum[i-2] + nums[i], max_accum[i-1])`
        * recursively break down subproblems, take 1 house out until reached base case of house 1 and 2
        * save values for those houses for later lookups -> using solutions to subproblems, continue to build problem back up by adding 1 house cumulatively and storing max_accum value for future use
        * get back to org problem of robbing all houses and look up 2 max_accum values req to calc final answer

        ```py
        def rob(self, nums: list[int]) -> int:
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
                take = solve(max_accum, nums, i-2) + nums[i]
                notTake = solve(max_accum, nums, i-1)
                max_accum[i] = max(take, notTake)
                return max_accum[i]

            ans = solve(max_accum, nums, len(nums)-1)
            return ans
        ```

* __Bottom Up - iterative utilizing tabulation__
    ```py
    def rob(self, nums: list[int]) -> int:
        # edge case of empty array case
        if len(nums) == 0:
            return 0

        # base cases
        if len(nums)==1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        # dynamic programming cases
        # build up the table with the max_accum value at each position
        max_accum = [0] * len(nums)
        max_accum[0] = nums[0]
        max_accum[1] = max(nums[1], nums[0])

        for i in range(2, len(nums)):
            max_accum[i] = max(max_accum[i-2] + nums[i], max_accum[i-1])

        return max_accum[-1]
    ```

## Look @ TC, SC
* Top Down
    - TC of top down is O(n) as a result of using memoization to avoid recomputation of same subproblems, w/o memo it is O(2**n) as each house has 2 choices of robbing or not robbing (binary tree structure)
    - SC: O(n), dict with n entries tracking max accumulated val at each house
* Bottom Up
    - Bottom up has a O(n) tc, n being the array length with a for loop iterating through
    - sc is O(n) also, where an array of size of input array tracks max accumulated values
