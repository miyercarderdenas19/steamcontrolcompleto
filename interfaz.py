from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image


class Producto:
    def __init__(self, ventana_producto):
        self.window = ventana_producto
        self.window.title("STEAMCONTROL")
        self.window.geometry("1200x700")
        self.window.resizable(0, 0)
        self.window.config(bd=10)

        "--------------- Titulo --------------------"
        titulo = Label(ventana_producto, text="REGISTRO DE EQUIPOS", fg="black", font=("Comic Sans", 17, "bold"),
                       pady=10)
        titulo.pack()

        "--------------- Logos productos --------------------"
        frame_logo_productos = LabelFrame(ventana_producto)
        frame_logo_productos.config(bd=0)
        frame_logo_productos.pack()

        # Logo SAMSONLOGO
        imagen_samson = Image.open("imagenes/SAMSONLOGO.png")
        nueva_imagen_samson = imagen_samson.resize((60, 60))
        render_samson = ImageTk.PhotoImage(nueva_imagen_samson)
        label_samson = Label(frame_logo_productos, image=render_samson)
        label_samson.image = render_samson
        label_samson.grid(row=0, column=0, padx=15, pady=5)

        # Logo PrismaLOGO
        imagen_prisma = Image.open("imagenes/PrismaLOGO.png")
        nueva_imagen_prisma = imagen_prisma.resize((60, 60))
        render_prisma = ImageTk.PhotoImage(nueva_imagen_prisma)
        label_prisma = Label(frame_logo_productos, image=render_prisma)
        label_prisma.image = render_prisma
        label_prisma.grid(row=0, column=1, padx=15, pady=5)

        # Logo WilkersonVLOGO
        imagen_wilkerson = Image.open("imagenes/wilkersonLOGO.png")
        nueva_imagen_wilkerson = imagen_wilkerson.resize((60, 60))
        render_wilkerson = ImageTk.PhotoImage(nueva_imagen_wilkerson)
        label_wilkerson = Label(frame_logo_productos, image=render_wilkerson)
        label_wilkerson.image = render_wilkerson
        label_wilkerson.grid(row=0, column=2, padx=15, pady=5)

        # logo BurkertLOGO
        imagen_burkert = Image.open("imagenes/burkertLOGO.png")
        nueva_imagen_burkert = imagen_burkert.resize((60, 60))
        render_burkert = ImageTk.PhotoImage(nueva_imagen_burkert)
        label_burkert = Label(frame_logo_productos, image=render_burkert)
        label_burkert.image = render_burkert
        label_burkert.grid(row=0, column=3, padx=15, pady=5)

        # logo gastLOGO
        imagen_gast = Image.open("imagenes/gastLOGO.png")
        nueva_imagen_gast = imagen_gast.resize((60, 60))
        render_gast = ImageTk.PhotoImage(nueva_imagen_gast)
        label_gast = Label(frame_logo_productos, image=render_gast)
        label_gast.image = render_gast
        label_gast.grid(row=0, column=4, padx=15, pady=5)

        # logo rcmLOGO
        imagen_rcm = Image.open("imagenes/rcmLOGO.png")
        nueva_imagen_rcm = imagen_rcm.resize((60, 60))
        render_rcm = ImageTk.PhotoImage(nueva_imagen_rcm)
        label_rcm = Label(frame_logo_productos, image=render_rcm)
        label_rcm.image = render_rcm
        label_rcm.grid(row=0, column=5, padx=15, pady=5)

        # logo tlvLOGO
        imagen_tlv = Image.open("imagenes/tlvLOGO.png")
        nueva_imagen_tlv = imagen_tlv.resize((60, 60))
        render_tlv = ImageTk.PhotoImage(nueva_imagen_tlv)
        label_tlv = Label(frame_logo_productos, image=render_tlv)
        label_tlv.image = render_tlv
        label_tlv.grid(row=0, column=8, padx=15, pady=5)

        "--------------- Frame marco --------------------"
        marco = LabelFrame(ventana_producto, text="Informacion del producto", font=("Comic Sans", 10, "bold"), pady=50)

        marco.pack()

        "--------------- Formulario --------------------"
        label_marca = Label(marco, text="Tipo de mantenimiento: ", font=("Comic Sans", 10, "bold"))
        label_marca.grid(row=0, column=0, sticky='s', padx=5, pady=8)
        self.combo_marca = ttk.Combobox(marco,
                                        values=["-Selecione-", "Configuracion", "Correctivo", "Estudio", "Preventivo", "N/A", "No Reparable", "ICPV"],
                                        width=22, state="readonly")
        self.combo_marca.current(0)
        self.combo_marca.grid(row=0, column=1, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_responsable = Label(marco, text="Lugar: ", font=("Comic Sans", 10, "bold"))
        label_responsable.grid(row=1, column=0, sticky='s', padx=5, pady=8)
        self.combo_responsable = ttk.Combobox(marco,
                                              values=["-Selecione-", "Steamcontrol", "Planta del Cliente"], 
                                              width=22, state="readonly")
        self.combo_responsable.current(0)
        self.combo_responsable.grid(row=1, column=1, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_lugar = Label(marco, text="Responsable: ", font=("Comic Sans", 10, "bold"))
        label_lugar.grid(row=0, column=2, sticky='s', padx=5, pady=9)
        self.combo_lugar = ttk.Combobox(marco,
                                        values=["-Selecione-", "Juan Araque", "Pedro Cofles", "Heldert Blanco", "Robinson Martinez", "Esteban Meza", "Juan Araque / Pedro Cofles"],
                                        width=22, state="readonly")
        self.combo_lugar.current(0)
        self.combo_lugar.grid(row=1, column=3, padx=5, pady=0)

        "--------------------------------------------------------------------------------"
        label_conocimiento = Label(marco, text="Torcometro: ", font=("Comic Sans", 10, "bold"))
        label_conocimiento.grid(row=0, column=2, sticky='s', padx=5, pady=8)
        self.combo_conocimiento = ttk.Combobox(marco,
                                               values=["-Selecione-", "10-411111", "14-175037", "G-9/NI-002BP", "N/A"],  
                                               width=22, state="readonly")
        self.combo_conocimiento.current(0)
        self.combo_conocimiento.grid(row=0, column=3, padx=5, pady=8)

        "--------------------------------------------------------------------------------"
        label_descripcion = Label(marco, text="Descripcion: ", font=("Comic Sans", 10, "bold"))
        label_descripcion.grid(row=2, column=0, sticky='s', padx=10, pady=3)
        self.descripcion = Text(marco, width=80, height=5)  # Use Text instead of Entry
        self.descripcion.grid(row=2, column=1, padx=10, pady=8)

        "--------------- Frame botones --------------------"
        frame_botones = Frame(ventana_producto)
        frame_botones.pack()

        "--------------- Botones --------------------"
        boton_registrar = Button(frame_botones, text="REGISTRAR", command=self.Agregar_producto, height=2, width=10,
                                 bg="green", fg="white", font=("Comic Sans", 10, "bold"))
        boton_registrar.grid(row=0, column=1, padx=10, pady=15)

        "--------------- Tabla --------------------"
        self.tree = ttk.Treeview(height=10, columns=("columna1", "columna2", "columna3"))

        self.tree.heading("#0", text='MODELO', anchor=CENTER)
        self.tree.column("#0", width=250, minwidth=75, stretch=NO)

        # Campos desplegables en lugar de Entry
        combo_tamaño_header = ttk.Combobox(self.tree, values=["Tamaño 1", "Tamaño 2", "Tamaño 3"], state="readonly",
                                           width=22)
        
        self.tree.column("columna1", width=250, minwidth=75, stretch=NO)

        combo_cantidad_header = ttk.Combobox(self.tree, values=["Cantidad 1", "Cantidad 2", "Cantidad 3"],
                                             state="readonly", width=22)
        
        self.tree.column("columna2", width=250, minwidth=75, stretch=NO)

        self.tree.pack()

    "--------------- CRUD --------------------"

    def Agregar_producto(self):
        if self.Validar_formulario_completo():
            messagebox.showinfo("REGISTRO EXITOSO", f'Producto registrado: {self.combo_marca.get()}')
            print('REGISTRADO')
        self.Limpiar_formulario()

    def Eliminar_producto(self):
        messagebox.showinfo("ELIMINAR", "Eliminar producto")
        # Implementar la lógica de eliminación aquí
        self.Limpiar_formulario()

    def Editar_producto(self):
        messagebox.showinfo("EDITAR", "Editar producto")
        # Implementar la lógica de edición aquí
        self.Limpiar_formulario()

    "--------------- OTRAS FUNCIONES --------------------"

    def Validar_formulario_completo(self):
        if len(self.combo_marca.get()) != 0 and len(self.combo_responsable.get()) != 0 and len(
                self.combo_lugar.get()) != 0 and len(self.combo_conocimiento.get()) != 0 and len(
            self.descripcion.get("1.0", END)) != 0:
            return True
        else:
            messagebox.showerror("ERROR", "Complete todos los campos del formulario")
            return False

    def Limpiar_formulario(self):
        self.combo_marca.set('')
        self.combo_responsable.set('')
        self.combo_lugar.set('')
        self.combo_conocimiento.set('')
        self.descripcion.delete('1.0', END)


if __name__ == '__main__':
    # Crear la ventana principal
    root = Tk()
    root.title("steamcontrol")
    root.iconbitmap("steamcontrol.ico")
    root.config(cursor="hand2")

    # Crear la instancia de la clase Producto (interfaz de registro de equipos)
    ventana_producto = Producto(root)

    # Iniciar el bucle principal de la interfaz gráfica
    root.mainloop()
