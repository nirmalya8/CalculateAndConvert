class inf_to_post:

    precedence={'^':5,'*':4,'/':4,'+':3,'-':3,'(':2,')':1}

    def __init__(self):

        self.items=[]

        self.size=-1

    def push(self,value):

        self.items.append(value)

        self.size+=1

    def pop(self):

        if self.isempty():

            return 0

        else:

            self.size-=1

            return self.items.pop()

    def isempty(self):

        if(self.size==-1):

            return True

        else:

            return False

    def seek(self):

        if self.isempty():

            return false

        else:

            return self.items[self.size]

    def isOperand(self,i):

        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':

            return True

        else:

            return False

    def infixtopostfix (self,exprs):

        postfix=""
        expr=""
        for i in exprs:
            if (i.islower()):
                expr = expr+i.upper()
            elif (i==' '):
                continue
            else:
                expr = expr+i


        for i in expr:

            if(len(expr)%2==0):

                

                return False

            elif(self.isOperand(i)):

                postfix +=i

            elif(i in '+-*/^'):

                while(len(self.items)and self.precedence[i]<=self.precedence[self.seek()]):

                    postfix+=self.pop()

                self.push(i)

            elif i is '(':

                self.push(i)

            elif i is ')':

                o=self.pop()

                while o!='(':

                    postfix +=o

                    o=self.pop()

            print(postfix)

                #end of for

        while len(self.items):

            if(self.seek()=='('):

                self.pop()

            else:

                postfix+=self.pop()

        return postfix