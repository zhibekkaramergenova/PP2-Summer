import re
t=int(input())
pattern='\d{3,8}[A-Z]{2,7}'
flag=True
res=[]
for i in range(t):  
    s=input()
    sett=set()
    for i in s:
        sett.add(i)
    if len(sett)!=len(s):res.append("Invalid")
    else:
        s=sorted(s)
        s=''.join(s)
        if re.search(pattern,s):res.append("Valid")
        else:res.append("Invalid")
    del sett
for i in res:
    print(i)
