
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

from eval import evaluate as ev
obj = ev()
res = ev.calc()
print("Result {}".format(res))