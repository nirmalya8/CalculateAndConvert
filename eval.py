class evaluate:
    def calc():
        a = int(input("Number "))
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