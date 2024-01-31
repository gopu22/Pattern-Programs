
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(i-1),end=' ')
    for j in range(i,i+1):
        print(i,end='')
        if i<=4:
            print(' '*(2*n-2*i-2),end=' ')
            for k in range(i,i+1):
                print(i,end=' ')
    print()


#OUTPUT
 1       1 
  2     2 
   3   3 
    4 4 
     5 