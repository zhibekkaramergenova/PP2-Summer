import re
pattern=re.compile(r'<[a-z][\w\-\_\.]+@[a-zA-Z]+\.[a-z]{1,3}>')
resname=[]
resemail=[]
n=int(input())
for i in range(n):
    name,email=input().split()
    if pattern.search(email):
       resname.append(name)
       resemail.append(email)
for i in range(len(resname)):
    print(resname[i],resemail[i])
