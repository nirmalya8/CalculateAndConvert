class post_to_inf:
    def getInfix(self,str):
        l=[]
        for i in str:
            if i == ' ':
                return l,False 
        stack=[]
        
        for j in range(len(str)) :
            if self.operand(str[j]) :
                stack.append(str[j])
                l.append(str[j])
            else :
                operator1=stack.pop()
                operator2=stack.pop()
                stack.append("(" + operator2 + str[j] + operator1 + ")")
                l.append("(" + operator2 + str[j] + operator1 + ")")
        return l,stack.pop()        
    
    def operand(self,char) :
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or char in "0123456789" : 
            return True 
        else :
            return False     