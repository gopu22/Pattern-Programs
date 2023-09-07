
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(1,i):
        print(chr(65+(i-j)),end=' ')
    for k in range(0,i):
        print(chr(65+k),end=' ')
    print()


#OUTPUT
     A 
    B A B 
   C B A B C 
  D C B A B C D 
 E D C B A B C D E