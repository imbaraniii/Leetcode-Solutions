# You are given a 0-indexed string array words.

# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:

#     isPrefixAndSuffix(str1, str2) returns true if str1 is both a
#     prefix
#     and a
#     suffix
#     of str2, and false otherwise.

# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.

# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        # Define the function to check the condition for the prefix and suffix
        # O(1)
        def isPrefixAndSuffix(str1, str2):
            n = len(str1)
            # Check if the first n strings and the last n string match with str1
            if str1 == str2[ :n] and str1 == str2[-(n): ]:
                return True

            return False

        ans = 0
        # O(n^2)
        for i, str1 in enumerate(words):
            for j, str2 in enumerate(words):
                # Satisfy the condition given (i < j)
                if i < j:
                    ans += 1 if isPrefixAndSuffix(str1, str2) else 0

        return ans



# O(n^2)
