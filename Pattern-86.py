
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(i,i+1):
        print(n+1-i,end='')
        if i>=2:
            print(' '*(2*i-4),end=' ')
            for k in range(i,i+1):
                print(n+1-i,end=' ')
    print()


#OUTPUT
     5
    4 4 
   3   3 
  2     2 
 1       1 