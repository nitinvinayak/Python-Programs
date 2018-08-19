class ThirdClass():
    def __init__(self, value): # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other): # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data
def abst(obj):
    return abs(obj.data)
ThirdClass.abso=abst#Dynamically adding methods to a class

