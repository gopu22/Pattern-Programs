
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(i-1),end=' ')
    for j in range(1,n+2-i):
        print(n+2-i-j,end=' ')
    print()


#OUTPUT
 5 4 3 2 1 
  4 3 2 1 
   3 2 1 
    2 1 
     1 