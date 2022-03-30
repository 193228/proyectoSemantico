'''import re
textoBinDec = "este es un texto de prueba 1000 1001"
textoDecBin = "este es un texto de prueba 8 9"

def binDecimal():
    x = ""
    regex = re.compile('[0-1]+')
    busqueda = regex.findall(textoBinDec)
    for i in range(len(busqueda)):
        if len(x) == 0:
            x = textoBinDec.replace(busqueda[i], str(int(busqueda[i],2)))
        x = x.replace(busqueda[i], str(int(busqueda[i],2)))
    return x

def decimalBin():
    x = ""
    regex = re.compile('[0-9]+')
    busqueda = regex.findall(textoDecBin)
    for i in range(len(busqueda)):
        if len(x) == 0:
            x = textoBinDec.replace(busqueda[i], bin(int(busqueda[i])).replace("0b", ""))
        x = x.replace(busqueda[i], bin(int(busqueda[i])).replace("0b", ""))
    return x

x = decimalBin()
print(x)'''