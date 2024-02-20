# Приложение "Решение квадратного уравнения"

# Создайте графическое окно для решения квадратного уравнения.

# Используйте максимально свойства виджетов.

# Проверяйте заполненность всех полей:
# Если поле не заполненно, то после нажатия на кнопку "Решить", должен, например, измениться цвет фона.

# Напишите функции, позволяющие найти решение/я.

# Выведите на экран подробное решение, если они есть и сообщение об их отсутствии, если таковые невозможно найти.

from tkinter import *
from wsgiref import validate

from math import sqrt

aken=Tk()
aken.geometry("600x500")
aken.title("Pealkiri")

aken.iconbitmap("potential.ico")

# f=Frame(aken,bg='lightblue',border=10,height=100,width=600)
l=Label(text="Решение квадратного уравнения",bg='lightblue',fg='Green',font='Arial 24',height=2,width=30)

# ent=Entry(text="Решение",fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)
btn=Button(text="Решить",fg='black',bg='green',font='Arial 15',width=20,relief=GROOVE)
l2=Label(text="Решение",fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)

# как 




# f.grid(row=0,column=0)


objects=[l,btn,l2]
for i in range(len(objects)):
    objects[i].pack()
aken.mainloop()