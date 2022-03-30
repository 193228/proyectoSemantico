from analizador.sintactico import ejecucionAlgoritmo
from conversiones import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from envioCorreos import enviarCorreo


def analisisContenido(cuerpo, opcionElegida, ventana):
    datos = ejecucionAlgoritmo(cuerpo)
    llenadoTabla(ventana, datos)
    if not datos:
        cuerpoCorreo = separarDatos(cuerpo)
        if opcionElegida == "binarioDecimal":
            binario_decimal = binarioNumero(cuerpoCorreo[4],"[0-1]+")
            cuerpoCorreo[4] = binario_decimal
            enviarCorreo(cuerpoCorreo)
        if opcionElegida == "decimalBinario":
            decimal_binario = numeroBinario(cuerpoCorreo[4],"[0-9]+")
            cuerpoCorreo[4] = decimal_binario
            enviarCorreo(cuerpoCorreo)
        if opcionElegida == "mensajeBinario":
            mensaje_binario = mensajeBinario(cuerpoCorreo[4])
            cuerpoCorreo[4] = mensaje_binario
            enviarCorreo(cuerpoCorreo)
        if opcionElegida == None:
            #print()
            enviarCorreo(cuerpoCorreo)

def separarDatos(cuerpo):
    remplazoPassword = cuerpo.replace("<P>", "<T>").replace("<A>", "<T>").replace("<D>", "<T>").replace("<M>","<T>")
    lista = remplazoPassword.split("<T>")
    nueva = []
    for i in lista:
        nueva.append(i.strip())
    return nueva

def llenadoTabla(ventana,sintaxis):
    ventana.tabla.setRowCount(0) #limpia la tabla
    ventana.tabla.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers) #no edita la tabla
    fila = 0
    for registro in sintaxis:
        columna = 0
        ventana.tabla.insertRow(fila)
        for elemento in registro:
            celda = QTableWidgetItem(elemento)
            ventana.tabla.setItem(fila, columna, celda)
            columna+=1
        fila+=1

