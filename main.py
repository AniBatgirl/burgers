import tkinter
from lib import *
from tkinter import *
from tkinter import ttk

window = tkinter.Tk()
window.title("hamburgr")
window.geometry('600x800')
window.configure(bg='#fff2e6')


CheckVar1 = IntVar()
CheckVar2 = IntVar()
CheckVar3 = IntVar()
CheckVar4 = IntVar()
CheckVar5 = IntVar()
CheckVar6 = IntVar()
CheckVar7 = IntVar()
CheckVar8 = IntVar()
CheckVar9 = IntVar()


hodnoty = [IntVar() for i in range(0, 9)]
text = Label(window, text="Sestav si burger", relief=GROOVE, font=("Arial", 10), bg='#ff9900')
text1 = Label(window, text="Na jake maso mas dneska chut?", relief=SUNKEN, pady=2, font=("Arial", 10), bg='#ffcc99')
text2 = Label(window, text="Vyber si druh masa", relief=SUNKEN, font=("Arial", 10), bg='#e63900')
text3 = Label(window, text="Zvol si propečení masa", relief=SUNKEN, font=("Arial", 10), bg='#b37700')
text4 = Label(window, text="Doplňující ingredience", relief=SUNKEN, font=("Arial", 10), bg='#ffff66')
text5 = Label(window, text="Navol si zeleninu", relief=SUNKEN, font=("Arial", 10), bg='#99ff66')
text6 = Label(window, text="Na jakou omáčku to dneska cítíš?", relief=SUNKEN, font=("Arial", 10), bg='#ffcc99')

C1 = Radiobutton(window, text="sezamová", variable=hodnoty[0], value="sezamová", height=1, bg='#fff2e6')
C2 = Radiobutton(window, text="sépiová", variable=hodnoty[0], value="sépiová", height=1, bg='#fff2e6')
C3 = Radiobutton(window, text="hovězí", variable=hodnoty[1], value="hovězí", height=1, bg='#fff2e6')
C4 = Radiobutton(window, text="kuřecí", variable=hodnoty[1], value="kuřecí", height=1, bg='#fff2e6')
C5 = Radiobutton(window, text="telecí", variable=hodnoty[1], value="telecí", height=1, bg='#fff2e6')
C6 = Radiobutton(window, text="rare", variable=hodnoty[2], value="rare", height=1, bg='#fff2e6')
C7 = Radiobutton(window, text="medium", variable=hodnoty[2], value="medium", height=1, bg='#fff2e6')
C8 = Radiobutton(window, text="well done", variable=hodnoty[2], value="well done", height=1, bg='#fff2e6')
C9 = Checkbutton(window, text="sýr", variable=hodnoty[3], onvalue="sýr", offvalue="ne", height=1, bg='#fff2e6')
C10 = Checkbutton(window, text="slanina", variable=hodnoty[4], onvalue="slanina", offvalue="ne", height=1, bg='#fff2e6')
C11 = Checkbutton(window, text="cibule", variable=hodnoty[5], onvalue="cibule", offvalue="ne", height=1, bg='#fff2e6')
C12 = Checkbutton(window, text="salat", variable=hodnoty[6], onvalue="salat", offvalue="ne", height=1, bg='#fff2e6')
C13 = Checkbutton(window, text="rajcata", variable=hodnoty[7], onvalue="rajcata", offvalue="ne", height=1, bg='#fff2e6')
C14 = Radiobutton(window, text="kečup", variable=hodnoty[8], value="kečup", height=1, bg='#fff2e6')
C15 = Radiobutton(window, text="mayoneza", variable=hodnoty[8], value="mayoneza", height=1, bg='#fff2e6')
C16 = Radiobutton(window, text="hořtice", variable=hodnoty[8], value="hořtice", height=1, bg='#fff2e6')
C17 = Radiobutton(window, text="bez omáčky", variable=hodnoty[8], value="bez_omáčky", height=1, bg='#fff2e6')
submit = Button(window, text="Vytvoř burger", height=1, bg='#ff9900', command=lambda:vytvor(hodnoty))

text.pack()
text1.pack()
C1.pack()
C2.pack()
text2.pack()
C3.pack()
C4.pack()
C5.pack()
text3.pack()
C6.pack()
C7.pack()
C8.pack()
text4.pack()
C9.pack()
C10.pack()
text5.pack()
C11.pack()
C12.pack()
C13.pack()
text6.pack()
C14.pack()
C15.pack()
C16.pack()
C17.pack()
submit.pack()



window.mainloop()
