from tkinter import *



aken=Tk()
aken.geometry("600x500")
aken.title("Pealkiri")

aken.iconbitmap("potential.ico")
f=Frame(aken,bg='blue',border=10,height=100,width=600)
l=Label(f,text="Tere",bg='gold',fg='#aa4a44',font='Arial 24',height=3,width=17)


f.grid(row=0,column=0) #pack(), place()
l.pack()
aken.mainloop()
