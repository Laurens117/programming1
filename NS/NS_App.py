from tkinter import *
from NS_Api import *


def raise_frame(frame):                                         #Met deze functie wissel je van pagina.
    frame.tkraise()

root = Tk()
root.title("NS app")
root.geometry('1280x800')
root.configure(bg="#f7d53d")


Home = Frame(root)
PageOne = Frame(root)

for frame in(Home, PageOne):
    frame.grid(row=0, column=0, sticky='news')

#Home(startscherm)

Home.configure(bg="#f7d53d")                                    #achtergrond

logo = PhotoImage(file='logo.gif')
logo_label = Label(Home,image= logo, bg="#f7d53d")
logo_label.pack(padx=50, pady=0)

Label(Home, text='Welkom bij NS', font= "Helvetica, 28", fg= "#1f0396", bg="#f7d53d").pack()

chipkaart = PhotoImage(file='ns.gif')
chipkaart_label = Label(Home,image= chipkaart, bg="#f7d53d")
chipkaart_label.pack(padx=50, pady=10)

Button(Home, text='Druk om verder te gaan',bg= "#1f0396", fg='white', command=lambda:raise_frame(PageOne)).pack()


def Stations():                                             #Met deze functie kan je in de entry een station invoeren.
    station = stationEntry.get()                            #Met de vertrrektijden als output.
    bestemming = station_vertrektijd(station)

#Pagina_1

PageOne.configure(bg='#f7d53d')
Label(PageOne, text='Actuele vertrektijden', font= "Helvetica, 28", fg= "#1f0396", bg= "#f7d53d").pack()

invoer=Label(PageOne, text='Voer een station in:', bg='#f7d53d').pack()

stationEntry = Entry(PageOne)
stationEntry.pack()

button = Button(PageOne, text="Druk hier", command=Stations)
button.pack()

Button(PageOne, text='Terug', command=lambda:raise_frame(Home)).pack()

raise_frame(Home)                                                            #Als het programma opent, toon het de startscherm.
root.mainloop()

