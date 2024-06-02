import numpy as np
import copy

'''
1 2 3 4 5 0 7 8 6
'''

Queue = []
Visited = []
GOAL = np.array([1,2,3,4,5,6,7,8,0])

def Input():
    print("Enter a start node ")
    A= [int(i) for i in input().split()]
    return A

def Search(M):
    for pos in range(9):
        if M[pos]==0:
            return pos
def Up(M,pos):
    U = []
    if pos>=3:
        U = copy.deepcopy(M)
        U[pos] = U[pos-3]
        U[pos-3] = 0
        return U
    return [-1,-1,-1,-1,-1,-1,-1,-1,-1]

def Down(M,pos):
    D = []
    if pos<6:
        D = copy.deepcopy(M)
        D[pos] = D[pos+3]
        D[pos+3] = 0
        return D
    return [-1,-1,-1,-1,-1,-1,-1,-1,-1]

def Right(M,pos):
    R = []
    if pos!=2 and pos!=5 and pos!=8:
        R = copy.deepcopy(M)
        R[pos] = R[pos+1]
        R[pos+1] = 0
        return R
    return [-1,-1,-1,-1,-1,-1,-1,-1,-1]

def Left(M,pos):
    L = []
    if pos!=0 and pos!=3 and pos!=6:
        L = copy.deepcopy(M)
        L[pos] = L[pos-1]
        L[pos-1] = 0
        return L
    return [-1,-1,-1,-1,-1,-1,-1,-1,-1]

def notVisited(M,Visited):
    M = np.array(M)
    if M[0] != [-1]:
        temp = copy.deepcopy(Visited)
        for i in temp:
            check = np.array(temp.pop()) == M
            c = check.all()
            if c == True:
                return False
    return True


def BFS(BOARD):
    Queue.append(BOARD)
    check = np.array(BOARD) == GOAL

    while Queue:
        if check.all() == True:
            break

        M = Queue.pop(0)
        Visited.append(M)
        pos = Search(M)
        
        u=Up(M,pos)
        d=Down(M,pos)
        r=Right(M,pos)
        l=Left(M,pos)
        
        if notVisited(u,Visited) and u[0] != -1:
            Queue.append(u)
            check = GOAL == np.array(u)
            #print(u)
            
        if notVisited(d,Visited) and d[0] != -1:
            Queue.append(d)
            check = GOAL == np.array(d)
            #print(d)

        if notVisited(r,Visited) and r[0] != -1:
            Queue.append(r)
            check = GOAL == np.array(r)
            #print(r)

        if notVisited(l,Visited) and l[0] != -1:
            Queue.append(l)
            check = GOAL == np.array(l)
            #print(l)

def run(BOARD):
    inv=0
    for i in range(8):
        for j in range(i,9):
            if BOARD[i]>BOARD[j] and BOARD[j]!=0:
                inv=inv+1
    if inv%2!=0:
        print("No solution exists for this initial state")
    else:
        print(" solution exists for this initial state",'\n',"Solving...")
        BFS(BOARD)    


BOARD = input()
run(BOARD)
print(Visited.pop())
print(Queue.pop())