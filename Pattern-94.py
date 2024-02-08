
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(' '*(i-1),end=' ')
    for j in range(1,n+1):
        print("* ",end=' ')
    print()


#OUTPUT
 *  *  *  *  *  
  *  *  *  *  *  
   *  *  *  *  *  
    *  *  *  *  *  
     *  *  *  *  *  