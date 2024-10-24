#simple program to create a object using oops concept
class dog:
    def __init__(self,n,a):
        self.n=n
        self.a=a
    def bark (self):
        return f"{self.n}is barking"
m=dog("Buddy",5)
print(m.n)
print(m.a)
print(m.bark())

#program 2 to show oops
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet (self):
        return f"hello, my name is {self.name} and i m {self.age} years old"
p=person("Kinjal",19)
print(p.name)
print(p.age)
print(p.greet())


#wap to create class car which can store brand and model and print brand and model
class car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def car1(self):
        return f"{self.brand} is a brand and model is {self.model}"
a=car("Mahindra","XUV400")
print(a.brand)
print(a.model)
print(a.car1())


#super () function
class parent:
    def __init__(self,name):
        self.name=name
    def greet(self):
        return f"Hello,{self.name}"
class child(parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age
    def dage(self):
        return f"{self.name} is {self.age} years old"
p=parent("kinjal")
p.greet()
g=child("kinjal",20)
g.dage()

#multi level inderitance
class a:
    def see(self):
        return "CLASS A"
class b:
    def get(self):
        return "CLASS B"
class c(a,b):
    def show(self):
        return "CLASS C"
class d(c):
    def display(self):
        return "CLASS D"
r=d()
print(r.display(),r.see(),r.show(),r.get())


#method overiding
class animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        return f"{self.name} makes a sound"
class dog(animal):
    def speak(self):
        return f"{self.name} bark"
v=animal("tiger")
print(v.speak())
t=dog("Buddy")
print(t.speak())

class base:
    def __init__(self):
        self._a=2
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("calling protected no. of base class",self._a)
        self._a=3
        print("callinf modified protected member",self._a)

o1=derived()
o2=base()
print("accessing protected member of o1",o1._a)
print("accessing protected member of o2",o2._a)

#private members
class base:
    def __init__(self):
        self.a="PCU"
        self.__c="PCU1"
class derived(base):
    def __init__(self):
        base.__init__(self)
        print("calling private member of base")
        print(self.__c)
obj1=base()
print(obj1.a)
