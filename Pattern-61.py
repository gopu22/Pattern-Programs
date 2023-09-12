
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(0,i):
        print(n+j-i,end=' ')
    print()

for k in range(1,n+1):
    for l in range(0,n-k):
        print(l+k,end=' ')
    print()


#OUTPUT
4 
3 4 
2 3 4 
1 2 3 4 
0 1 2 3 4 
1 2 3 4 
2 3 4 
3 4 
4