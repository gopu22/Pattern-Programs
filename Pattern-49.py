
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(0,n+1-i):
        print(2*n+1-2*i,end=' ')
    for k in range(1,n+1-i):
        print(2*n+1-2*i,end=' ')
    print()


#OUTPUT
 9 9 9 9 9 9 9 9 9 
  7 7 7 7 7 7 7 
   5 5 5 5 5 
    3 3 3 
     1 