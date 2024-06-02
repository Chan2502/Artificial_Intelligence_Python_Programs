import queue
import sys

Frontier = queue.Queue()
Visited = []
GOAL = [1,2,3,4,5,6,7,8,0]

def copy(A):
    copy = []
    for i in range(A.__len__()):
        copy.append(A[i])
    return copy

def Input():
    print("Enter a start node ")
    A= [int(i) for i in input().split()]
    inv=0
    for i in range(8):
        for j in range(i,9):
            if A[i]>A[j] and A[j]!=0:
                inv=inv+1
    if inv%2!=0:
        print("No solution exists for this initial state")
        sys.exit()
        

    else:
        print(" solution exists for this initial state",'\n',"Solving...")
        return A

def Search(M):
    for pos in range(9):
        if M[pos]==0:
            return pos
        
def Up(M,pos):
    #U = []
    if pos>=3:
        U = copy(M)
        U[pos] = U[pos-3]
        U[pos-3] = 0
        if notVisited(U):
            return U

def Down(M,pos):
    #D = []
    if pos<6:
        D = copy(M)
        D[pos] = D[pos+3]
        D[pos+3] = 0
        if notVisited(D):
            return D

def Right(M,pos):
    #R = []
    if pos!=2 and pos!=5 and pos!=8:
        R = copy(M)
        R[pos] = R[pos+1]
        R[pos+1] = 0
        if notVisited(R):
            return R

def Left(M,pos):
    #L = []
    if pos!=0 and pos!=3 and pos!=6:
        L = copy(M)
        L[pos] = L[pos-1]
        L[pos-1] = 0
        if notVisited(L):
            return L

def notVisited(M):
    if M != None:
        temp = copy(Visited)
        for i in range(temp.__len__()):
            check = temp[i] == M
            # c = check.all()
            if check == True:
                return False
    return True

def reached(generated):
    for i in range(generated.__len__()):
        check = generated[i] == GOAL
        if check == True:
            return True
    return False

def Update(A):
    for i in range(A.__len__()):
        if A[i] != None:
            Frontier.put(A[i])
    #print('updated')

# print(copy(GOAL))
Board = Input()
Frontier.put(Board)
check = True
M = copy(Board)

while M != GOAL:
    if Frontier.empty():
        check = False

    M = Frontier.get()
    print(M)
    Visited.append(M)
    pos = Search(M)

    u = Up(M,pos)
    d = Down(M,pos)
    r = Right(M,pos)
    l = Left(M,pos)

    generated = [u,d,r,l]
    #print(generated)

    if reached(generated):
        check = False
        break
    else:
        Update(generated)

    


print(len(Visited))
print(GOAL)