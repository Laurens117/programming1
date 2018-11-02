from tkinter import *
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

Label(Home, text='Welkom bij NS', font= "Helvetica, 55", fg= "#1f0396", bg="#f7d53d").pack(padx=770, pady=0)

chipkaart = PhotoImage(file='ns.gif')
chipkaart_label = Label(Home,image= chipkaart, bg="#f7d53d")
chipkaart_label.pack(padx=50, pady=10)

Button(Home, text='Druk om verder te gaan', font= "Helvetica, 30", bg= "#1f0396", fg='white', command=lambda:raise_frame(PageOne)).pack(padx=0,pady=50)

lijst=[]
def Stations():
    """Met deze functie kan je in de entry een station invoeren."""
    station = stationEntry.get()
    lijst.clear()
    tijdEnBestemmingen = station_vertrektijd(station)

    for tijdEnBestemming in tijdEnBestemmingen:
        bestemming=Label(PageOne, text='Om {} vertrekt er een trein naar {} op spoor {}'
                                       ''.format(tijdEnBestemming[0],tijdEnBestemming[1], tijdEnBestemming[2]), font="Helvetica, 23", fg="#1f0396", bg="#f7d53d")
        bestemming.pack()
        lijst.append(bestemming)

help(Stations)

#PageOne

PageOne.configure(bg='#f7d53d')

Label(PageOne, text='Actuele vertrektijden', font= "Helvetica, 40", fg= "#1f0396", bg= "#f7d53d").pack()

invoer=Label(PageOne, text='Voer een station in:',font= "Helvetica, 28", bg='#f7d53d').pack(padx=0,pady=5)

stationEntry = Entry(PageOne)
stationEntry.pack()

button = Button(PageOne, text="Druk hier",font= "Helvetica, 10", bg= "#1f0396", fg='white', command=Stations)
button.pack()

Button(PageOne, text='Terug',font= 'Helvetica, 10', bg= "#1f0396", fg='white', command=lambda:raise_frame(Home)).pack()

raise_frame(Home)                                           #Als het programma opent, toon het de startscherm.

root.overrideredirect(True)
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.bind("<Escape>", lambda e: e.widget.quit())

root.mainloop()
