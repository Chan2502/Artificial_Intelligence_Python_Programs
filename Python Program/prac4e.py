# Zero Division Error
'''try:
    a=input("Enter the number : ")
    num=a/0
    print(num)
except: 
    print("Zero division error")'''
#SyntaxErrors
'''try:
    if(i==0):
            print(i)
except:
      print("Syntax Error")'''
# Index Error
'''try:
    a=[1,2,3,4,5]
    print(a[10])
except:
    print("Index Error")'''
# Import Error
'''try:
    import chandra
except:
    print("Import error")'''
# Assertion error
'''
try:
    a=1
    b=0
    assert b!=0,"Invalid operator"
except:
    print("Assertion error")'''
#System Exit
try:
    raise SystemExit
except:
    print("System Exit")
