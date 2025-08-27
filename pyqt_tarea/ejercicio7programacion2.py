# Ejercicio 7: Personalización visual
# -----------------------------------------------------------------------------
# Consigna:
# - Cambiar colores de fondo, fuentes y tamaño de los widgets.
# - Centrar el formulario en la ventana.
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QVBoxLayout,
    QRadioButton, QButtonGroup, QComboBox, QCheckBox, QPushButton, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Usuario")
        self.setGeometry(100, 100, 500, 500)
        self.setStyleSheet("background-color: #ffe6e6;")  # Fondo rojo claro

        # Layout principal vertical para centrar
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)
        self.setLayout(main_layout)

        # Layout del formulario
        layout = QGridLayout()
        layout.setSpacing(15)

        # Título
        titulo = QLabel("Formulario de Registro")
        titulo.setFont(QFont("Arial", 18))
        titulo.setAlignment(Qt.AlignCenter)
        titulo.setStyleSheet("color: #b30000;")  # Rojo oscuro
        layout.addWidget(titulo, 0, 0, 1, 2)

        # Campo "Nombre:"
        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Ingresa tu nombre")
        layout.addWidget(QLabel("Nombre:"), 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)

        # Campo "Email:"
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("ejemplo@email.com")
        layout.addWidget(QLabel("Email:"), 2, 0)
        layout.addWidget(self.email_input, 2, 1)

        # Campo "Contraseña:"
        self.contraseña_input = QLineEdit()
        self.contraseña_input.setEchoMode(QLineEdit.Password)
        self.contraseña_input.setPlaceholderText("••••••••")
        layout.addWidget(QLabel("Contraseña:"), 3, 0)
        layout.addWidget(self.contraseña_input, 3, 1)

        # Género
        self.masculino_radio = QRadioButton("Masculino")
        self.femenino_radio = QRadioButton("Femenino")
        self.grupo_genero = QButtonGroup(self)
        self.grupo_genero.addButton(self.masculino_radio)
        self.grupo_genero.addButton(self.femenino_radio)
        layout.addWidget(self.masculino_radio, 4, 0)
        layout.addWidget(self.femenino_radio, 4, 1)

        # País
        self.pais_combo = QComboBox()
        self.pais_combo.addItems(["Argentina", "México", "España", "Colombia", "Chile"])
        layout.addWidget(QLabel("País:"), 5, 0)
        layout.addWidget(self.pais_combo, 5, 1)

        # Checkbox
        self.terminos_checkbox = QCheckBox("Acepto los términos y condiciones")
        layout.addWidget(self.terminos_checkbox, 6, 0, 1, 2)

        # Botón "Registrarse"
        boton_registrar = QPushButton("Registrarse")
        boton_registrar.clicked.connect(self.validar_formulario)
        boton_registrar.setStyleSheet("""
            QPushButton {
                background-color: #cc0000;
                color: white;
                font-size: 14px;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #990000;
            }
        """)
        layout.addWidget(boton_registrar, 7, 0, 1, 2, alignment=Qt.AlignCenter)

        # Estilos comunes
        estilo_widget = """
            QLineEdit, QComboBox {
                padding: 6px;
                font-size: 14px;
                border: 1px solid #cc0000;
                border-radius: 4px;
                background-color: white;
            }
            QLabel {
                font-size: 14px;
                color: #800000;
            }
            QCheckBox {
                font-size: 13px;
                color: #800000;
            }
            QRadioButton {
                font-size: 13px;
                color: #800000;
            }
        """
        self.setStyleSheet(self.styleSheet() + estilo_widget)

        # Agregar layout interno al layout principal
        main_layout.addLayout(layout)

    def validar_formulario(self):
        nombre = self.nombre_input.text()
        email = self.email_input.text()
        contraseña = self.contraseña_input.text()
        genero = self.masculino_radio.isChecked() or self.femenino_radio.isChecked()
        acepta_terminos = self.terminos_checkbox.isChecked()

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


