# You are given a string s.

# You can perform the following process on s any number of times:

#     Choose an index i in the string such that there is at least one character to the left of index i that is equal to s[i], and at least one character to the right that is also equal to s[i].
#     Delete the closest character to the left of index i that is equal to s[i].
#     Delete the closest character to the right of index i that is equal to s[i].

# Return the minimum length of the final string s that you can achieve.


from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s) # Finding the freq of each character in s
        min_len = len(s) # Min length will be the actual length of s
        
        # O(n): n, number of distinct characters in s
        for key in freq:
            # skip the characters which have freq less than 3
            if freq[key] < 3:
                continue
            else:
                f = (freq[key] - 3) // 2 + 1 # number of times the min_len should be decremented by 2 such that it gets less than 3
                min_len -= (2 * f)
                freq[key] -= (2 * f)


        return min_len

# O(n)
        
        


