# Приложение "Решение квадратного уравнения"

# Создайте графическое окно для решения квадратного уравнения.

# Используйте максимально свойства виджетов.

# Проверяйте заполненность всех полей:
# Если поле не заполненно, то после нажатия на кнопку "Решить", должен, например, измениться цвет фона.

# Напишите функции, позволяющие найти решение/я.

# Выведите на экран подробное решение, если они есть и сообщение об их отсутствии, если таковые невозможно найти.

#a*x^2+b*x+c=0

# from tkinter import *
# from wsgiref import validate

# from math import sqrt

# aken=Tk()
# aken.geometry("600x500")
# aken.title("Pealkiri")

# aken.iconbitmap("potential.ico")

# # f=Frame(aken,bg='lightblue',border=10,height=100,width=600)
# l=Label(text="Решение квадратного уравнения",bg='lightblue',fg='Green',font='Arial 24',height=2,width=30)
# l.pack()
# l2=Label(text="Введите коэффициенты",fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)
# l2.pack()
# ent=Entry(fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)
# ent.pack()
# ent2=Entry(fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)
# ent2.pack()
# ent3=Entry(fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)
# ent3.pack()


# # ent=Entry(text="Решение",fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)
# btn=Button(text="Решить",fg='black',bg='green',font='Arial 15',width=20,relief=GROOVE)
# l2=Label(text="Решение",fg='black',bg='yellow',font='Arial 15',width=20,relief=GROOVE)


# def solve(a,b,c):
#     d=b**2-4*a*c
#     if d>0:
#         x1=(-b+sqrt(d))/(2*a)
#         x2=(-b-sqrt(d))/(2*a)
#         return x1,x2
#     elif d==0:
#         x1=-b/(2*a)
#         return x1
#     else:
#         return "No roots"
    
#     def on_click():
#         a=ent.get()
#         b=ent2.get()
#         c=ent3.get()
#         if a=="":
#             ent.config(bg='red')
#         if b=="":
#             ent2.config(bg='red')
#         if c=="":
#             ent3.config(bg='red')
#         if a!="" and b!="" and c!="":
#             ent.config(bg='white')
#             ent2.config(bg='white')
#             ent3.config(bg='white')
#             a=int(a)
#             b=int(b)
#             c=int(c)
#             res=solve(a,b,c)
#             l2.config(text=res)

#             btn.config(command=on_click)
#             btn.pack()
# # f.pack()




           






# # f.grid(row=0,column=0)


# objects=[l,btn,l2]
# for i in range(len(objects)):
#     objects[i].pack()
# aken.mainloop()


from tkinter import *
from math import sqrt

aken = Tk()
aken.geometry("600x500")
aken.title("Pealkiri")

l = Label(text="Решение квадратного уравнения", bg='lightblue', fg='Green', font='Arial 24', height=2, width=30)
l.pack()

l2 = Label(text="Введите коэффициенты", fg='black', bg='yellow', font='Arial 15', width=20, relief=GROOVE)
l2.pack()

ent = Entry(fg='black', bg='yellow', font='Arial 15', width=20, relief=GROOVE)
ent.pack()

ent2 = Entry(fg='black', bg='yellow', font='Arial 15', width=20, relief=GROOVE)
ent2.pack()

ent3 = Entry(fg='black', bg='yellow', font='Arial 15', width=20, relief=GROOVE)
ent3.pack()

btn = Button(text="Решить", fg='black', bg='green', font='Arial 15', width=20, relief=GROOVE)

l2_res = Label(text="Решение", fg='black', bg='yellow', font='Arial 15', width=20, relief=GROOVE, height=5)
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
        return "No roots"

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