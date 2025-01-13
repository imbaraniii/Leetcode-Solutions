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

        b = True # Loop-breaking Variable
        while b:
            temp = 0 # Counts the number of characters which have freq less than 3
            # O(n): n, number of distinct char in s
            for key in freq:
                if freq[key] < 3:
                    temp += 1
                    if temp == len(freq): # if the count == len(freq) then we can break the while loop
                        b = False
                        break

                else:
                    # decrement the min_len and freq[key] by 2 (one for left and one for right)
                    min_len -= 2
                    freq[key] -= 2


        return min_len

# O(n)
        


