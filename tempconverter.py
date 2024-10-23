import tkinter as tk

def convertdegrees():
    fahrenheit=1000*float(degrees.get())
   
    #.delete(0, tk.END) 


    indication.insert(tk.END,degrees)
    
# Window
window = tk.Tk()
window.geometry("510x300")
window.title("Celsisus to Fahrenheit Converter")

# Weight label
CFlabel = tk.Label(window, text="Celsius -> Fahrenheit", font=("Helvetica", 20), fg="grey")
CFlabel.place(x=140, y=0)

#enterlabel
enterlabel=tk.Label(window,text="Enter the temperature in Celsius", font=("Helvetica", 10), fg="black")
enterlabel.place(x=80, y=70)

#degree entry
degrees=tk.Entry(window, bg="white", fg="black", bd=2)
degrees.place(x=300, y=70)

#enterlabel
indication=tk.Label(window,text="Temperature in Fahrenheit", font=("Helvetica", 10), fg="black")
indication.place(x=100, y=100)

#enterde entry
degreesconverted=tk.Entry(window, bg="white", fg="black", bd=2)
degreesconverted.place(x=280, y=100)

# Convert button
convert = tk.Button(window, text="Convert", font=("Helvetica", 10), bg="green", fg="black", bd=2, relief=tk.RIDGE,  command=convertdegrees)
convert.place(x=225, y=150)


window.mainloop()