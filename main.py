"""
Created on Sun Mar  5 16:05:59 2023

@author: saketh
"""
from tkinter import *

root = Tk()
e = Entry(root, borderwidth=5, font=('Arial 13', 15))
e.grid(row=0, columnspan=4)
global math
math = 'num'


def bottom_click(num):
    c = e.get()
    e.delete(0, END)
    return e.insert(0, c + str(num))


def bottom_clear():
    e.delete(0, END)
    e.config(background='white')


def bottom_add():
    global math
    math = 'add'
    global num1
    num = e.get()
    num1 = int(num)
    bottom_clear()


def bottom_sub():
    global math
    math = 'sub'
    global num1
    num1 = int(e.get())
    bottom_clear()


def bottom_mul():
    global math
    math = 'mul'
    global num1
    num1 = int(e.get())
    bottom_clear()


def bottom_div():
    global math
    math = 'div'
    global num1
    num1 = int(e.get())
    bottom_clear()


def bottom_power():
    global math
    math = 'power'
    global num1
    num1 = int(e.get())
    bottom_clear()


def bottom_equall():
    if math == 'add':
        num = (e.get())
        num2 = int(num)
        s = num1 + num2
        bottom_clear()
        e.insert(0, str(s))
    if math == 'sub':
        num = (e.get())
        num2 = int(num)
        s = num1 - num2
        bottom_clear()
        e.insert(0, s)
    if math == 'mul':
        num2 = int(e.get())
        s = num1 * num2
        bottom_clear()
        e.insert(0, str(s))

    if math == 'div':
        num2 = int(e.get())
        if num2 == 0:
            e.insert(0, ' error ')
            e.config(background='red')

        else:
            s = num1 / num2
            bottom_clear()
            e.insert(0, str(s))

    if math == 'power':
        num2 = int(e.get())
        s = num1 ** num2
        bottom_clear()
        e.insert(0, str(s))


b1 = Button(root, text="1", command=lambda: bottom_click(1), padx=20, pady=20)
b2 = Button(root, text="2", command=lambda: bottom_click(2), padx=20, pady=20)
b3 = Button(root, text="3", command=lambda: bottom_click(3), padx=20, pady=20)
b4 = Button(root, text="4", command=lambda: bottom_click(4), padx=20, pady=20)
b5 = Button(root, text="5", command=lambda: bottom_click(5), padx=20, pady=20)
b6 = Button(root, text="6", command=lambda: bottom_click(6), padx=20, pady=20)
b7 = Button(root, text="7", command=lambda: bottom_click(7), padx=20, pady=20)
b8 = Button(root, text="8", command=lambda: bottom_click(8), padx=20, pady=20)
b9 = Button(root, text="9", command=lambda: bottom_click(9), padx=20, pady=20)
b0 = Button(root, text="0", command=lambda: bottom_click(0), padx=50, pady=20)
badd = Button(root, text="+", command=bottom_add, padx=30, pady=20)
bsub = Button(root, text="-", command=bottom_sub, padx=20, pady=20)
bmul = Button(root, text="*", command=bottom_mul, padx=20, pady=20)
bdiv = Button(root, text="/", command=bottom_div, padx=20, pady=20)
bpower = Button(root, text="^", command=bottom_power, padx=30, pady=20)
bclear = Button(root, text="clear", command=bottom_clear, padx=10, pady=20)
bequall = Button(root, text="=", command=bottom_equall, padx=30, pady=55)
bexit = Button(root, text="off", command=root.quit, padx=25, pady=20)

b1.grid(row=4, column=0)
b2.grid(row=4, column=1)
b3.grid(row=4, column=2)
b4.grid(row=3, column=0)
b5.grid(row=3, column=1)
b6.grid(row=3, column=2)
b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)
b0.grid(row=5, column=0, columnspan=2)
badd.grid(row=2, column=3)
bclear.grid(row=5, column=2)
bequall.grid(row=4, column=3, rowspan=2)
bsub.grid(row=1, column=0)
bdiv.grid(row=1, column=1)
bmul.grid(row=1, column=2)
bpower.grid(row=3, column=3)
bexit.grid(row=1, column=3)
root.mainloop()
