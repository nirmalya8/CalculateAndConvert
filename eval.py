class evaluate:
    
    def calc(a,s):
        import numpy 
        import math
        try:
            a = int(a)
            s = s.replace("a",a)
            try:
                c = compile(s,"<string>","eval")
                res = eval(c)
            except Exception as e:
                return "Wrong Input"
        except Exception as e:
            c = compile(s,"<string>","eval")
            x =""
            try:
                res = eval(c)
            except Exception as E:
               #print("Wrong input somewhere, please check the instructions again!")
               x = "Wrong input"
               return x
            return res

        