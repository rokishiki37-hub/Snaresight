class a:
    def m1(self):
        print("m1 method of class a")
class b(a):
    def m2(self):
        print("m2 method of class b")
class c(b):
    def m3(self):
        print("m3 method of class c")                    
obj = c()
obj.m1()
obj.m2()
obj.m3()        