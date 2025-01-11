# Given a string s and an integer k, return true if you can use all the characters in s to construct k palindrome strings or false otherwise.

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        # if no of char in s is less than k, then we cannot create k pal strings
        if n < k:
            return False
        # if no of char == k, then each pal string will have one character
        if n == k:
            return True

        # take frequency of the characters in string
        # annabelle: {a:2, b:1, e:2, l:2}
        freq = Counter(s)

        # to count number of characters which has odd frequency
        odd_count = 0
        # O(n)
        for key in freq:
            if freq[key] % 2 != 0:
                odd_count += 1

        # if odd count is greater than k, then its not possible to create k pal strings with all the char in s
        if odd_count > k:
            return False

        # if less than or equal to k
        return True

        
# O(n): n, number of distinct strings in s
