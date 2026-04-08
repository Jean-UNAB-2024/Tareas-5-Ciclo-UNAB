import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_ventana import Ui_MainWindow

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnSaludar.clicked.connect(self.saludar)

    def saludar(self):
        nombre = self.ui.txtNombre.text().strip()

        if nombre == "":
            self.ui.lblResultado.setText("Por favor, ingrese su nombre")
        else:
            self.ui.lblResultado.setText(f"Hola, {nombre}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())