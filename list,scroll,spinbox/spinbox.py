import tkinter as tk

#select/detect function

def select():
    print("Value selected in Spinbox is...", spinbox3.get())

#window

window=tk.Tk()
window.title("Spinbox")
window.geometry("500x600")

#spinbox

#text
spinbox=tk.Spinbox(window, values=("apples", "bananas", "pears", "watermelon", "blueberries"))#
spinbox.pack()

#integer
spinbox2=tk.Spinbox(window, from_=0, to=10, increment=1)
spinbox2.pack()

#float
spinbox3=tk.Spinbox(window, from_=0 ,to=100, increment=0.5, format="%04.1f", command=select)
spinbox3.pack()

window.mainloop()