#Class keyword is used to define the class.
#def keyword is used to define the function or methods(special functions in class).
#self is a reference to objects made on this class, arguments to functions.
#self will alwaysbe initial parameters but not necessarily the only one

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
