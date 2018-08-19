#Embedding and __getattr__
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
class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay) # Embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus) # Intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr) # Delegate all other attrs
    def __repr__(self):
        return str(self.person) # Must overload again (in 3.X)
