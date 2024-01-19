
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

for k in range(1,n):
    print(' '*k,end=' ')
    for l in range(1,n+1-k):
        print(l,end=' ')
    print()


#OUTPUT
     1 
    1 2 
   1 2 3 
  1 2 3 4 
 1 2 3 4 5 
  1 2 3 4 
   1 2 3 
    1 2 
     1 