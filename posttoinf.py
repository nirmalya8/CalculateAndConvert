class post_to_inf:
    def getInfix(self,str):
        stack=[]
        for j in range(len(str)) :
            if self.operand(str[j]) :
                stack.append(str[j])
                print(str[j])
            else :
                operator1=stack.pop()
                operator2=stack.pop()
                stack.append("(" + operator2 + str[j] + operator1 + ")")
                print("(" + operator2 + str[j] + operator1 + ")")
        return stack.pop()        
    
    def operand(self,char) :
        if (char >= 'a' and char <= 'z') or (char >= 'A' and char <= 'Z') or char in "0123456789" : 
            return True 
        else :
            return False     