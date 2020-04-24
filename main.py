#!/usr/bin/python3
# -*- coding: utf-8 -*-
# QR Code

from qrcode import make #Importamos 'make' de 'qrcode'.

class QrCode():
    def __init__(self):
        self.image = make(input("Conviertelo a codigo QR: ")) #Lo que se ingrese sera convertido en QR.
        self.qr_name = input("Nombre del archivo: ") #Creamos un nombre .png desde la terminal.

    def save(self): #Salvamos el archivo.
        self.image.save(self.qr_name)

    def show(self): #Mostramos el archivo
        self.image.show(self.qr_name)



if __name__ == '__main__':
    qr = QrCode()
    qr.save()
    qr.show()

