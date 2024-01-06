# import required modules 
import tkinter as tk 
from tkinter import *
from PIL import Image 
from PIL import ImageTk
import os
import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

path = 'assets'
if n > 1:  #handle first argument - dictionary (default assets)
  path = sys.argv[1]

print("Files and directories in '", path, "' :")
dir_list = os.listdir(path)

images = []
root=tk.Tk()
root.geometry("1920x1080")

for file in dir_list:
    images.append(ImageTk.PhotoImage(Image.open(path + '/' + file))) #this maybe not the perfect idea, may cause a lot of memory problems

l=Label()
l.pack()

root.attributes('-fullscreen', True)

# using recursion to slide to next image 
x = 1
def move():
    global x
    if x == len(images):
        x = 1
    l.config(image=images[x])
    x = x+1

    root.after(5000, move)

# calling the function
move()

root.mainloop()
# function to change to next image 
