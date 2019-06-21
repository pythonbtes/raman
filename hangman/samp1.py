from tkinter import *
root=Tk()
var1=StringVar()
var3=StringVar()
word="oxygen"
def box():
    for char in word:
        Label(root,text="Enter Your Name",bg="black", fg="white", font="none 10 italic").grid(row=1,column=0)
        textentry=Entry(root,width=10,bg="white")
        textentry.grid(row=1,column=150)
        if char in 'aeiou':
            print(char)
        else:
             print("_")
root.mainloop()
