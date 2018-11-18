import tkinter as tk


def convert():
    f = float(f1.get())
    c = (f - 32) * 5 / 9
    dis["text"] = str(c)


window = tk.Tk()
window.title("My GUI")
l1 = tk.Label(window, text="Enter Fahrenheit")
l2 = tk.Label(window, text="Celsius Temperature")
dis = tk.Label(window)
f1 = tk.Entry(window)
cbutton = tk.Button(window, text="convert", command=convert)

l1.grid(row=0, column=0)
f1.grid(row=0, column=1)
l2.grid(row=1, column=0)
dis.grid(row=1, column=1)
cbutton.grid(row=2, column=0)

window.mainloop()
