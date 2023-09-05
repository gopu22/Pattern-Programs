
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(n+1-i),end=' ')
    for j in range(1,i):
        print(i-j,end=' ')
    for k in range(0,i):
        print(k,end=' ')
    print()


#OUTPUT
      0 
     1 0 1 
    2 1 0 1 2 
   3 2 1 0 1 2 3 
  4 3 2 1 0 1 2 3 4