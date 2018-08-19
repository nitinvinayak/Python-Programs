class ListInstance:
    def __attrnames(self, indent=' '*4):
        result = 'Unders%s\n%s%%s\nOthers%s\n' % ('-'*77, indent, '-'*77)
        unders = []
        for attr in dir(self): # Instance dir()
            if attr[:2] == '__' and attr[-2:] == '__': # Skip internals
                unders.append(attr)
            else:
                display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
                result += '%s%s=%s\n' % (indent, attr, display)
        return result % ', '.join(unders)
    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, # My class's name
            id(self), # My address
            self.__attrnames())
class Super(ListInstance):
    def __init__(self):
        self.a=2
        self.b=3
class Sub(Super,ListInstance):
    def __init__(self):
        self.c=3
        Super.__init__(self)
        print('Created')
class One(ListInstance):
    def __init__(self):
        print('No data attributes')
if __name__ == '__main__':
    a=Super()
    b=Sub()
    c=One()
    c.x=3;c.y="hello"
    #print(a)
    #print(b)
    print(c)
    
