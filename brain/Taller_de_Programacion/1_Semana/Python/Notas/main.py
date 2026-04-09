import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from notas import Ui_MainWindow

class NotaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnEstado.clicked.connect(self.estado)

    def estado(self):
        actiducinal_text = self.ui.txtActitudinal.text().strip()
        procedimental_text = self.ui.txtProcedimental.text().strip()
        cognocitivo_text = self.ui.txtCognocitivo.text().strip()

        if actiducinal_text == "" or procedimental_text == "" or cognocitivo_text == "":
            self.ui.lblResult.setText("Resultado: Complete todas las notas")
            return

        try:
            numAct = float(actiducinal_text)
            numPro = float(procedimental_text)
            numCog = float(cognocitivo_text)
            resultado = (numAct*0.4) + (numPro*0.5) + (numCog*0.1)
            if resultado < 10.5:
                self.ui.lblResult.setText(f"El estudiante reprobó con: {resultado}")
            else:
                self.ui.lblResult.setText(f"El estudiante Aprobó con: {resultado}")
        except ValueError:
            self.ui.lblResult.setText("Resultado: Ingrese valores numéricos válidos")    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = NotaApp()
    ventana.show()
    sys.exit(app.exec())
    
    
# venv\Scripts\activate --> tiene ejecutarse en la carpeta en donde se encuentra incluido el venv
