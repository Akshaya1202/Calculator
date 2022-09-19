from tkinter import*
root = Tk()
root.geometry('326x225')
root.title("My Calculator")
root.resizable(0,0)

def clickkk(item):
    global expression
    expression = expression + str(item)
    inputtext.set(expression)

def clearrr():
    global expression
    expression = ""
    inputtext.set("")

def equalll():
    global expression
    result = str(eval(expression))
    inputtext.set(result)
    expression = ""
expression = ""

inputtext = StringVar()
inputfield = Entry(root,text=inputtext,width=53)
inputfield.grid(row=0,column=0,columnspan=4)

#display = Entry(easy,text='',width=53).grid(row=0,column=0,columnspan=4)
clear = Button(root,text='C',width=33,height=2,command=lambda:clearrr()).grid(row=1,column=0,columnspan=3)
slash = Button(root,text=('/'),width=10,height=2,command=lambda:clickkk("/")).grid(row=1,column=3)

seven = Button(root,text=('7'),width=10,height=2,command=lambda:clickkk("7")).grid(row=2,column=0)
eight = Button(root,text=('8'),width=10,height=2,command=lambda:clickkk("8")).grid(row=2,column=1)
nine = Button(root,text=('9'),width=10,height=2,command=lambda:clickkk("6")).grid(row=2,column=2)
mul = Button(root,text=('*'),width=10,height=2,command=lambda:clickkk("*")).grid(row=2,column=3)

four = Button(root,text=('4'),width=10,height=2,command=lambda:clickkk("4")).grid(row=3,column=0)
five = Button(root,text=('5'),width=10,height=2,command=lambda:clickkk("5")).grid(row=3,column=1)
six = Button(root,text=('6'),width=10,height=2,command=lambda:clickkk("6")).grid(row=3,column=2)
sub = Button(root,text=('-'),width=10,height=2,command=lambda:clickkk("-")).grid(row=3,column=3)

one = Button(root,text=('1'),width=10,height=2,command=lambda:clickkk("1")).grid(row=4,column=0)
two = Button(root,text=('2'),width=10,height=2,command=lambda:clickkk("2")).grid(row=4,column=1)
three = Button(root,text=('3'),width=10,height=2,command=lambda:clickkk("3")).grid(row=4,column=2)
add = Button(root,text=('+'),width=10,height=2,command=lambda:clickkk("+")).grid(row=4,column=3)

zero = Button(root,text=('0'),width=22,height=2,command=lambda:clickkk("0")).grid(row=5,column=0,columnspan=2)
dot = Button(root,text=('.'),width=10,height=2,command=lambda:clickkk(".")).grid(row=5,column=2)
equal = Button(root,text=('='),width=10,height=2,command=lambda:equalll()).grid(row=5,column=3)

root.mainloop()

