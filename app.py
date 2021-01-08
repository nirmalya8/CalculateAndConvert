
#this part will be in infix to postfix app route
from inftopost import inf_to_post as itf 
s = input()
obj=itf()
result=obj.infixtopostfix(s)
if (result!=False):
    print(result)
print("Final output:") 
if (result!=False):
    print(result)
else:
    print("Incorrect input")

#this is for postfix to infix part
from posttoinf import post_to_inf as pti 
s = input()
obj1=pti()
r = []
#r[:] =s
for i in s:
    r.append(i)
result=obj1.getInfix(r)
if (result!=False):
    print(result)
print("Final output:") 
if (result!=False):
    print(result)
else:
    print("Incorrect input")


#this will be for the evaluate part
from eval import evaluate as ev
obj = ev()
res = ev.calc()
print("Result {}".format(res))

