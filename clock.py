import tkinter as tk
import datetime
def show_time():
    x=datetime.datetime.now()
    a=x.strftime('%H:%M:%S')
   
    l2.config(text=a)
    l2.after(1000,show_time)


def show_date():
    x=datetime.datetime.now()
    b=x.strftime('%Y/%m/%d')
    l3.config(text=b)
    







screen=tk.Tk()
screen.title('clock')
screen.configure(bg='blue')
screen.geometry('600x600')
l1=tk.Label( text='digtal clock',bg='red', fg='green',width=20,height=2)
l1.place(x=100,y=50)
b1=tk.Button(text='show time',bg='white',fg='blue',height=1,width=20,command=show_time)
b1.place(x=100,y=100)
l2=tk.Label(width=20,height=2,bg='red',fg='blue')
l2.place(x=100,y=150)
b2=tk.Button(text='show date ',bg='white',fg='blue',height=1,width=20,command=show_date)
b2.place(x=100,y=200)
l3=tk.Label(width=20,height=2,bg='red',fg='blue')
l3.place(x=100,y=250)
