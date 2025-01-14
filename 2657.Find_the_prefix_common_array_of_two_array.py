# You are given two 0-indexed integer permutations A and B of length n.

# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.

# Return the prefix common array of A and B.

# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        out = []
        count = 0 # Counts the number of similar occurences
        a = set() 
        b = set()
        # O(n)
        for i in range (len(A)):
            # add the each number from A and B to set a and b
            a.add(A[i])
            b.add(B[i])
            # If ith value is present in both A and B increase the count
            if A[i] == B[i]:
                count += 1

            # If not
            else:
                # Check if ith value is present in set b
                if A[i] in b:
                    count += 1
                # Check if ith value is present in set a    
                if B[i] in a:
                    count += 1
    
            out.append(count)           
    
        return out
# O(n)

    # Second Way
        # n = len(A)
        # out = []
        # for i in range (n):
        #     freq = Counter(A[ :i+1] + B[ :i+1])
        #     count = 0
        #     for key in freq:
        #         if freq[key] == 2:
        #             count += 1
            
        #     out.append(count)

        # return out

# O(n^2)
