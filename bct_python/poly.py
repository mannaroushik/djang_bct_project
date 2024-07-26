class A:
    def f1(self):
        print("A + f1")
class B:
    def f1(self):
        print("B + f1")
obj1 = A()
obj1.f1()
obj2 = B()
obj2.f1()