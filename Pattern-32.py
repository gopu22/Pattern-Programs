
n=int(input("Enter the number: "))
p=0
for i in range(1,n+1):
    print("  "*p,end=' ')
    for j  in range(1,n+2-i):
        print(chr(65+n-i),end=' ')
    print()
    p+=1


#OUTPUT
 E E E E E 
   D D D D 
     C C C 
       B B 
         A