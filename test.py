class klass:
    def over(self,other):
        x=other.__len__();
        print(other, x)
        if(x==1):
            print("CircleArea")
        elif(x==2):
            print("RectArea")
        elif(x==3):
            print("EllipArea")

if __name__=='__main__':
    x=klass();
    a=[str(x) for x in input("Enter:").split()]
    x.over(a);    
         
           
