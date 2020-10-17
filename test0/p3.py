n = int(input())
arr=[]
for i in range(n):
    m = int(input())
    for j in range(m):
        ele = list(map(int, input().split()))
        arr.append(ele)

for i in arr:
    revlist = i.reverse()
    for j in revlist: 
        print(j, end =" ")
    

 
      

    
