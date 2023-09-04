
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-j),end=' ')
    print()


#OUTPUT
E D C B A 
E D C B 
E D C 
E D 
E