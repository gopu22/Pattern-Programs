
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(1,n+2-i):
        print(j,end=' ')
    for k in range(2,n+2-i):
        print(n+k-i,end=' ')
    print()


#OUTPUT
 1 2 3 4 5 6 7 8 9 
  1 2 3 4 5 6 7 
   1 2 3 4 5 
    1 2 3 
     1 