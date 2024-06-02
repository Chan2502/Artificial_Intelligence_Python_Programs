print("WELCOME TO THE TIC TAC TOE GAME")
a=[0,1,2,3,4,5,6,7,8]
print(a[0],"|",a[1],"|",a[2])
print("--|---|---")
print(a[3],"|",a[4],"|",a[5])
print("--|---|---")
print(a[6],"|",a[7],"|",a[8])
print("")
player1=input("Enters Player 1 name : ")
player2=input("Enters Player 2 name : ")
count=0
for i in range(0,9):
    if(count%2==0):
        print(player1," turn ")
        choose=int(input(""))
        if (choose in a ):
        
            a[choose]="X"
            count=count+1
            print(a[0],"|",a[1],"|",a[2])
            print("--|---|---")
            print(a[3],"|",a[4],"|",a[5])
            print("--|---|---")
            print(a[6],"|",a[7],"|",a[8])
            print("")
    else:
        print(player2," turn ")
        choose=int(input(""))
        a[choose]="0"
        count=count+1
        print(a[0],"|",a[1],"|",a[2])
        print("--|---|---")
        print(a[3],"|",a[4],"|",a[5])
        print("--|---|---")
        print(a[6],"|",a[7],"|",a[8])
        print("")

