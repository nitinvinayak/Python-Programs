#OOPs Implementation
#• Instance creation—filling out instance attributes
#• Behavior methods—encapsulating logic in a class’s methods
#• Operator overloading—providing behavior for built-in operations like printing
#• Customizing behavior—redefining methods in subclasses to specialize them
#• Customizing constructors—adding initialization logic to superclass steps
import time
t=time.time()
class AttrDisplay:
    def gatherAttrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ', '.join(attrs)
    def __repr__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s, %s]' % (self.name, self.pay, self.job)
class Manager(Person):
    def __init__(self, name, pay): # Redefine constructor
        Person.__init__(self, name, 'mgr', pay) # Run original with 'mgr'
    def giveRaise(self, percent, bonus=.10): # Redefine at this level
        Person.giveRaise(self, percent + bonus) # Call Person's version
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000) # Make a Manager: __init__
    tom.giveRaise(.10) # Runs custom version
    print(tom.lastName()) # Runs inherited method
    print(tom) # Runs inherited __repr__
    development = Department(bob, sue) # Embed objects in a composite
    development.addMember(tom)
    development.giveRaises(.10) # Runs embedded objects' giveRaise
    development.showAll() # Runs embedded objects' __repr__
    #Another way without actually knowing the members of a class object
    for key in bob.__dict__:
        print(key,' =>',getattr(bob,key))
    	
print(time.time()-t)
