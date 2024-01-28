
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(" "*(n-i),end=' ')
    for j in range(i,i+1):
        print(chr(65+n-i),end='')
        if i>=2:
            print(' '*(2*i-4),end=' ')
            for k in range(i,i+1):
                print(chr(65+n-i),end=' ')
    print()


#OUTPUT
     E
    D D 
   C   C 
  B     B 
 A       A 