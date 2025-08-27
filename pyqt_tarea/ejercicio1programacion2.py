# Práctico PyQt5: Construcción guiada de una interfaz completa
# ------------------------------------------------------------
#
# Objetivo: Construir paso a paso un formulario de registro moderno y funcional.
# Cada ejercicio suma widgets y lógica, guiando al alumno en el uso de PyQt5 y QGridLayout.
#
# -----------------------------------------------------------------------------
# Ejercicio 1: Estructura básica y primer campo
# -----------------------------------------------------------------------------
# Teoría:
# - QLabel muestra texto en la interfaz.
# - QLineEdit permite ingresar texto.
# - QGridLayout organiza los widgets en filas y columnas.
#
# Consigna:
# - Ventana 400x300, título “Registro de Usuario”.
# - QLabel grande y centrado: “Formulario de Registro”.
# - QLabel “Nombre:” y QLineEdit al lado, usando QGridLayout.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)
        layout = QGridLayout()
        self.setLayout(layout)
        # COMPLETAR: Crear QLabel grande y centrado ("Formulario de Registro")
        titulo = QLabel("Formulario de Registro")
        titulo.setFont(QFont("Arial", 16, QFont.Bold))  # Fuente grande
        titulo.setAlignment(Qt.AlignCenter)  # Centrado
        layout.addWidget(titulo, 0, 0, 1, 2)  # Fila 0, columna 0, ocupa 2 columnas
        # COMPLETAR: Crear QLabel "Nombre:" y QLineEdit al lado
        nombre_label = QLabel("Nombre:")
        nombre_input = QLineEdit()
        layout.addWidget(nombre_label, 1, 0)  # Fila 1, columna 0
        layout.addWidget(nombre_input, 1, 1)  # Fila 1, columna 1
       

       



# -----------------------------------------------------------------------------
# Ejercicio 3: Selección de género
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción.
# - QButtonGroup agrupa los radio buttons para que solo uno esté activo.
#
# Consigna:
# - Agregar dos QRadioButton: “Masculino” y “Femenino”, en la misma fila.
# - Usar QButtonGroup para agruparlos.

# -----------------------------------------------------------------------------
# Ejercicio 4: Selección de país
# -----------------------------------------------------------------------------
# Teoría:
# - QComboBox permite elegir una opción de una lista desplegable.
#
# Consigna:
# - Agregar QLabel “País:” y QComboBox con al menos 5 países.

# -----------------------------------------------------------------------------
# Ejercicio 5: Checkbox de términos
# -----------------------------------------------------------------------------
# Teoría:
# - QCheckBox permite aceptar o rechazar condiciones.
#
# Consigna:
# - Agregar QCheckBox: “Acepto los términos y condiciones”.

# -----------------------------------------------------------------------------
# Ejercicio 6: Botón de envío y validación
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Registrarse”.
# - Al hacer clic, validar que todos los campos estén completos y el checkbox marcado.
# - Mostrar mensaje de éxito o error.

# -----------------------------------------------------------------------------
# Ejercicio 7: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores de fondo, fuentes y tamaño de los widgets.
# - Centrar el formulario en la ventana.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())