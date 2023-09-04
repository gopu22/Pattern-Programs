
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(n+1-i):
        print(chr(65+j),end=' ')
    print()


#OUTPUT
A B C D E 
A B C D 
A B C 
A B 
A