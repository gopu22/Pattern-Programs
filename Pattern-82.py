
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print(n+j-i,end=' ')
    for k in range(1,i):
        print(n-k,end=' ')
    print()

for l in range(1,n):
    print(' '*l,end=' ')
    for m in range(1,n+1-l):
        print(l+m,end=' ')
    for p in range(1,n-l):
        print(n-p,end=' ')
    print()


#OUTPUT
     5 
    4 5 4 
   3 4 5 4 3 
  2 3 4 5 4 3 2 
 1 2 3 4 5 4 3 2 1 
  2 3 4 5 4 3 2 
   3 4 5 4 3 
    4 5 4 
     5 