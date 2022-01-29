class OSINT():
    __slots__ = ['nombreYapellido','sobrenombre']
    def __init__(self,nombreYapellido) -> None:
        self.nombreYapellido = nombreYapellido.split()
    
    def posibles_nombres_de_usuario(self) -> list:
        opcion = input("""

este usuario tiene un sobrenombre?
1. si
2. no
opcion: """)
        print()
        if opcion == "1":
            self.sobrenombre = input("ingrese el sobrenombre: ")
        else:
            cont = 1
            while len(self.nombreYapellido[0])!=cont-1:
                print("mostrando posible sobre nombre")
                print(self.nombreYapellido[0][0:cont])
                opcion = input("es posible que este sea su sobrenombre?\n1. si\n2. no\n3. no intentar generar otro sobrenmbre\nopcion: ")
                if opcion == "1":
                    self.sobrenombre = self.nombreYapellido[0][0:cont]
                    break
                elif opcion == "2":
                    cont += 1
                elif opcion == "3":
                    self.sobrenombre = self.nombreYapellido[0]
                    break
        lista = []
        lista.append(self.nombreYapellido[0]+self.nombreYapellido[1])
        lista.append(self.nombreYapellido[1]+self.nombreYapellido[0])

        lista.append(self.sobrenombre+self.nombreYapellido[1])
        lista.append(self.sobrenombre+self.sobrenombre[-1]+self.nombreYapellido[1])

        lista.append(self.sobrenombre+"_"+self.nombreYapellido[1])
        lista.append(self.sobrenombre+self.sobrenombre[-1]+"_"+self.nombreYapellido[1])
        
        lista.append(self.sobrenombre+self.nombreYapellido[1]+"_")
        lista.append(self.sobrenombre+"_"+self.nombreYapellido[1]+"_")
        lista.append(self.sobrenombre+self.sobrenombre[-1]+"_"+self.nombreYapellido[1]+"_")

        lista.append(self.nombreYapellido[0]+"_"+self.nombreYapellido[1])
        lista.append(self.nombreYapellido[1]+"_"+self.nombreYapellido[0])
        lista.append("_"+self.nombreYapellido[0]+"_"+self.nombreYapellido[1])
        lista.append(self.nombreYapellido[0]+"_"+self.nombreYapellido[1]+"_")

        lista.append(self.sobrenombre+"."+self.nombreYapellido[1])
        lista.append(self.sobrenombre+self.sobrenombre[-1]+"."+self.nombreYapellido[1])

        lista.append(self.nombreYapellido[0]+"."+self.nombreYapellido[1])
        lista.append(self.nombreYapellido[1]+"."+self.nombreYapellido[0])

        lista.append("_"+self.nombreYapellido[0]+"."+self.nombreYapellido[1])
        lista.append(self.nombreYapellido[0]+"."+self.nombreYapellido[1]+"_")

        return lista
        
    def generar_posibles_redes(self):
        nombres_de_usuario = self.posibles_nombres_de_usuario()
        print("posibles nombres de usuario:",nombres_de_usuario)
        print("posibles linkedin:")
        for i in range(3):
            print(f"linkedin: https://www.linkedin.com/in/{nombres_de_usuario[i]}/")
        
        print()
        print("posibles twitter:")
        for i in nombres_de_usuario:
            print(f"twitter: https://twitter.com/{i}/")
        
        print()
        print("posibles instagram:")
        for i in nombres_de_usuario:
            print(f"instagram: https://www.instagram.com/{i}/?hl=es-la")

if __name__ == '__main__':
    nombreYapellido = input("ingrese su nombre y apellido: ")
    osint = OSINT(nombreYapellido)
    osint.generar_posibles_redes()