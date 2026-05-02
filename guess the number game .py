import tkinter as tk
from tkinter import messagebox
def show_message():
    messagebox.showinfo('heading','message')




















screen=tk.Tk()
screen.configure(bg='green')
screen.title('guess the number game ✌️')
screen.geometry('700x700')
l1=tk.Label(text='welcometo number guessing game',bg='red',fg='green',width=30,height=2)
l1.place(x=200,y=50)
l2=tk.Label(text='guess the number 1 to 20',bg='yellow',fg='red',width=30,height=2)
l2.place(x=50,y=100)
e1=tk.Entry(width=20,bg='white',fg='blue')
e1.place(x=400,y=100)
b1=tk.Button(text='submit',bg='red',fg='blue',width=15,height=2,command=show_message)
b1.place(x=300,y=150)
