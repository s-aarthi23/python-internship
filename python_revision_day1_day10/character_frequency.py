a="apple"
char={}
for i in a:
   if i in char:
      char[i]=char[i]+1
   else:
      char[i]=1
print(char)