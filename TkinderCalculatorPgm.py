from tkinter import *

window = Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)

positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)

#window.geometry("500x600")
window.geometry("+{}+{}".format(positionRight, positionDown))
window.title("Calculator")
window.configure(bg="green")


def hello():
    print("Clicked")


button1 = Button(text="ok", command=hello, width=10, height=10, bg="red", fg="green")
button2 = Button(text="ok", command=hello, width=10, height=10, bg="red", fg="red")

button1.grid(row=0, column=0)
button2.grid(row=1, column=0)

label = Label(window, text="Welcome")
#button1.pack()
#label.pack()

window.mainloop()
