X= int(input("Enter the Capacity 1: "))
Y= int(input("Enter the Capacity 2: "))
target=int(input("Enter the target Capacity: "))
print("Steps: ")
def jug(x,y):
    print(x,y)
    if(x==target and y==0):
        return
    elif(y==Y):
        jug(x,0)
    elif(x!=0):
        if (x+y>=Y):
            jug(x-(Y-y),Y)
        else:
            jug(0,x+y)
    else:
        jug(X,y)

jug(0,0)