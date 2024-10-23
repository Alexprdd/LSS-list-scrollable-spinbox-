import tkinter as tk


#functions

def insertdata():
    userinput=entry.get()
    listbox.insert(tk.END, userinput)
    entry.delete(0, tk.END)

def getdata():
    dataindex=listbox.curselection()
    label.configure(text=str(dataindex))

def delete():
    dataindex=listbox.curselection()
    


#window
window=tk.Tk()
window.title("LSS")
window.geometry("1000x1000")

#listbox
listbox=tk.Listbox(window, height=10, width=20)
listbox.pack()
fruits=["apples","bananas","pinneapple","blueberry","oranges","grapes"]
for apples in fruits:
    listbox.insert(tk.END, apples)

#label
label=tk.Label(window, text="ENTRY", font="Arial", fg="black")
label.pack()
#entry
entry=tk.Entry(window)
entry.pack()

#buttons

insert=tk.Button(window, text="Insert", fg="black", font=("Arial",12), command=insertdata)
insert.pack()

delete=tk.Button(window, text="Delete", fg="Black", font=("Arial",12))
delete.pack()

clear=tk.Button(window, text="Clear", fg="Black",font=("Arial",12))
clear.pack()

get=tk.Button(window, text="Get", fg="Black", font=("Arial",12), command=getdata)
get.pack()




window.mainloop()