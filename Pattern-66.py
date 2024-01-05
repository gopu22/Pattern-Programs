
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(1,i+1):
        print(i,end=' ')
    print()


#OUTPUT
     1 
    2 2 
   3 3 3 
  4 4 4 4 
 5 5 5 5 5