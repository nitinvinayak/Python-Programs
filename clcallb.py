import tkinter as tk
import turtle
#import tkMessageBox
class Callback:
    def __init__(self, color): # Class with state information
        self.color = color
    def changeColor(self): # A normal named method
        print('turn', self.color)
#def helloCallBack():
 #  tkMessageBox.showinfo( "Hello Python", "Hello World")
top=tk.Tk()
cb1 = Callback('blue')
cb2 = Callback('yellow')
B1 = tk.Button(command=cb1.changeColor) # Bound method: reference, don't call
B2 = tk.Button(command=cb2.changeColor) # Remembers function + self pair
#B = tk.Button(top, text ="Hello", command = helloCallBack)
#B.pack()
B1.pack()
B2.pack()
