class Squares:
    def __init__(self, start, stop): # Save state when created
        self.value = start - 1
        self.stop = stop
    def __iter__(self): # Get iterator object on iter, this is essential for iteration
        return self #Other wise object is non iterable
    def __next__(self): # Return a square on each iteration
        if self.value == self.stop: # Also called by next built-in
            raise StopIteration
        self.value += 1
        return self.value ** 2
for i in Squares(1,5):
    print(i,end=" ")
print('\nnext')
I=Squares(3,8)
print(I.value)
for i in I:
    print(i,end=" ")
