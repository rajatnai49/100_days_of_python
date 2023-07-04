from tkinter import *


def miles_to_km():
    calc_num = float(num_miles.get()) * 1.609
    answer_label.config(text=round(calc_num, 2))


window = Tk()
window.title("Miles to Km")
window.config(padx=40, pady=40)

miles_label = Label(text="Miles", font="Arial")
miles_label.grid(column=2, row=0)
miles_label.config(padx=20, pady=20)

miles_label = Label(text="KM", font="Arial")
miles_label.grid(column=0, row=0)
miles_label.config(padx=20, pady=20)

answer_label = Label(text="Equals", font="Arial")
answer_label.grid(column=1, row=1)
answer_label.config(padx=20, pady=20)

num_miles = Entry(width=10)
num_miles.grid(column=1, row=0)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)
num_miles

window.mainloop()
