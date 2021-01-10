'''@app.route('/inftopost')
from inftopost import inf_to_post as itf 
print("INFIX TO POSTFIX")
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
print("POSTFIX TO INFIX")
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

#infix to prefix
print("INFIX TO PREFIX")
from inftopre import infix_to_prefix as intpr 
obj2 = intpr()
expr=input()
rev=""
rev=obj2.reverse(expr)
#print(rev)
result=obj2.infixtoprefix(rev)
if (result!=False):
    
    prefix=obj2.reverse(result)
    print("the prefix expr of :",expr,"is",prefix)
else :
    print("Incorrect expression")


#prefix to infix
print("PREFIX TO INFIX")
from pretoinf import prefixtoinfix as prtin 
obj3 = prtin()
expr=input()
result = obj3.prefixToInfix(expr)


#this will be for the evaluate part
print("EVALUATE")
from eval import evaluate as ev
obj = ev()
res = ev.calc()
print("Result {}".format(res))'''
from flask import *
app = Flask(__name__,static_folder="assets")
@app.route('/')
def homepage():
    return render_template('index.html')

#this part will be in infix to postfix app route
@app.route('/InfixtoPostfix.html')
def showinftopost():
    return render_template("InfixtoPostfix.html")

@app.route('/InfixtoPostfix.html/show',methods=['POST'])
def send():
    from inftopost import inf_to_post as itf 
    s = request.form['x']
    obj=itf()
    l=[]
    l,result=obj.infixtopostfix(s)
    if (result==False):
        result = "Wrong input given, Follow directions of use given above"
    return render_template('InfixtoPostfix.html',results = result,l=l)

#this part is for the postfix to infix app route
@app.route('/PostfixtoInfix.html')
def showposttoinf():
    return render_template("PostfixtoInfix.html")

@app.route('/PostfixtoInfix.html/show',methods=['POST'])
def postinfshow():
    from posttoinf import post_to_inf as pti 
    s = request.form['x']
    obj1=pti()
    r = []
    #r[:] =s
    for i in s:
        r.append(i)
    l,result=obj1.getInfix(r)
    if (result==False):
        result = "Wrong Input, Check Directions of use and try again"
    return render_template('PostfixtoInfix.html',results = result,l=l)

#the following part is for Infix to Prefix
@app.route('/InfixtoPrefix.html')
def showinftopre():
    return render_template("InfixtoPrefix.html")

@app.route('/InfixtoPrefix.html/show',methods=['POST'])
def send2():
    from inftopre import infix_to_prefix as intpr 
    obj2 = intpr()
    expr=request.form['x']
    rev=""
    rev=obj2.reverse(expr)
    #print(rev)
    l,result=obj2.infixtoprefix(rev)
    if (result!=False):
        prefix=obj2.reverse(result)
        return render_template('PostfixtoInfix.html',results = prefix,l=l)
    else :
        return render_template('PostfixtoInfix.html',results = "Wrong Input, Check Directions of Use and try again",l=[])

#this part is for prefix to infix
@app.route('/PrefixtoInfix.html')
def pretoinf():
    return render_template("PrefixtoInfix.html")

@app.route('/PrefixtoInfix.html/show',methods=['POST'])
def send3():
    from pretoinf import prefixtoinfix as prtin 
    obj3 = prtin()
    l = []
    expr=request.form['x']
    l,result = obj3.prefixToInfix(expr)
    if (result!=False):
        return render_template('PostfixtoInfix.html',results = result,l=l)
    else :
        return render_template('PostfixtoInfix.html',results = "Wrong Input, Check Directions of Use and try again",l=[])



#Calculator
@app.route('/Calculator.html')
def showeval():
    return render_template('Calculator.html')

@app.route('/Calculator.html/show',methods = ['POST'])
def outcalc():
    from eval import evaluate as ev
    obj = ev()
    a = request.form['a']
    s = request.form['s']
    res = ev.calc(a,s)
    return render_template('Calculator.html',results = res)


if __name__ == "__main__":
    app.run(debug=True)