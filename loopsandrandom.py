import random;
guess=1;
while guess<5:
    guess=random.randint(1,5);
    print(guess);
for i in range(2,20,3):        #You can pass upto 3 arguments in range
    print(i);                  #Where as i is the iterating variable
                               #The args are(start,stop,step);Similar to C++ loops
                               #The stop value is not inclusive
print(random.random());        #Prints a decimal value between 0 and 1
print(random.choice(['q','r','w','s'])); #prints one of the items in the list
nat_numbers=[];
for i in range(1,10):
    nat_numbers.append(i);
print(nat_numbers);
letters=[];
#Type Casting Done
for i in range(1,27):
    print(str(i)+"th letter is "+chr(i+96));#Data type converstion- int to char
    letters.append(chr(i+96));
print(letters);
for j in range(26):
    print(ord(letters[j]));#Data type conversion- char to int
