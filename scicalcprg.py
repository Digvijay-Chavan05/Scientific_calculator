import tkinter as tk                                                 #tkinter is a python library used for creating graphical user interface
import tkinter.messagebox                                  #<-- this is used to provide different set of dialogues that are used to display message boxes,showing errors or warnings
from tkinter.constants import SUNKEN          #SUNKEN is a constant used for the appearance of the text entry box
import math                                                              #math module is python library which provides std mathematical constants and functions

window = tk.Tk()                                                    #<-- Initialization of main window
window.title('Scientific Calculator')                 #<-- Sets the window title
frame = tk.Frame(master=window, bg="#f0f0f0", padx=10)    #<--Sets a frame within the window
frame.pack()                                                                                            #<-- Places the frame within the window
entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=5, width=50)         #<-- Creates text entry widgets where the user can enter the widgets
                                                                                                                                                              #^--relief=SUNKEN gives entry a sunken appearance
entry.grid(row=0, column=0, columnspan=3, ipady=25, pady=2)                   #<--places the entry widget according to specified location

#Defineing some functions to add in the calculator

def myclick(number):                                              #This will enter the clicked number or operator in the entry field
	entry.insert(tk.END, number)            #tk.END specifies that the number should be inserted at the end of current content
	


def equal():                                                                             #This function will evaluate the expression entered
	try:
		y = str(eval(entry.get()))          #eval(entry(entry.get())) evaluates the string expression
		entry.delete(0, tk.END)
		entry.insert(0, y)
	except:
		tkinter.messagebox.showinfo("Error", "Syntax Error")        #if there will be any kind of invalid expression an error will be displayed using this code of line


def clear():                                                    #This function will be clearing all the entered expression
	entry.delete(0, tk.END)

def delete_digit():                                               #This function will be deleting the last entered number/operator . will work as a backspace button
    current=entry.get()
    if len(current)>0:
        entry.delete(len(current)-1,tk.END)
	
#Creating the buttons of calculator using the tkinter 


#Creating the DIGITS
button_7= tk.Button(master=frame, text='7',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(7))
button_7.grid(row=2, column=0, pady=2)

button_8= tk.Button(master=frame, text='8',bg="light blue",padx=20,pady=20, width=5, command=lambda: myclick(8))
button_8.grid(row=2, column=1, pady=2)

button_9 = tk.Button(master=frame, text='9',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(9))
button_9.grid(row=2, column=2, pady=2)

button_4 = tk.Button(master=frame, text='4',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(4))
button_4.grid(row=3, column=0, pady=2)

button_5 = tk.Button(master=frame, text='5',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(5))
button_5.grid(row=3, column=1, pady=2)

button_6 = tk.Button(master=frame, text='6',bg="light blue",padx=20,pady=20, width=5, command=lambda: myclick(6))
button_6.grid(row=3, column=2, pady=2)

button_1 = tk.Button(master=frame, text='1',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(1))
button_1.grid(row=4, column=0, pady=2)

button_2 = tk.Button(master=frame, text='2',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(2))
button_2.grid(row=4, column=1, pady=2)

button_3 = tk.Button(master=frame, text='3',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(3))
button_3.grid(row=4, column=2, pady=2)

button_0 = tk.Button(master=frame, text='0',bg="light blue", padx=20,pady=20, width=5, command=lambda: myclick(0))
button_0.grid(row=5, column=1, pady=2)

#POINT button
button_dot=tk.Button(master=frame,text=".",bg="light blue",padx=20,pady=20,width=5,command=lambda:myclick("."))
button_dot.grid(row=5,column=2,pady=2)
#DOUBLE ZERO button
button_doublezero=tk.Button(master=frame,text="00",bg="light blue",padx=20,pady=20,width=5,command=lambda:myclick(00))
button_doublezero.grid(row=5,column=0,pady=2)
#ADDITION button
button_add = tk.Button(master=frame,bg="orange", text="+", padx=20,pady=20, width=5, command=lambda: myclick('+'))
button_add.grid(row=4, column=3, pady=2)
#SUBSTRACTION button
button_subtract = tk.Button(master=frame,bg="orange", text="-", padx=20, pady=20, width=5, command=lambda: myclick('-'))
button_subtract.grid(row=3, column=3, pady=2)
#MULTIPLICATION button
button_multiply = tk.Button(master=frame,bg="orange", text="x", padx=20, pady=20, width=5, command=lambda: myclick('*'))
button_multiply.grid(row=2, column=3, pady=2)
#DIVISION button
button_div = tk.Button(master=frame,bg="orange", text="÷", padx=20,pady=20, width=5, command=lambda: myclick('/'))
button_div.grid(row=1, column=3, pady=2)
#CLEAR button
button_clear = tk.Button(master=frame,bg="Dark orange", text="C",padx=20, pady=20, width=5, command=clear)
button_clear.grid(row=1, column=1,  pady=2)
#EQUAL button
button_equal = tk.Button(master=frame,bg="dark green", text="=", padx=20,pady=20, width=5, command=equal)
button_equal.grid(row=5, column=3, pady=2)
#MODULO button
button_modulo=tk.Button(master=frame,bg="orange",text="%",padx=20,pady=20,width=5,command=lambda:myclick("%"))
button_modulo.grid(row=1,column=2,pady=2)
#BACKSPACE button
button_oneback=tk.Button(master=frame,bg="dark orange",text="⌫",padx=20,pady=20,width=5,command=delete_digit)
button_oneback.grid(row=1,column=0,pady=2)

