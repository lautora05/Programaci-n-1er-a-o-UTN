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


import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout,
    QRadioButton, QButtonGroup, QComboBox, QCheckBox,
    QPushButton, QMessageBox
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
        titulo.setFont(QFont("Arial", 16))
        titulo.setAlignment(Qt.AlignCenter)
        layout.addWidget(titulo, 0, 0, 1, 2)

        # Campo "Nombre:"
        self.nombre_input = QLineEdit()
        layout.addWidget(QLabel("Nombre:"), 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)

        # Campo "Email:"
        self.email_input = QLineEdit()
        layout.addWidget(QLabel("Email:"), 2, 0)
        layout.addWidget(self.email_input, 2, 1)

        # Campo "Contraseña:"
        self.contraseña_input = QLineEdit()
        self.contraseña_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(QLabel("Contraseña:"), 3, 0)
        layout.addWidget(self.contraseña_input, 3, 1)

        # Radio buttons: "Masculino" y "Femenino"
        self.masculino_radio = QRadioButton("Masculino")
        self.femenino_radio = QRadioButton("Femenino")
        self.grupo_genero = QButtonGroup(self)
        self.grupo_genero.addButton(self.masculino_radio)
        self.grupo_genero.addButton(self.femenino_radio)
        layout.addWidget(self.masculino_radio, 4, 0)
        layout.addWidget(self.femenino_radio, 4, 1)

        # Campo "País:"
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Argentina", "México", "España", "Colombia", "Chile"])
        layout.addWidget(QLabel("País:"), 5, 0)
        layout.addWidget(self.pais_combo, 5, 1)

        # Checkbox "Acepto los términos"
        self.terminos_checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.terminos_checkbox, 6, 0, 1, 2)

        # COMPLETAR: Botón "Registrarse"
        boton_registrar = QPushButton("Registrarse")
        boton_registrar.clicked.connect(self.validar_formulario)
        layout.addWidget(boton_registrar, 7, 0, 1, 2)

    def validar_formulario(self):
        # Obtener datos
        nombre = self.nombre_input.text()
        email = self.email_input.text()
        contraseña = self.contraseña_input.text()
        genero = self.masculino_radio.isChecked() or self.femenino_radio.isChecked()
        pais = self.pais_combo.currentText()
        acepta_terminos = self.terminos_checkbox.isChecked()

        # Validación
        if not nombre or not email or not contraseña:
            QMessageBox.warning(self, "Error", "Todos los campos deben estar completos.")
        elif not genero:
            QMessageBox.warning(self, "Error", "Debe seleccionar un género.")
        elif not acepta_terminos:
            QMessageBox.warning(self, "Error", "Debe aceptar los términos y condiciones.")
        else:
            QMessageBox.information(self, "Éxito", f"¡Registro exitoso para {nombre}!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())
