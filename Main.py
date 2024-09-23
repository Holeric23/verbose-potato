import tkinter as tk
from tkinter import *
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
        def click(event):
            text = event.widget.cget("text")
            if text == "Русский":
                webbrowser.open('https://forms.gle/oqCfDySvMRcVuqm57', new=2)
            elif text == "English":
                webbrowser.open('https://forms.gle/2J89mQKpFeZH5Mpy8', new=2)
            elif text == "中文":
                webbrowser.open('https://forms.gle/24SQqLGP3vrXqM1R8', new=2)
            elif text == "한국어":
                webbrowser.open('https://forms.gle/t7gtcP6D1qzN7RPW6', new=2)
            elif text == "हिन्दी":
                webbrowser.open('https://forms.gle/foitrVxHPS1PaW3E7', new=2)
            elif text == "Español":
                webbrowser.open('https://forms.gle/LbLhUbWu9HXor7t67', new=2)

        root = tk.Tk()
        root.title("")
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w = w // 2  # середина экрана
        h = h // 2
        w = w - 200  # смещение от середины
        h = h - 200
        root.geometry(f'420x280+{w}+{h}')
        lbl =Label(root, text="Select a language", font=("Arial Bold", 14))
        lbl.grid(column=0, row=0)  
        # Кнопки
        buttons = [
            'Русский', 
            'English', 
            '中文',
            '한국어',
            'हिन्दी',
            'Español'
        ]
        row_val = 2
        col_val = 0
        for button in buttons:
            if button=='Русский' or button=='English' or button=='中文' or button=='한국어' or button == 'हिन्दी' or button == 'Español':
                b = tk.Button(root, text=button, font=('Arial', 18), width=14, height=2)
                b.grid(row=row_val, column=col_val,columnspan=3,padx=2,pady=2)
                b.bind("<Button-1>", click)
                col_val+=2
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        root.mainloop()
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
