"""
Course objective:
.Design reusable object oriented python classes
.Apply powerful oop concepts to handle complexity
    classes, instances
    encapsulation, inheritance, polymorphism
.Handle errors (exceptions)
.Serialize(store) objects for later use
.Debug, test and benchmark your code


Purpose and outcomes:

learn OOP concepts used across many languages:
Java, C++, JS etc.

Be able to contribute Python code on a professional level
Understand OOP terminology when descussed online or in interviews
Take an essential next step in your Python education
If already familiar with OOP, see how it is applied in a "Pythonic" way



Section 1:
Video 1: What is OOP and why?

Developed in the 1960;s
A paradigm for code organization and design
The OOP paradigm:
    Organizes data into objects and functionality into methods
    Defines object specifications (data and methods) in classes.
Promote collaboration, code extension and maintenance
The primary paradigm for software design worldwide.


Procedural paradigm:                            Object paradigm

this = 0                                        this = MyCustomInt()
this = increment(this)                          this.increment()
print(this)                                     print(this)

                                             (this is a MyCustomInt Object)



def increment(arg):                             class MyCustomInt(object):
    arg = arg + 1                                   def __int__(self)
    return arg                                          self.val = 0
                                                    def increment(self):
                                                        self.val = self.val + 1
                                                    def __repr__(self):
                                                        return str(self.val)


One definition of object:  a unit of data that has associated functionality

OOP: Why?

OOP organizes code so it is:
    easier to use
    easier to understand
    easier to maintain and extend
    easier to collaborate
Complexity must always be managed
OOP is a universal paradigm (many languages)
Learning OOP is a necessary next step into the larger world of software engineering.


OOP: Three pillars

Encapsulation
Inheritance
Polymorphism


Video 2: Object oriented python:

Everything is an object, even numbers
Other languages employs primitives (non-object data)

All entities in Python follow the same rules of objects
    every object (instance of a class) has a type (the class)
    the object or class has attributes, some of which are methods


What is an object?

An object is a unit of data (having one or more attributes), of a particular class or type, with associated functionality (methods).

type is roughly synonyms to class.

>>>
>>>
>>> var = 5
>>> dir(var)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>>
>>>
>>>
>>> var.__abs__()
5
>>> var.__abs__(.2)
Traceback (most recent call last):

>>> var.__abs__()
5.67
>>> var.__trunc__()
5
>>> var.__str__()
'5.67'
>>> var.__repr__()
'5.67'

>>> var.bit_length()
3

Video 3: Modules vs Classes:

Python Modules are files that contain Python code
Python modules can be executed or imported
Modules can contain class definitions.
Sometimes a module consists of a single class; in this case a module may seem synonymous with a class.

import mymod
no need to provide .py. mymode is a python file.
when we import a module, the code present in that python file is made avaialable in the python file.

ex:
var = 10

def dothis():
    print "executing the dothis() function"

this is not designed to be executed, it is designed to be imported.

in another python file:
    import mymod

    print mymod.var
    mymod.dothis()

    mymod namespace includes mymod variables

other ways to import:

---> import mymod as mm

and you can call the mymod variables as :

mm.var
mm.dothis()

---> import variables directly.

from mymod import var, dothis

now, you can use var and dothis without mymod.



Video 4: Classes, instances, type, methods, and attributes


Class :     a blueprint for an instance
Instance:   a constructed object of the class
type:       indicates the class the instance belongs to
Attribute:  any object value:   object.attribute
Method:     a "callable attribute" defined in the class (like a function defined under class)

var = 'hello, world!'
print(type(var))
var.upper()

>>> var = 'hello, world!'
>>> print(type(var))
<class 'str'>
>>> var.upper()                     --> as mentioned earlier, everything in python is an object. str is also an object. when calling upper method, it is one of the method in class (type) of str.
'HELLO, WORLD!'
>>>

>>>
>>>
>>> dir(var)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>

Instance method and attributes:

A car can be seen as  a class of object.
The car class provides the blueprint for a car object.
Each instance of a car does the same things (methods)
But, each car instance has its own state (attributes)


redcar = Car('red')
bluecar = Car('blue')

redcar.start()
redcar.openleft()
redcar.start()

bluecar.start()

redcar.stop()


ex 2: An Object's interface

an object's interface is made up of its methods.
Methods are like "bottons" that operate the object
Methods often change an instance's state (its data)
A method's often complex implementation is hidden behind the interface.

ATM. ATM is just an idea as long as you insert the ATM card inside. (Class)
once inserted, the machine becomes your machine as it has some data to work on (an instance is created with your ATM card data).
you can withdraw, deposit and check balance from your account. (your instance's methods)


Video 5: Defining a class

Defining a class; constructing an instance

Reveiw: class

    classes are "instance factories"
    classes define an "instance blueprint"
Construct an instance or object of the class
    instances know to which class they belong("type")
    instances can access variables defined in the class


ex:

class Myclass():
    pass

this_obj = Myclass()

print(this_obj)


>>> class Myclass():
...     pass
...
>>> this_obj=Myclass()
>>> print(this_obj)
<__main__.Myclass object at 0x105b8ff60>
>>>


>>> class Myclass():
...     var = 10
...
>>> this_obj = Myclass()
>>> that_obj = Myclass()
>>>
>>> print(this_obj.var)
10
>>> print(that_obj.var)
10
>>>


6 points to understanding classes:

1. An instance of a class knows what class it's from
2. vars defined in the class are available to the instance
3. A method on an instance passes instance as the first argument to the method (named self in the method)
4. Instances have their own data, called instance attributes
5. Variables defined in the class are called class attributes
6. When we read an attribute, Python looks for it first in the instance, and then the class



Video 5: Instance methods

>>> class Joe():
...     greeting = 'hello, Joe'
...
>>> thisjoe = Joe()
>>> print(thisjoe.greeting)
hello, Joe
>>>

the string greeting is accessible from instance 'thisjoe' as the instance looks for the attribute in the class.
An instance knows which class it is from and it knows that it has to look in the class for the variable.


>>> class Joe():
...     def callme(self):       --> if you notice here, function definition requires one argument that is called as self. it is a single argument required function,
...             print('we are calling the callme function from the instance')
...
>>>
>>> thisjoe=Joe()               --> thisjoe is an instance of class Joe.
>>> thisjoe.callme()            --> if you notice the function call, it is not provided with any argument. (callme is the method)
we are calling the callme function from the instance
>>>

but, there is no error when executing the thisjoe.callme().
because of the point 3 above.

"A method on an instance passes instance as the first argument to the method (named self in the method)"


ex:

>>> class Joe():
...     def callme():       --> when the method is defined without self parameter, the method call on the instance fails as below.
...             print('we are calling the callme function from the instance')
...
>>> thisjoe=Joe()
>>> thisjoe.callme()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: callme() takes 0 positional arguments but 1 was given

if you notice, the TypeError: the actual method callme, doesn't take any arguments but one of provided when the "thisjoe.callme()" is executed.


 A method on an instance passes instance as the first argument to the method (named self in the method)


>>> class Joe():
...     def callme(self):
...             print("this is just testing")
...             print(self)             --> notice we are printing self
...
>>> thisjoe = Joe()
>>> print(thisjoe)
<__main__.Joe object at 0x105c42e80>
>>> thisjoe.callme()
this is just testing
<__main__.Joe object at 0x105c42e80>     --> this is the output after printing self. if you notice self and thisjoe is same. In otherwords, method call on an instance passes the instance as the first argument to the method.

>>>


Instance methods recap:

instance methods are variables defined in the class.
They are accessed through the instance:
instance.method()
When called through the instance, the instance is automatically passed as 1st argument to the method.
Because of this automatic passing of the instance, instance methods are known as "bound" methods, i.e. bound to the instance upon which is called.

self is the instance upon which the method is called.
in the above example:
self = thisjoe

Video 6: Instance attributes ("state")


what is an object ?
an object is a unit of data (having one or more attributes), of a particular class or type, with associated functionality (methods).


>>> import random
>>>
>>> class Myclass():
...     def dothis(self):
...             self.rand_val = random.randint(1,10)
...
>>> myinst=Myclass()
>>> print(myinst)
<__main__.Myclass object at 0x105c529b0>
>>> myinst.dothis()
>>> print(myinst.rand_val)
5
>>>


myinst.rand_val -- this is same as the way we have been accessing the class variables. But, there is no class variable that is defined with the name.
it is not set in the class but in the instance itself.


recap:

we have seen that an instance can access variables defined in the class.
An instance can also get and set values in "itself".
Because these values change according to what happens to the object, we call these values "state".
Instance data takes the form of "instance attribute" values, set and accessed through "object.attribute" syntax.

Video 7: Three pillers

Encapsulation
Inheritance
Polymorphism

Encapsulation:


>>>
>>> class Myclass():
...     def set_val(self, val):
...             self.value = val
...     def get_val(self):
...             return self.value
...
>>> a = Myclass()
>>> b = Myclass()
>>>
>>> a.set_val(10)
>>> b.set_val(100)
>>>

>>> print(a.get_val())
10

>>> print(b.get_val())
100

>>>
>>> a.value = 'hello'           --> since a = self / instance of class Myclass, we can directly set the value outside or in the main body of the code like this.
>>> print(a.get_val())
hello
>>>

now the questions is: if we can set the value like that, why write the whole method to it,
reason is, using such methods kind of provide a gateway for an operations having to do with the instances state and in this gateway, we can ensure the integrity of the data / attributes by using these methods, we are "encapsulating" the instance and showing the integrity of its data.



>>>
>>> class MyInteger():
...     def set_val(self, val):
...             try:
...                     val = int(val)
...             except:
...                     return
...             self.val = val
...     def get_val(self):
...             return self.val
...     def increment_val(self):
...             self.val = self.val + 1
...
>>> i = MyInteger()
>>> i.set_val(9)
>>> print(i.get_val())
9
>>> i.set_val('hi')
>>> print(i.get_val())
9
>>>

in the above execution, we see that when we enter an invalid data (hi), set_val returns without setting anything. Protecting the integrity of the data.
Now, if you do as below:


>>> class MyInteger():
...     def set_val(self, val):
...             try:
...                     val = int(val)
...             except:
...                     return
...             self.val = val
...     def get_val(self):
...             return self.val
...     def increment_val(self):
...             self.val = self.val + 1
...
>>> i = MyInteger()
>>> i.set_val(9)
>>> print(i.get_val())
9
>>> i.val = 'hi'                --> see this. you can set the value like this. But, integrity of the data is lost and hence when you tried to increment the val, it fails.
>>> print(i.get_val())
hi
>>> i.increment_val()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 11, in increment_val
TypeError: can only concatenate str (not "int") to str

Recap:

Encapsulation: the first of the three pillers of OOP
Encapsulation refers to the safe storage of data (as attributes) in an instance.
Data should be accessed only through instance methods.
Data should be validated as correct (depending on the requirements set in class methods)
Data should be safe from changes by external processes.

Breaking encapsulation:
Although normally set in a setter method, instance attribute values can be set anywhere
Encapsulation in python is a voluntary  restriction
Python does not implement data hiding, as does other languages.

Video 8: Init constructor: (it is a special method)

Allows us to initialize the attributes at the time when the instance is constructed.
to create an attribute right at the beginning right before the instance is created.


__init__ --> underscore is to denote that it is a special / magic private method. Private being should be used internally to the class not to be called by the instance. Magic being, it is automatically called when the event happens.

Init is called automatically whenever a new instance is created.

>>>
>>> class MyNum():
...     def __init__(self):
...             print("calling __init__")
...             self.val = 0
...     def increment(self):
...             self.val = self.val + 1
...
>>> dd = MyNum()        --> calling __init__
calling __init__
>>> dd.increment()
>>> dd.increment()
>>> print(dd.val)
2
>>>

you can also pass a value


>>>
>>> class MyNum():
...      def __init__(self, value):
...              print("calling __init__")
...              self.val = value
...      def increment(self):
...              self.val = self.val + 1
...
...
>>> dd = MyNum(100)             ---> to pass a value / argument while you are creating an instance.
calling __init__
>>> dd.val
100
>>> dd.increment()
>>> dd.val
101
>>>


recap:

__init__ is a "keyword" variable: it must be named init
It is a method automatically called when a new instance is constructed
If it is not present, it is not called
The "self" argument is the first appearance of the instance
__init__ offers the opportunity to initialzie attributes in the instance at the time of construction


Video 9: Class Attributes vs Instance attributes

Instance can access both class and instance attributes.

>>> class YourClass():
...     classy = 10                             --> an attribute defined in the class - class attribute
...     def set_val(self):
...             self.insty = 100                --> an attribute defined inside an Object / instance - instance attribute.
...
>>> dd = YourClass()
>>> dd.set_val()
>>> print(dd.classy)
10
>>> print(dd.insty)
100
>>>

Breaking the encapsulation for testing :

>>>
>>> class YourClass():
...     classy = "class value!"
...
>>> dd = YourClass()
>>> print(dd.classy)
class value!
>>> dd.classy = "inst value!"
>>> print(dd.classy)
inst value!
>>> del dd.classy
>>> print(dd.classy)
class value!
>>>


Recap:

Attributes / variables in the class are accessible through the instance.
Instance attributes are also accessible by the instance
When we use the syntax "object.attribute", we are asking Python to look up the attribute
    first in the instance
    then in the class
Method calls through the instance follow this lookup


Video 10: Working with Class and instance data:



>>> class InstanceCounter():
...     count = 0           --> class variable ? Yes.
...     def __init__(self, val):
...             self.val = val
...             InstanceCounter.count +=1     --> we are using it as an object with object.attribute syntax to increment the value of count. It is not just a class variable, it is a class attribute and it is accessible through the class name. But this time, instead of using the instance, the class itself is standing as the object. Does it mean the class is also an object ? Yes.
...     def set_val(self, newval):
...             self.val = newval
...     def get_val(self):
...             return self.val
...     def get_count(self):
...             return InstanceCounter.count
...
>>> a = InstanceCounter(5)
>>> b = InstanceCounter(13)
>>> c = InstanceCounter(17)
>>>
>>> for obj in (a,b,c):
...     print ("val of obj %s" % (obj.get_val()))
...     print("count: %s" % (obj.get_count()))
...
val of obj 5
count: 3
val of obj 13
count: 3
val of obj 17
count: 3                --> always 3.
>>>


checking if class is also an object :

>>>
>>> class MyClass():
...     pass
...
>>> print(MyClass)
<class '__main__.MyClass'>          ---> indicating it is a class object.
>>>
>>> dir(MyClass)            ---> contains attribute list. They are all magic or private attribute but nonetheless, attributes.
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
>>>
>>>

>>>
>>> MyClass.var = 5
>>>
>>> print(MyClass.var)
5

>>>
>>> dir(MyClass)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'var']

notice here, now, the variable (var) shows up as an attribute.


>>> dir(MyClass.var)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
>>>



>>>
>>> class InstanceCounter():
...          count = 0
...          def __init__(self, val):
...                  self.val = val
...                  InstanceCounter.count +=1
...                  print(InstanceCounter.count)
...          def set_val(self, newval):
...                  self.val = newval
...          def get_val(self):
...                  return self.val
...          def get_count(self):
...                  return InstanceCounter.count
...
>>>
>>>
>>>
>>> a = InstanceCounter(5)
1
>>> b = InstanceCounter(13)
2
>>> c = InstanceCounter(17)
3
>>> for obj in (a,b,c):
...     print ("val of obj %s" % (obj.get_val()))
...     print("count: %s" % (obj.get_count()))
...
val of obj 5
count: 3
val of obj 13
count: 3
val of obj 17
count: 3
>>>

If we are in the code for the class, and we are referrring to a variable that was set count = 0, why then do we have to qualify it, with the class name when we are trying to get the value out ? (i.e. why use, InstanceCounter.count ? instead of count directly)


Answer has to do with the global variables.
If Python does not require you to qualify this variable with a class name, then you would not be able to access the global variables from within the class and that is something that you would conceviably would want to be able to do. Therefore, any variable set in the class, needs to be accessed with object.attribute syntax  and we are using the class object itself to access this attribute.


>>>
>>> class InstanceCounter():
...          count = 0
...          def __init__(self, val):           ---> think if we treat it as a function, any variable, defined inside a function is a local variable. we are trying to increment the local variable before the assignment. Hence the error.
...                  self.val = val
...                  count +=1
                     print(count)
...          def set_val(self, newval):
...                  self.val = newval
...          def get_val(self):
...                  return self.val
...          def get_count(self):
...                  return count
...
>>>
>>> a = InstanceCounter(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in __init__
UnboundLocalError: local variable 'count' referenced before assignment



>>> class InstanceCounter():
...          count = 0
...          def __init__(self, val):
...                  self.val = val
...                  count = 5
...                  count +=1
...                  print(InstanceCounter.count)
...                  print(count)
...          def set_val(self, newval):
...                  self.val = newval
...          def get_val(self):
...                  return self.val
...          def get_count(self):
...                  return count
...
>>>
>>> a = InstanceCounter(5)
0
6
>>>


Video 11: Inheritance

Encapsulation : A facility to store data in an object.

Inheritance : The ability to have one class to inherit the attributes of another class.


>>

>>> class Date():                       --> parent class
...     def get_date(self):
...             return '2019-06-21'
...
>>> class Time(Date):                   --> inherits from the Date class.
...     def get_time(self):
...             return '08:13:21'
...
>>> dt = Date()
>>> print(dt.get_date())
2019-06-21
>>> tm = Time()
>>> print(tm.get_date())                --> found this method in the 'Date' class.
2019-06-21
>>> print(tm.get_time())
08:13:21
>>>

>>> dir(tm)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'get_date', 'get_time']
>>>

notice that 'get_date', 'get_time' became attributes of tm object.

at base, inheritance is another level of attribute lookup.


Object.attribute lookup hierarchy:

    the instance                                    ---> instance attribute ?
    the class                                       ---> that class ?
    Any class from which this class inherits        ---> the parent class.


Some inheritance terms:

An inheriting class                         class MyClass(YourClass):

    child class
    derived class
    Subclass

An inherited class                          class YourClass():

    Parent class
    Base class
    Superclass


Recap:
    Inheritance : The second piller of OOP
    One class can inherit from another
        the class attributes are inherited
        In particular, its methods are inherited.
        This means that instances of an inheriting (child) class can access attributes of the inherited (parent) class.
    This is simply another level of attribute lookup: instance, then class, then inherited classes.

Video 12: Inheritance examples:


>>> class Animal():
...     def __init__(self, name):
...         self.name = name
...     def eat(self, food):
...         print('%s is eating %s.' % (self.name, food))
...
>>> class Dog(Animal):
...     def fetch(self, thing):
...         print("%s goes after the %s" % (self.name, thing))
...
>>> class Cat(Animal):
...     def swatstrings(self):
...         print("%s shreds the string! " % (self.name))
...
>>> r = Dog('Rover')
>>> f = Cat('Fluffy')
>>>
>>> r.fetch('paper')
Rover goes after the paper
>>> f.swatstrings()
Fluffy shreds the string!
>>> r.eat('dog food')
Rover is eating dog food.
>>> f.eat('cat food')
Fluffy is eating cat food.


>>> r.swatstring()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Dog' object has no attribute 'swatstring'

when we construct the dog object, the first thing that python does is that it checks in the dog class for __init__ attribute. If it doesn't find, then it checks if dog inherits from any other class and if so, looks into the parent class.


Recap:

Classes can be organised into an inheritance hierarchy
A child class can access the attributes of all parent (grandparent, etc.) classes.
Inheritance promotes code collaboration and reuse
No code should appear twice.

Video 13: Polymorphism:


Polymorphism means "Many shapes"

Two classes with same interface (i.e. method name)
The methods are often different, but conceptually similar.



class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))

class Dog(Animal):

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))
    def show_affection(self):
        print('{0} wags tail'.format(self.name))

class Cat(Animal):

    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))
    def show_affection(self):
        print('{0} purrs'.format(self.name))



for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()


Connected to pydev debugger (build 191.7479.19)
Rover wags tail
Fluffy purrs
Precious purrs


Recap:

Two classes with same interface(i.e. method name)
The methods are often differnt, but conceptually similar
Allows for expressiveness in design: we can sy that this group of related classes implement the same action
Duck typing refers to reading an object's attributes to decide whether it is of a proper type, rather than checking the type itself.


>>> var = 'hello'
>>>
>>> len(var)
5
>>>
>>> var.__len__()
5
>>>
>>> dir(var)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>>

__contains__ --> translates to "in"
string concatenation --> '__add__'


var = type = class/object and calling the method len() on the object.

>>>
>>>
>>>
>>> dir(['a', 'b'])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
>>>
>>>
>>> dir({'a': 1})
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>>
>>>
>>>

polymorphism = same interface (methods) between two objects.

__len__ method / interface between two or more objects like tuples, string, dictionary etc.

Types are also classes. ?



Video 14: Inheriting a constructor:

We may wish to initialize an instance by first processing it through parent class constructor and then through child class constructor.

__init__ = constructor.



import random

class Animal():

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)                             -->
        self.breed = random.choice(['shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))

d = Dog('dogname')

print(d.name)
print(d.breed)


----


import random

class Animal():

    breed = 'vinay'                     #---> global variable. Available anywhere.
    def __init__(self, name):
        self.name = name
        breed = 'vinay-local-inside__init__'  #--> local variable. Only available inside the method/funcion.
        print(breed)

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['shih Tzu', 'Beagle', 'Mutt'])
        print(Animal.breed)
    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))

d = Dog('dogname')

print(d.name)
print(d.breed)
print(Animal.breed)

output:

vinay-local-inside__init__
vinay
dogname
Mutt
vinay

---


import random

class Animal():

    breed = 'vinay-global-outside-function'                     #---> global variable. Available anywhere.
    name = 'global-name'
    def __init__(self, name):
        print("printing the global name variable as there is: ", self.name)
        self.name = name
        breed = 'vinay-local-inside__init__'  #--> local variable. Only available inside the method/funcion.
        print("printing the local breed name: ", breed)

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
#        self.breed = random.choice(['shih Tzu', 'Beagle', 'Mutt'])
#        print(Animal.breed)
    def fetch(self, thing):
        print('%s goes after the %s!' % (self.name, thing))

d = Dog('dogname')

print("printing the name as dogname as self.name is set on line 10 now: ", d.name)
print("printing the global breed variable /class attribute in the parent class as there is not breed variable in Dog object: ", d.breed)
print("Printing the global breed variable / class attribute in the parent class as we are directly referring to that: ", Animal.breed)

output:

printing the global name variable as there is:  global-name
printing the local breed name:  vinay-local-inside__init__
printing the name as dogname as self.name is set on line 10 now:  dogname
printing the global breed variable /class attribute in the parent class as there is not breed variable in Dog object:  vinay-global-outside-function
Printing the global breed variable / class attribute in the parent class as we are directly referring to that:  vinay-global-outside-function

https://stackoverflow.com/questions/5690888/variable-scopes-in-python-classes

 explain it with a simple example. It also includes some things like __something variables you did not mention in your list.

class Test:
    a = None
    b = None

    def __init__(self, a):
        print self.a
        self.a = a
        self._x = 123
        self.__y = 123
        b = 'meow'
At the beginning, a and b are only variables defined for the class itself - accessible via Test.a and Test.b and not specific to any instance.

When creating an instance of that class (which results in __init__ being executed):

print self.a doesn't find an instance variable and thus returns the class variable
self.a = a: a new instance variable a is created. This shadows the class variable so self.a will now reference the instance variable; to access the class variable you now have to use Test.a
The assignment to self._x creates a new instance variable. It's considered "not part of the public API" (aka protected) but technically it has no different behaviour.
The assignment to self.__y creates a new instance variable named _Test__y, i.e. its name is mangled so unless you use the mangled name it cannot be accessed from outside the class. This could be used for "private" variables.
The assignment to b creates a local variable. It is not available from anywhere but the __init__ function as it's not saved in the instance, class or global scope.




super(Dog, self).__init__(name):

Super is a built in function that relates the object / class to its super class.
in this case, we are asking, get the super class of Dog (Dog in above super line) and pass the dog instance(self in the above super line.) to whatever the method we say here.. here, it is constructor method


we can do Animal.__init__(name) instead of super(Dog, self).__init__(name). But, we did it this way because, if the name of the Animal object is to change in the future or we are going to rearrange the hierarchy of Dog instance or Dog inherits from a different class, we have to edit the code to call the constructor of the new parent etc.



Recap:


__init__ is like any other method; it can be inherited.
If a class does not have an __init__ constructor, Python will check its parent class to see if it can find one.
As soon as it finds one, Python calls it and stops looking.
We can use the super() function to call methods in the parent class
We may want to initialize in the parent as well as our own class.



Video 15: Multiple Inheritance and the lookup tree.

Ability to inherit from one or more classes.


class A():
    def dothis(self):

        ^
        |
        |
    class B(A):                        class C():
        pass                                def dothis(self):

        ^                                    ^
        |                                    |
        |__________class D(B,C):   __________|
                        pass


Class D is inheriting from B and C. Where B is a chlld class of A.

d_inst = D()
d_inst.dothis()

#which dothis() will be called ?
# mro: D-B-A-C

what order the classes are searched ? Depth first or Breadth first.
Answer is Depth.

Since class definition of D says, B is the first parent and C is the next.
So, it checks B and since, B is a child of A, it checks for dothis in A.
If it is found, it calls the dothis method from A.


mro = method resolution order.



>>> class A():
...
...     def dothis(self):
...         print('doing this in A')
...
>>> class B(A):
...     pass
...
>>>
>>> class C():
...
...     def dothis(self):
...         print('doing this in C')
...
>>> class D(B,C):
...     pass
...
>>> d_inst = D()
>>>
>>> d_inst.dothis()
doing this in A
>>>
>>> print(D.mro())
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class 'object'>]
>>>
>>>


we can use a special method called mro to make python show the order that it checks the attributes.

D.mro()




                                    class A():
                                        def dothis(self):
                                            |
                                            |
                      ______________________________________________
                     |                                              |
                     |                                              |
                class B(A):                                     class C(A):
                    pass                                            def dothis(self):

                     |                                              |
                     |                                              |
                      ______________________________________________
                                            |
                                            |
                                        class D(B,C)
                                            pass

                            "Diamond shape" inheritance:
                                ambiguous!


                                d_inst = D()
                                d_inst.dothis()
                                which dothis() will it call ?

                                mro : D-B-C-A



>>> class A():
...
...     def dothis(self):
...         print('doing this in A')
...
>>> class B(A):
...     pass
...
>>>
>>> class C(A):
...
...     def dothis(self):
...         print('doing this in C')
...
>>> class D(B,C):
...     pass
...
>>> d_inst = D()
>>>
>>> d_inst.dothis()
doing this in C
>>>
>>> print(D.mro())
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
>>>

if we see this, now, the order is D-B-C-A


Recap:

Any class can inherit from multiple classes.
Python normally uses a "depth first" order when searching inheriting classes.
But when two classes inherit from the same class, Python eliminates the first mention of that class from the mro (method resolution order)
The above applies to "new style" classes (inheriting from object)



Video 16: Decorators, Static and Class Methods.

The methods that we have seen so far are instance methods.
two special methods that are alternatives to the methods we have seen so far.

ex:

class Animal():
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eats {1}'.format(self.name, food))

class Dog(Animal):

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))
    def show_affection(self):
        print('{0} wags tail'.format(self.name))

class Cat(Animal):

    def swatstring(self):
        print('{0} shreds the string!'.format(self.name))
    def show_affection(self):
        print('{0} purrs'.format(self.name))



for a in (Dog('Rover'), Cat('Fluffy'), Cat('Precious'), Dog('Scout')):
    a.show_affection()

above methods are instance methods because, instance (self) is the first argument in all of them.

instance methods are bound methods. thats because, instances are bound to the method.

The new special methods that we see now are called class methods and static methods and they are not bound to the instance.

Class is a library of functionality that is assoicated with the instances that it produces. But, some of the functionality may not have to do with the instance itself. some of the functionality might be related directly to the class itself, dealing with class data.
ex: InstanceCounter.count.

We might even have some methods that are utility methods. They are not designed to work with class or instance.



>>>
>>> class InstanceCounter():
...          count = 0
...          def __init__(self, val):
...                  self.val = val
...                  InstanceCounter.count +=1
...                  print(InstanceCounter.count)
...          def set_val(self, newval):
...                  self.val = newval
...          def get_val(self):
...                  return self.val
...          def get_count(self):
...                  return InstanceCounter.count
...
>>>
>>>
>>>
>>> a = InstanceCounter(5)
1
>>> b = InstanceCounter(13)
2
>>> c = InstanceCounter(17)
3
>>> for obj in (a,b,c):
...     print ("val of obj %s" % (obj.get_val()))
...     print("count: %s" % (obj.get_count()))
...
val of obj 5
count: 3
val of obj 13
count: 3
val of obj 17
count: 3
>>>


Q) the get_count method, is it an instance method (bound method) or class method?


def get_count(self):  --> takes instance (self) as the arugument. So, it is a bound / instance method.
But, is it necessary to pass self ?

InstanceCounter.count is present in the constructor of the class where we are incrementing the count each time an instance is created.

So, when calling get_count, it doesn't look like we need instance to be passed.

Decorator is a special function that modifies the functions.


...          def get_count(self):
...                  return InstanceCounter.count
...

can be modified as below:

             @classmethod                           -->function decorator.
...          def get_count(cls):
...                  return cls.count
...

If we apply the classmethod decorator to a method, we could cause the method to pass the class automatically when called instead of the instance.


class InstanceCounter():
    count = 0
    def __init__(self, val):
        self.val = val
        InstanceCounter.count +=1
    def set_val(self, newval):
        self.val = newval
    def get_val(self):
        return self.val

    @classmethod
    def get_count(cls):
        return cls.count


a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a,b,c):
    print ("val of obj %s" % (obj.get_val()))
    print("count: %s" % (obj.get_count()))


Static method:

class InstanceCounter():
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count +=1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)


print(a.val)
print(b.val)
print(c.val)


Recap: Decorators; Class and Static Methods:

A class method takes the class (not instance) as argument and works with the class object.
A static method requires no argument and does not work with the class or instance (but it still belongs in the class code)
A decorator is a processor that modifies a function
@classmethod and @staticmethod modify the default binding that instance methods provide



Video 17: Abstract Classes

Abstract base class:

An "abstract class" is a kind of "model" for other classes to be defined. It is not designated to construct instances, but can be subclassed by regular classes.
Abstract classes can define an "interface", or methods that must be implemented by its subclasses.


Abstract classes are blueprints of how a subclass can be defined.

classes are blueprints to objects.



import abc


class GetterSetter():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def set_val(self, value):
        return

    @abc.abstractmethod
    def get_val(self):
        return


class MyClass(GetterSetter):

    def set_val(self, value):
        self.val = value

    def get_val(self):
        return self.val


x = MyClass()
print(x)


recap:

An abstract class is a kind of model for other classes to be defined. It is not designed to construct instances, but can be subclassed by regular classes.
Abstract classes can define an interface, or methods that must be implemented by its subclasses.
The pyton abc module enables the creation of abstract base classes.
For information, see the abc module and related docs.


Video 18: Inheritance examples.

When working in a child class we can choose to implement parent class methods in different ways

    inherit: simply use the parent class defined method
    Override/overload: provide child's own version of a method
    Extend: do work in addition to that in parent's method
    Provide: Implement abstract method tht parent requires.



import abc

class GetSetParent():
    __metaclass__ = abc.ABCMeta

    def __init__(self, value):
        self.val = 0
    def set_val(self, value):
        self.val = value
    def get_val(self):
        return self.val

    @abc.abstractmethod
    def showdoc(self):
        return

class GetSetInt(GetSetParent):
    def set_val(self, value):
        if not isinstance(value, int):
            value = 0
        super(GetSetInt, self).set_val(value)

    def showdoc(self):
        print("GetSetInt object ({0}), only accepts integer values".format(id(self)))


class GetSetList(GetSetParent):
    def __init__(self, value=0):
        self.vallist = [value]
    def get_val(self):
        return self.vallist[-1]
    def get_vals(self):
        return self.vallist
    def set_val(self, value):
        self.vallist.append(value)
    def showdoc(self):
        print("GetSetList object, len {0}, stores history of values set".format(len(self.vallist)))

gsl = GetSetList(5)
gsl.set_val(10)
gsl.set_val(20)

print(gsl.get_vals())



When working in a child class we can choose to implement parent class methods in different ways.




Video 19: Composition vs Inheritance:

Inheritance can be brittle (a change may require changes elsewhere)
Decoupled code is classes, functions, etc. that work independently and don't depend on one another.
As long as the interface is maintained, interactions between classes will work.
Not checking or requiring particular types is polymorphic and Pythonic.































Trapping and raising exceptions:

Identifying exceptions
trapping exceptions using try / except
Raising exceptions with raise
Defining custom exception classes.





"""