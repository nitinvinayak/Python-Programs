x=set('spam');
y=set('mail');
print( x & y );     #Intersection
print( x|y );       #Union
print(x,y);         #Shows both sets 
print(x-y)          #Difference of sets

#>>> if type(L) == type([]): # Type testing, if you must...
#print 'yes'
#yes
#>>> if type(L) == list: # Using the type name
#print 'yes'
#yes
#>>> if isinstance(L, list): # Object-oriented tests
#print 'yes'
#yes
