
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(i-1),end=' ')
    for j in range(i,i+1):
        print(n+1-i,end='')
        if i<=4:
            print(' '*(2*n-2*i-2),end=' ')
            for k in range(i,i+1):
                print(n+1-i,end=' ')
    print()


#OUTPUT
 5       5 
  4     4 
   3   3 
    2 2 
     1 