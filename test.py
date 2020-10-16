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


'''def quit_msg():
    qw=Tk()
    frame1 = Frame(qw, highlightbackground="green", highlightcolor="green",highlightthickness=1, bd=0)
    frame1.pack()
    qw.overrideredirect(1)
    qw.geometry("200x70+650+400")
    lbl = Label(frame1, text="are you sure you want to quit")
    lbl.pack()
    yes_btn = Button(frame1, text="Yes", bg="light blue", fg="red",command=quit, width=10)
    yes_btn.pack(padx=10, pady=10 , side=LEFT)
    no_btn = Button(frame1, text="No", bg="light blue", fg="red",command=qw.destroy, width=10)
    no_btn.pack(padx=10, pady=10, side=LEFT)
    qw.mainloop()'''

def EXIT():
    exitsure = Tk()
    exitsure.attributes('-type', 'dock')
    areyousure = Label(exitsure, text="Are you sure you want to exit?")
    areyousure.grid(column=0, row=0)
    exitsure.focus_force()

    ExitYes = Button(exitsure, text="Yes", command=quit)
    ExitYes.grid(column=0, row=2)

    NoYes = Button(exitsure, text="No", command=exitsure.destroy)
    NoYes.grid(column=2, row=2)


my_input = Entry(window)
my_input.pack(pady=10)

my_button = Button(window, text="Click me!", command=number)
my_button.pack(pady=10)

my_label = Label(window)
my_label.pack(pady=10)

exit_button = Button(window, text="Exit", command=EXIT)
exit_button.pack()

window.mainloop()
