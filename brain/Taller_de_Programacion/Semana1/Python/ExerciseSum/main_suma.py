import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_ventana_suma import Ui_MainWindow

class VentanaSuma(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnSumar.clicked.connect(self.sumar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)

    def sumar(self):
        numero1_texto = self.ui.txtNumero1.text().strip()
        numero2_texto = self.ui.txtNumero2.text().strip()

        if numero1_texto == "" or numero2_texto == "":
            self.ui.lblResultado.setText("Resultado: Complete ambos números")
            return

        try:
            numero1 = float(numero1_texto)
            numero2 = float(numero2_texto)
            resultado = numero1 + numero2
            self.ui.lblResultado.setText(f"Resultado: {resultado}")
        except ValueError:
            self.ui.lblResultado.setText("Resultado: Ingrese valores numéricos válidos")

    def limpiar(self):
        self.ui.txtNumero1.clear()
        self.ui.txtNumero2.clear()
        self.ui.lblResultado.setText("Resultado:")
        self.ui.txtNumero1.setFocus()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaSuma()
    ventana.show()
    sys.exit(app.exec())