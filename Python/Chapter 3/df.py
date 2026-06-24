from tkinter import *
top=Tk()
top.title("main")
top.geometry('800x800')

n1=Label(top,text="Name").grid(row=0,column=0)
t1=Entry(top).grid(row=0, column=1)


n2=Label(top,text="Address").grid(row=1,column=0)
t2=Entry(top).grid(row=1, column=1)
btn=Button(top, text="Save").grid(row=2,column=0)