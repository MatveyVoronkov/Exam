'''
class Human:
    height = 170

class Student(Human):
    satiety=0

class Worker(Human):
    satiety=100
nick=Student()
ann=Worker()
print(nick.height)
print(nick.satiety)
print(ann.height)
print(ann.satiety)

class Grandparent:
    height = 170
    satiety = 100
    age = 60

class Parent(Grandparent):
    age = 40

class Child(Parent):
    height = 50
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

nick=Child()

class Wow:
    def __wow(self):
        print('Wow')
    def __hello(self):
        print('Hello')

some_obj=Wow()
some_obj._hello()
some_obj.__Wow__wow()


class Hello_world:
    hello="Hello"
    _hello = "_Hello"
    __hello = "__Hello"
    def __init__(self):
        self.world='World'
        self._world = '_World'
        self.__world = '__World'

    def printer(self):
        print(self.hello)
        print(self._hello)
        print(self.__hello)
        print(self.world)
        print(self._world)
        print(self.__world)

class Hi(Hello_world):
    def hi_print(self):
        print(self.hello)
        print(self.world)
        print(self._hello)
        print(self._world)
        print(self.__hello)
        print(self.__world)
hello=Hello_world()
hello.printer()
hi=Hi()
hi.hi_print()


class Hello:
    def __init__(self):
        print('Hello')

class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print('World!')

obj=Hello_World()


class Class1:
    var = 20
    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super(Class2, self).__init__()
        print(self.var)
        print(super().var)
hello_world=Class2()

class Grandparent:
    def about(self):
        print('I am Grandparent')

    def about_myself(self):
        print('About myself Grandparent')

class Parent(Grandparent):
    def about(self):
        print('I am Parent')
'''
