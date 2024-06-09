from  tkinter import *

STYLE = ("Arial", 24, "bold")

window = Tk()
window.title("Miles to Km Converter")
window.minsize()
window.config(padx= 20, pady= 20)

def calculate_miles_to_km():
    km_calculate.config(text= (float(miles_input.get()) * 1.609344))

equals_label = Label(text= "is equal to: ")
equals_label.grid(row= 1, column= 0)

miles_label = Label(text= "Miles")
miles_label.grid(row= 0, column= 2)

km_calculate = Label(text= "0")
km_calculate.grid(row= 1, column= 1)

km_label = Label(text= "Km")
km_label.grid(row= 1, column= 2)

miles_input = Entry()
miles_input.config(width= 10)
miles_input.grid(row= 0, column= 1)

calculate_button = Button(text= "Calculate", command= calculate_miles_to_km)
calculate_button.grid(row= 2, column= 1)




window.mainloop()