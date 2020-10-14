from tkinter import *

window = Tk()
window.geometry("550x400")
window.title("Temperature Conversion")
window.configure(bg="green")


def number():
    try:
        float(my_input.get())
        my_label.configure(text="it's a number")
    except ValueError:
        my_label.configure(text="it's not a number!")


my_input = Entry(window)
my_input.pack(pady=10)

my_button = Button(window, text="Click me!", command=number)
my_button.pack(pady=10)

my_label = Label(window)
my_label.pack(pady=10)

exit_button = Button(window, text="Exit", command=window.quit)
exit_button.pack()

window.mainloop()
