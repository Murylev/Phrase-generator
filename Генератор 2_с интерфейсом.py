from tkinter import *
import random

win=Tk()
win.title("Предсказатель")
win.geometry("500x500")

w1=("хороший ","глупый ","спящий ","гениальный ","деревянный ")
w2=("слон ","бомж ","порося ","слесарь ","птушник ")
w3=("в столовой","под мостом","в туалете","в ванной")

def cl():
    wr1=random.choice(w1)
    wr2=random.choice(w2)
    wr3=random.choice(w3)
    wr4=wr1+wr2+wr3
    a2.configure(text=wr4)
    
def cl2():
    a2.configure(text="П***** ответ!")
    

a1=Label(win, text="Привет!", font=("Comic",15))
a1.grid(column=0,row=0)

a2=Label(win, text="Хочешь узнать кто ты сегодня?", font=("Comic",15))
a2.grid(column=0,row=1)
b1=Button(win, text="ДА", bg="blue", fg="gold", command=cl)
b1.grid(column=0,row=3, sticky = W)
b2=Button(win, text="НЕТ", bg="blue", fg="silver", command=cl2)
b2.grid(column=0,row=3, sticky = E)



win.mainloop()
