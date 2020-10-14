from tkinter import *

window = Tk()
window.geometry("550x400")
window.title("Temperature Conversion")
window.configure(bg="skyblue")


def convert_function():
    if radio_button1:
        c = int(float(fahrenheit_input.get()))
        celsius = (c - 32) * (5 / 9)
        output_label.configure(text=celsius)


def convert_function1():
    if radio_button2:
        f = int(float(celsius_input.get()))
        fahrenheit = f * (9 / 5) + 32
        output_label.configure(text=fahrenheit)


def active_entry():
    if radio_button1:
        fahrenheit_input.configure(state="disable")
        celsius_input.configure(state="normal")


def active_entry2():
    if radio_button2:
        fahrenheit_input.configure(state="normal")
        celsius_input.configure(state="disable")


def clear_function():
    celsius_input.delete(0, 'end')
    fahrenheit_input.delete(0, 'end')
    output_label.configure(text="")
    celsius_input.configure(state="disable")
    fahrenheit_input.configure(state="disable")
    radio_button1.deselect()
    radio_button2.deselect()


# Label frame for cels to fahr
label_frame1 = LabelFrame(window, bg="pink", text="Celsius to fahrenheit", font=("arial", 10, "bold"), pady=45, padx=45)
label_frame1.grid(row=0, column=0)
celsius_input = Entry(label_frame1)
celsius_input.grid(row=1, column=0, pady=10)

# Label frame for fahr to cels
label_frame2 = LabelFrame(window, bg="pink", text="fahrenheit to Celsius", font=("arial", 10, "bold"), pady=45, padx=45)
label_frame2.grid(row=0, column=2)
fahrenheit_input = Entry(label_frame2)
fahrenheit_input.grid(row=1, column=0, pady=10)

# activate radio buttons
radio = IntVar()
radio_button1 = Radiobutton(window, text='Activate Celsius', variable=radio, value=1, font=("arial", 12, "bold"), command=active_entry)
radio_button1.grid(row=2, column=0, pady=15)
radio_button2 = Radiobutton(window, text='Activate fahrenheit', variable=radio, value=2, font=("arial", 12, "bold"), command=active_entry2)
radio_button2.grid(row=2, column=2, pady=15)

# conversion button
convert_button = Button(window, text="Calculate conversion", bg="green", activeforeground="green",font=("arial", 15, "bold"), command=convert_function)
convert_button.grid(row=3, column=0, pady=10)

convert_button1 = Button(window, text="Calculate conversion", bg="green", activeforeground="green",font=("arial", 15, "bold"), command=convert_function1)
convert_button1.grid(row=5, column=0, pady=10)

# results label
output_label = Label(window, width=27, height=2, font=("arial", 13, "bold"), fg="purple")
output_label.grid(row=3, column=2)

# clear button
clear_button = Button(window, text="Clear", bg="orange", activeforeground="orange", font=("arial", 15, "bold"), width=18, command=clear_function)
clear_button.grid(row=4, column=0, pady=10)

# Exit button
exit_button = Button(window, text="Exit", bg="red", width=18, activeforeground="red", font=("arial", 15, "bold"), command=window.quit)
exit_button.grid(row=4, column=2, pady=10)

window.mainloop()
