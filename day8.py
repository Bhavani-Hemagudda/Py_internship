# encapsulation

class bikes:
    def __init__(self,name,cc,m,cost):
        self.name = name
        self.cc = cc
        self.m = m
        self.cost = cost
    def performance(self):
        print("abt bikes:" , self.name,self.cc,self.m,self.cost)
gt=bikes("gt",650,12,4)
duke=bikes("duke",390,30,2)
gt.performance()
duke.performance()

# static method and class method and instance

class cars:
    wheels=4
    def __init__(self,mil,car):
        self.mil=mil
        self.car=car
    def get_mil(self):
        return c1.mil
    def set_mil(self):
        c1.mil=12
    @staticmethod
    def info():
        print("hi hello")
    @classmethod
    def infor(cls):
        return cls.wheels
print(cars.infor())
c1=cars(10,"bmw")
c2=cars(15,"audi")
c1.wheels=9
print(c1.mil)
print(c1.wheels)
print(c2.wheels)
print(c1.get_mil())
print(c1.set_mil())
print(c1.mil)

# duck typing:(method overloading)

class pycharm:
    def execute(self):
        print("compiling")
        print("running")
class myeditor:
    def execute(self):
        print("debugging")
        print("printing error")
        print("compiling")
        print("running")
class laptop:
    def code(self,ide):
        ide.execute()
ide=myeditor()
lap1=laptop()
lap1.code(ide)

# operator overloading using magic methods

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3
    def __gt__(self,other):
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
s1=student(59,65)
s2=student(67,85)
s3=s1+s2
print(s3.m1)
print(s3.m2)
if s1>s2:
    print("s1 is having more marks then s2")
else:
    print("s2 is having more marks then s1")


# method overloading

class math:
    def add(self,a=0,b=0,c=0):
        return a+b+c
m =math()
print(m.add(1,2))
print(m.add(1,2,3))
print(m.add())

# single level inheritance

class animal:
    def sound(self):
        return "animals make different sounds"
class dog(animal):
    def s(self):
        return "dog barks"
d=dog()
print(d.sound())
print(d.s())

# multiple inheritance

class engine:
    def engine_info(self):
        return "this is an engine"
class wheels:
    def wheels_info(self):
        return "car has 4 wheels"
class car(engine,wheels):
    def car_info(self):
        return "this a car"
c=car()
print(c.engine_info())
print(c.wheels_info())
print(c.car_info())

# multilevel inheritance

class animal:
    def species(self):
        return "this is an animal"
class mammal(animal):
    def category(self):
        return "this is a mammal"
class human(mammal):
    def speak(self):
        return "humans can speak"
h=human()
print(h.species())
print(h.category())
print(h.speak()) 

# hierarchial inheritance

class vehicle:
    def fuel_type(self):
        return "vehicles can use petrol,diesel and LPG"
class car(vehicle):
    def type(self):
        return "car is a 4-wheeler"
class bike(vehicle):
    def type(self):
        return "bike is a 2 wheeler"
c=car()
b=bike()
print(c.fuel_type())
print(c.type())
print(b.type())

# hybrid inheritance

class a:
    def display(self):
        print("display from a class")
class b(a):
    def display(self):
        print("dislpay from b class")
class c:
    def show(self):
        print("hi from class c")
class d(b,c):
    def display(self):
        print("display from d class")
d1=d()
d1.display()
d1.show()
print(d.mro()) #mro-method resolution order
