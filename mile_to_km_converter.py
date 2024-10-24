from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles*1.609
    kilometer_label_result.config(text=f"{km}")


window = Tk()

window.title("Mile to Km Converter")

# window.minsize(width=300, height=300)

window.config(padx=20,pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)


miles_label = Label(text="is equal to")
miles_label.grid(column=2,row=0)

kilometer_label_result = Label(text="0")
kilometer_label_result.grid(column=1,row=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=miles_to_km)
calculate_button.grid(column=1,row=2)

window.mainloop()