#Lists In Python
#Empty list
elist=[];
#Integer List
ilist=[10,12,3221,98];
#Mixed type Lists
mlist=[12,"qwe",13.2];
#Nested list
nlist=[12,[12,421,12],"sd"]
print(nlist[2][1]);#Prints 'd'
#The method above is Indexing elements for easy accessing
#Negative Indexing is also possible like -1 index means final item,-2 second last and so on
mylist=['p','r','o','g','r','a','m','m','i','n','g'];
print(mylist[2:5]);#prints 2,3,4 indexes
print(mylist[:3]);#prints 0,1,2 indexes
print(mylist[7:]);#prints elements starting from index 7
print(mylist[:-3]);#prints elements before 3rd last item
print(mylist[:]);#prints entire list
ilist.append(3);#adds element into list
print(ilist);
ilist.extend([32,12,23,2]);#adds these elements to the end of the list
print(ilist);
ilist.insert(4,9000);#at index 4, 9000 is inserted
print(ilist);
del mylist[7:];#deletes all elements starting from index 7
print(mylist);
print(mylist.pop(3));#prints element at index 3
print(mylist);#prints the list after the pop.
nlist.remove(12);#removes element 12 from nlist
print(nlist);
nlist.clear();#removes all elements from nlist
print(nlist);
print(mylist.index('r'));#returns the value of the index where it is found
print(mylist.count('r'));#counts the number of times it is found in the list
mylist.sort();#sorts the list in ascending order
print(mylist);
mylist.reverse();#sorts the list in descending order
print(mylist);
M = [[1, 2, 3], # A 3 x 3 matrix, as nested lists
[4, 5, 6],
[7, 8, 9]]
print(M);
col2=[];
col2=[row[1] for row in M];# Saves every element in row[1] 
print(col2);
e=[];
e=[row[1] for row in M if row[1] % 2 == 0];#Saves only even elements in row[1]
print(e);


