from tkinter import *
from tkinter import messagebox

window = Tk()
window.title('Temperature Convertor')
window.minsize(width=300, height=250)
window.config(bg="black")
celcius_var= IntVar
fahrenheit_var =IntVar


l1=LabelFrame(window,text='Celcius To Fahrenheit',bg="red", fg="Black", borderwidth=3, font=("Sans-serif 15"), padx=10, pady=5)
l1.grid(row=2, column=0)
E1=Entry(l1,state='disable')
E1.grid(row=4, column=0)

#Activates celcuis to fahrenheit
def Cel_Active():
    E2.configure(state='disable')
    E1.configure(state='normal')

btn_active=Button(window,text='Convert -Celcius to Fahrenheit', bg="red", fg="Black", borderwidth=3, font=("Sans-serif 15"), command=Cel_Active)
btn_active.grid(row=6, column=0)

l2=LabelFrame(window, text='Fahrenheit to Celcius', bg="blue", fg="white", borderwidth=3, font=("Sans-serif 15"), padx=10, pady=5)
l2.grid(row=2, column=5)
E2=Entry(l2,state='disable')
E2.grid(row=4, column=5)

#Activates Fahrenheit to Celcuis
def Far_Active():
    E1.configure(state='disable')
    E2.configure(state='normal')
btn_active1=Button(window,text='Convert -Fahrenheit to Celcius', bg="blue", fg="white", borderwidth=3, font=("Sans-serif 15"), command=Far_Active)
btn_active1.grid(row=6, column=5)


#exits
def exit():
    window.destroy()


exit_btn = Button(text = "Quit",bg="blue", fg="white", borderwidth=3, font=("Serif 15 bold"), command=exit)
exit_btn.place(x=700, y=200, height=50, width=80)
#Converts Celcuis to Fahrenheit
def convert_C():
    if E1:
        try:
            celcius = float(E1.get())
            fahrenheit = (celcius*9/5)+32
            result_entry.insert(0, str(fahrenheit))
        except:
            messagebox.showinfo("ERROR", "Please insert correct data values")
            E1.delete(0, END)
#Converts Fahrenheit to Celcuis
def convert_f():
    if E2:
        try:
            fahrenheit = float(E2.get())
            celcius = (fahrenheit-32)*5/9
            result_entry.insert(0, str(round(celcius,1)))
        except:
            messagebox.showinfo("ERROR", "Please insert correct data values")
            E2.delete(0, END)
#Covert button left
result_bnt=Button(window, text='Convert C-F', bg="red", fg="Black", borderwidth=3, font=("Serif 15"), command=convert_C)
result_bnt.grid(row=7, column=1)
#Convert button right
result_bnt2=Button(window, text='Convert F-C',bg="blue", fg="white", borderwidth=3, font=("Serif 15"), command=convert_f)
result_bnt2.grid(row=7, column=4)


#Answer
result_entry=Entry(window, bg='purple', fg='white')
result_entry.grid(row=8, column=2)

#Clears info
def Clear():
    E1.configure(state="disable")
    E2.configure(state="disable")
    E1.delete(0, END)
    E2.delete(0, END)
    result_entry.delete(0,END)
#Clears info
Clear_btn=Button(window, text='Clear', bg="red", fg="Black", borderwidth=3, font=("Serif 15 bold"), command=Clear)
Clear_btn.place(x=400, y=200, height=50, width=80)

window.mainloop()
