
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(1,i+1):
        print(chr(64+i),end=' ')
    print()

for k in range(1,n):
    print(' '*k,end=' ')
    for l in range(1,n+1-k):
        print(chr(64+n-k),end=' ')
    print()


#OUTPUT
     A 
    B B 
   C C C 
  D D D D 
 E E E E E 
  D D D D 
   C C C 
    B B 
     A 