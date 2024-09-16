import tkinter as tk
import math
import webbrowser

def click(event):
    text = event.widget.cget("text")
    if text == "√":
#Тут код самого вычисления
        try:
            inp=entry.get()
            inp=inp.replace(',','.')
            number = float(inp)
            result = math.sqrt(number)
            entry.delete(0, tk.END)
            entry.insert(tk.END, format(result,".17g"))
        except ValueError:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "SOS":
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)
    else:
        entry.insert(tk.END, text)


# Создание основного окна
root = tk.Tk()
root.title("")
# Поле ввода
entry = tk.Entry(root, width=22, font=('Arial', 22), borderwidth=2, relief="solid")
entry.grid(row=0, column=0,columnspan=6,rowspan=1)

# Кнопки
buttons = [
    '√','SOS',
    '7', '8', '9','+',
    '4', '5', '6','-',
    '1', '2', '3',',',
    '0','i'
]

row_val = 2
col_val = 0

for button in buttons:
    if button=='SOS':
        b = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2, fg="red")
        b.grid(row=row_val, column=col_val,columnspan=1,padx=2,pady=2)
        b.bind("<Button-1>", click)

    elif button=='√' or button=='0':
        b = tk.Button(root, text=button, font=('Arial', 18), width=14, height=2)
        b.grid(row=row_val, column=col_val,columnspan=3,padx=2,pady=2)
        b.bind("<Button-1>", click)
        col_val+=2

    else:
        b = tk.Button(root, text=button, font=('Arial', 18), width=4, height=2)
        b.grid(row=row_val, column=col_val,padx=2,pady=2)
        b.bind("<Button-1>", click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

bc=tk.Button(root, text="C", font=('Arial', 18), width=4, height=14)
bc.grid(column=5, row=1,rowspan=6,padx=2,pady=2)
bc.bind("<Button-1>", click)


root.mainloop()
