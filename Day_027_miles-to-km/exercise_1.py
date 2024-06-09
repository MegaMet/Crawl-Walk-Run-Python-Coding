## Sandbox and experiments

import  tkinter

STYLE = ("Arial", 24, "bold")

window = tkinter.Tk()
window.title("Sting")
window.minsize(width= 500, height=300)
window.config(padx= 100, pady= 200)

label = tkinter.Label(text="I am a Lable", font=STYLE)
#label.pack(side= "left")
label.grid(row=0, column=0)
label.config(padx= 10, pady= 20)

label["text"] = "New Text"

def button_clicked():
    label["text"] = "EXPLOSIONS!?"
    print("EXPLOSIONS!?")

def get_user_text():
    label["text"] = input.get()

button1 = tkinter.Button(text= "Click Me", command= get_user_text)
button1.grid(row=1, column=1)

button2 = tkinter.Button(text= "NO CLICK ME!", command= button_clicked)
button2.grid(row=0, column=2)

input = tkinter.Entry(width= 10)
input.grid(row=2, column=3)


def add(*args):
    for n in args:
        print(n)
    return sum(args)

def calculate(n, **keyword):
    print(type(keyword))

    n += keyword["add"]
    print(n)
    n *= keyword["multiply"]
    print(n)

print(add(2,3,5,1,6,3,7,3))
print(calculate(20, add=3, multiply=5))


class Car:
    def __init__(self, **kw):
        #self.make = kw["make"]
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GTR")
print(my_car.model)