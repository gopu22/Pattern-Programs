
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(1,n+2-i,):
        print(chr(65+2*n-2*i),end=' ')
    for k in range(2,n+2-i):
        print(chr(65+2*n-2*i),end=' ')
    print()


#OUTPUT
 I I I I I I I I I 
  G G G G G G G 
   E E E E E 
    C C C 
     A