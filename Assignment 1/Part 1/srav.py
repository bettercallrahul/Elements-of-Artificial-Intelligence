#!/usr/local/bin/python3
# solver2021.py : 2021 Sliding tile puzzle solver
#
# Code by: name IU ID
#
# Based on skeleton code by D. Crandall & B551 Staff, September 2021
#

from os import closerange
import sys
import numpy as np


ROWS=5
COLS=5


def move_clockwise(board):
    """Move the outer ring clockwise"""
    board[0]=[board[1][0]]+board[0]
    residual=board[0].pop()
    board=transpose_board(board)
    residual=rotate_right(board,-1,residual)
    board=transpose_board(board)
    residual=rotate_left(board,-1,residual)
    board=transpose_board(board)
    residual=rotate_left(board,0,residual)
    board=transpose_board(board)
    return board

def move_cclockwise(board):
    """Move the outer ring counter-clockwise"""
    board[0]=board[0]+[board[1][-1]]
    residual=board[0].pop(0)
    board=transpose_board(board)
    residual=rotate_right(board,0,residual)
    board=transpose_board(board)
    residual=rotate_right(board,-1,residual)
    board=transpose_board(board)
    residual=rotate_left(board,-1,residual)
    board=transpose_board(board)
    return board

def move_right(board, row):
  """Move the given row to one position right"""
  board[row] = board[row][-1:] + board[row][:-1]
  return board

def move_left(board, row):
  """Move the given row to one position left"""
  board[row] = board[row][1:] + board[row][:1]
  return board

def rotate_right(board,row,residual):
    board[row] = [board[row][0]] +[residual] + board[row][1:]
    residual=board[row].pop()
    return residual

def rotate_left(board,row,residual):
    board[row] = board[row][:-1] + [residual] + [board[row][-1]]
    residual=board[row].pop(0)
    return residual

def transpose_board(board):
  """Transpose the board --> change row to column"""
  return [list(col) for col in zip(*board)]


def printable_board(board):
    return [ ('%3d ')*COLS  % board[j:(j+COLS)] for j in range(0, ROWS*COLS, COLS) ]

# return a list of possible successor states
def successors(state):
    return True
    
# check if we've reached the goal
def is_goal(state):
    goal_state=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    if state==goal_state:
        return True

# Calculates the sshortest heuristic
def short_heu(board, x, y, endx, endy):
    irm, ilm, ium, idm, nm=0, 0, 0, 0, 0
    #print(" xyx endx endy ", x,y,endx,endy)
    
    # for adding moves till the right end
    irm=4-y+1
    ilm=y+1
    ium=x+1
    idm=4-x+1

    # manhattan from right
    mfr=irm+(abs(x-endx)+abs(0-endy))

    # manhattan from left
    mfl=ilm+(abs(x-endx)+abs(4-endy))

    # manhattan from up
    mfu=ium+(abs(4-endx)+abs(y-endy))

    # manhattan from down
    mfd=idm+(abs(0-endx)+abs(y-endy))

    # normal manhattan
    nm=(abs(x-endx)+abs(y-endy))

    #print(mfr, mfl, mfu, mfd, nm)
    min_manhattan=min(mfr, mfl, mfu, mfd, nm)
    return min_manhattan


# calculate heuristic wiht wrapping around.
def cal_heu(board1):
    board=list(board1)
    rows=5
    col=5
    count=0
    sum_manhattan=0


# checks the sum of mahattan distances for all puzzle pieces adn returns the sum/16
    for i in range(rows):
        for j in range(col):
            if board[i][j]==1:
                sum_manhattan=sum_manhattan+short_heu(board, i, j, 0, 0)
            if board[i][j]==2:
                sum_manhattan=sum_manhattan+short_heu(board, i, j, 0, 1)
            if board[i][j]==3:
                sum_manhattan=sum_manhattan+short_heu(board, i, j, 0, 2)
            if board[i][j]==4:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 0, 3))
            if board[i][j]==5:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 0, 4))
            if board[i][j]==6:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 1, 0))
            if board[i][j]==7:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 1, 1))
            if board[i][j]==8:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 1, 2))
            if board[i][j]==9:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 1, 3))
            if board[i][j]==10:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 1, 4))
            if board[i][j]==11:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 2, 0))
            if board[i][j]==12:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 2, 1))
            if board[i][j]==13:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 2, 2))
            if board[i][j]==14:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 2, 3))
            if board[i][j]==15:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 2, 4))
            if board[i][j]==16:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 3, 0))
            if board[i][j]==17:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 3, 1))
            if board[i][j]==18:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 3, 2))
            if board[i][j]==19:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 3, 3))
            if board[i][j]==20:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 3, 4))
            if board[i][j]==21:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 4, 0))
            if board[i][j]==22:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 4, 1))
            if board[i][j]==23:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 4, 2))
            if board[i][j]==24:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 4, 3))
            if board[i][j]==25:
                sum_manhattan=sum_manhattan+(short_heu(board, i, j, 4, 4))

    ref_board=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    for i in range (rows):
        for j in range(col):
            if board[i][j] == ref_board[i][j]:
                count=count+1
    return ((sum_manhattan/16)+(25-count))


