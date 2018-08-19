#Working with shelve module
import sys
sys.path.insert(0,'/progs/')
from progs import clinh
bob = clinh.Person('Bob Smith') # Re-create objects to be stored
sue = clinh.Person('Sue Jones', job='dev', pay=100000)
tom = clinh.Manager('Tom Jones', 50000)
import shelve
db=shelve.open('persondb') # Filename where objects are stored
for obj in (bob, sue, tom): # Use object's name attr as key
    db[obj.name] = obj # Store object on shelve by key
db.close() # Close after making changes
print(open('persondb.dir').read())
#print(open('persondb.dat','rb').read())#Binary content
db=shelve.open('persondb')
for a in list(db.keys()):
    print(db[a])
#The downside is that classes and their module’s files must be importable when an instance is later loaded.

