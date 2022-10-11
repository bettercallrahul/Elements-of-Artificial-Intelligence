
#!/usr/local/bin/python3
#
# arrange_pichus.py : arrange agents on a grid, avoiding conflicts
#
# Submitted by : [NAME: RAHUL GOMATHI SANKARAKRISHNAN USERNAME: RGOMATHI]
#
# Based on skeleton code in CSCI B551, Fall 2021.

import sys

# Parse the map from a given filename
def parse_map(filename):
	with open(filename, "r") as f:
		return [[char for char in line] for line in f.read().rstrip("\n").split("\n")][3:]

# Count total # of pichus on house_map
def count_pichus(house_map):
    return sum([ row.count('p') for row in house_map ] )

# Return a string with the house_map rendered in a human-pichuly format
def printable_house_map(house_map):
    return "\n".join(["".join(row) for row in house_map])

# Add a pichu to the house_map at the given position, and return a new house_map (doesn't change original)
def add_pichu(house_map, row, col):
    return house_map[0:row] + [house_map[row][0:col] + ['p',] + house_map[row][col+1:]] + house_map[row+1:]

# To check if a particular move is valid
def is_valid(house_map,R,C,d1,d2):
    for i in R:
        if house_map[i[0]][i[1]]=='p':
            return False
    for i in C:
        if house_map[i[0]][i[1]]=='p':
            return False
    for i in d1:
        if house_map[i[0]][i[1]]=='p':
            return False
    for i in d2:
        if house_map[i[0]][i[1]]=='p':
            return False
    return True

# Get list of successors of given house_map state
def successors(house_map):
    return [ add_pichu(house_map, r, c) for r in range(0, len(house_map)) for c in range(0,len(house_map[0])) if house_map[r][c] == '.' ]

# check if house_map is a goal state
def is_goal(house_map, k):
    return count_pichus(house_map) == k 

# Recalibrate row,col and diag matrices
def calibrate(house_map, plist, last):
    x = [[(r,c) for c in range(0,len(house_map[0])) if house_map[r][c]=='X'] for r in range(0,len(house_map))]
    X = [tup for se in x for tup in se]
    p1 = [(r,c) for r,ro in enumerate(house_map) for c,co in enumerate(ro) if co=='p']
    p = ()
    for i in p1:
        if i not in plist:
            p=i
    if not last:
        last=p
    if house_map[last[0]][last[1]]=='p' and last not in plist:
        row=[(last[0],c) for c in range(0,len(house_map[0]))]
        row.remove((last[0],last[1]))
        col=[(r,last[1]) for r in range(0,len(house_map))]
        col.remove((last[0],last[1]))
        diag1=[]
        diag2=[]
        rt=last[0]
        ct=last[1]
        while rt and ct:
            diag1.append((rt-1,ct-1))
            rt-=1
            ct-=1
        rt=last[0]
        ct=last[1]
        while rt<len(house_map)-1 and ct<len(house_map[0])-1:
            diag1.append((rt+1,ct+1))
            rt+=1
            ct+=1
        rt=last[0]
        ct=last[1]
        while rt and ct<len(house_map[0])-1:
            diag2.append((rt-1,ct+1))
            rt-=1
            ct+=1
        rt=last[0]
        ct=last[1]
        while rt<len(house_map)-1 and ct:
            diag2.append((rt+1,ct-1))
            rt+=1
            ct-=1
        diag1.sort()
        diag2.sort()
        for i in X:
            if i in row:
                ind=row.index(i)
                if last[1]<i[1]:
                    del row[ind:]
                else:
                    del row[:ind+1]
            if i in col:
                ind=col.index(i)
                if last[0]<i[0]:
                    del col[ind:]
                else:
                    del col[:ind+1]
            if i in diag1:
                ind=diag1.index(i)
                if last[0]<i[0]:
                    del diag1[ind:]
                else:
                    del diag1[:ind+1]
            if i in diag2:
                ind=diag2.index(i)
                if last[0]<i[0]:
                    del diag2[ind:]
                else:
                    del diag2[:ind+1]
        plist.append(last)
        last=p
        return row,col,diag1,diag2,plist,last
    else:
        last=p
    return [],[],[],[],plist,last

# Arrange agents on the map
#
# This function MUST take two parameters as input -- the house map and the value k --
# and return a tuple of the form (new_house_map, success), where:
# - new_house_map is a new version of the map with k agents,
# - success is True if a solution was found, and False otherwise.
#

def solve(initial_house_map,k):
    fringe = [initial_house_map]
    row=[]
    col=[]
    diag1=[]
    diag2=[]
    r=[]
    c=[]
    d1=[]
    d2=[]
    plist=[]
    last=()
    row,col,diag1,diag2,plist,last=calibrate(initial_house_map,plist,last)
    while len(fringe) > 0:
        for new_house_map in successors( fringe.pop()):         
            if is_valid(new_house_map,row,col,diag1,diag2):
                if is_goal(new_house_map,k):
                    r,c,d1,d2,plist,last=calibrate(new_house_map,plist,last)
                    row.extend(r)
                    col.extend(c)
                    diag1.extend(d1)
                    diag2.extend(d2)
                    if is_valid(new_house_map,row,col,diag1,diag2):
                        return(new_house_map,True)
                    else:
                        b=plist[1]
                        a=list(b)
                        plist=plist[0:1]
                        last=plist[0]
                        row,col,diag1,diag2,plist,last=calibrate(initial_house_map,[],last)
                        h=1
                        while h:
                            if a[1]==0:
                                a[0]-=1
                                a[1]=len(initial_house_map[0])-1
                            else:
                                a[1]-=1
                            if initial_house_map[a[0]][a[1]]=='.' and is_valid(initial_house_map,row,col,diag1,diag2):
                                h=0
                            if a[0]==0:
                                return(False,False)
                        new_house_map = add_pichu(initial_house_map,a[0],a[1])
                        b=tuple(a)
                        new_house_map[b[0]][b[1]]='p'
                        last=b
                r,c,d1,d2,plist,last=calibrate(new_house_map,plist,last)
                if not last:
                    return(False,False)
                row.extend(r)
                col.extend(c)
                diag1.extend(d1)
                diag2.extend(d2)
                fringe.append(new_house_map)
    return(False,False)


# Main Function
if __name__ == "__main__":
    house_map=parse_map(sys.argv[1])
    # This is k, the number of agents
    k = int(sys.argv[2])
    print ("Starting from initial house map:\n" + printable_house_map(house_map) + "\n\nLooking for solution...\n")
    solution = solve(house_map,k)
    print ("Here's what we found:")
    print (printable_house_map(solution[0]) if solution[1] else "False")
