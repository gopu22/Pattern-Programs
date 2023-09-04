
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(n-j,end=' ')
    print()


#OUTPUT
5 4 3 2 1 
5 4 3 2 
5 4 3 
5 4 
5