
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print(' '*(n-i),chr(64+i)*(2*i-1))


#OUTPUT
     A
    BBB
   CCCCC
  DDDDDDD
 EEEEEEEEE