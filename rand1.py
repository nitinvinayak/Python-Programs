import random;
guess=1;
while guess<5:
    guess=random.randint(1,5);
    print(guess);
for i in range(2,20,3):        #You can pass upto 3 arguments in range
    print(i);                  #Where as i is the iterating variable
                               #The args are(start,stop,step);Similar to C++ loops
                               #The stop value is not inclusive
nat_numbers=[];
for i in range(1,10):
    nat_numbers.append(i);
print(nat_numbers);
print(random.random());        #Prints random floating point value between 0 and 1
print(random.choice(['2','1','3','4']));
