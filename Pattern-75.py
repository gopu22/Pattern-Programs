
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(i-1),end=' ')
    for j in range(1,n+2-i):
        print(chr(64+j),end=' ')
    print()


#OUTPUT
 A B C D E 
  A B C D 
   A B C 
    A B 
     A 