import tkinter as tk

def convert_weight():
    kilogram=int(e1.get())
    grams=kilogram*1000
    l3.config(text=str(grams)  +' grams')
    pounds=kilogram*2.5
    l4.config(text=str(pounds) +' pounds')
    ounces=kilogram*35
    l5.config(text=str(ounces)+'  ounces')
 
screen=tk.Tk()
screen.configure(bg='blue')
screen.geometry('600x600')
screen.title("weight conventor")
l1=tk.Label (text='weight convertor',bg='red',fg="green",width=20,height=2)
l1.place(x=100,y=50)
l2=tk.Label (text='enter your weight in kgs',bg="yellow",fg="pink",width=20,height=1)
l2.place(x=50,y=100)
e1=tk.Entry(width=20,bg='white',fg='black')
e1.place(x=250,y=100)
l3=tk.Label (text='weight in grams ',bg="red",fg="blue",width=20,height=2)
l3.place(x=10,y=150)
l4=tk.Label (text='weight in pounds',bg="green",fg="pink",width=20,height=2)
l4.place(x=200,y=150)
b1=tk.Button(text='convert',bg='white',fg='blue',width=10,height=1,command=convert_weight)
b1.place(x=200,y=250)
l5=tk.Label (text=' weight in ounces',bg='yellow',fg='pink',width=20,height=2)
l5.place(x=400,y=150)
