import re
pattern="[VLD]{0,1}[IXCM]{0,3}  "
num=input()
if len(num)==re.match(pattern,num):
    print("True")
else:
    print("False")