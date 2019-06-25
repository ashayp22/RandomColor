import random
import tkinter as tk

def randomRGB():
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    color = ""
    for i in range(6):
        color += numbers[random.randint(0, 15)]
    return color


#window
root = tk.Tk()

root.geometry("140x140")

#create canvas
canvas = tk.Canvas(root, width=140, height=140)
canvas.pack()
canvas.old_coords = None
canvas.create_rectangle(0, 0, 140, 140, fil="#" + randomRGB())

root.mainloop() #loop, no code after gets run


