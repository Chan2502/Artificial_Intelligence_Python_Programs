"""list=['s','r','i','r','a','m','d','e','o','b','a','b','a','c','o','l','l','e','g','e']
count=0
for i in list:
    if(i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
        count+=1
print("The number of vowel present is : ",count)
"""
tuple1=("shoes","watch","shirt","pant","ring","watch","watch","watch","watch")
count=0
count1=0
count2=0
count3=0
count4=0
for i in tuple1:
    if(i=="shoes"):
        count+=1
    elif(i=="watch"):
        count1+=1
    elif(i=="shirt"):
        count2+=1
    elif(i=="pant"):
        count3+=1
    else:
        print("Empty Tuple")
print("Items \t count")
print("shoes: \t",count)
print("watch: \t",count1)
print("shirt: \t",count2)
print("pant: \t",count3)

