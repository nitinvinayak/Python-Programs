import pickle
f=open('t.txt','w');
s=[];
s=input("Enter Lines:");
f.write(str(s));
f.close();
i=open('t.txt','r');
t=i.read();
print(t);
i.close();
k={'Name':'Ieshaan','No.':'180'};
d=input("Enter for d:");
l=open('t2.bin','wb');
#print(type(d));
pickle.dump(k,l);
l.close();
i=open('t2.bin','rb');
t=pickle.load(i);
print(t);
i.close()
