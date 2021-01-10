class prefixtoinfix:
    def prefixToInfix(self,prefix):
        stack = []
        l = []
        # read prefix in reverse order
        i = len(prefix) - 1
        while i >= 0:
            if not self.isOperator(prefix[i]):
                
                # symbol is operand
                stack.append(prefix[i])
                i -= 1
            else:
            
                # symbol is operator
                str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
                l.append(str)
                stack.append(str)
                i -= 1
        
        return l,stack.pop()
 
    def isOperator(self,c):
        if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
            return True
        else:
            return False