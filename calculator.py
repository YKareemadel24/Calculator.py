import tkinter 
from tkinter import *

calculation = ""


def add(operation):
    global calculation
    calculation += str(operation)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear()
        text_result.insert(1.0, "Invalid operation")


def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


root =Tk()
root.title("Calculator")
root.geometry("570x600+100+200")
root.configure(bg="#17161b")
root.resizable(False,False)


text_result = Text(root, height=2, width=25, font=("Arial", 30))
text_result.pack()

Button(root,text="C", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("/")).place(x=150,y=100)
Button(root,text="%", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("%")).place(x=290,y=100)
Button(root,text="*", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("*")).place(x=430,y=100)

Button(root,text="7", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("-")).place(x=430,y=200)

Button(root,text="4", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("+")).place(x=430,y=300)

Button(root,text="1", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("3")).place(x=290,y=400)
Button(root,text="0", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("0")).place(x=10,y=500)

Button(root,text="(", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add("(")).place(x=150,y=500)
Button(root,text=")", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add(")")).place(x=430,y=500)

Button(root,text=".", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=lambda:add(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=1, font=("arial",30,),bd=1,fg="#fff",bg="#2a2d36",command=evaluate).place(x=430,y=400)
root.mainloop()
