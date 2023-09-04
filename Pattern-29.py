
n=int(input("Enter the number: "))
p=0
for i in range(1,n+1):
    print('  '*p,"* "*(n+1-i))
    p+=1


#OUTPUT
 * * * * * 
   * * * * 
     * * * 
       * * 
         *