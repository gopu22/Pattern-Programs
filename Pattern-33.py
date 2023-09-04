
n=int(input("Enter the number: "))
p=0
for i in range(1,n+1):
    print("  "*p,end=' ')
    for j  in range(65,66+n-i):
        print(chr(j),end=' ')
    print()
    p+=1


#OUTPUT
 A B C D E 
   A B C D 
     A B C 
       A B 
         A