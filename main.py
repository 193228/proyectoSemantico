import sys
import PyQt5
from vista.main import Ui_MainWindow as ventanaPrincipal
from analizador.semantico import analisisContenido

class MyApp(PyQt5.QtWidgets.QMainWindow, ventanaPrincipal):
    def __init__(self):
        PyQt5.QtWidgets.QMainWindow.__init__(self)
        ventanaPrincipal.__init__(self)
        self.setupUi(self)
        acciones(self)

def acciones(ventana):
    ventana.envioCorreos.clicked.connect(lambda: obtenerInfo(ventana))

def obtenerInfo(ventana):
    cuerpoMensaje = ventana.cuerpoTexto.toPlainText() #obtengo el cuerpo
    eleccion = obtenerTipoEleccion(ventana)
    analisisContenido(cuerpoMensaje,eleccion,ventana)

def obtenerTipoEleccion(ventana):
    if ventana.decimalBinario.isChecked():
        return "decimalBinario"
    if ventana.binarioDecimal.isChecked():
        return "binarioDecimal"
    if ventana.mensajeBinario.isChecked():
        return "mensajeBinario"

if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)  # crea un objeto de aplicación (Argumentos de sys)
    window = MyApp()
    window.show()
    window.setFixedSize(window.size())
    app.exec_()
