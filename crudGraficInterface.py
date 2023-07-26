#References:
#tkinter module: https://docs.python.org/es/3/library/tkinter.html#module-tkinter
#Tkinter options: https://docs.python.org/es/3/library/tkinter.ttk.html#widget
#widgets entry: https://www.tutorialspoint.com/python/tk_entry.htm
#estilos: https://www.pythontutorial.net/tkinter/tkinter-frame/
#dialog modules: https://docs.python.org/es/3/library/dialog.html#module-tkinter.filedialog
#use github sqlite3-viewer: https://inloop.github.io/sqlite-viewer/  or  App: https://sqliteviewer.app/

#*******************************************************IMPORT MODULES************************************************
from tkinter import *
from tkinter import messagebox
import sqlite3

root=Tk()
root.title("CRUD-Python-SQLite3")
#**************************************************FUNCTIONS***************************************************

def conectionBBDD():
    #create conection, and a new instance of cursor object
    myConection = sqlite3.connect("login")
    
    #Objeto cursor permite seguimiento de las filas en base de datos.
    myCursor= myConection.cursor()
    
    try:
        myCursor.execute('''
                     CREATE TABLE DATOS (
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE_USUARIO VARCHAR(50),
                     APELLIDO_USUARIO VARCHAR(50),
                     PASSWORD VARCHAR(50),
                     DIRECCION VARCHAR(50),
                     comentarios varchar (100))
        ''')
        #creación de las ventanas de dialogo emergentes
        messagebox.showinfo("BBDD", "BBDD created!")
        
    except:
        messagebox.showwarning("This BBDD exists!")
        
def exitFromApp():
    valor=messagebox.askquestion("Exit", "Do you want to exit")
    if valor=="yes":
        root.destroy()     
#clear inputs without deleting data en databeses   
def clearInputs():
    myId.set("")
    myName.set("")    
    myLastName.set("")
    myPassword.set("")
    myDirection.set("")
    textComments.delete(1.0, END)
    
      
def create():
    myConection=sqlite3.connect("login")
    myCursor=myConection.cursor()
    infoUser=myName.get(), myLastName.get(), myPassword.get(), myDirection.get(), textComments.get("1.0", END)
    
    myCursor.execute("INSERT INTO DATOS VALUES(NULL,?,?,?,?,?)",(infoUser))
    myConection.commit()
    messagebox.showinfo("BBDD", "Data Inserted!")
    
def read():
    myConection=sqlite3.connect("login")
    myCursor=myConection.cursor()
    myCursor.execute("SELECT * FROM DATOS WHERE ID=" + myId.get())
    dataUser=myCursor.fetchall()
    for data in dataUser:
        myId.set(data[0])
        myName.set(data[1])
        myLastName.set(data[2])
        myPassword.set(data[3])
        myDirection.set(data[4])
        textComments.insert(1.0, data[5])
        
def update():
    myConection=sqlite3.connect("login")
    myCursor=myConection.cursor()
    infoUser=myName.get(), myLastName.get(), myPassword.get(), myDirection.get(), textComments.get("1.0", END)
    myCursor.execute("UPDATE DATOS SET NOMBRE_USUARIO=?, APELLIDO_USUARIO=?, PASSWORD=?, DIRECCION=?, comentarios=?" + "WHERE ID=" + myId.get(), (infoUser))
    myConection.commit()
    messagebox.showinfo("BBDD", "Data updated!")
    
def delete():
    myConection=sqlite3.connect("login")
    myCursor=myConection.cursor()
    myCursor.execute("DELETE FROM DATOS WHERE ID=" + myId.get())
    myConection.commit()
    messagebox.showinfo("BBDD", "Data deleted!")
      
# Method to make Label(Widget) invisible
def hide_label(label):
    # This will remove the widget
    label.pack_forget()
      
#**********************************Grafic Interface #Barra del menu: interface grafica********************************
menuBar=Menu(root)
root.config(menu=menuBar, width=400, height=400)

bbddMenu = Menu(menuBar, tearoff=0)
bbddMenu.add_command(label="connect", command=conectionBBDD)
bbddMenu.add_command(label="exit", command=exitFromApp)

deleteMenu = Menu(menuBar, tearoff=0)
deleteMenu.add_command(label="clear inputs", command=clearInputs)


crudMenu = Menu(menuBar, tearoff=0)
crudMenu.add_command(label="create", command=create)
crudMenu.add_command(label="read", command=read)
crudMenu.add_command(label="update", command=update)
crudMenu.add_command(label="delete",command=delete)

helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="about")

menuBar.add_cascade(label="OPTIONS",menu=bbddMenu )
menuBar.add_cascade(label="CLEAR",menu=deleteMenu )
menuBar.add_cascade(label="FUNCTIONS",menu=crudMenu )
menuBar.add_cascade(label="HELP",menu=helpMenu )

# text inputs: entries #campos de texto

frame = Frame(root)
frame.pack()
frame.config(width="650", height="450")


myId=StringVar()
myName=StringVar()
myLastName=StringVar()
myPassword=StringVar()
myDirection=StringVar()

inputId = Entry(frame, textvariable=myId)
inputId.grid(row=0, column=1,padx=10, pady=10)


inputNombre = Entry(frame, textvariable=myName)
inputNombre.grid(row=1, column=1,padx=10, pady=10)
inputNombre.config(fg="green", justify="left")


inputApellido = Entry(frame, textvariable=myLastName)
inputApellido.grid(row=2, column=1,padx=10, pady=10)
inputApellido.config(fg="green", justify="left")

inputPassword = Entry(frame, textvariable=myPassword)
inputPassword.grid(row=3, column=1,padx=10, pady=10)
inputPassword.config(justify="left", show="*")

inputDireccion = Entry(frame, textvariable=myDirection)
inputDireccion.grid(row=4, column=1,padx=10, pady=10)
inputDireccion.config(fg="green", justify="left")

textComments = Text(frame, width=16, height=5)
textComments.grid(row=5, column=1,padx=10, pady=10)
scrollVert=Scrollbar(frame, command=textComments.yview)
scrollVert.grid(row=5, column=2,padx=10, sticky="nsew")
textComments.config(yscrollcommand=scrollVert.set)

#labels #tituos campos

idLabel = Label(frame, text="Id:")
idLabel.grid(row=0,column=0, sticky="e", padx=10, pady=10)


nombreLabel = Label(frame, text="Name: ")
nombreLabel.grid(row=1,column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(frame, text="Last Name: ")
apellidoLabel.grid(row=2,column=0, sticky="e", padx=10, pady=10)

passwordLabel = Label(frame, text="Password")
passwordLabel.grid(row=3,column=0, sticky="e", padx=10, pady=10)

direcciónLabel = Label(frame, text="Direction: ")
direcciónLabel.grid(row=4,column=0, sticky="e", padx=10, pady=10)

comentariosLabel = Label(frame, text="Comments: ")
comentariosLabel.grid(row=5,column=0, sticky="e", padx=10, pady=10)

#Buttons
frame1=Frame(root)
frame1.pack()

botonC= Button(frame1, text="Create", command=create)
botonC.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonR= Button(frame1, text="Read", command=read)
botonR.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonU= Button(frame1, text="Update", command=update)
botonU.grid(row=1, column=2, sticky="e", padx=10, pady=10)
            
botonD= Button(frame1, text="Delete", command=delete)
botonD.grid(row=1, column=3, sticky="e", padx=10, pady=10)


root.mainloop()