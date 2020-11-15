## Multi-Level  Inheritance
class  A:
    def  display1(self):
        print("I am  inside  class  A")

class  B(A):
    def  display2(self):
        print("I am  inside  class  B")

class  C(B):
    def  display3(self):
        super().display1()
        super().display2()
        print("I am  inside  class  C")

c =C()
c.display3()


##Multiple Inheritance



class  E:
    def  display(self):
        print("I am  inside  class  E")

class  F:
    def  display(self):
        print("I am  inside  class  F")

class  G(E,F):
         pass

g = G()
g.display()