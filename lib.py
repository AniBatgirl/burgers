from tkinter import *
from PIL import ImageTk, Image, ImageEnhance


def vytvor_burger(hodnoty, burger_f, vyber_f):
    for widget in burger_f.winfo_children():
        widget.destroy()
    vymen_obrazovku(vyber_f, burger_f)
    fotky = ziskej_fotky(hodnoty)
    top = Label(burger_f, image=fotky["top"], bg='#fff2e6')
    top.image = fotky["top"]
    bot = Label(burger_f, image=fotky["bot"], bg='#fff2e6')
    bot.image = fotky["bot"]
    slanina = Label(burger_f, image=fotky["slanina"], bg='#fff2e6')
    slanina.image = fotky["slanina"]
    syr = Label(burger_f, image=fotky["syr"], bg='#fff2e6')
    syr.image = fotky["syr"]
    maso = Label(burger_f, image=fotky["maso"], bg='#fff2e6')
    maso.image = fotky["maso"]
    cibule = Label(burger_f, image=fotky["cibule"], bg='#fff2e6')
    cibule.image = fotky["cibule"]
    salat = Label(burger_f, image=fotky["salat"], bg='#fff2e6')
    salat.image = fotky["salat"]
    rajce = Label(burger_f, image=fotky["rajce"], bg='#fff2e6')
    rajce.image = fotky["rajce"]
    omacka = Label(burger_f, image=fotky["omacka"], bg='#fff2e6')
    omacka.image = fotky["omacka"]
    top.pack()
    slanina.pack() if fotky["slanina"] is not None else None
    syr.pack() if fotky["syr"] is not None else None
    maso.pack()
    cibule.pack() if fotky["cibule"] is not None else None
    salat.pack() if fotky["salat"] is not None else None
    rajce.pack() if fotky["rajce"] is not None else None
    omacka.pack() if fotky["omacka"] is not None else None
    bot.pack()

    goback = Button(burger_f, bg='#fff2e6', text="Zpátky na výběr", command=lambda:vymen_obrazovku(burger_f, vyber_f))
    goback.pack(pady=10)


def vymen_obrazovku(frame1, frame2):
    frame1.pack_forget()
    frame2.pack()


def ziskej_fotky(hodnoty):
    ret = {}
    bulka_top = ImageTk.PhotoImage(Image.open(f"burger_bun_{hodnoty['bulka'].get()}_top.png"))
    bulka_bottom = ImageTk.PhotoImage(Image.open(f"burger_bun_{hodnoty['bulka'].get()}_bottom.png"))
    if hodnoty["propecenost"].get() == "maso1":
        value = 1.5
    elif hodnoty["propecenost"].get() == "maso2":
        value = 1
    else:
        value = 0.65
    maso = Image.open(f"{hodnoty['maso'].get()}.png")
    maso = ImageEnhance.Color(maso)
    maso = maso.enhance(value)
    maso = ImageTk.PhotoImage(maso)
    ret["top"] = bulka_top
    ret["bot"] = bulka_bottom
    ret["maso"] = maso
    ret["omacka"] = ImageTk.PhotoImage(Image.open(f"{hodnoty['omacka'].get()}.png")) if hodnoty[
                                                                                        "omacka"].get() not in ["0", "ne"] else None
    ret["syr"] = ImageTk.PhotoImage(Image.open(f"{hodnoty['syr'].get()}.png")) if hodnoty["syr"].get() != "0" else None
    ret["slanina"] = ImageTk.PhotoImage(Image.open(f"{hodnoty['slanina'].get()}.png")) if hodnoty[
                                                                                          "slanina"].get() != "0" else None
    ret["cibule"] = ImageTk.PhotoImage(Image.open(f"{hodnoty['cibule'].get()}.png")) if hodnoty[
                                                                                        "cibule"].get() != "0" else None
    ret["salat"] = ImageTk.PhotoImage(Image.open(f"{hodnoty['salat'].get()}.png")) if hodnoty[
                                                                                      "salat"].get() != "0" else None
    ret["rajce"] = ImageTk.PhotoImage(Image.open(f"{hodnoty['rajce'].get()}.png")) if hodnoty[
                                                                                      "rajce"].get() != "0" else None
    return ret
