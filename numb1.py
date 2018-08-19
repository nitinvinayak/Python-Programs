x=1/23;             #Classic Division. Shows decimals
y=1//23;            #Floor Division. No remainders. Only integers.
print("%2.5f" %x);  #prints with upto 5 decimal precision
print("%e" %x);     #prints the number in exponential format
print(x);           #As it is
t=143;
b=0b10;             #Binary
o=0o10;             #Octal
h=0x10;             #Hexadecimal
print(b,o,h);
print("%o,%x"%(t,t));
print(bin(t),oct(t),hex(t));
import math;
print(math.pi,math.e);
print(math.sin(math.pi/4)); #Takes arguments in radians
print(round(x,3));
s=312.232
print(round(s));
L=[2,3,4,5];    #Mutable Object
M=L;
L[2]=32;
print(L);       #L prints 2,3,32,5
print(M);       #M also prints 2,3,32,5
print(L==M);
#The reason to the above thing is that the components of the list is changed. Meaning that the object to which the refernce is made changes. This change is therefore reflected in other parts of the program, here M.
#To avoid the problem we can initialize M as a copy of L by the following
M=L[:];
L[2]=4;
print(L);
print(M);
print(L==M);
