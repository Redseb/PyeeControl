import tkinter
from tkinter.colorchooser import *
from yeelight import Bulb, discover_bulbs
from PIL import Image
import pyautogui

listOfBulbs = []
brightness = 100


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
        bulb.start_music()
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

def updateBrightness(value):
    global brightness
    brightness = value

def setBrightness():
    global brightness
    global listOfBulbs
    global brightnessScale
    for bulb in listOfBulbs:
        bulb.set_brightness(int(brightness))

def averageRGB(image):
    pixels = screen.load()
    width = image.size[0]
    height = image.size[1]
    averageR = 0
    averageG = 0
    averageB = 0

    for i in range(width):
        for j in range(height):
            averageR += pixels[i,j][0]
            averageG += pixels[i,j][1]
            averageB += pixels[i,j][2]
    area = width * height
    averageR = averageR / area
    averageG = averageG / area
    averageB = averageB / area

    return averageR, averageG, averageB
    

#Building Tkinter window
window = tkinter.Tk()
window.title("PyeeControl")
matchScreen = tkinter.IntVar()

top_frame = tkinter.Frame(window, background = "blue").pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

label = tkinter.Label(window, text = "Welcome to PyeeControl").pack()

searchBtn = tkinter.Button(top_frame, text = "Search for Bulbs", command = searchForBulbsGUI).pack()
toggleBtn = tkinter.Button(top_frame, text = "Toggle All", command = toggleAll).pack()
colorBtn = tkinter.Button(top_frame, text = "Change Color", command = changeColor).pack()
brightnessScale = tkinter.Scale(top_frame, from_=0, to=100, orient = tkinter.HORIZONTAL, command = updateBrightness).pack()
setBrightness = tkinter.Button(top_frame, text = "Set Brightness", command = setBrightness).pack()
matchScreenBox = tkinter.Checkbutton(top_frame, text = "Match Screen", variable = matchScreen).pack()


#Main program loop, cupdate tkinter window and check for matchScreen

while(True):
    window.update_idletasks()
    window.update()
    if matchScreen.get() == 1:
        screen = pyautogui.screenshot()
        rgb = averageRGB(screen)
        for bulb in listOfBulbs:
            if bulb.get_properties().get('music_on') == 0:
                bulb.start_music()
            bulb.set_rgb(int(rgb[0]), int(rgb[1]), int(rgb[2]))