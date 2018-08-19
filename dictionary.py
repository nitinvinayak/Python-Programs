#Dictionaries
d=dict(); #Create a New Dictionary
#Generating key-value pairs
d['name']='SpecialOne';
d['id']=1232017;
d['status']='pass';
print(d);#Prints all key-value pairs
print(d.keys());#Prints keys
print(d.values());#Prints values
print(d['name']);#Prints the value corresponding to key
print(d.items());#Prints all the dictionary items of that name
#This loop iterates through the dictionary
for key,value in d.items():
    print(key,' : ',value);
name={'d':'SpecialOne'};
name['c']='SimpleOne';
print(name);

d.update({'id':2312312});#Updates value of id
print(d.items());
print('points' in d);
del d;
del name;
#new Dictionary
username={'Axel':'Axel10','Mark':'Evans1','Jude':'Jude14'};
while True:
    print("Enter a name:");
    name=input();#Obtaining input from user.
    if name in username:
        print(username[name]+' : '+name);
    else:
        print("not in data, please input to add");
        use=input()
        username[name]=use;
        print("updated");
#No exit in above loop
