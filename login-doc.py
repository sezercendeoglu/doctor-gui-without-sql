from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


# Tk sınıfını 'window'a atadık.
window = Tk()

# Pencere Başlığı
window.title("DOCTOR GUI")



# Pencerenin yeniden boyutlandırılmasını engelledik
window.geometry('1000x500')


resim = ImageTk.PhotoImage(Image.open("Desktop/doctor.png"))
lresim = Label(window,image=resim)
lresim.place(x=250,y=10)


L3 = Label(window)
L3.place(x=500,y=500)

def giris():
    
    
    if (E1.get() == str("admin")) and (E2.get() == str("1234")):
        L3['text'] = ("LOGED IN SUCCESFULLY...")
        messagebox.showinfo("Successful Title", "Loged in successfully")
        print("başarılı")
    else:
        L3['text'] = ("ERROR!!!!")
        messagebox.showerror("Error Title", "404 NOT FOUND  ")

L1 = Label(window, text="Username")
L1.place(x=75, y=15)

E1 = Entry(window, width=25)
E1.place(x=77,y=45)

L2 = Label(window, text="Password")
L2.place(x=75, y=80)

E2 = Entry(window, textvariable=StringVar(),show='*', width=25)
E2.place(x=77, y=110)

bt = Button(window, text="TRY TO LOGIN", padx="20",pady="5", command=giris)
bt.place(x=75,y=150)

window.mainloop()