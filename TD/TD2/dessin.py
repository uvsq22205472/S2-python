import tkinter as tk
from random import randint

ROOT = tk.Tk()
ROOT.title("Mon dessin")

Canvas_Height = 500
Canvas_Width = 500
Canvas = tk.Canvas(ROOT,bg="black",height=Canvas_Height,width=Canvas_Width)
ChosenColor = "blue"

def RandomizeCoordinates():
    global x,y
    x,y = randint(0,Canvas_Width-50),randint(0,Canvas_Height-50)
    return x,y

def CreateRandomCircleInSpace():
    RandomizeCoordinates()
    Canvas.create_oval((x,y),(x+50,y+50),fill="blue",width=2)

Button1 = tk.Button(ROOT,text="Choisir une couleur", font=("helvetica", "12"), relief="groove")
Button1.grid(column=6,row=0)

Button2 = tk.Button(ROOT,text="Cercle", font=("helvetica", "12"), relief="groove",command=CreateRandomCircleInSpace)
Button2.grid(column=0,row=3,rowspan=3)

def CreateRandomSquareInSpace():
    RandomizeCoordinates()
    Canvas.create_rectangle((x,y),(x+50,y+50),fill="blue",width=2)

Button3 = tk.Button(ROOT,text="Carré", font=("helvetica", "12"), relief="groove", command=CreateRandomSquareInSpace)
Button3.grid(column=0,row=9,rowspan=3)

def CreateRandomCrossInSpace():
    RandomizeCoordinates()
    Canvas.create_rectangle((x,y),(x+50,y+50),width=1,outline="green")
    Canvas.create_line((x,y),(x+50,y+50),width=3,fill="yellow")
    Canvas.create_line((x+50,y),(x,y+50),width=3,fill="yellow")
Button4 = tk.Button(ROOT,text="Croix", font=("helvetica", "12"), relief="groove", command=CreateRandomCrossInSpace)
Button4.grid(column=0,row=16,rowspan=3)

Canvas.grid(column=1,row=1,columnspan=20,rowspan=20)
ROOT.mainloop()