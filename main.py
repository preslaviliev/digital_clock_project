from tkinter import *
import time
root=Tk()
root.title("Digital Clock")
root.geometry("1200x600+0+0")
root.config(bg="#081923")

def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    hour.config(text=h)
    minutes.config(text=m)
    seconds.config(text=s)
    hour.after(200,clock)
    print(h,m,s)


hour = Label(root,text="12", font=("times new roman",50,"bold"),bg="#5D3F6A",fg="white")
hour.place(x=350,y=200, width=150, height=150)
hour_label = Label(root,text="hour", font=("times new roman",20,"bold"),bg="#5D3F6A",fg="white")
hour_label.place(x=350,y=360, width=150, height=50)

minutes = Label(root,text="24", font=("times new roman",50,"bold"),bg="#5D3F6A",fg="white")
minutes.place(x=520,y=200, width=150, height=150)
minutes_label = Label(root,text="minutes", font=("times new roman",20,"bold"),bg="#5D3F6A",fg="white")
minutes_label.place(x=520,y=360, width=150, height=50)


seconds = Label(root,text="24", font=("times new roman",50,"bold"),bg="#8F1D21",fg="white")
seconds.place(x=690,y=200, width=150, height=150)
seconds_label = Label(root,text="seconds", font=("times new roman",20,"bold"),bg="#8F1D21",fg="white")
seconds_label.place(x=690,y=360, width=150, height=50)

clock()
root.mainloop()