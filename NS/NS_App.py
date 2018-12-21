from tkinter import *
from urllib.request import urlopen
from NS_Api import *


def raise_frame(frame):
    """ Met deze functie wissel je van pagina."""
    for i in lijst:
        i.destroy()
    frame.tkraise()

help(raise_frame)


root = Tk()
root.title("NS app")
root.configure(bg="#f7d53d")


Home = Frame(root)
PageOne = Frame(root)

for frame in(Home, PageOne):
    frame.grid(row=0, column=0, sticky='news')

#Home(startscherm)

Home.configure(bg="#f7d53d")

logo = PhotoImage(file='logo.gif')
logo_label = Label(Home,image= logo, bg="#f7d53d")
logo_label.pack(padx=50, pady=0)

Label(Home, text='Welkom bij NS', font= "Helvetica, 55", fg= "#1f0396", bg="#f7d53d").pack(padx=700, pady=0)

chipkaart = PhotoImage(file='ns.gif')
chipkaart_label = Label(Home,image= chipkaart, bg="#f7d53d")
chipkaart_label.pack(padx=50, pady=10)

Button(Home, text='Actuele vertrektijden', font= "Helvetica, 30", bg= "#1f0396", fg='white',
       command=lambda:raise_frame(PageOne)).pack(padx=0,pady=50)

PinFoto="https://i.imgur.com/I55owpM.png"
Pin_picture = PhotoImage(data=urlopen(PinFoto).read())
MaestroFoto="https://i.imgur.com/yzS6qoe.png"
Maestro_picture = PhotoImage(data=urlopen(MaestroFoto).read())

Pinnen = Button(Home, image=Pin_picture, width=190, height=120, borderwidth=0)
Maestro = Button(Home, image=Maestro_picture, width=190, height=120, borderwidth=0)
Enkele_Reis = Button(Home, text="Enkele reis", bg="#003082", fg="white", width=20, height=4,
                     anchor="w", borderwidth=0, font=("", 9, "bold"))
Dag_Retour = Button(Home, text="Dag retour", bg="#003082", fg="white", width=20, height=4,
                    anchor="w", borderwidth=0, font=("", 9, "bold"))
Retourkaart = Button(Home, text="5-Retourkaart", bg="#003082", fg="white", width=20, height=4,
                     anchor="w", borderwidth=0, font=("", 9, "bold"))
Weekendretour = Button(Home, text="Weekendretour", bg="#003082", fg="white", width=20, height=4,
                       anchor="w", borderwidth=0, font=("", 9, "bold"))
Railrunner = Button(Home, text="Railrunner\n4 t/m 11 jaar", justify=LEFT, bg="#003082",
                    fg="white", width=20, height=4, anchor="w", borderwidth=0, font=("", 9, "bold"))

Enkele_Reis.place(x=5, y=5)
Dag_Retour.place(x=5, y=80)
Retourkaart.place(x=5, y=155)
Weekendretour.place(x=5, y=230)
Railrunner.place(x=5, y=305)
Pinnen.place(x=1700, y=10)
Maestro.place(x=1700, y=300)

lijst=[]
def Stations():
    """Met deze functie kan je in de entry een station invoeren."""
    station = stationEntry.get()
    for item in lijst:
        item.destroy()
    tijdEnBestemmingen = station_vertrektijd(station)
    posx = 500
    posy = 245
    for tijdEnBestemming in tijdEnBestemmingen:
        bestemming=Label(PageOne, text='Om {} vertrekt er een trein naar {} op spoor {}'
                                       ''.format(tijdEnBestemming[0],tijdEnBestemming[1], tijdEnBestemming[2]),
                                font="Helvetica, 23", fg="#1f0396", bg="#f7d53d")
        bestemming.place(x=posx, y=posy)
        posy+=40
        lijst.append(bestemming)

help(Stations)


def StationUtrecht():
    """Met deze functie kan je in de entry een station invoeren."""
    station = 'ut'
    for item in lijst:
        item.destroy()
    tijdEnBestemmingen = station_vertrektijd(station)
    posx = 500
    posy = 245
    for tijdEnBestemming in tijdEnBestemmingen:
        bestemming = Label(PageOne, text='Om {} vertrekt er een trein naar {} op spoor {}'
                                         ''.format(tijdEnBestemming[0], tijdEnBestemming[1], tijdEnBestemming[2]),
                           font="Helvetica, 23", fg="#1f0396", bg="#f7d53d")
        bestemming.place(x=posx, y=posy)
        posy += 40
        lijst.append(bestemming)


#PageOne

PageOne.configure(bg='#f7d53d')

Label(PageOne, text='Actuele vertrektijden', font= "Helvetica, 40", fg= "#1f0396", bg= "#f7d53d").pack()

invoer=Label(PageOne, text='Voer een station in:',font= "Helvetica, 28", bg='#f7d53d').pack(padx=0,pady=5)

stationEntry = Entry(PageOne)
stationEntry.pack()

button = Button(PageOne, text="Druk hier",font= "Helvetica, 10", bg= "#1f0396", fg='white', command=Stations)
button.place(x=1090, y=145)
buttonUt = Button(PageOne, text="Utrecht",font= "Helvetica, 10", bg= "#1f0396", fg='white', command=StationUtrecht)
buttonUt.pack()
Button(PageOne, text='Terug',font= 'Helvetica, 10', bg= "#1f0396", fg='white', command=lambda:raise_frame(Home)).pack()

raise_frame(Home)                                           #Als het programma opent, toon het de startscherm.

root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()
