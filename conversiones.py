import re

def mensajeBinario(texto):
    mensaje_binario = ' '.join(format(ord(c), 'b') for c in texto)
    return mensaje_binario #este ya esta

def binarioNumero(texto,regex):
    binNum = ""
    regex = re.compile(regex)
    busqueda = regex.findall(texto)
    for i in range(len(busqueda)):
        if len(binNum) == 0:
            binNum = texto.replace(busqueda[i], str(int(busqueda[i], 2)))
        binNum = binNum.replace(busqueda[i], str(int(busqueda[i], 2)))
    return binNum

def numeroBinario(texto,regex):
    numBin = ""
    regex = re.compile(regex)
    busqueda = regex.findall(texto)
    for i in range(len(busqueda)):
        if len(numBin) == 0:
            numBin = texto.replace(busqueda[i], bin(int(busqueda[i])).replace("0b", ""))
        numBin = numBin.replace(busqueda[i], bin(int(busqueda[i])).replace("0b", ""))
    return numBin