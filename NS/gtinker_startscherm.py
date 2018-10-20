from tkinter import *




root = Tk()                                         #Hiermee maak je het startscherm.
root.title("NS Automaat")                           #Maakt titel aan(boven in scherm.)
root.geometry("1280x1000")                          #Formaat scherm in pixels.
root.configure(bg="#f7d53d")                        #Kleur van achtergrond.


label_text= Label(master=root,                      #Maakt tekst aan.
                  text= "Welkom bij NS",
                  font= "Helvetica, 28",
                  foreground= "#1f0396",            #kleur tekst
                  bg= "#f7d53d")                    #Kleur van achtergrond.


logo = PhotoImage(file='logo.gif')                  #opent ns logo afbeelding
logo_label = Label(root,
                 image= logo,
                 bg= '#f7d53d')


chipkaart = PhotoImage(file='ns.gif')               #opent ov afbeelding
chipkaart_label = Label(root,
                        image= chipkaart)


button = Button(master=root,                                #Maakt hier een knop aan.
                text='Druk hier om verder te gaan',
                bg='#1f0396',
                fg='white')

logo_label.pack(padx=50, pady=0)                              #Toont logo van ns locatie(x as en y as)
label_text.pack(padx=50, pady=10)                             #Toont tekst
chipkaart_label.pack(padx=50, pady=10)                        #ov chipkaart afbeelding
button.pack(padx=200, pady=40)                                #Toont knop.


root.mainloop()                                               #Toont hoofdscherm.
