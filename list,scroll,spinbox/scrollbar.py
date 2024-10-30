import tkinter as tk

#window

window=tk.Tk()
window.title=("Scrollbar")
window.geometry("400x500")

#listbox
listbox=tk.Listbox(window)
for i in range(100):
    listbox.insert(tk.END, f"item {i}")
listbox.pack()

#scrollbar
scrollbar=tk.Scrollbar(window, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#configuring listbox with scrollbar

scrollbar.config(command=listbox.yview)
listbox.config(yscrollcommand=scrollbar.set)


window.mainloop()