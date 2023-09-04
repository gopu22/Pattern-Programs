
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print('  '*(n-i),(chr(64+2*i-1)+" ")*(2*i-1))


#OUTPUT
         A 
       C C C 
     E E E E E 
   G G G G G G G 
 I I I I I I I I I