
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(1,i+1):
        print(chr(64+j),end=' ')
    print()


#OUTPUT
     A 
    A B 
   A B C 
  A B C D 
 A B C D E