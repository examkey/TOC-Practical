#program for creating a machine which  acc strings contanning equal number of 0s and equal no of 1s

s=input("give string in 1s and 0s:")
count1 = 0
count0 = 0
for i in range (len(s)):
    if(s[i]=='0'):
        count0 +=1
    if(s[i]=='1'):
        count1 +=1
if(count1 == count0):
    print("string is acc")
else:
    print("string is rej")
