
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-i),end=' ')
    print()

for k in range(1,n+1):
    for l in range(1,n+1-k):
        print(chr(65+k),end=' ')
    print()


#OUTPUT
E 
D D 
C C C 
B B B B 
A A A A A 
B B B B 
C C C 
D D 
E 