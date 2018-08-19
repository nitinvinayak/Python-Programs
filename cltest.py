class emp:
    def __init__(self,name,pay=10000):
        self.name=name
        self.pay=pay
    def __iter__(self):
        return self
    def __getitem__(self,index):
        if isinstance(index,int):
            print('index',index)
        else:
            print('slicing',index.start,index.stop,index.step)
    def __add__(self,other):
        if isinstance(other,emp):#To avoid nesting of class
            other=other.pay
        return emp(self.name,self.pay+other)
    def __radd__(self,other):
        if isinstance(other,emp):#To avoid nesting of class
            other=other.pay
        return emp(self.name,other+self.pay)
    def __iadd__(self,other):
        if isinstance(other,emp):#To avoid nesting of class
            other=other.pay
        return emp(self.name,self.pay+other)
    def __next__(self):
        pass
    def __str__(self):
        return ("Name:"+str(self.name)+" Pay:"+str(self.pay))
    def __getattr__(self,attrname):
        for i in dir(self):
            if not i.startswith('_'):
                if i==attrname:
                    print('found:',attrname,',attrvalue is:',end=" ")
                    print(self.__dict__[i])
                    return
        raise AttributeError()
    '''
    def __setattr__(self, attr, value):
        #for i in dir(self):
        #if not i.startswith('_'):
        if attr=='pay':
           self.__dict__['pay'] = value + 10 # Not self.name=val or setattr
           print(self.__dict[attr])
        else:
           raise AttributeError(attr + ' not allowed')   
    '''
T=emp('Jobs',12000)
S=emp('Cook',12000)
print(T)
print(type(T.pay))
T=T+100
T+=300
print(T)
T.__getattr__('pay')
T.__setattr__('pay',20000)
print(T)
S=S+T
print(S)
