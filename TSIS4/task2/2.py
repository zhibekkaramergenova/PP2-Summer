import re
string=input()
res=re.split('[,.]',string)
for i in res:
    print(i)
