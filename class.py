#Class keyword is used to define the class.
#def keyword is used to define the function or methods(special functions in class).
#self is a reference to objects made on this class, arguments to functions.
#self will always be initial parameters but not necessarily the only one

class Shark:
    def __init__(self,name):     #Constructor Definition.
        print("Object created");
        self.name=name;
    def swim(self):
        print(self.name+" shark is swimming.");
    def awesome(self):
        print(self.name+" shark is opting to be awesome.");
blue=Shark('sammy');  #Object Created
blue.swim();   #Method called
blue.awesome();#Method called again
class Worker:
    def __init__(self,name,pay):    #Initial when created
        self.name=name;
        self.pay=pay;
    def lastName(self):
        return self.name.split()[-1];
    def giveRaise(self,percent):
        self.pay=self.pay*(1+percent);
bob=Worker("Bob Smith",23000);
eni=Worker("Eni Keller",30000);
print(bob.lastName());
eni.giveRaise(0.2);
print(eni.pay);
