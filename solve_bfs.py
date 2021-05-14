'''IS 427 UMBC Spring 2021 Individual Project 1 
   Emily Wang 
   This file implements the BFS algorithm for the test cases 
   '''
import copy
import time
from queue import Queue

HEIGHT_QUAD = 3 # Defines height of quadrant (2 for 6x6, 3 for 9x9)

class Sudoku_Problem(object):

    def __init__(self, initial):
        self.initial = initial
        self.type = len(initial) # Defines board type
        self.height = int(self.type/HEIGHT_QUAD) 

    # Return set of valid numbers from values that do not appear in used
    def filter_values(self, values, used):
        return [number for number in values if number not in used]

    # Return first empty spot on grid (marked with 0)
    def get_spot(self, board, state):
        for row in range(board):
            for column in range(board):
                if state[row][column] == 0:
                    return row, column   

    def actions(self, state):
        number_set = range(1, self.type+1) # Defines set of valid numbers that can be placed on board
        in_column = [] # List of valid values in spot's column
        in_block = [] # List of valid values in spot's quadrant

        row,column = self.get_spot(self.type, state) # Get first empty spot on board

        # Filter valid values based on row
        in_row = [number for number in state[row] if (number != 0)]
        options = self.filter_values(number_set, in_row)
        
        # Filter valid values based on column
        for column_index in range(self.type):
            if state[column_index][column] != 0:
                in_column.append(state[column_index][column])
        options = self.filter_values(options, in_column)

        # Filter with valid values based on quadrant
        row_start = int(row/self.height)*self.height
        column_start = int(column/3)*3
        
        for block_row in range(0, self.height):
            for block_column in range(0,3):
                in_block.append(state[row_start + block_row][column_start + block_column])
        options = self.filter_values(options, in_block)
      
        for number in options:
            yield number, row, column      

    # Returns updated board after adding new valid value
    def result(self, state, action):

        play = action[0]
        row = action[1]
        column = action[2]

        # Add new valid value to board
        new_state = copy.deepcopy(state)
        new_state[row][column] = play

        return new_state

    # Use sums of each row, column and quadrant to determine validity of board state
    def goal_test(self, state):

        # Expected sum of each row, column or quadrant.
        total = sum(range(1, self.type+1))

        # Check rows and columns and return false if total is invalid
        for row in range(self.type):
            if (len(state[row]) != self.type) or (sum(state[row]) != total):
                return False

            column_total = 0
            for column in range(self.type):
                column_total += state[column][row]

            if (column_total != total):
                return False

        # Check quadrants and return false if total is invalid
        for column in range(0,self.type,3):
            for row in range(0,self.type,self.height):

                block_total = 0
                for block_row in range(0,self.height):
                    for block_column in range(0,3):
                        block_total += state[row + block_row][column + block_column]

                if (block_total != total):
                    return False

        return True

class Node:

    def __init__(self, state, action=None):
        self.state = state
        self.action = action
        

    # Use each action to create a new board state
    def expand(self, problem):
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    # Return node with new board state
    def child_node(self, problem, action):
        next = problem.result(self.state, action)
        return Node(next, action)


##The function for the BFS algorithm 
def BFS(problem):

    #variables 
    initial_node = Node(problem.initial) #create initial node 
    frontier = Queue() #add nodes to the end of the frontier in a queue- BFS usues queue- FIFO
    frontier.put(initial_node)
    
    #check the original node and return it if valid 
    if problem.goal_test(initial_node.state):
        return initial_node 
    
    #search through each node until a solution is found 
    while(frontier.qsize() != 0):
        initial_node = frontier.get() 
        #for each node in the puzzle return the solution based on the neighboring node
        for child in initial_node.expand(problem):
            if problem.goal_test(child.state):
                return child 
            frontier.put(child)

    return None 

##Display the results for BFS 
def SOLVE_SUDOKU_USING_BFS(board):
    #TO DO
    print ("\nSolving Puzzle With BFS: ")

    #variables 
    start_time = time.time()
    end_time = time.time() - start_time
    problem = Sudoku_Problem(board)
    answer = BFS(problem)

    #print out the correct answer if the solution is found 
    if answer: 
      print("Solution Found")
      for row in answer.state: 
        print(row)
    else: 
      print ('no possible solutions')
    print('Elapsed time: ' + str(end_time))