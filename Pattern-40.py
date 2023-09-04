
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print("  "*(n+1-i),end=' ')
    for j in range(1,2*i):
        print(chr(64+j),end=' ')
    print()


#OUTPUT
           A 
         A B C 
       A B C D E 
     A B C D E F G 
   A B C D E F G H I