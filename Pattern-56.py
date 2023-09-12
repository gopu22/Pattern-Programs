
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print(n-j,end=' ')
    print()

for k in range(1,n):
    print(' '*k,end=' ')
    for l in range(1,n+1-k):
        print(n-l,end=' ')
    print()


#OUTPUT
     4 
    4 3 
   4 3 2 
  4 3 2 1 
 4 3 2 1 0 
  4 3 2 1 
   4 3 2 
    4 3 
     4