
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print('* '*(i),end=' ')
    print()

for j in range(1,n):
    print('* '*(n-j),end=' ')
    print()


#OUTPUT
*  
* *  
* * *  
* * * *  
* * * * *  
* * * *  
* * *  
* *  
*