from tkinter import *
from NS_Api import *


def raise_frame(frame):                                         #Met deze functie: wissel je van pagina frame
    frame.tkraise()


root = Tk()
root.title("NS Automaat")
root.geometry('1280x800')
root.configure(bg="#f7d53d")


Home = Frame(root)
PageOne = Frame(root)

for frame in(Home, PageOne):
    frame.grid(row=0, column=0, sticky='news')

Home.configure(bg="#f7d53d")
PageOne.configure(bg='#f7d53d')

logo = PhotoImage(file='logo.gif')
logo_label = Label(Home,image= logo, bg="#f7d53d")
logo_label.pack(padx=50, pady=0)

Label(Home, text='Welkom bij NS', font= "Helvetica, 28", fg= "#1f0396", bg="#f7d53d").pack()

chipkaart = PhotoImage(file='ns.gif')
chipkaart_label = Label(Home,image= chipkaart, bg="#f7d53d")
chipkaart_label.pack(padx=50, pady=10)

Button(Home, text='Druk om verder te gaan',bg= "#1f0396", fg='white', command=lambda:raise_frame(PageOne)).pack()

Label(PageOne, text='Kies een station', font= "Helvetica, 28", fg= "#1f0396", bg= "#f7d53d").pack()
Button(PageOne, text='Terug', command=lambda:raise_frame(Home)).pack()

invoer=Label(PageOne, text='Voer een station in:').pack()
entry_1= Entry(PageOne).pack()
button_1=Button(PageOne, text='Enter').pack()


raise_frame(Home)
root.mainloop()