# successor functions that return the board state with the move string
def next_moves(ini_board):
    #print("in next moves")
    moves=[]

    for idx in range (0,5):
        curr_board=ini_board.copy()
        curr_board = move_right(curr_board, idx)
        moves.append([curr_board,"R"+str(idx)])

        curr_board=ini_board.copy()
        curr_board = move_left(curr_board, idx)
        moves.append([curr_board,"L"+str(idx)])

        curr_board=ini_board.copy()
        curr_board = transpose_board(move_left(transpose_board(curr_board), idx))
        moves.append([curr_board,"U"+str(idx)])


        curr_board=ini_board.copy()
        curr_board = transpose_board(move_right(transpose_board(curr_board), idx))
        moves.append([curr_board,"D"+str(idx)])

    curr_board=ini_board.copy()
    curr_board = move_clockwise(curr_board)
    moves.append([curr_board,"Oc"])

    curr_board=ini_board.copy()
    curr_board = move_cclockwise(curr_board)
    moves.append([curr_board,"Occ"])
    
    curr_board=ini_board.copy()
    board=np.array(curr_board)
    inner_board=board[1:-1,1:-1].tolist()
    inner_board = move_clockwise(inner_board)
    board[1:-1,1:-1]=np.array(inner_board)
    board=board.tolist()
    curr_board=board
    moves.append([curr_board,"Ic"])

    curr_board=ini_board.copy()
    board=np.array(curr_board)
    inner_board=board[1:-1,1:-1].tolist()
    inner_board = move_cclockwise(inner_board)
    board[1:-1,1:-1]=np.array(inner_board)
    board=board.tolist()
    curr_board=board
    moves.append([curr_board,"Icc"])


    return moves
    
# Sorts the fringe in Ascending order according to the Cost
def sort_acc_to_cost(fringe):
    return fringe[1]

def solve(initial_board):
    goal_state = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    n=5
    initial_board=[initial_board[i:i + n] for i in range(0, len(initial_board), n)]
    initial_board = [list(x) for x in initial_board]

        
    fringe=[[initial_board, 0, ""]]
    visited=[initial_board]
    new_string=[]
    move_string=[]

    
    while(fringe):
        curr_board, heuristic_cost, each_string= fringe.pop()
        move_string.append(each_string)
        visited.append(curr_board)
        all_moves=next_moves(curr_board)
        for x in all_moves:
            if goal_state==x[0]:
                move_string.append(x[1])
                for i in range (1,len(move_string)):
                    new_string.append(move_string[i])
                return new_string
            
            else:
                if x[0] not in visited: #Checks for visited states
                    heuristic_cost= float(cal_heu(x[0]))
                    fringe.append([x[0], heuristic_cost + 1, x[1]])
                    fringe.sort(key=sort_acc_to_cost, reverse=True)

    """
    1. This function should return the solution as instructed in assignment, consisting of a list of moves like ["R2","D2","U1"].
    2. Do not add any extra parameters to the solve() function, or it will break our grading and testing code.
       For testing we will call this function with single argument(initial_board) and it should return 
       the solution.
    3. Please do not use any global variables, as it may cause the testing code to fail.
    4. You can assume that all test cases will be solvable.
    5. The current code just returns a dummy solution.
    """

# Please don't modify anything below this line
#
if __name__ == "__main__":
    if(len(sys.argv) != 2):
        raise(Exception("Error: expected a board filename"))

    start_state = []
    with open(sys.argv[1], 'r') as file:
        for line in file:
            start_state += [ int(i) for i in line.split() ]

    if len(start_state) != ROWS*COLS:
        raise(Exception("Error: couldn't parse start state file"))

    print("Start state: \n" +"\n".join(printable_board(tuple(start_state))))
    print("")

    print("Solving...")
    route= solve(tuple(start_state))

    print("Solution found in " + str(len(route)) + " moves:" + "\n" + " ".join(route))