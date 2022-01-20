import os

opcion = '1' 
def calcularHash(archivos):
    print("calcular hash")
    archivo = input("Ingrese el nombre del archivo: ")
    if archivo in archivos:
        print("El archivo existe")
        print('hash: ',hash(archivo))
    else:
        print("El archivo no existe")

def verificarHash(archivos):
    print("verificar hash")
    archivo = input("Ingrese el nombre del archivo: ")
    if archivo in archivos:
        print("El archivo existe")
        hashaaverificar = input("Ingrese el hash del archivo: ")
        print('hash: ',hash(archivo))
        print('hash a verificar: ',hashaaverificar)
        if str(hash(archivo)) == hashaaverificar:
            print("El hash es correcto")
        else:
            print("El hash es incorrecto")
    else:
        print("El archivo no existe")

def verarchivos(archivos):
    print("ver archivos")
    for file in archivos:
        print(file)

def moverse():
    carpeta = input("Ingrese el nombre de la carpeta: ")
    if os.path.isdir(carpeta):
        print("La carpeta existe")
        os.chdir(carpeta)
    else:
        print("La carpeta no existe")

def vercarpetas(archivos):
    print("ver carpetas")
    for carpeta in archivos:
        print(carpeta)

def vercarpetaactual():
    print("la carpeta actual es: ")
    print(os.getcwd())

def retroceder():
    print("retroceder")
    os.chdir('..')


while opcion != "0":
    archivos = os.listdir(os.getcwd())
    print("""
1. calcular hash de un archivo
2. Verificar de un archivo
4. Ver archivos
5. moverse a otra carpeta
6. ver carpetas
7. ver carpeta actual
8. retornar al directorio anterior
0. Salir
    """)
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        calcularHash(archivos)

    elif opcion == "2":
        verificarHash(archivos)

    elif opcion == "4":
        verarchivos(archivos)

    elif opcion == "5":
        moverse()
    
    elif opcion == "6":
        vercarpetas(archivos)

    elif opcion == "7":
        vercarpetaactual()

    elif opcion == "8":
        retroceder()
    
    elif opcion == "0":
        print("Saliendo...")
    
    else:
        print("Opción inválida")