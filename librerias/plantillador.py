"""
OscarGonzalez1987/plantillador_py is licensed under the
GNU General Public License v3.0

Permissions of this strong copyleft license are conditioned on making available 
complete source code of licensed works and modifications, which include larger 
works using a licensed work, under the same license. Copyright and license notices 
must be preserved. Contributors provide an express grant of patent rights.
"""

def plantillador(archivo, nombre, datos):

    def ejecutar(archivo, nombre, datos):
        leer = open(archivo, "r")
        inicia_concatenado(nombre)
        ciclo_lecto_escritura(archivo, leer, datos)
        leer.close()
        
    def inicia_concatenado(nombre):   
        escribe = open(nombre, "w")
        escribe.write("")
        escribe.close()
    
    def ciclo_lecto_escritura(archivo, leer, datos):
        nro_lineas = consulta_de_lineas(archivo, leer)
        nn=0
        while(nro_lineas > nn):
            #-------------------------------------
            toma = leer.readline()
            contenido = tratamiento(toma, datos).rstrip("\n")
            escribe_ciclo(contenido)
            #-------------------------------------
            nn+=1

    def consulta_de_lineas(archivo, leer):
        nro_lineas = len(leer.readlines())
        leer.seek(0)
        return nro_lineas
        
    def tratamiento(toma, datos):
        y = 0
        while(y < len(datos)):
            x = 0
            primero = datos[y][x]
            segundo = datos[y][x+1]
            toma = toma.replace(primero, segundo)
            y += 1
        return toma        
          
    def escribe_ciclo(contenido):    
        escribe = open(nombre, "a")
        escribe.write(contenido + "\n")
        escribe.close()
        
    ejecutar(archivo, nombre, datos)
    
    

"""
#-------------------------------------
# ejemplo de uso en otro archivo (.py):
#-------------------------------------
# import librerias.concatenar as lbr
archivo = "archivo.py"
ruta = "../plantillas/"+ archivo
nombre = "../productos/plancha_"+ archivo
variable = "variable"
concatenar(ruta, nombre, variable)
"""















