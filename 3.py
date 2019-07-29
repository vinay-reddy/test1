
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

