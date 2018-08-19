class ListInstance:
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result
    
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
    print(a)
    print(b)
    print(c)
