import copy
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        length = len(matrix)
        l = [i for i in range(len(matrix))]
        l.reverse()
        x = copy.deepcopy(matrix)
        
        for i in range(length):
            for j in range(length):
                matrix[i][j] = x[l[j]][i]
                
        
        