# a1-forrelease
# B551 Assignment 1: 
Name- Sai Saathvik Domala , Sravani Wayangankar, Rahul Gomathi

# Part 1 - 2021 Solver

## 1) Abstraction
State Space – Set of all valid states from one rotation of the puzzle.
Initial States – The initial jumbled state before performing A* search.
Successor Function – Set of RIGHT, LEFT, UP, DOWN, COUNTERCLOCKWISE, COUNTER CLOCKWISE moves. A total of 24 moves.{'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}
Goal State – This is the state where all the numbers are in order from 1-25.
Cost Function – The cost function is considered to be 1 as there is only one step needed to take to reach the next state, and it is same for all the states.
Heuristic function- The heuristic considered is the manhattan distance with wrapping around (minimum distance considered even after travelling till the end- up, down, left right, and coming from the other side). It is then divided by 16 for the number of tiles getting affected. The number of misplaced tiles is added to it.
Therefore the cumulative heuristic function is the shortest manhattan distance/16+number of misplaced tiles.
The branching factor is considered to be 24- which is the total number of possible configurations(state space). It will branch out and check all 24 configurations at each stage.
To answer the question that if a state is reached in 7 moves, it will explore around 170 moves using BFS.

## In this problem, what is the branching factor of the search tree?
The branching factor of the search tree is 24. One for all the 24 moves. A total of 24 moves.{'R1','R2','R3','R4','R5','L1','L2','L3','L4','L5','U1','U2','U3','U4','U5','D1','D2','D3','D4','D5','Oc','Ic','Occ','Icc'}



# Part 2 - Road Trip!
## 1) Abstractions
State Space – Set of all valid cities one can travel from start city to destination city.
Initial States – The initial city before performing A* search.
Successor Function – Set of neighbouring cities one can travel from the previous city.
Goal State – This is the state where we reach the destination city through the given cost function.
Cost Function – The cost function is one of shortest distance, shortest time, shortest segments and shortest delivery.

## 2) Additional Conditions
If a delivery truck travels at a speed >50, there is a chance a package may fall out. Initially, we use the same heuristic as time and later we implement a function to calculate the extra time to deliver including the rerouting to the start city.

## 3) Overview
Our approach uses FRINGE as the data structure with cost, route_taken, total_miles, total_segments and total_hours. We implement Search Algorithm #3 which implements the "cleanup" step.

## 4)Heuristics used:
a) Distance - Haversine Distance is used as the heuristic to calculate the distance between the current city and the destination.
b) Time - The maximum speed of all road segments is found and divided by the distance of the current road segment. 
c) Delivery - The heuristic used for delivery is the same as that of time since we want to find the fastest route for delivery too.
d) Segment - The heuristic for segment is simple. It is just a 1 to every fringe.
 
## 5) The algorithm is given below –
The algorithm used below is the Search Algorithm #3 taught by Prof. David Crandall.
I.	Initialise a FRINGE with 5 values- with cost, route_taken, total_miles, total_segments and total_hours.
II.	Pop the node with the smallest cost value.
III.Find the neighbour cities and check if they are valid.
IV.	Calculate the cost for the neighbour and add it to the fringe if it is not already visited.
    - Cost is found for 4 different cost functions with their respective heuristics.
V. Check if the neighbour city is visited and whether the cost is less than the city cost
    -Append this neighbour city to the fringe.
VI.	Sort the fringe according to the lowest cost.
VII.	Run the search algorithm until it hits a goal, if it doesn’t reach the goal, return Failure.
VIII.If the Goal is hit, find the delivery hours using a seperate function.
IX.  Return the final dictinoary with route-taken, total-miles, total-hours, total-segments, total-delivery hours


## 6) Problems Faced
One of the main issues we faced with this problem was tackling the missing coordinates. The idea we implemented was to find the nearest city to the city with missing values and impute this to calculate the heuristic.
Another issue was finding the distance. We initially implemented Manhattan distance but the resutls were flawed. I found a code for Haversine distance which gave me much better results. 




# Part 3 - Choosing teams

Initial State : Individual students to be grouped based on preferences

Goal State: A solution in which the AI takes the least amount of time to evaluate the student groups.

Heuristic used : Total cost of evaluating every group in a particular state

Successor function : A state in which the total cost is less than that of the predecessor.

### Solution : To start with, each student is allotted to his/ her individual group. The groups are now passed into a recursive function that sort the group in the descending order of their cost and evaluate different combination of groups for the first element in the sorted list(the group with the highest cost). This continues until the cost of the successor state is not less than that of the previous state. The resulting groups and the total cost are returned.
