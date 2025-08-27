# Ejercicio extra: Agregar un campo de fecha de nacimiento y validación avanzada
# -----------------------------------------------------------------------------
# Consigna:
# - Agrega un QLabel "Fecha de nacimiento:" y un QDateEdit al lado, usando el grid.
# - Al hacer clic en "Registrarse", valida que la fecha no sea posterior a hoy y que el usuario tenga al menos 13 años.
# - Si la validación falla, muestra un mensaje de error; si es correcta, muestra un mensaje de éxito.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDateEdit, QRadioButton, QSpinBox, QGroupBox, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QDate 

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f4f8;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #333;
                font-size: 14px;
            }
            QLineEdit, QComboBox, QDateEdit, QSpinBox {
                background-color: #fff;
                border: 1px solid #ccc;
                border-radius: 4px;
                padding: 6px;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QGroupBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                margin-top: 10px;
                padding-top: 15px;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 3px;
                color: #555;
            }
        """)

        
        diseno = QGridLayout()
       
        self.setLayout(diseno)
        diseno.setAlignment(Qt.AlignCenter)

        # 1. Creamos un QLabel grande y centrado para el título del formulario.
        etiqueta_titulo = QLabel("Formulario de Compra")
        etiqueta_titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a1a1a;")
        etiqueta_titulo.setAlignment(Qt.AlignCenter) 
        diseno.addWidget(etiqueta_titulo, 0, 0, 1, 2)

        # 2. Creamos etiquetas y campos de texto para Nombre, Apellido y DNI.
        etiqueta_nombre = QLabel("Nombre:")
        self.campo_nombre = QLineEdit()

        etiqueta_apellido = QLabel("Apellido:")
        self.campo_apellido = QLineEdit()

        etiqueta_dni = QLabel("DNI:")
        self.campo_dni = QLineEdit()

        # Agregamos la etiqueta y el QDateEdit para la fecha de nacimiento.
        etiqueta_nacimiento = QLabel("Fecha de nacimiento:")
        self.campo_nacimiento = QDateEdit()
        self.campo_nacimiento.setCalendarPopup(True)
        self.campo_nacimiento.setDisplayFormat("dd/MM/yyyy")
        self.campo_nacimiento.setDate(QDate.currentDate())
        
        # 3. Agregamos las etiquetas y los QComboBox para Origen y Destino.
        etiqueta_origen = QLabel("Origen:")
        self.combo_origen = QComboBox()
        self.combo_origen.addItems(["Buenos Aires", "Córdoba", "Mendoza", "Rosario"])

        etiqueta_destino = QLabel("Destino:")
        self.combo_destino = QComboBox()
        self.combo_destino.addItems(["Santiago", "Madrid", "Miami", "Sao Paulo"])
        
        # 4. Agregamos la etiqueta y el QDateEdit para la fecha de vuelo.
        etiqueta_fecha = QLabel("Fecha de vuelo:")
        self.campo_fecha = QDateEdit(QDate.currentDate())
        self.campo_fecha.setCalendarPopup(True) 
        
        # 5. Agregamos QRadioButton para la clase de pasaje dentro de un QGroupBox.
        grupo_clase = QGroupBox("Clase de pasaje:")
        diseno_clase = QVBoxLayout()
        self.radio_turista = QRadioButton("Turista")
        self.radio_ejecutiva = QRadioButton("Ejecutiva")
        self.radio_turista.setChecked(True) 
        diseno_clase.addWidget(self.radio_turista)
        diseno_clase.addWidget(self.radio_ejecutiva)
        grupo_clase.setLayout(diseno_clase)
        
        # 6. Agregamos QLabel y QSpinBox para la cantidad de pasajeros.
        etiqueta_pasajeros = QLabel("Cantidad de pasajeros:")
        self.spinbox_pasajeros = QSpinBox()
        self.spinbox_pasajeros.setMinimum(1)
        self.spinbox_pasajeros.setMaximum(10)

        # 7. Agregamos un QPushButton para procesar la compra.
        self.boton_comprar = QPushButton("Comprar Pasaje")
        
        
        self.boton_registrar = QPushButton("Registrarse")
        self.boton_registrar.setStyleSheet("background-color: #28a745; color: white; font-weight: bold; padding: 10px; border: none; border-radius: 5px;")
        self.boton_registrar.clicked.connect(self.validar_registro)
        
        self.boton_comprar.clicked.connect(self.procesar_compra)
        
        diseno.addWidget(etiqueta_nombre, 1, 0)
        diseno.addWidget(self.campo_nombre, 1, 1)

        diseno.addWidget(etiqueta_apellido, 2, 0)
        diseno.addWidget(self.campo_apellido, 2, 1)

        diseno.addWidget(etiqueta_dni, 3, 0)
        diseno.addWidget(self.campo_dni, 3, 1)

        diseno.addWidget(etiqueta_nacimiento, 4, 0)
        diseno.addWidget(self.campo_nacimiento, 4, 1)
        
        diseno.addWidget(etiqueta_origen, 5, 0)
        diseno.addWidget(self.combo_origen, 5, 1)
        
        diseno.addWidget(etiqueta_destino, 6, 0)
        diseno.addWidget(self.combo_destino, 6, 1)
        
        diseno.addWidget(etiqueta_fecha, 7, 0)
        diseno.addWidget(self.campo_fecha, 7, 1)
        
        diseno.addWidget(grupo_clase, 8, 0, 1, 2)
        diseno.addWidget(etiqueta_pasajeros, 9, 0)
        diseno.addWidget(self.spinbox_pasajeros, 9, 1)
        
        diseno.addWidget(self.boton_comprar, 10, 0, 1, 2)
        diseno.addWidget(self.boton_registrar, 11, 0, 1, 2)
        
    def procesar_compra(self):
        """
        Este método se llama cuando se hace clic en el botón 'Comprar Pasaje'.
        Recopila los datos del formulario y los muestra en un cuadro de mensaje.
        """
        
        nombre = self.campo_nombre.text()
        apellido = self.campo_apellido.text()
        dni = self.campo_dni.text()
        origen = self.combo_origen.currentText()
        destino = self.combo_destino.currentText()
        fecha = self.campo_fecha.date().toString(Qt.ISODate)
        
        if self.radio_turista.isChecked():
            clase = "Turista"
        else:
            clase = "Ejecutiva"
            
        pasajeros = self.spinbox_pasajeros.value()
        
        
        resumen = f"--- Resumen de la Compra ---\n\n"
        resumen += f"Nombre: {nombre}\n"
        resumen += f"Apellido: {apellido}\n"
        resumen += f"DNI: {dni}\n"
        resumen += f"Origen: {origen}\n"
        resumen += f"Destino: {destino}\n"
        resumen += f"Fecha de Vuelo: {fecha}\n"
        resumen += f"Clase: {clase}\n"
        resumen += f"Pasajeros: {pasajeros}\n\n"
        resumen += "¡Compra realizada con éxito!"
        
        
        msg = QMessageBox()
        msg.setWindowTitle("Compra de Pasaje Aéreo")
        msg.setIcon(QMessageBox.Information)
        msg.setText(resumen)
        msg.exec_()
    
    def validar_registro(self):
        fecha_nacimiento = self.campo_nacimiento.date()
        fecha_actual = QDate.currentDate()
        
       
        edad_anios = fecha_actual.year() - fecha_nacimiento.year()
        if fecha_nacimiento.month() > fecha_actual.month() or \
           (fecha_nacimiento.month() == fecha_actual.month() and fecha_nacimiento.day() > fecha_actual.day()):
            edad_anios -= 1
        
        
        if fecha_nacimiento > fecha_actual:
            QMessageBox.critical(self, "Error de Validación", "La fecha de nacimiento no puede ser en el futuro.")
            return

        
        if edad_anios < 13:
            QMessageBox.critical(self, "Error de Validación", "Debes tener al menos 13 años para registrarte.")
            return

      
        QMessageBox.information(self, "Validación Exitosa", "Registro validado correctamente.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.resize(500, 450)
    screen = app.primaryScreen()
    size = ventana.geometry()
    x = (screen.geometry().width() - size.width()) // 2
    y = (screen.geometry().height() - size.height()) // 2
    ventana.move(x, y)
    ventana.show()
    sys.exit(app.exec_())