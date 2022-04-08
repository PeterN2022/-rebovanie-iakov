import tkinter 
import random
canvas=tkinter.Canvas ()
canvas.pack()
canvas.create_text (190,40,text='Odpovedať príde:', font='Arial 20', fill='black')
def button1_klik(): 
  canvas.delete('all')
  canvas.create_text (190,40,text='Odpovedať príde:', font='Arial 20', fill='black')
  canvas.create_text (190,80,text=random.choice(('Samuel Simon Birks',
'Sara Crugliano',
'Sheryl Doničová',
'Jakub Gajdoš',
'Ela Gajdošová','Tomáš Kuba',
'Nina Maľcovská',
'Dominik Marcin',
'Martin Mikloš',
'Michal Pastirčák',
'Richard Remeta',
'Kristína Špirengová',
'Tadeáš Taiš',
'Timotej Taiš'
)), font='Arial 13 bold', fill='blue') 

button1 = tkinter.Button(text='IX.B', command=button1_klik)
button1.pack()
button1.place(x=200, y=200)

def button2_klik(): 
  canvas.delete('all')
  canvas.create_text (190,40,text='Odpovedať príde:', font='Arial 20', fill='black')
  canvas.create_text (190,80,text=random.choice(('Peter Anderko',
'Nathaniel Martin Bechera',
'Viliam Dzurenda',
'Daniel Fečo',
'Alica Fečová',
'Patrícia Franková',
'Sára Grejtáková',
'Gabriel Hreňo',
'Adam Kožuško',
'Michaela Ligmajerová',
'Oliver Novický',
'Diana Olejníková',
'Alex Penev',
'Casidy Kristy Lee Pulleyová',
'Sofia Sedláková',
'Adam Slivka',
'Martin Tabačko',
'Soňa Vašková',
'Matej Vidumský',
'Adam Zubrický',
'Martin Želonka'
)), font='Arial 13 bold', fill='blue') 
  

button2 = tkinter.Button(text='IX.A', command=button2_klik)
button2.pack()
button2.place(x=120, y=200)
