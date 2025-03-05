#write a program for generating regular expression for regular grammer

import re
s= 'Swayam: A online portal for course certiifcation'
match=re.search(r'portal',s)
print("Start Index: ",match.start())
print("End Index :",match.end())

string="""Hello my Number is 123456789 and my friend's number is 9321923550"""
regex='\d+'
match=re.findall(regex,string)
print(match)


p=re.compile('[a-z]')
print(p.findall("Aye,said Mr.Gibenson Stark"))

p=re.compile(r'\b\w{5}\b')
print(p.findall("Aye,said Mr.Gibenson Stark"))

str1="Emma's luck numbers are 129  761 231 451"
string_pattern=r"\d{3}"
regex_pattern=re.compile(string_pattern)
result=regex_pattern.findall(str1)
print(result)

p=re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

p=re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 12th August 2005"))

p=re.compile('ab*')
print(p.findall("ababbbaabbb"))
`                   





