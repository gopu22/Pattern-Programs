
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end=' ')
    print()


#OUTPUT
A 
B B 
C C C 
D D D D 
E E E E E