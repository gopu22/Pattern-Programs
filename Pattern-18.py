
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(chr(64+i),end=' ')
    print()


#OUTPUT
A A A A A 
B B B B 
C C C 
D D 
E