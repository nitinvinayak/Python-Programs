stri='dksadkjsahdsalkdjsja'
print(stri);
print(stri[12:15]);     #prints that part of the stri
strj='hello';
strk=strj+stri;         #concatenation
print(strk);        
print(strj*3);          #prints contents of strj thrice in succession
count=0;
for l in stri:          
 if(l=='d'):            #checks if d is present in stri
  count+=1;             #counts the number of 'd' in stri
print(count);           
print('l' in strj);     #prints True if present False if not
print(len(stri));       #prints string length of stri
lis=list(enumerate(strj));
print(lis);             #prints number with all their index numbers
del stri;               #del deletes the entire variable
print("hello\n\x72");   #This takes the escape sequences
print(r"hello\n\x72");  #Using r or R before the string ignores the escape sequences
print(stri);            #this would give an error
