class Parent:
    def Func1(self):
        print("This is parent Function1:")

class Child(Parent):
    def Func1(self):
        print("This is child function1.")

    def Func2(self):
        super().Func1()  # calling parent function
        self.Func1()# calling child function
        print("This is Child function2.")

ch=Child()
ch.Func2()
