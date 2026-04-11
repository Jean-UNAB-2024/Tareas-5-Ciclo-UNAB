"Configuración de Entornos Profesionales y GUI con PySide6"
________________________________________
Capacidades y Desempeños
En el contexto técnico/universitario, estas son las capacidades que tus estudiantes activarán:
1.	Gestión de Entornos de Desarrollo: Capacidad para configurar y aislar espacios de trabajo independientes, asegurando la portabilidad y el orden del software.
2.	Implementación de Librerías Externas: Capacidad para utilizar gestores de paquetes (pip) para integrar herramientas de terceros en proyectos de Python.
3.	Pensamiento Sistémico: Comprende la diferencia entre configuraciones globales y locales para evitar conflictos de software en el sistema operativo.
________________________________________
Estructura de la Sesión
Inicio (Motivación)
•	Pregunta retadora: "¿Qué pasa si un proyecto requiere la versión 1.0 de una librería y otro proyecto requiere la 2.0 en la misma computadora?"
•	Introducción: Hoy aprenderemos a instalar herramientas para crear interfaces gráficas (ventanas) y cómo mantener nuestra "casa" (la PC) limpia usando entornos virtuales.
________________________________________
Actividad 1: Instalación de Python y PySide6 (Nivel Global)
Esta actividad busca que el alumno pierda el miedo a la terminal y entienda el ecosistema de paquetes.
•	Paso 1: Verificación de Python en el sistema (python --version).
•	Paso 2: Introducción a pip (Python Package Index).
•	Paso 3: Ejecución del comando:
Bash
pip install pyside6
•	Concepto clave: Explicar que PySide6 es el framework oficial de Qt para Python, que permite crear aplicaciones de escritorio profesionales (como las que usan en sus clases de ingeniería).
________________________________________
Actividad 2: Gestión de Entornos Virtuales (venv)
Aquí es donde pasan de "amateurs" a "profesionales".
•	¿Qué es venv?: Es una "burbuja" donde instalas solo lo que ese proyecto necesita.
•	Proceso práctico:
1.	Crear la carpeta del proyecto.
2.	Crear el entorno: python -m venv venv
3.	Activar el entorno: (Crucial, recuerda el error de permisos de PowerShell que vimos antes).
	Windows: .\venv\Scripts\activate
4.	Diferenciación: Mostrar que, al estar dentro del entorno, si escribes pip list, la lista de librerías está limpia, a diferencia del entorno global.
________________________________________
Evaluación (Cierre)
Para verificar que las capacidades se lograron, los alumnos deben:
1.	Entregar una captura de pantalla de su terminal con el entorno virtual activado (donde aparezca el (.venv) al inicio).
2.	Ejecutar un pequeño script de prueba que importe PySide6 sin errores:
Python
import PySide6.QtCore
print("¡PySide6 instalado y listo!")
________________________________________
Tip para tu clase:
Como sé que a tus alumnos les gustan los temas de gaming y anime (como Genshin o Jujutsu Kaisen), podrías decirles que:
"El entorno global es como el mundo abierto del juego, pero el venv es como una Expansión de Dominio o una Instancia: un lugar con sus propias reglas y recursos donde nada de afuera interfiere."
¿Te parece bien este enfoque para tus alumnos de ciclo 5 o prefieres algo más técnico?

