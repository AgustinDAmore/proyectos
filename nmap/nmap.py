import subprocess, diccionarioPuertos
class nmap():

    __slots__ = ['ip']

    def __init__(self,interfazRed = "wlan0") -> None:
        self.ip = str(subprocess.check_output("ifconfig"))
        self.ip = self.ip[self.ip.index(interfazRed):-1]
        self.ip = self.ip[self.ip.index("inet "):self.ip.index("netmask")]
        self.ip = self.ip.replace("inet ","")
        self.ip = self.ip[::-1]
        self.ip = self.ip.replace(self.ip[0:self.ip.index(".")],"0")
        self.ip = self.ip[::-1]
    
    def ipenlared(self):
        lista = list(subprocess.check_output(f"nmap -sP {self.ip}/24",shell=True).decode("utf-8").split("\n"))
        listadeip = []
        for i in lista:
            if "Nmap scan report for" in i:
                listadeip.append(i.replace("Nmap scan report for ",""))

        return listadeip

    def puertosabiertos(self,ip):
        lista = subprocess.check_output(f"nmap --open {ip}",shell=True).decode("utf-8").split("\n")
        corte = True
        for i in range(len(lista)):
            if "PORT" in lista[i] and corte:
                lista = lista[i:-3]
                break
        else:
            return ["No hay puertos abiertos"]

        return lista
    
    def puertosabiertosconinformacion(self,ip):
        lista = self.puertosabiertos(ip)
        listaDePuertos = diccionarioPuertos.Puertos()
        for i in range(len(lista)):
            if "/tcp" in lista[i]:
                try:
                    lista[i] = (lista[i],f"{listaDePuertos.diccionario(ip)[lista[i][:lista[i].index('/tcp')]]}")
                    lista[i] = str(lista[i]).replace(",","").replace(")","").replace("(","").replace("'","")
                except KeyError:
                    pass

        return lista

if __name__ == '__main__':
    nmap = nmap("wlan0")
    dispositivos = nmap.ipenlared()
    for i in dispositivos:
        print(i)
        for i in nmap.puertosabiertos(i):
            print(i)
        print("\n")
    print("\n")
    for i in dispositivos:
        print(i)
        for i in nmap.puertosabiertosconinformacion(i):
            print(i)
        print("\n")