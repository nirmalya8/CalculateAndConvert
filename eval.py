class evaluate:
    
    def calc():
        import numpy 
        import math
        a = (input("Number "))
        try:
            a = int(a)
        except Exception as e:
            s = input("Expression ")
            c = compile(s,"<string>","eval")
            x =""
            #try:
            res = eval(c)
            print(res)
            #except Exception as E:
            #   print("Wrong input somewhere, please check the instructions again!")
            #    x = "wrong input"
            #    return x
            return res

        s = input("Expression ")
        s = s.replace("a",str(a))
        c = compile(s,"<string>","eval")
        x =""
        try:
            res = eval(c)
            print(res)
        except Exception as E:
            print("Wrong input somewhere, please check the instructions again!")
            x = "wrong input"
            return x
        return res