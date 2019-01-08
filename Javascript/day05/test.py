class MyClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __add__(self,others):
        return MyClass(self.name + others.name,self.age+others.age)

    def info(self):
        print('%s,%d.' %(self.name,self.age))


a = MyClass('Tom',18)
b = MyClass('Jack', 18)
e = MyClass('Rose', 18)

c = a + b + e

c.info()
