from tkinter import Tk

root = Tk()

root.title("steamcontrol")  # Función para poner título a la ventana
root.geometry("600x300")    # Dimensiones de la ventana
root.iconbitmap("steamcontrol.ico")  # Colocando un icono en la ventana (asegúrate de tener el archivo "steamcontrol.ico" en la misma carpeta)
root.resizable(0, 0)        # Hace que la ventana no sea redimensionable

root.config(bg="#808080", cursor="")  # Configuración de fondo y cursor

root.mainloop()
