#------------------------------ 1. Sorting -------------------------------
l=[4,5,20,1,3,2]
pivot=l[0]

left=[i for i in l[1:] if i<pivot]
right=[i for i in l[1:] if i>=pivot]

print(left+[pivot]+right)


#------------------------------ 2. two pointer approach for reversing -------------------------------
s = "the sky is blue"
a=s.split()
i=0
j=len(a)-1
while i<j:
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
    i+=1
    j-=1
print(' '.join(a))


#------------------------------ 3. swapping of two nos. using XOR -------------------------------
a=202
b=365
a=a^b
b=b^a
a=b^a
print(a,b)


#------------------------------ 4. swapping of two nos. using addition & substraction -------------------------------
a=202
b=365
a=a-b
b=b+a
a=b-a
print(a,b)
