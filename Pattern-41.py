
n=int(input("Enter the number: "))
for i in range(1,n+1):
    print("  "*(n+1-i),end=' ')
    for j in range(2*i-1,0,-1):
        print(chr(64+j),end=' ')
    print()


#OUTPUT
           A 
         C B A 
       E D C B A 
     G F E D C B A 
   I H G F E D C B A