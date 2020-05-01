"""
OscarGonzalez1987/concatenador is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license notices 
must be preserved. Contributors provide an express grant of patent rights.
"""

import librerias.plantillador as lbr

# configuración
# ------------------------------------------------------------------------------------
# plantilla
# ------------------------------------------------------------------------------------
archivo = "archivo.py"
archivo_ruta = "plantillas/"+ archivo

# destino del resultado de la implementación de la plantilla
# ------------------------------------------------------------------------------------
nombre = "productos/resultado_plantilla_"+ archivo
linea = ("-"*40)
# entrada de datos
# ------------------------------------------------------------------------------------
print("entrada de datos:\n" + linea)
titulo = str(input("titilo\t(Ej.: ventana):\t\t\t"))
icono = str(input("icono\t(Ej.: imagenes/imagen.ico):\t"))
ancho = str(input("ancho\t(Ej.: 300):\t\t\t"))
alto = str(input("alto\t(Ej.: 300):\t\t\t"))
color = str(input("color\t(Ej.: blue):\t\t\t"))
redimencionamiento = str(input("\nredimencionamiento\n\t(vertical, horizontal):\t\t"))

# sustitución de datos en la plantilla 
# ------------------------------------------------------------------------------------
print("\n" + linea + "\nsustitución de datos en la plantilla\n")
datos = {}
datos[0] = ("ventana", titulo)
datos[1] = ("imagenes/imagen.ico", icono)
datos[2] = ("300", ancho)
datos[3] = ("300", alto)
datos[4] = ("blue", color)
datos[5] = ("vertical", redimencionamiento)

# implementación de la libreria plantillador 
# ------------------------------------------------------------------------------------
lbr.plantillador(archivo_ruta, nombre, datos)

mensaje = (linea + "\nEjecución completada.\n")
mensaje += ("Por favor revice el destino:\n\n\t" + nombre)
fin = input(mensaje)















