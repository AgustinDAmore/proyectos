from typing import Any


class Puertos():
    def __init__(self) -> None:
        pass

    def diccionario(self,ip = Any) -> dict:
        return {
            "1": "Multiplexor TCP", 
            "5": "Entrada de trabajo remota",
            "7":"Protocolo Echo (Eco) Responde con eco a llamadas remotas",
            "9":"Protocolo Discard, elimina cualquier dato que recibe, sirve para la evaluación de conexiones",
            "11":"Servicio del sistema para listar los puertos conectados",
            "13":"Protocolo Daytime, envía la fecha y hora actuales",
            "17":"Quote of the Day, envía la cita del día",
            "18":"Protocolo de envío de mensajes",
            "19":"Protocolo Chargen o Generador de caracteres, envía flujos infinitos de caracteres",
            "20":"FTPS File Transfer Protocol (Protocolo de Transferencia de Ficheros) - datos",
            "21":"FTP File Transfer Protocol (Protocolo de Transferencia de Ficheros) - control", 
            "22": "conexiones seguras SSH y SFTP", 
            "23":"Telnet manejo remoto de equipo, inseguro",
            "25":"SMTP Simple Mail Transfer Protocol (Protocolo Simple de Transferencia de Correo)",
            "37":"Time Protocol. Sincroniza hora y fecha",
            "39":"Protocolo de ubicación de recursos",
            "42":"Servicio de nombres de Internet",
            "43":"Servicio de directorio WHOIS",
            "49":"Terminal Access Controller Access Control System para el acceso y autenticación basado en TCP/IP",
            "50":"Protocolo de verificación de correo remoto",
            "53":"DNS Domain Name System (Sistema de Nombres de Dominio)",
            "63":"Servicios extendidos de WHOIS (WHOIS++)",
            "66":"Software de red que permite acceso remoto entre los programas y la base de datos Oracle.",
            "67":"BOOTP BootStrap Protocol (servidor), también usado por DHCP",
            "68":"BOOTP BootStrap Protocol (cliente), también usado por DHCP",
            "69":"TFTP Trivial File Transfer Protocol (Protocolo Trivial de Transferencia de Ficheros)",
            "70":"Gopher",
            "79":"Finger",
            "80": f"http://{ip}",
            "88":"Kerberos Agente de autenticación",
            "95":"Extensión del protocolo Telnet",
            "101":"Servicios de nombres de host en máquinas SRI-NIC",
            "107":"Telnet remoto",
            "109":"POP2 Post Office Protocol (E-mail)",
            "110":"POP3 Post Office Protocol (E-mail)",
            "111":"sunrpc",
            "113":"ident (auth) antiguo sistema de identificación",
            "115":"SFTP (Simple FTP) Protocolo de transferencia de archivos simple",
            "117":"Servicios de rutas de Unix-to-Unix Copy Protocol (UUCP)",
            "119":"NNTP usado en los grupos de noticias de usenet",
            "123":"NTP Protocolo de sincronización de tiempo",
            "135":"epmap",
            "137":"NetBIOS Servicio de nombres",
            "138":"NetBIOS Servicio de envío de datagramas",
            "139":"NetBIOS Servicio de sesiones",
            "143":"IMAP4 Internet Message Access Protocol (E-mail)",
            "161":"SNMP Simple Network Management Protocol",
            "162":"SNMP-trap",
            "174":"Cola de transporte de correos electrónicon MAILQ",
            "177":"XDMCP Protocolo de gestión de displays en X11",
            "178":"Servidor de ventanas NeXTStep",
            "179":"Border Gateway Protocol",
            "194":"Internet Relay Chat",
            "199":"SNMP UNIX Multiplexer",
            "201":"Enrutamiento AppleTalk",
            "202":"Enlace de nembres AppleTalk",
            "204":"Echo AppleTalk",
            "206":"Zona de información AppleTalk",
            "209":"Protocolo de transferencia rápida de correo (QMTP)",
            "210":"Base de datos NISO Z39.50",
            "213":"El protocolo de intercambio de paquetes entre redes (IPX)",
            "220":"IMAP versión 3",
            "245":"Servicio LINK / 3-DNS iQuery",
            "347":"Servicio de administración de cintas y archivos FATMEN",
            "363":"Túnel RSVP",        
            "369":"Portmapper del sistema de archivos Coda",
            "370":"Servicios de autenticación del sistema de archivos Coda",
            "372":"UNIX LISTSERV",
            "389":"	LDAP Protocolo de acceso ligero a Directorios",
            "427":"Protocolo de ubicación de servicios (SLP)",
            "434":"	Agente móvil del Protocolo Internet",
            "435":"Gestor móvil del Protocolo Internet",
            "443":"HTTPS/SSL usado para la transferencia segura de páginas web",
            "444":"Protocolo simple de Network Pagging",
            "445":"Microsoft-DS (Active Directory, compartición en Windows, gusano Sasser, Agobot) o también es usado por Microsoft-DS compartición de ficheros",
            "465":"SMTP Sobre SSL. Utilizado para el envío de correo electrónico (E-mail)",
            "500":"IPSec ISAKMP, Autoridad de Seguridad Local",
            "512":"exec",
            "513":"Rlogin",
            "514":"syslog usado para logs del sistema",
            "515":"usado para la impresión en windows",
            "520":"RIP Routing Information Protocol (Protocolo de Información de Enrutamiento)",
            "521":"RIP Routing Information Protocol IPv6 (Protocolo de Información de Enrutamiento Internet v6)",        
            "587":"SMTP Sobre TLS",
            "591":"FileMaker 6.0 (alternativa para HTTP, ver puerto 80)",
            "631":"	CUPS sistema de impresión de Unix",
            "666":"identificación de Doom para jugar sobre TCP",
            "690":"VATP (Velneo Application Transfer Protocol) Protocolo de comunicaciones de Velneo",
            "993":"IMAP4 sobre SSL (E-mail)",
            "995":"POP3 sobre SSL (E-mail)",
            "1001":"SOCKS Proxy",
            "1194":"OpenVPN Puerto por defecto en NAS Synology y QNAP",
            "1337":"suele usarse en máquinas comprometidas o infectadas",
            "1352":"IBM Lotus Notes/Domino RCP",
            "1433":"Microsoft-SQL-Server",
            "1434":"Microsoft-SQL-Monitor",
            "1494":"Citrix MetaFrame Cliente IC",
            "1512":"WINS Windows Internet Naming Service",
            "1521":"Oracle puerto de escucha por defecto",
            "1701":"Enrutamiento y Acceso Remoto para VPN con L2TP",
            "1720":"H.323",
            "1723":"Enrutamiento y Acceso Remoto para VPN con PPTP.",
            "1761":"Novell Zenworks Remote Control utility",
            "1812":"RADIUS authentication protocol, radius",
            "1813":"RADIUS accounting protocol, radius-acct",
            "1863":"MSN Messenger",
            "1883":"MQTT protocol",
            "1935":"FMS Flash Media Server",
            "2049":"NFS Archivos del sistema de red",
            "2082":"cPanel puerto por defecto",
            "2083":"CPanel puerto por defecto sobre SSL",
            "2086":"Web Host Manager puerto por defecto",
            "2427":"Cisco MGCP",
            "3030":"NetPanzer",
            "3074":"Xbox Live",
            "3128":"HTTP usado por web caches y por defecto en Squid cache o NDL-AAS",
            "3306":"MySQL sistema de gestión de bases de datos",
            "3389":"RDP (Remote Desktop Protocol) Terminal Server",
            "3396":"Novell agente de impresión NDPS",
            "3690":"Subversion (sistema de control de versiones)",
            "3799":"RADIUS CoA -change of authorization",
            "4200":"Angular, puerto por defecto",
            "4443":"AOL Instant Messenger (sistema de mensajería)",
            "4662":"eMule (aplicación de compartición de ficheros)",
            "4672":"eMule (aplicación de compartición de ficheros)",
            "4899":"RAdmin (Remote Administrator), herramienta de administración remota (normalmente troyanos)",
            "5000":"Universal plug-and-play",
            "5001":"Agente v6 Datadog",
            "5060":"Session Initiation Protocol (SIP)",
            "5190":"AOL y AOL Instant Messenger",
            "5222":"Jabber/XMPP conexión de cliente",
            "5223":"Jabber/XMPP puerto por defecto para conexiones de cliente SSL",
            "5269":"Jabber/XMPP conexión de servidor",
            "5432":"PostgreSQL sistema de gestión de bases de datos",
            "5517":"Setiqueue proyecto SETI@Home",
            "5631":"PC-Anywhere protocolo de escritorio remoto",
            "5632":"PC-Anywhere protocolo de escritorio remoto",
            "5400":"VNC protocolo de escritorio remoto (usado sobre HTTP)",
            "5500":"VNC protocolo de escritorio remoto (usado sobre HTTP)",
            "5600":"VNC protocolo de escritorio remoto (usado sobre HTTP)",
            "5700":"VNC protocolo de escritorio remoto (usado sobre HTTP)",
            "5800":"VNC protocolo de escritorio remoto (usado sobre HTTP)",
            "5900":"VNC protocolo de escritorio remoto (usado sobre HTTP)",
            "6000":"X11 usado para X-windows",
            "6112":"Blizzard",
            "6129":"Dameware Software conexión remota",
            "6346":"Gnutella compartición de ficheros (Limewire, etc.)",
            "6347":"Gnutella",
            "6348":"Gnutella",
            "6349":"Gnutella",
            "6350":"Gnutella",
            "6355":"Gnutella",
            "6667":"IRC IRCU Internet Relay Chat",
            "6881":"BitTorrent puerto por defecto",
            "6969":"BitTorrent puerto de tracker",
            "7100":"Servidor de Fuentes X11",
            "8000":"iRDMI por lo general, usado erróneamente en sustitución de 8080. También utilizado en el servidor de streaming ShoutCast",
            "8080":"HTTP HTTP-ALT ver puerto 80. Tomcat lo usa como puerto por defecto.",
            "8118":"privoxy",
            "9009":"Pichat peer-to-peer chat server",
            "9898":"Gusano Dabber (troyano/virus)",
            "10000":"Webmin (Administración remota web)",
            "19226":"Panda Security Puerto de comunicaciones de Panda Agent.",
            "12345":"NetBus en:NetBus (troyano/virus)",
            "25565":"Minecraft Puerto por defecto usado por servidores del juego.",
            "31337":"Back Orifice herramienta de administración remota (por lo general troyanos)",
            "41121":"Protocolo de transferencia utilizado por Pandora FMS",
            "42000":"Utilizado por Percona Monitoring Management para recoger métricas generales",
            "42001":"Utilizado por Percona Monitoring Management para recabar datos de desempeño",
            "42002":"Utilizado por Percona Monitoring Management para recabar métricas de MySQL",
            "27017":"Utilizado por Percona Monitoring Management para recabar métricas de MongoDB",
            "42004":"Utilizado por Percona Monitoring Management para recabar métricas de ProxySQL",
            "45003":"Calivent herramienta de administración remota SSH con análisis de paquetes. smb /tcp/udp 137-19,445",
            }