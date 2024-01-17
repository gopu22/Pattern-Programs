
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(1,i+1):
        print(i,end=' ')
    print()

for k in range(1,n):
    print(' '*k,end=' ')
    for l in range(1,n+1-k):
        print(n-k,end=' ')
    print()


#OUTPUT
     1 
    2 2 
   3 3 3 
  4 4 4 4 
 5 5 5 5 5 
  4 4 4 4 
   3 3 3 
    2 2 
     1 