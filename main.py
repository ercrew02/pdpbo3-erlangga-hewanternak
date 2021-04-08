# Saya Erlangga mengerjakan evaluasi Tugas Praktikum 3 DPBO dalam mata kuliah Desain dan Pemrograman Berorientasi Objek
# untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin.
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Window")

lblnama = Label(root, text="Nama Hewan:").grid(column=0, row=0)
nama = Entry(root, width=20, borderwidth=5)
nama.insert(0, "")
nama.grid(column=1, row=0)

lbljenis = Label(root, text="Jenis:").grid(column=0, row=1)
options = [
    "Anak",
    "Dewasa",
    "Tua"
]

jenis = StringVar()
jenis.set(options[0])

drop = OptionMenu(root, jenis, *options)
drop.grid(column=1, row=1)


lbljk = Label(root, text="Jenis Kelamin:").grid(column=0, row=2)
JK = StringVar()
jk = Checkbutton(root, text="Jantan", variable=JK,
                 onvalue="Jantan", offvalue="")
jk.deselect()
jk.grid(column=1, row=2, columnspan=1)

jk = Checkbutton(root, text="Betina", variable=JK,
                 onvalue="Betina", offvalue="")
jk.deselect()
jk.grid(column=2, row=2, columnspan=1)

# combobox
lblBerat = Label(root, text="Berat:").grid(column=0, row=3)
CB = StringVar()
c = Checkbutton(root, text="10 - 20", variable=CB,
                onvalue="10 - 20", offvalue="")
c.deselect()
c.grid(column=1, row=3)

c = Checkbutton(root, text="20 - 30", variable=CB,
                onvalue="20 - 30", offvalue="")
c.deselect()
c.grid(column=2, row=3)

c = Checkbutton(root, text="40 - 50", variable=CB,
                onvalue="40 - 50", offvalue="")
c.deselect()
c.grid(column=3, row=3)

c = Checkbutton(root, text="60 - 70", variable=CB,
                onvalue="60 - 70", offvalue="")
c.deselect()
c.grid(column=4, row=3)

# combobox
Asal = [
    ("Jakarta", "Jakarta"),
    ("Bandung", "Bandung"),
    ("Tanggerang", "Tanggerang"),
    ("Karawang", "Karawang")
]
lblBerat = Label(root, text="Asal Hewan:").grid(column=0, row=4)
VarAsal = StringVar()
VarAsal.set("")

i = 4
for text, asal, in Asal:
    Radiobutton(root, text=text, variable=VarAsal,
                value=asal).grid(column=1, row=i)
    i = i+1

# Button
foto = Button(root, text="foto", fg="black", bg="#FFFFFF")
foto.grid(column=0, row=8)

submit = Button(root, text="submit",  fg="black", command=lambda: popup(
    nama.get(), jenis.get(), JK.get(), CB.get(), VarAsal.get()), bg="#FFFFFF")
submit.grid(column=1, row=8)

SeeAllSubmit = Button(root, text="seeAllSubmit",  fg="black", bg="#FFFFFF")
SeeAllSubmit.grid(column=0, row=9)

HapusData = Button(root, text="HapusData",  fg="black", bg="#FFFFFF")
HapusData.grid(column=1, row=9)

Tentang = Button(root, text="Tentang",  fg="black", bg="#FFFFFF")
Tentang.grid(column=2, row=9)

Exit = Button(root, text="Exit",  fg="black", bg="#FFFFFF")
Exit.grid(column=1, row=10)


def popup(Data, Data2, Data3, Data4, Data5):
    response = messagebox.showinfo(
        "This is my Popup", Data + Data2 + Data3 + Data4 + Data5)
    Label(root, text=response).grid()


root.mainloop()
