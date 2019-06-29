class A :
    def feature1(self):
        print("print feature 1")
    def feature2(self):
        print("print features 2")

class B(A):
    def feature3(self):
            print("print feature 3")
    def feature4(self):
            print("print feature 4")

class C(B):
    def feature5(self):
        print("print feature 5")


a1=A()
b1=B()
c1=C()

c1.feature5()