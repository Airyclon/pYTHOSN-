from tkinter import *
root = Tk()
root.title("Subtraction")
root.geometry("420x200")

num = Label(root, text = "69420")
veh = Label(root, text = "Vehicle- 3028b")
pin = Label(root, text = "994000")
add = Label(root, text = "78th street, Arjun road")
name = Label(root, text = "Arjun")
bod = Label(root, text = "March 5th, 2010")
sr = Label(root, text = "hello")

name.pack()
bod.pack()
num.pack()
veh.pack()
pin.pack()
add.pack()
sr.pack()

def ye():
    result = 9-3
    sr["text"] = result

btn = Button(root, text = "idk", command = ye)

root.mainloop()