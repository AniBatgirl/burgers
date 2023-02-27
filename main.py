from tkinter import *
import tkinter

window = tkinter.Tk()
window.title("hamburgr")
window.geometry('600x800')

# CheckVar1 = IntVar()
# CheckVar2 = IntVar()
# CheckVar3 = IntVar()
# CheckVar4 = IntVar()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()

text = Label(window, text="Sestav si burger", relief=GROOVE, font=("Arial", 50))

C1 = Radiobutton(window, text="sezamová", variable=CheckVar1, value="sezamová", height=1, width=100 )
C2 = Radiobutton(window, text="sépiová", variable=CheckVar1, value="sépiová", height=1, width=100 )
C3 = Radiobutton(window, text="hovězí", variable=CheckVar2, value="hovězí", height=1, width=100 )
C4 = Radiobutton(window, text="kuřecí", variable=CheckVar2, value="kuřecí", height=1, width=100 )
# C3 = Checkbutton(window, text = "Video", variable = CheckVar3, onvalue = 1, offvalue = 0, height=5, width = 20)
# C4 = Checkbutton(window, text = "Video", variable = CheckVar4, onvalue = 1, offvalue = 0, height=5, width = 20)
text.pack()
C1.pack()
C2.pack()
C3.pack()
C4.pack()
# C2.pack()
# C3.pack()
# C4.pack()
window.mainloop()
