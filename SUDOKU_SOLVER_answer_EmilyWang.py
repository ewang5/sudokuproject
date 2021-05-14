'''IS 427 UMBC Spring 2021 Individual Project 1
   Emily Wang 
   This file contains the test cases for the program
   There are 2 test cases- 6x6 and 9x9 board 
   The program gets the algorithms from other files and prints out the output using bfs and dfs searches sudok
'''
#import bfs and dfs algorithms 
from solve_bfs import SOLVE_SUDOKU_USING_BFS 
from solve_dfs import SOLVE_SUDOKU_USING_DFS 

print('\n\n6x6 board')    
    ## TEST CASES 
    # 6x6 board
board_6x6 = [[0,0,0,0,4,0],
          [5,6,0,0,0,0],
          [3,0,2,6,5,4],
          [0,4,0,2,0,3],
          [4,0,0,0,6,5],
          [1,5,6,0,0,0]]

print ('Problem:')
for row in board_6x6: 
  print(row)

SOLVE_SUDOKU_USING_BFS (board_6x6)
SOLVE_SUDOKU_USING_DFS (board_6x6)

print ('\n\nTesting on 9x9 board')
    # 9x9 board
board_9x9 = [[3,0,6,5,0,8,4,0,0], 
          [5,2,0,0,0,0,0,0,0], 
          [0,8,7,0,0,0,0,3,1], 
          [0,0,3,0,1,0,0,8,0], 
          [9,0,0,8,6,3,0,0,5], 
          [0,5,0,0,9,0,6,0,0], 
          [1,3,0,0,0,0,2,5,0], 
          [0,0,0,0,0,0,0,7,4], 
          [0,0,5,2,0,6,3,0,0]]
print ('Problem:')
for row in board_9x9:
  print (row)
   
SOLVE_SUDOKU_USING_BFS(board_9x9)
SOLVE_SUDOKU_USING_DFS(board_9x9)