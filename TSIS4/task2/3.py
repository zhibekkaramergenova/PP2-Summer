import re
t=int(input())
res=[]
pattern='[+-]{0,1}\d*\.\d+'
for i in range(t):
    string=input()
    x=re.search(pattern,string)
    if x.group(0)==string:res.append("True")
    else:res.append('False')
    """
    if len(re.findall(pattern,string))==0:
        res.append("False")
    else:
        if string==re.findall(pattern,string)[0]:
           res.append("True")
        else:
            res.append("False")
    """
for i in res:
    print(i)