# You are given a 0-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all the integers in the range [1, m * n].

# Go through each index i in arr starting from index 0 and paint the cell in mat containing the integer arr[i].

# Return the smallest index i at which either a row or a column will be completely painted in mat.


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        freq = {} # Take note of the indexes of each value
        r = len(mat) # Row Length
        c = len(mat[0]) # Col length
        
        # Take note of the indexes
        # O(m*n)
        for i in range (len(mat)):
            for j in range (len(mat[i])):
                freq[mat[i][j]] = (i,j)

        row_count = [0] * r
        col_count = [0] * c
    
        # O(n)
        for idx, val in enumerate(arr):
            # if the val in arr is also present in the mat, we increase that ith and jth col's freq by 1
            if val in freq:
                i, j = freq[val]
                row_count[i] += 1
                col_count[j] += 1
                
                # If the freq of row or freq or col gets equal to m or n, then we return the current index of arr
                if row_count[i] == c or col_count[j] == r:
                    return idx
        
        # if no such possibilities
        return -1


# O(m*n)
