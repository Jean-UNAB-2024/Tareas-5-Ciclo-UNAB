print("Hi") --> esto es codigo en python
instalamos pyside6 en el entorno virtual
con pip install pyside6

para abrir pyside6 tienes q escribir: pyside6-designer.exe
porq ya esta en tu .venv\scripts\
Recuerda siempre cerrar con deactive, CIERRA EL ENTORNO VIRTUAL ctm

quieren q agreges en el path para que solo escribiento pyside6-designer se pueda abrir
pero, tu hazlo con entorno virtual, te lo recomiendo, te servira mas, en un futuro

ahora 
pip install --upgrade pip
para refrescar


para crear un requirements.txt
usas pip freeze > requirements.txt

para volver a instalar usas pip install -r requirements.txt

---
para convertir el archivo.ui a python se hace lo siguiente:
pyside6-uic ventana.ui -o ui_ventana.py

La contraseña no se tiene q ver en la base de datos :D
