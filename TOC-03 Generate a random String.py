#Generate a sequence of string

#Write a Python Program To generate a String over {0 , 1, 2,3,4,...9}  
def stringMatch(S):
    Io,hi=0,len(S)
    ans=[]
    for x in S:
        if x=='I':
            ans.append(Io)
            Io +=1
        else:
            ans.append(hi)
            hi -=1
    return ans +[Io]

S=(input("Enter your string value: "))
print(stringMatch(S))

#Create a program to generate a Random String using the random.choices() function
import string
import random

s=(int(input("Enter your string value: ")))
ran="".join(random.choices(string.ascii_uppercase+string.digits,k=s))
print("The randomly genrated string is: "+str(ran))

#write a program to generate the random string in upper and lower case letters

def Upper_Lower_String(length):
    result="".join((random.choice(string.ascii_lowercase)for x in range(length)))
    print("Randome string generated in Lowercase: ",result)

    result1="".join((random.choice(string.ascii_uppercase)for x in range(length)))
    print("Randome string generated in Uppercase: ",result1)

Upper_Lower_String(10)
    
