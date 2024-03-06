# Приложение "Решение квадратного уравнения"

# Создайте графическое окно для решения квадратного уравнения.

# Используйте максимально свойства виджетов.

# Проверяйте заполненность всех полей:
# Если поле не заполненно, то после нажатия на кнопку "Решить", должен, например, измениться цвет фона.

# Напишите функции, позволяющие найти решение/я.

# Выведите на экран подробное решение, если они есть и сообщение об их отсутствии, если таковые невозможно найти.

#a*x^2+b*x+c=0




from tkinter import *
from math import sqrt

aken = Tk()
aken.geometry("600x500")
aken.title("Pealkiri")

l = Label(text="Решение квадратного уравнения", bg='lightblue', fg='Green', font='Arial 24', height=2, width=30)
l.pack()

# Создаем фрейм для размещения полей ввода коэффициентов
coeff_frame = Frame(aken, bg='yellow')
coeff_frame.pack()



ent = Entry(coeff_frame, fg='black', font='Arial 15', width=6, relief=GROOVE)
ent.pack(side=LEFT, padx=5)

l1= Label(coeff_frame, text="Х**2+", fg='Green', font='Arial 15', width=5, relief=GROOVE)
l1.pack(side=LEFT, padx=5)

ent2 = Entry(coeff_frame, fg='black', font='Arial 15', width=6, relief=GROOVE)
ent2.pack(side=LEFT, padx=5)

l2= Label(coeff_frame, text="Х+", fg='Green', font='Arial 15', width=5, relief=GROOVE)
l2.pack(side=LEFT, padx=5)

ent3 = Entry(coeff_frame, fg='black', font='Arial 15', width=6, relief=GROOVE)
ent3.pack(side=LEFT, padx=5)

l3= Label(coeff_frame, text="=0", fg='Green', font='Arial 15', width=5, relief=GROOVE)
l3.pack(side=LEFT, padx=5)

btn = Button(coeff_frame, text="Решить", fg='black', bg='green', font='Arial 15', width=10, relief=GROOVE)
btn.pack(side=LEFT, padx=5)

l2_res = Label(text="Решение", fg='black', bg='yellow', font='Arial 15', width=30, relief=GROOVE, height=5)
l2_res.pack()



def solve(a, b, c):
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        return "Не имеет корней"

def on_click():
    a = ent.get()
    b = ent2.get()
    c = ent3.get()

    if a == "":
        ent.config(bg='red')
    else:
        ent.config(bg='white')
        
    if b == "":
        ent2.config(bg='red')
    else:
        ent2.config(bg='white')
        
    if c == "":
        ent3.config(bg='red')
    else:
        ent3.config(bg='white')

    if a != "" and b != "" and c != "":
        a = int(a)
        b = int(b)
        c = int(c)
        res = solve(a, b, c)
        discriminant = b ** 2 - 4 * a * c

        if isinstance(res, tuple):
            res_text = "\n".join([f"X {i + 1}: {round(root, 2)}" for i, root in enumerate(res)])
            l2_res.config(text=f"Корни:\n{res_text}\nD: {round(discriminant, 2)}")
        elif isinstance(res, (int, float)):
            l2_res.config(text=f"Уравнение имеет один корень: {round(res, 2)}\nD: {round(discriminant, 2)}")
        else:
            l2_res.config(text=f"{res}\nD: {round(discriminant, 2)}")



btn.config(command=on_click)
btn.pack()

aken.mainloop()