 #Operator Overloading
#• Operator overloading lets classes intercept normal Python operations.
#• Classes can overload all Python expression operators.
#• Classes can also overload built-in operations such as printing, function calls, attribute access, etc.
#• Overloading makes class instances act more like built-in types.
#• Overloading is implemented by providing specially named methods in a class.
class Number:
    def __init__(self, start): # On Number(start)
        self.data = start
    def __sub__(self, other): # On instance - other
        return Number(self.data - other) # Result is a new instance
    def __add__(self,other):
        return Number(self.data+other)
    def __iadd__(self,number):
        return Number(self.data+number)
class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int): # Test usage mode
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)
class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]
X=Number(3)
Y=X-100
print(Y.data)
Z=X+100
print(Z.data)
X+=3
print(X.data)
A=Indexer()
A[2:5:2]
A[4]
T=StepperIndex();
T.data="Spam"
for i in T.data:
    print(i,end=" ")
     

