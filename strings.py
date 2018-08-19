#Strings are immutable, meaning it is not possible to change a variable at a particular location.
#S='Spam'
#>>> S
#'Spam'
#>>> S[0] = 'z' # Immutable objects cannot be changed
#...error text omittted...
#TypeError: 'str' object does not support item assignment
#>>> S = 'z' + S[1:] # But we can run expressions to make new objects
#>>> S
#'zpam' //overwritten
p="Black";
print(p.find('ck'));    #Finds position of 'ck' in string
print(p.replace('ck','de'));#Replaces a substring with another
print(p);               #Displays original string
l='a,b,c,d,e,f';
print(l.split(',')); #Removes all 'commas'(delimiter) and prints the string as a list
print(l);
t="Hello I am a guy";
t=t.rstrip();       #Removes whitespaces on the right.
print(t.isalpha()); #Returns true only if all characters are letters
print(t.upper());   #Converts all letters to upper case
#the dir() command gives you all the methods for the corresponding argument
print(ord(l[0]));   #Prints the ASCII code of the character
print(len(l));     #Returns length of string
#Multiline Strings are used with triple single/double quotes.For eg.
k='''
sada"'sadsakhlkg
sdaas
'''
print(k);
#If you write only k in interpreter mode it returns >>> '\nsada"\'sadsakhlkg\nsdaas\n'
lt=[];
for i in range(1,27):
    lt.append(chr(64+i));
print(lt[::2]);
reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name': 'Bob', 'age': 40}
print(reply % values);
'''
Table 7-4. String method calls
S.capitalize( )                      S.ljust(width)
S.center(width)                      S.lower( )
S.count(sub [, start [, end]])       S.lstrip( )
S.encode([encoding [,errors]])       S.replace(old, new [, maxsplit])
S.endswith(suffix [, start [, end]]) S.rfind(sub [,start [,end]])
S.expandtabs([tabsize])              S.rindex(sub [, start [, end]])
S.find(sub [, start [, end]])        S.rjust(width)
S.index(sub [, start [, end]])       S.rstrip( )
S.isalnum( )                         S.split([sep [,maxsplit]])
S.isalpha( )                         S.splitlines([keepends])
S.isdigit( )                         S.startswith(prefix [, start [, end]])
S.islower( )                         S.strip( )
S.isspace( )                         S.swapcase( )
S.istitle( )                         S.title( )
S.isupper( )                         S.translate(table [, delchars])
S.join(seq)                          S.upper( )
'''
#Interesting Replace function
S = 'a+b+c+'
x = S.replace('+', 'spam')
print(x);
import string;
y = string.replace(S, '+', 'spam')
print(y);

