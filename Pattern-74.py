
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(i-1),end=' ')
    for j in range(1,n+2-i):
        print(chr(65+n+1-i-j),end=' ')
    print()


#OUTPUT
 E D C B A 
  D C B A 
   C B A 
    B A 
     A 