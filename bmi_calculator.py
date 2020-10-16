from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.geometry("356x320")
window.title("Temperature Conversion")
# window.configure(bg="skyblue")

def calculate_func():
    if gender_select == "Male":
        bmi_output.config(text="awrhf")


def clear_func():
    weight_entry.delete(0, "end")
    height_entry.delete(0, "end")
    age_entry.delete(0, "end")
    bmi_output.config(text="")
    ideal_bmi_output.config(text="")


label1 = Label(window, text="Ideal Body Mass Index Calculator", font=("arial", 15, "bold"))
label1.grid(row=0, columnspan=4, pady=10, padx=10)

# the label frame
frame = LabelFrame(window, text="Enter your weight, height and gender", font=("arial", 10, "bold"), pady=7, padx=7)
frame.grid(row=1, columnspan=4, padx=5, pady=10)

# first row in frame
weight_label = Label(frame, text="Weight:")
weight_label.grid(row=0, column=0, padx=5, pady=2)

weight_entry = Entry(frame)
weight_entry.grid(row=0, column=1, pady=2)

weight_label = Label(frame, text="Kilograms")
weight_label.grid(row=0, column=2, columnspan=3, padx=5, pady=2)

# second row in frame
height_label = Label(frame, text="Height:")
height_label.grid(row=1, column=0, padx=5, pady=2)

height_entry = Entry(frame)
height_entry.grid(row=1, column=1, pady=2)

height_label = Label(frame, text="cm")
height_label.grid(row=1, column=2, padx=5, pady=2)

# third row in frame
gender_label = Label(frame, text="Gender:")
gender_label.grid(row=2, column=0, padx=5, pady=2)

gender_select = Combobox(frame, width=18, values=["Male", "Female"])
gender_select.grid(row=2, column=1, pady=2)

age_label = Label(frame, text="Age:")
age_label.grid(row=2, column=2, padx=5, pady=2)

age_entry = Entry(frame, width=5)
age_entry.grid(row=2, column=3, pady=2, padx=5)

# calculate button
calculate_button = Button(window, text="Calculate Your Ideal Body Mass Index", font=("arial", 12, "bold"), padx=28, command=calculate_func)
calculate_button.grid(row=2, columnspan=4)

# output row
bmi_output_label = Label(window, text="BMI:")
bmi_output_label.grid(row=3, column=0, pady=8)

bmi_output = Label(window, text="", bg="yellow", width=10)
bmi_output.grid(row=3, column=1, pady=8)

ideal_bmi = Label(window, text="Ideal BMI:")
ideal_bmi.grid(row=3, column=2, pady=8)

ideal_bmi_output = Label(window, text="", bg="yellow", width=10)
ideal_bmi_output.grid(row=3, column=3, pady=8)

# last row======> exit and clear buttons
clear_button = Button(window, text="Clear", font=("arial", 12, "bold"), width=6, command=clear_func)
clear_button.grid(row=4, column=0)

exit_button = Button(window, text="Exit", font=("arial", 12, "bold"), width=6, command=window.quit)
exit_button.grid(row=4, column=3)

window.mainloop()