#CREATING TRIGNOMETRIC BUTTONS
def trig_func(func):
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        if func == "sin":
            entry.insert(0, str(math.sin(math.radians(x))))  # radians to degrees
        elif func == "cos":
            entry.insert(0, str(math.cos(math.radians(x))))
        elif func == "tan":
            entry.insert(0, str(math.tan(math.radians(x))))
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
        
button_sin = tk.Button(master=frame, text="sin",bg="turquoise", padx=20, pady=20, width=5, command=lambda: trig_func("sin"))
button_sin.grid(row=2, column=4, pady=2)
button_cos = tk.Button(master=frame, text="cos",bg="turquoise", padx=20, pady=20, width=5, command=lambda: trig_func("cos"))
button_cos.grid(row=3, column=4, pady=2)
button_tan = tk.Button(master=frame, text="tan",bg="turquoise",  padx=20, pady=20, width=5, command=lambda: trig_func("tan"))
button_tan.grid(row=4, column=4, pady=2)
#CREATING LOGARITHIC BUTTON
def log_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.log10(x)))  # log base 10
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
        
button_log = tk.Button(master=frame, text="log",bg="turquoise",  padx=20, pady=20, width=5, command=log_func)
button_log.grid(row=1, column=4, pady=2)

#CREATING EXPONENT BUTTONS
def exp_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.exp(x)))  # e^x
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

button_exp = tk.Button(master=frame, text="exp",bg="turquoise",  padx=20, pady=20, width=5, command=exp_func)
button_exp.grid(row=5, column=4, pady=2)

#CREATING SQUARE ROOT BUTTON
def sqrt_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.sqrt(x)))
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
        
button_sqrt = tk.Button(master=frame, text="√",bg="turquoise", padx=20, pady=20, width=5, command=sqrt_func)
button_sqrt.grid(row=1, column=5, pady=2)

#CREATING  FACTORIAL BUTTON
def factorial_func():
    try:
        x = int(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.factorial(x)))
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")

button_factorial = tk.Button(master=frame, text="n!",bg="turquoise",  padx=20, pady=20,width=5, command=factorial_func)
button_factorial.grid(row=2, column=5,pady=2)

#CREATING SQUARE BUTTON
def square_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(x**2))
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
button_square = tk.Button(master=frame, text="x²",bg="turquoise",  padx=20, pady=20,width=5, command=square_func)
button_square.grid(row=3, column=5,pady=2)

#CREATING CUBE BUTTON
def cube_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(x**3))
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
button_cube = tk.Button(master=frame, text="x³",bg="turquoise",  padx=20, pady=20,width=5 ,command=cube_func)
button_cube.grid(row=4, column=5,pady=2)

#CREATING BRACKET BUTTONS

def open_bracket_func():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + "(")

def close_bracket_func():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + ")")
    
button_open_bracket = tk.Button(master=frame, text="(", bg="turquoise", padx=20, pady=20, width=5,command=open_bracket_func)
button_close_bracket = tk.Button(master=frame, text=")",bg="turquoise",  padx=20, pady=20,width=5, command=close_bracket_func)
button_open_bracket.grid(row=5, column=5,pady=2)
button_close_bracket.grid(row=5, column=6,pady=2)

#CREATING INVERSE  BUTTON
def inverse_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(1/x))
    except ZeroDivisionError:
        tkinter.messagebox.showinfo("Error", "Cannot divide by zero")
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
button_inverse = tk.Button(master=frame, text="1/x", bg="turquoise", padx=20, pady=20,width=5, command=inverse_func)
button_inverse.grid(row=4, column=6,pady=5)

#CREATING A PIE BUTTON
def pi_func():
    entry.insert(tk.END, str(math.pi))
button_pi = tk.Button(master=frame, text="π",bg="turquoise",  padx=20, pady=20,width=5, command=pi_func)
button_pi.grid(row=3,column=6,pady=2)

#CREATE A POWER  RAISE TO BUTTON
def power_func():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + "**")
button_power = tk.Button(master=frame, text="x^y",bg="turquoise",  padx=20, pady=20, width=5,command=power_func)
button_power.grid(row=2,column=6,pady=2)

#CREATING A LN BUTTON
def ln_func():
    try:
        x = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(math.log(x)))
    except:
        tkinter.messagebox.showinfo("Error", "Invalid Input")
button_ln = tk.Button(master=frame, text="ln",bg="turquoise",  padx=20, pady=20, width=5,command=ln_func)
button_ln.grid(row=1,column=6,pady=2)



        

window.mainloop()    #It keeps the application running and waits for the user interaction

