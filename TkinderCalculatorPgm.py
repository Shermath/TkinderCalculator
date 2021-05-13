from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Calculator")
window.configure(bg="green")


def hello():
    print("Clicked")


button1 = Button(text="ok", command=hello, width=10, height=10, bg="red", fg="red")
button2 = Button(text="ok", command=hello, width=10, height=10, bg="red", fg="red")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)

label = Label(window, text="Welcome")
#button1.pack()
#label.pack()

window.mainloop()
