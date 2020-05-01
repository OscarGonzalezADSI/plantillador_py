datos={}

datos[0] = ("ventana", "remplazo 1")
datos[1] = ("imagenes/imagen.ico", "remplazo 2")
datos[2] = ("300", "remplazo 3")
datos[3] = ("300", "remplazo 4")
datos[4] = ("blue", "remplazo 5")
datos[5] = ("vertical", "remplazo 6")

def tratamiento(datos):
    y = 0
    while(y < len(datos)):
        x = 0
        primero = datos[y][x]
        segundo = datos[y][x+1]
        print(primero, segundo)
        y += 1

tratamiento(datos)

pause = input("")


