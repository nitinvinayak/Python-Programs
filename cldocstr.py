"I am: docstr.__doc__"
def func(args):
    "I am: docstr.func.__doc__"
    pass
class spam:
    "I am: spam.__doc__ or docstr.spam.__doc__ or self.__doc__"
    def method(self):
        "I am: spam.method.__doc__ or self.method.__doc__"
        print(self.__doc__)
        print(self.method.__doc__)
'''• Modules
— Implement data/logic packages
— Are created with Python files or other-language extensions
— Are used by being imported
— Form the top-level in Python program structure
'''
'''
• Classes
— Implement new full-featured objects
— Are created with class statements
— Are used by being called
— Always live within a module
'''
