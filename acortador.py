#si el IDE no reconoce el paquete pyshorteners se debe instalar desde la consola:
# pip install pyshorteners

import pyshorteners

def main():
    link = input('ingrese la url a recortar: ')

    short = pyshorteners.Shortener()
    x =  short.tinyurl.short(link)
    print('En enlace recortado es: ' + x)
    

if __name__ == '__main__':
    main()

