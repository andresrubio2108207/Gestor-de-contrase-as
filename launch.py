from tkinter import Tk, Label, Button, Entry, Frame, messagebox
from PIL import Image, ImageTk

class Login:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("400x700")
        self.ventana.title("Login de Andres")

        fondo = "#87CEEB"

        # Frames

        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(bg = fondo)
        self.frame_superior.pack(fill = "both", expand = True)

        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(bg=fondo)
        self.frame_inferior.pack(fill="both", expand = True)

        self.frame_inferior.columnconfigure(0, weight = 1 )
        self.frame_inferior.columnconfigure(1, weight = 1 )

        self.titulo = Label(self.frame_superior,
                    text = "Bienvenido!",
                    font = ("Calisto MT", 36, "bold"),  
                    bg = fondo)
        self.titulo.pack(side = "top", pady = 20)

        # Imagenes

        self.img = Image.open("Images/User-Image.webp")  
        self.img = self.img.resize((300, 180))
        self.render = ImageTk.PhotoImage(self.img)
        self.fondo = Label(self.frame_superior, image = self.render, bg = fondo)
        self.fondo.pack(expand = True, fill = "both", side = "top")

        # Datos del usuario

        self.usuario_label = Label(self.frame_inferior, 
                                   text="Usuario:", 
                                   font=("Calisto MT", 14), 
                                   bg=fondo)
        self.usuario_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.usuario_entry = Entry(self.frame_inferior, 
                                   font=("Calisto MT", 14))
        self.usuario_entry.grid(row=0, column=1, padx=10, pady=10)

        self.contraseña_label = Label(self.frame_inferior, 
                                      text="Contraseña:", 
                                      font=("Calisto MT", 14), 
                                      bg=fondo)
        self.contraseña_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.contraseña_entry = Entry(self.frame_inferior, 
                                      font=("Calisto MT", 14), 
                                      show="*")
        self.contraseña_entry.grid(row=1, column=1, padx=10, pady=10)

        # Boton de inicio de sesión

        self.login_button = Button(self.frame_inferior, 
                                   text="Iniciar sesión", 
                                   font=("Calisto MT", 14), 
                                   bg="#4682B4", 
                                   fg="white", 
                                   command=self.iniciar_sesion)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def iniciar_sesion(self):

        # Leer el usuario y contraseña desde los archivos en la carpeta "User dates"

        with open("usuario.txt", "r", encoding="utf-8") as archivo_usuario:
            usuario_guardado = archivo_usuario.read()
        with open("password.txt", "r", encoding="utf-8") as archivo_password:
            contraseña_guardada = archivo_password.read()

        # Obtener los valores ingresados por el usuario

        usuario = self.usuario_entry.get()
        contraseña = self.contraseña_entry.get()

        # Comparar los valores
        
        if usuario == usuario_guardado and contraseña == contraseña_guardada:
            messagebox.showinfo("Inicio de sesión", "¡Inicio de sesión exitoso!")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

Login().ventana.mainloop()
