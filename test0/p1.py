def isOdd(n) :  
    if n%2==1:  
        return True
    else: 
        return False
def getVal(n) :
    if n == 0:  
       return 3
    else: 
        if isOdd(n):
           return n*n
        else:
            return 2*n
           

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(arr[i]):
        print(getVal(j), end=" ")
    print()
    
    
    

    

