
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(0,i):
        print(n+j-i,end=' ')
    print()

for k in range(1,n):
    print(' '*k,end=' ')
    for l in range(1,n+1-k):
        print(l+k-1,end=' ')
    print()


#OUTPUT
     4 
    3 4 
   2 3 4 
  1 2 3 4 
 0 1 2 3 4 
  1 2 3 4 
   2 3 4 
    3 4 
     4