# - QCheckBox permite aceptar o rechazar condiciones.
#
# Consigna:
# - Agregar QCheckBox: “Acepto los términos y condiciones”.

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
    QRadioButton, QButtonGroup, QComboBox, QCheckBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 400, 300)

        layout = QGridLayout()
        self.setLayout(layout)

        # Título centrado
        titulo = QLabel("Formulario de Registro")
        titulo.setFont(QFont("Arial", 16))  # Fuente grande sin negrita
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0, 0, 1, 2)

        # Campo "Nombre:"
        nombre_label = QLabel("Nombre:")
        nombre_input = QLineEdit()
        layout.addWidget(nombre_label, 1, 0)
        layout.addWidget(nombre_input, 1, 1)

        # Campo "Email:"
        email_label = QLabel("Email:")
        email_input = QLineEdit()
        layout.addWidget(email_label, 2, 0)
        layout.addWidget(email_input, 2, 1)

        # Campo "Contraseña:"
        contraseña_label = QLabel("Contraseña:")
        contraseña_input = QLineEdit()
        contraseña_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(contraseña_label, 3, 0)
        layout.addWidget(contraseña_input, 3, 1)

        # Radio buttons: "Masculino" y "Femenino"
        masculino_radio = QRadioButton("Masculino")
        femenino_radio = QRadioButton("Femenino")

        grupo_genero = QButtonGroup(self)
        grupo_genero.addButton(masculino_radio)
        grupo_genero.addButton(femenino_radio)

        layout.addWidget(masculino_radio, 4, 0)
        layout.addWidget(femenino_radio, 4, 1)

        # Campo "País:"
        pais_label = QLabel("País:")
        pais_combo = QComboBox()
        pais_combo.addItems(["Argentina", "México", "España", "Colombia", "Chile"])

        layout.addWidget(pais_label, 5, 0)
        layout.addWidget(pais_combo, 5, 1)

        # COMPLETAR: Agregar QCheckBox “Acepto los términos y condiciones”
        terminos_checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(terminos_checkbox, 6, 0, 1, 2)  # Ocupa 2 columnas

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
