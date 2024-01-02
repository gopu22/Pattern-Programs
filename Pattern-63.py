
n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-j),end=' ')
    print()

for k in range(1,n):
    for l in range(1,n+1-k):
        print(chr(65+n-l),end=' ')
    print()


#OUTPUT
E 
E D 
E D C 
E D C B 
E D C B A 
E D C B 
E D C 
E D 
E 