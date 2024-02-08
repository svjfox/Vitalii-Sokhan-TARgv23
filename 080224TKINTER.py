from tkinter import *
from wsgiref import validate
def FromEntryToLabel(event):
    t=ent.get()
    l.configure(text=t)
    
def valik():
    t=var.get()
    ent.delete(0,END)
    ent.insert(END,t)


showflag=False
def showtarnid(event):
        global showflag
        if showflag:
            ent.configure(show='*')
            showflag=False
        else:
            ent.configure(show='')
            showflag=True 
        
   #на поыторный Enter можно сделать ent.configure(show='')
   
    

aken=Tk()
aken.geometry("600x500")
aken.title("Pealkiri")

aken.iconbitmap("potential.ico")
f=Frame(aken,bg='blue',border=10,height=100,width=600)
l=Label(f,text="Tere",bg='gold',fg='#aa4a44',font='Arial 24',height=3,width=17)
ent=Entry(f,fg='gold',bg='#aa4a44',font='Arial 24',width=17,justify=CENTER) #show='*'
btn=Button(f,text="Vajuta siia",fg='gold',bg='lightblue',font='Arial 18',width=17,relief=GROOVE) #SUNKEN, FLAT, RAISED, RIDGE, GROOVE


var=IntVar() #StringVar() можно также использовать
r1=Radiobutton(f,text='Esimene',font='Arial 14',variable=var,value=1,command=valik)
r2=Radiobutton(f,text='Teine',font='Arial 14',variable=var,value=2,command=valik)
r3=Radiobutton(f,text='Kolmas',font='Arial 14',variable=var,value=3,command=valik)

btn.bind('<Button-1>',FromEntryToLabel) #LKM , -2 средняя, -3 правая
ent.bind('<Return>',showtarnid) # Enter


f.grid(row=0,column=0) #pack(), place()

objects=[l,ent,btn,r1,r2,r3]
for i in range(len(objects)):
    objects[i].pack()

aken.mainloop()
