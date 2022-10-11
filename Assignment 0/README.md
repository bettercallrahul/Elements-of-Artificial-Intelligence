                                                            ELEMENTS OF AI                                
                                                             ASSIGNMENT-0 					
                                                                 REPORT
                                                 Submitted by – Rahul Gomathi Sankarakrishnan

route_pichu.py
2. Valid states – Pichu moving to locations marked with dots(.), goal location (@), and initial location of Pichu(p)
    Successor function – Pichu moving Right(R), Left(L), Up(U), Down(D) given that the successor location exists.
    Cost function – Cost to move from one cell to the successor cell is 1.
    Goal state definition – Pichu reaching the destination in an N x M map is the goal state.
    Initial state – Pichu in an N x M map marked with dots(.) and crosses(x) indicating a valid move and a block respectively to reach the goal (@).

3. The given code does not work because we do not keep a track of the visited cells. So, it keeps
     re–visiting the cells from which a valid path does not exist. 
     To fix this error, a list called “visited” has been initialized in the code. This keeps track of all the cells which have been visited by Pichu, hence it will stop at a visited cell and start exploring the successor cells which are unvisited.

4.  In this code, the search function has been executed using  DFS. Backtracking is done here if Pichu encounters a dead end, going back to the last legal cell and it explores its other unvisited successors.

arrange_pichus.py
Valid states – Any number of Pichus from 1 - k existing in an N x M map such that no two Pichus can see one another (i.e.) two Pichus can stay in the same row, column or diagonal only if there exists a block(x) between them.
Successor function – Adding a Pichu in a cell such that it cannot see any pre-existing Pichu.
Cost function – cost function is irrelevant in this case.
Goal state definition – k Pichus in an N x M map in which they cannot see one another.
Initial state – An N x M map marked with crosses(x) indicating a block with one pre-existing Pichu.

Overview
The existing code fails primarily because there is no condition that checks for pichus present in the same row, column or diagonal as a pre-existing pichu. To combat this, an “is_valid()” function has been defined in order to check if a pichu exists in the same row, column or diagonal in a potential location for the next pichu to be added to. A second function “calibrate()” is defined to constantly calibrate the row, column and diagonal values based that are prohibited from addition on every incoming pichu. This takes into consideration every block present in the map, meaning if there exists a block in between a pichu and a potential location, it is removed from the row, column or diagonal lists. This in turn makes entering pichus on the other side of blocks possible, even if on the same row, column or diagonal. Plist and last keep count of pre-existing pichu locations and last location checked, which would be added to plist if the number of existing pichus increases by 1. If a state is valid and contains k pichus, it is returned.

  

