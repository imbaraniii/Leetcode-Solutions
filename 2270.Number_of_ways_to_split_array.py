# You are given a 0-indexed integer array nums of length n.

# nums contains a valid split at index i if the following are true:

#     The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
#     There is at least one element to the right of i. That is, 0 <= i < n - 1.

# Return the number of valid splits in nums.


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        valid_splits = 0
        # Array initialisation for finding the prefix sum of nums
        # O(n)
        pref_sum = [nums[0]] * len(nums)
        #O(n)
        for i in range (1, len(nums)):
            pref_sum[i] = pref_sum[i-1] + nums[i]
        
        # O(n)
        for i in range (len(nums)-1):
            l_sum = pref_sum[i] # First i+1 elements sum
            r_sum = pref_sum[-1] - pref_sum[i] # i+1 till the end elements sum

            # Valid split condition
            if l_sum >= r_sum:
                valid_splits += 1


        return valid_splits



# O(n)

