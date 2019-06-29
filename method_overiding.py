class A:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self,base,height):
        a=0.5*self.base*self.height
        print("The area of given triangle is {}".format(a))
class B(A):
    def area(self, base, height):
        b=self.base+self.height
        print("The sum of the base and height of a given triangle{}".format(b))
a1=A(3,4)
b1=B(3,4)
a1.area(3,4)
b1.area(3,4)

