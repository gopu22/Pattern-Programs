
s1 = "adbc"
s2 = "eiacdbhjikadbc"
j=len(s1)
for i in range(len(s2)-len(s1)+1):
    if sorted(s1) == sorted(s2[i:j]):
        print(True)
        break
    j+=1
print(False)
