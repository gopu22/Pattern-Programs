
n=int(input("Enter the number: "))
p=0
for i in range(1,n+1):
    print('  '*p,(str(n+1-i)+" ")*(n+1-i))
    p+=1


#OUTPUT
 5 5 5 5 5 
   4 4 4 4 
     3 3 3 
       2 2 
         1