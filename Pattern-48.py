
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(0,n+1-i):
        print(n+1-i,end=' ')
    for k in range(1,n+1-i):
        print(n+1-i,end=' ')
    print()


#OUTPUT
 5 5 5 5 5 5 5 5 5 
  4 4 4 4 4 4 4 
   3 3 3 3 3 
    2 2 2 
     1