# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

# Question Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

# Intution
# 1. As mentioned in the question that we can return the final intersection at any order which means not only adjacent elements are allowed as intersection but any value that is repeating in both the arrays and return it any order.
# 2. So, we can use a hashmap to store the count of each element in nums1 and nums2, Say temp1 and temp2 respectively.
# 3. Then, we can iterate over any of that hashmap/dictionary and check if that number present in temp1 also presents in temp2. If True, create another "count" variable and store the min count of that number from temp1 and temp2 (because the min count of that number from temp1 and temp2 will tell us the total number of times that number is repeating in both the nums1 and nums2 array.)
# 4. Then, we append that number repeating "count" no of times in the result say "intersection".
# 5. We check this for all the elements in temp1. After the loop ends, We return the final result that is the "intersection" which contains all the numbers that are available both in the nums1 and nums2 and repeating as many as times in both the arrays.



# Code
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = []

        temp1 = Counter(nums1)
        temp2 = Counter(nums2)

        for num in temp1:
            if num in temp2:
                count = min(temp1[num], temp2[num])
                intersection.extend([num] * count)

        return intersection
    



# 94.85%