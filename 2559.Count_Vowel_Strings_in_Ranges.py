# You are given a 0-indexed array of strings words and a 2D array of integers queries.

# Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

# Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

# Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        vow = {'a', 'e', 'i', 'o', 'u'}
        word_length = len(words)
        
        # A Boolean array for each word whether if the conditions are satisfied or not (starting from index 1)
        check_vow = [0]

        # O(n)
        for word in words:
            if word[0] in vow and word[-1] in vow:
                check_vow.append(1)
            
            else:
                check_vow.append(0)

        # [0, 1, 0, 1, 1, 1]: Boolean Array
        # [0, 1, 1, 2, 3, 4]: Prefix Sum
        
        # Prefix sum, where the check_vow[i] will be the number of valid strings from 0 to i 
        # O(n)
        for i in range (1, len(check_vow)):
            check_vow[i] += check_vow[i-1]
        
        # O(m)
        for query in queries:
            l = query[0]
            r = query[1]
            s = check_vow[r+1] - check_vow[l] # Number of valid strings between l and r
            ans.append(s)

        return ans


# O(n+m)
# 71% (20ms)
