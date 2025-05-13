# INICIO DE SESIÓN DINÁMICO EN PYTHON #

# RICH

from rich import print
from rich.table import Table
from rich.console import Console
from rich.progress import track

# ADICIONALES

import random
import time

console = Console()


# Función para mostrar la bienvenida al usuario

def bienvenida():
    console.print("\n[bright_white]!Bienvenido al![/bright_white]", justify="center")
    console.print("[bright_red]Inicio de sesión dinámico en Python[/bright_red]", justify="center")
    console.print("[bright_cyan]¡Disfruta de la experiencia![/bright_cyan]", justify="center")
    console.print("Responde \"Si\" para comenzar el registro\n", justify="center")
    

# Función para iniciar sesión

def iniciar_sesion():

    # Comprobamos si el usuario quiere iniciar sesión o no

    while True:
        respuesta = input("¿Quieres iniciar tu registro? (Si/No): ").lower()
        if respuesta == "si":

            # Mensaje de confirmación y barra de progreso

            console.print("\n[bright_green]¡Perfecto! Vamos a iniciar sesión...[/bright_green]\n", justify="center")
            for i in track(range(10), description="Cargando..."):
                time.sleep(0.3)
            break

        elif respuesta == "no":
            # Mensaje de despedida si el usuario no desea continuar

            console.print("[bright_red]¡Hasta luego![/bright_red]", justify="center")
            exit()
        else:
            # Mensaje de error si la respuesta no es válida

            console.print("\n[bright_yellow]Respuesta no válida. Por favor, responde 'Si' o 'No'.[/bright_yellow]", justify="center")


# Función para crear un usuario

def crear_usuario():
    global user, password  # Declaramos estas variables como globales para usarlas en otras funciones

    # Lista de diccionario con sus keys (longitud) y valores (contraseñas)

    contraseñas = {
        3: ["sol", "pan", "luz", "voz", "mar"],
        4: ["luna", "casa", "río", "nube", "pato"],
        5: ["perro", "flore", "ratón", "hojas", "salud"],
        6: ["camino", "garras", "pirata", "laguna", "corral"],
        7: ["caracol", "lechuga", "abejero", "zapatos", "mañana"],
        8: ["caminito", "ternuras", "campanas", "cangrejo", "pasteles"],
        9: ["mariposas", "dinosaurio", "sandalias", "ventanaso", "gallinero"],
        10: ["bicicletas", "escaleras", "laberintos", "camarones", "navegante"]
    }

    # Mensaje inicial para crear un usuario

    console.print("\n[bright_green]¡Vamos a crear tu usuario![/bright_green]\n", justify="center")

    # Solicitar el nombre de usuario

    user = console.input("[bright_white]Introduce tu nombre de usuario: [/bright_white]")
    pregunta = console.input("[bright_white]¿Quieres generar una contraseña aleatoria? (Si/No): ").lower()

    if pregunta == "si":
        largo = 0
        while largo < 3 or largo > 10:
            largo = int(console.input("[bright_white]¿De cuántos caracteres deseas que sea tu contraseña? (3-10): [/bright_white]"))
            if largo < 3 or largo > 10:
                console.print("[bright_red]Por favor, elige un número entre 3 y 10.[/bright_red]", justify="center")

        # Seleccionar una contraseña aleatoria del diccionario

        password = random.choice(contraseñas[largo])
        console.print(f"\n[bright_green]Tu contraseña generada es: {password}[/bright_green]\n", justify="center")
    else:
        # Si el usuario no desea una contraseña aleatoria, se solicita manualmente

        password = console.input("[bright_white]Introduce tu contraseña: [/bright_white]")

    # Guardar el usuario en usuario.txt

    with open("usuario.txt", "w", encoding="utf-8") as archivo_usuario:
        archivo_usuario.write(user)

    # Guardar la contraseña en password.txt

    with open("password.txt", "w", encoding="utf-8") as archivo_password:
        archivo_password.write(password)

    # Barra de progreso para simular la creación del usuario

    for i in track(range(10), description="Cargando..."):
        time.sleep(0.3)

    # Mensaje de confirmación de creación de usuario

    console.print(f"\n[bright_cyan]Usuario '{user}' creado con éxito y ha sido almacenado en 'usuario.txt' y 'password.txt'. :)[/bright_cyan]", justify="center")
    console.print("[bright_yellow]Recuerda mantener tu contraseña en privado.[/bright_yellow]", justify="center")

# Función para mostrar los resultados en una tabla

def mostrar_resultados():
     
    # Si el usuario lo desea, se imprimirá una tabla con sus datos

    pregunta_resultados = console.input("\n[bright_white]Escribe 'Si' para ver tu usuario y contraseña o 'No' si deseas salir del programa: [/bright_white]").lower()
    if pregunta_resultados == "si":

        for i in track(range(10), description="Cargando..."):
            time.sleep(0.2)

        # Crear la tabla con el título y estilo

        table = Table(title="Datos", style="white")

        # Definir las columnas de la tabla

        table.add_column("Usuario", justify="center", style="cyan", no_wrap=True)
        table.add_column("Contraseña", justify="center", style="magenta")
        table.add_column("Estado", justify="center", style="green")

        # Agregar los datos del usuario como fila

        table.add_row(f"{user}", f"{password}", "Activo")
        console.print(table)
    
    elif pregunta_resultados == "no":

        # Mensaje de despedida si el usuario no desea ver los resultados

        console.print("[bright_red]¡Hasta luego![/bright_red]", justify="center")
        exit()
    
    else:
        
        # Mensaje de error si la respuesta no es válida

        console.print("\n[bright_yellow]Respuesta no válida. Por favor, responde 'Si' o 'No'.[/bright_yellow]", justify="center")
     
# Llamada a las funciones en orden para ejecutar el programa

if __name__ == "__main__":
    bienvenida()
    iniciar_sesion()
    crear_usuario()
    mostrar_resultados()