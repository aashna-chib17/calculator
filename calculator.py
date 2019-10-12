from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget('text')
    print(text)
    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error"

        scvalue.set(value)
        screen.update()
    elif text=="C":
        scvalue.set("")
        screen.update()
        pass
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root=Tk()
root.geometry('744x900')
root.title("Calculator by Aashna")
scvalue= StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 30 bold")
screen.pack(fill=X,ipadx=4,pady=6,padx=6)

f=Frame(root,bg='grey')
b=Button(f,text='9 ',padx=21,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='8',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='7',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg='grey')
b=Button(f,text='6',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='5',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='4',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg='grey')
b=Button(f,text='3',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='2',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='1',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg='grey')
b=Button(f,text='0',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='C',padx=28,pady=18,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
f.pack()

f=Frame(root,bg='grey')
b=Button(f,text='+',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='-',padx=28,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='*',padx=19,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='/',padx=19,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)

b=Button(f,text='=',padx=34,pady=12,bg='black',fg='white',font='lucida 35 bold')
b.pack(side=LEFT,padx=18,pady=3)
b.bind("<Button-1>",click)
f.pack()






root.mainloop()