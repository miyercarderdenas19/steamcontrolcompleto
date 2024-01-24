from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
from subprocess import call  # Agregado para importar la función call
import sys  # Agregado para importar el módulo sys
# Python image Library
from PIL import ImageTk, Image
import sqlite3

class Login:
    db_name = 'database_proyecto.db'
    
    def __init__(self, ventana_login):
        self.window = ventana_login  
        self.window.title("STEAMCONTROL")
        self.window.geometry("400x400")
        self.window.resizable(0, 0)
        self.window.config(bd=10)
        
        "--------------- Titulo --------------------"
        titulo = Label(ventana_login, text="INICIAR SESION", fg="black", font=("Comic Sans", 13, "bold"), pady=10).pack()

        "--------------- Loginlogo --------------------"
        imagen_login = Image.open("c:/nueva carpeta/imagenes/descarga.jpg")
        nueva_imagen = imagen_login.resize((150, 60))
        render = ImageTk.PhotoImage(nueva_imagen)
        label_imagen = Label(ventana_login, image=render)
        label_imagen.image = render
        label_imagen.pack(pady=5)

        "--------------- Marco --------------------"
        marco = LabelFrame(ventana_login, text="Ingrese sus datos", font=("Comic Sans", 10, "bold"))
        marco.config(bd=2)
        marco.pack()

        "--------------- Formulario --------------------"
        label_dni = Label(marco, text="ID: ", font=("Comic Sans", 10, "bold")).grid(row=0, column=0, sticky='s', padx=5, pady=10)
        self.dni = Entry(marco, width=25)
        self.dni.focus()
        self.dni.grid(row=0, column=1, padx=5, pady=10)

        label_nombres = Label(marco, text="Contraseña: ", font=("Comic Sans", 10, "bold")).grid(row=1, column=0, sticky='s', padx=10, pady=10)
        self.password = Entry(marco, width=25, show="*")
        self.password.grid(row=1, column=1, padx=10, pady=10)

        "--------------- Frame botones --------------------"
        frame_botones = Frame(ventana_login)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_ingresar = Button(frame_botones, text="INGRESAR", command=self.Login, height=2, width=12, bg="green", fg="white", font=("Comic Sans", 10, "bold")).grid(row=0, column=1, padx=10, pady=15)
       
        
        
    
    def Validar_login(self, dni, password):
        with sqlite3.connect(self.db_name) as conexion:
            cursor = conexion.cursor()
            sql = f"SELECT * FROM Usuarios WHERE DNI = {dni} AND Contraseña = '{password}'"
            cursor.execute(sql)
            validacion = cursor.fetchall()  # obtener respuesta como lista
            cursor.close()
            return validacion
        
    def Validar_formulario_completo(self):
        if len(self.dni.get()) != 0 and len(self.password.get()) != 0:
            return True
        else:
            messagebox.showerror("ERROR DE INGRESO", "Ingrese su DNI y contraseña!!!")    
    
    def Login(self):
        if self.Validar_formulario_completo():
            dni = self.dni.get()
            password = self.password.get()
            dato = self.Validar_login(dni, password)
            if dato:
                messagebox.showinfo("BIENVENIDO", "Datos ingresados correctamente")  
            else:
                messagebox.showerror("ERROR DE INGRESO", "DNI o contraseña incorrecto") 
    
    # Call registro              
    def LLamar_registro(self):
        ventana_login.destroy()    
        call([sys.executable, 'D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/1-Formulario_registro.py', 'htmlfilename.htm'])

    # Call recuperar        
    def LLamar_recuperar(self):
        ventana_login.destroy()    
        call([sys.executable, 'D:/EIGHTA/PYTHON-TKINTER/SISTEMA DESKTOP/3-Recuperar_password.py', 'htmlfilename.htm'])
 
# Verificar si el módulo ha sido ejecutado correctamente  
if __name__ == '__main__':
    ventana_login = Tk()
    application = Login(ventana_login)
    ventana_login.mainloop()
