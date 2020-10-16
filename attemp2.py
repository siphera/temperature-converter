from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("280x320")
window.title("Temperature Conversion")
window.configure(bg="skyblue")


# My conversion functions
def to_celsius():
    try:
        f = float(temp_input.get())
        celsius = (f - 32) * (5 / 9)
        output_label.configure(text=round(celsius, 2))
    except ValueError:
        output_label.configure(text="Please enter a number")


def to_fahrenheit():
    try:
        f = float(temp_input.get())
        fahrenheit = f * (9 / 5) + 32
        output_label.configure(text=round(fahrenheit, 2))
    except ValueError:
        output_label.configure(text="Please enter a number")


def clear_function():
    temp_input.delete(0, END)
    output_label.config(text="")


def exit_confirm():
    message_box = messagebox.askquestion ('Exit Application', 'Are you sure you want to exit the application')
    if message_box == 'yes':
        window.destroy()
    else:
        pass


# Create a frame
frame = LabelFrame(window, bg="pink", text="Celsius to fahrenheit", font=("arial", 10, "bold"), pady=45, padx=45)
frame.grid(row=0, columnspan=2, padx=10, pady=10)

# pack label and Entry inside the frame
label1 = Label(frame, text="Enter Temperature:", bg="pink", font=("arial", 10, "bold"))
label1.pack()
temp_input = Entry(frame)
temp_input.pack()

# Calculate buttons
celsius_button = Button(window, text="To celsius", font=("arial", 12, "bold"), command=to_celsius)
celsius_button.grid(row=1, column=0)
fahrenheit_button = Button(window, text="To fahrenheit", font=("arial", 12, "bold"), command=to_fahrenheit)
fahrenheit_button.grid(row=1, column=1)

# Output label
output_label = Label(window, width=32, height=2, font=("arial", 11, "bold"), fg="blue")
output_label.grid(row=2, columnspan=2, pady=10)

# Clear and exit buttons
clear_button = Button(window, text="Clear", bg="yellow", width=7, activeforeground="yellow", font=("arial", 15, "bold"), command=clear_function)
clear_button.grid(row=3, column=0)
exit_button = Button(window, text="Exit", bg="red", width=7, activeforeground="red", font=("arial", 15, "bold"), command=exit_confirm)
exit_button.grid(row=3, column=1)

window.mainloop()
