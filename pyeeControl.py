import tkinter
from tkinter.colorchooser import *
from yeelight import Bulb
from yeelight import discover_bulbs

listOfBulbs = []

def searchForBulbs():
    global listOfBulbs
    listOfBulbs = []
    results = discover_bulbs()
    for bulb in results:
        listOfBulbs.append(Bulb(bulb.get("ip")))
    return listOfBulbs

def searchForBulbsGUI():
    global listOfBulbs
    listOfBulbs = searchForBulbs()
    for bulb in listOfBulbs:
        tkinter.Label(bottom_frame, text = str(bulb)).pack()

def toggleAll():
    global listOfBulbs
    for bulb in listOfBulbs:
        bulb.toggle()

def changeColor():
    global listOfBulbs
    color = askcolor()
    rgb = color[0]
    hexVal = color[1]
    for bulb in listOfBulbs:
        bulb.set_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2]))
    window.configure(background=hexVal)
    


window = tkinter.Tk()
window.title("PyeeControl")

top_frame = tkinter.Frame(window, background = "blue").pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

label = tkinter.Label(window, text = "Welcome to PyeeControl").pack()

searchBtn = tkinter.Button(top_frame, text = "Search for Bulbs", command = searchForBulbsGUI).pack()
toggleBtn = tkinter.Button(top_frame, text = "Toggle All", command = toggleAll).pack()
colorBtn = tkinter.Button(top_frame, text = "Change Color", command = changeColor).pack()
# # btn4 = tkinter.Button(bottom_frame, text = "button4", fg = "orange").pack(side = "left")

# tkinter.Label(window, text = "Suf. width", fg = "white", bg = "purple").pack()
# tkinter.Label(window, text = "Taking all available X width", fg = "white", bg = "green").pack(fill = "x")
# tkinter.Label(window, text = "Taking all available Y height", fg = "white", bg = "black").pack(side = "left", fill = "y")


window.mainloop()


# listOfBulbs = searchForBulbs()
# print(listOfBulbs)
# for bulb in listOfBulbs:
#     bulb = Bulb(bulb)
#     bulb.turn_on()