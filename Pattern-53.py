
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(1,n+2-i):
        print(chr(64+j),end=' ')
    for k in range(2,n+2-i):
        print(chr(68+k-i),end=' ')
    print()


#OUTPUT
 A B C D E E F G H 
  A B C D D E F 
   A B C C D 
    A B B 
     A