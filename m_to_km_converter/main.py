from tkinter import *

def mtokm():
    inp = float(entry.get())
    km_answer.config(text=str(round(inp*1.609344)))


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

window.minsize(width = 200, height = 100)

miles = Label(text="Miles")
miles.grid(column = 3, row= 0)

entry = Entry(width=5)
entry.grid(column=2, row=0)

equalto = Label(text="is equal to")
equalto.grid(column=1, row=1)

km_answer = Label(text="0")
km_answer.grid(column=2, row=1)

km = Label(text="Km")
km.grid(column=3, row=1)

calculate = Button(text="Calculate", command=mtokm)
calculate.grid(column=2, row=2)


window.mainloop()