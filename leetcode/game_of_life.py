"""
https://leetcode.com/problems/game-of-life/
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        coordinates = (
            (0,1), (1,1), (1,0), (1,-1), (0,-1),(-1,-1),(-1,0),(-1,1)
        )
        
        ROW = len(board)
        
        COL = len(board[0])
        
        for row in range(ROW):
            for col in range(COL):
                count_of_lives = 0
                for c in coordinates:
                    r1 = row + c[0]
                    c1 = col+c[1]
                    
                    if 0 <= r1 <= ROW-1 and 0 <= c1 <= COL-1:
                        if abs(board[r1][c1]) == 1:
                            count_of_lives+=1
                
                if board[row][col] ==1 and count_of_lives < 2:
                    board[row][col] = -1
                
                elif board[row][col] ==1 and count_of_lives > 3:
                    board[row][col] = -1
                
                elif board[row][col] ==0 and count_of_lives == 3:
                    board[row][col] = 2
                    
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == -1:
                    board[row][col] = 0
                elif board[row][col] == 2:
                    board[row][col] = 1
                
                
                
        