
n=int(input("Enter the number: "))
p=0
for i in range(1,n+1):
    print("  "*p,end=' ')
    for j  in range(1,n+2-i):
        print(j,end=' ')
    print()
    p+=1


#OUTPUT
 1 2 3 4 5 
   1 2 3 4 
     1 2 3 
       1 2 
         1