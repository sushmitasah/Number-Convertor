
from tkinter import *

def sel1():
    a=e1.get()
    if v.get()==1:
        label.config(text=a)
    if v.get()==2:
        label.config(text=bin(int(a)))
    if v.get()== 3:
        dec=int(a,16)
        label.config(text=bin(dec))
    if v.get()==4:
        dec1=int(a,8)
        label.config(text=bin(dec1))
        
def sel2():
    a=e1.get()
    if v.get()==1:
        dec2=int(a,2)
        label.config(text=dec2)
    if v.get()==2:
        label.config(text=a)
    if v.get()== 3:
        dec3=int(a,16)
        label.config(text=str(dec3))
    if v.get()==4:
        dec4=str(int(a,8))
        label.config(text=dec4)
        
def sel3():
    a=e1.get()
    if v.get()==1:
        dec5=int(a,2)
        label.config(text=hex(dec5))
    if v.get()==2:
        label.config(text=hex(int(a)))
    if v.get()== 3:
        label.config(text=a)
    if v.get()==4:
        dec6=str(int(a,8))
        dec7=int(dec6)
        label.config(text=hex(dec7))

def sel4():
    a=e1.get()
    if v.get()==1:
        dec8=int(a,2)
        label.config(text=oct(dec8))
    if v.get()==2:
        label.config(text=oct(int(a)))
    if v.get()== 3:
        dec9=int(a,16)
        label.config(text=oct(dec9))
    if v.get()==4:
        label.config(text=a)

def sel5():
    a=e1.get()
    if v.get()==1:
        dec2=int(a,2)
        dec8=int(a,2)
        dec5=int(a,2)
        selection="Decimal: "+str(dec2)+" Octal: "+str(oct(dec8))+" Hexadecimal: "+str(hex(dec5))
        
        label.config(text=selection)
        
    if v.get()==2:
        selection="Binary: "+str(bin(int(a)))+" Octal: "+str(oct(int(a)))+" Hexadecimal: "+str(hex(int(a)))
        label.config(text=selection)
        
    if v.get()== 3:
        dec=int(a,16)
        dec3=int(a,16)
        dec9=int(a,16)
        selection="Binary: "+str(bin(dec))+" Decimal: "+str(dec3)+" Octal: "+str(oct(dec9))
        label.config(text=selection)
    if v.get()==4:
        dec1=int(a,8)
        dec4=str(int(a,8))
        dec6=str(int(a,8))
        dec7=int(dec6)
      
        selection="Binary: "+str(bin(dec1))+" Decimal: "+str(dec4)+" Hexadecimal "+str(hex(dec7))                    
        label.config(text=selection)

top=Tk()


b=Button(top,text="WELCOME!!")
b.pack()
l1=Label(top,text="Enter a number:")
l1.pack()
e1=Entry(top,bd=7)
e1.pack()


def sel():
    selection="You selected the option "+str(v.get())
    l2.config(text=selection)
v=IntVar()

R1=Radiobutton(top,text="binary no",variable=v,value=1,command=sel)
R1.pack()

R2=Radiobutton(top,text="decimal no",variable=v,value=2,command=sel)
R2.pack()

R3=Radiobutton(top,text="hexadecimal no",variable=v,value=3,command=sel)
R3.pack()

R4=Radiobutton(top,text="octal no",variable=v,value=4,command=sel)
R4.pack()

l2=Label(top)
l2.pack()


l3=Label(top,text="Convert To:")
l3.pack()
CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
CheckVar5=IntVar()




C1=Checkbutton(top,text="to binary no",variable=CheckVar1,
               onvalue=1,offvalue=0,height=0,width=20,command=sel1)
C2=Checkbutton(top,text="to decimal no",variable=CheckVar2,
               onvalue=1,offvalue=0,height=0,width=0,command=sel2)
C3=Checkbutton(top,text="to hexadecimal no",variable=CheckVar3,
               onvalue=1,offvalue=0,height=0,width=0,command=sel3)
C4=Checkbutton(top,text="to octal no",variable=CheckVar4,
               onvalue=1,offvalue=0,height=0,width=0,command=sel4)
C5=Checkbutton(top,text="to all",variable=CheckVar5,
               onvalue=1,offvalue=0,height=0,width=0,command=sel5)
C1.pack()
C2.pack()
C3.pack()
C4.pack()
C5.pack()
label=Label(top)
label.pack()

top.mainloop()
