import Tkinter as tk   # python
from Tkinter import *
#from PIL import Image,ImageTk,ImageSequence

class App:
	def __init__(self,*args, **kwargs):
#        tk.Tk.__init__(self, *args, **kwargs)

canvas=tkinter.canvas(parent,width=300,height=300)
canvas.pack()
self.sequence =[ImageTK.PhotoImage(img)
		for img in ImageSequence.Iterator(
			Image.open(
			"/home/pi/Documents/robotdocteur/images/1.gif"))]
self.image=self.canvas.create_image(200,200,image=self.sequence[0])
self.animating=true
self.animate(0)

def animate(self,counter):
self.canvas.itemconfig(self.image,image=self.sequence[counter])
if not self.animating:
return 
self.parent.after(33,lambda:self.animate((counter+1)%len(self.sequence)))
root=tkinter.TK()
app=App(root)
root.mainloop()
