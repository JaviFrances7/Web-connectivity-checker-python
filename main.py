import tkinter as tk # libreria interfaz grafica
import urllib.request # librerias que trabaja con URL

# ---------------------------
# creamos la ventana principal
# ---------------------------
ventana = tk.Tk()
ventana.title('Prueba conectividad sitios web')
ventana.geometry("1000x800") 
ventana.resizable(False, False)  # Evita que el usuario cambie el tamaño

# ---------------------------
# creamos la funcion que comprueba la URL
# ---------------------------
def comprobar_url():
    url_usuario = entrada_usuario.get() # coje lo que ha escrito el usuario

    if not url_usuario: # comprueba si la cadena esta vacia
        etiqueta_resultado.config(text="Por favor, introduce una URL", fg="red") # cambia el texto de la etiqueta resultado
        return # para que salga de la funcion y no entre en bucle

    if not url_usuario.startswith("http://") and not url_usuario.startswith("https://"):
        url_usuario = "http://" + url_usuario

    '''CREAMOS UN TRY/EXCEPT EL CUAL INTENTA CONECTARSE A INTERNET SI PUEDE ENVIA RESPUESTA SINO PASA AL EXCEPT'''
    try:
        respuesta = urllib.request.urlopen(url_usuario)
        http = respuesta.getcode()

        if http == 200:
            etiqueta_resultado.config(
                text= f"Conectado correctamente a {url_usuario} (HTTP {http})",
                fg = 'green'
             )

            
        
        else:
            etiqueta_resultado.config(
                text= f"El sitio respondió con código HTTP {http}",
                fg= "orange"
            )

    except Exception:
        etiqueta_resultado.config(
            text= "No se pudo conectar al sitio web",
            fg= "red"
        )



# ---------------------------
# creamos una etiqueta para decirle al usuario lo que tiene que hacer
# ---------------------------
etiqueta_usuario = tk.Label(
    ventana,
    text = 'Introduzca la URL del sitio web:',
    font= ("Arial", 14),
    wraplength= 650,      # Ajusta el texto si es muy largo
    justify ="center"
)
etiqueta_usuario.pack(pady=20) # colocamos la etiqueta en pantalla

# ---------------------------
# creamos la entrada para que el usuario escriba la URL
# ---------------------------
entrada_usuario = tk.Entry(
     ventana,
    font= ("Arial", 14),
    width= 120,
    justify = 'center'
)
entrada_usuario.pack(pady=10)

# ---------------------------
# creamos un scroll para que el usuario pueda ver la URL completa moviendo con libertad
# ---------------------------
scroll = tk.Scrollbar(ventana, orient="horizontal", command=entrada_usuario.xview) # crear scroll
entrada_usuario.config(xscrollcommand=scroll.set) # conectar el scroll al Entry del usuario
scroll.pack(fill="x") # colocar barra en pantalla


# ---------------------------
# creamos un boton que compruebe conectividad
# ---------------------------
boton = tk.Button(
    ventana,
    text = 'Comprobar conectividad a internet',
    command = comprobar_url
)
boton.config(bg="blue", fg="white", font=("Arial", 14, "bold"))
boton.pack(pady=15)

# Con Enter funciona igual que al pulsar el botón
entrada_usuario.bind("<Return>", lambda event: comprobar_url())


# ---------------------------
# creamos una etiqueta para el resultado 
# ---------------------------
etiqueta_resultado = tk.Label(
    ventana,
    text = ' ',
    font= ("Arial", 16),
            fg= "blue",
            justify= "center",
    wraplength = 650
)
etiqueta_resultado.pack(pady=20)

ventana.mainloop() # ejecutar ventana y no se cierre


