import re
text="hello sathya"
k=re.findall("[a-m]",text)
x=re.findall("ya$",text)
print(k)
print(x)