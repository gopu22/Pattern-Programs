
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print(chr(64+n+j-i),end=' ')
    print()

for k in range(1,n):
    print(' '*k,end=' ')
    for l in range(1,n+1-k):
        print(chr(65+l+k-1),end=' ')
    print()


#OUTPUT
     E 
    D E 
   C D E 
  B C D E 
 A B C D E 
  B C D E 
   C D E 
    D E 
     E