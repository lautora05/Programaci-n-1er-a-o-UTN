# Ejercicio 4: Confirmación y resumen
# -----------------------------------------------------------------------------
# Teoría:
# - QPushButton ejecuta una función al hacer clic.
# - QMessageBox muestra mensajes emergentes.
#
# Consigna:
# - Agregar QPushButton “Comprar”.
# - Al hacer clic, mostrar un resumen de la compra en un QMessageBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDateEdit, QRadioButton, QSpinBox, QGroupBox, QVBoxLayout, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QDate 

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Compra de Pasaje Aéreo")
        self.setGeometry(100, 100, 500, 350)
        diseno = QGridLayout()
        self.setLayout(diseno)

        # 1. Creamos un QLabel grande y centrado para el título del formulario.
        etiqueta_titulo = QLabel("Formulario de Compra")
        etiqueta_titulo.setStyleSheet("font-size: 24px; font-weight: bold;")
        etiqueta_titulo.setAlignment(Qt.AlignCenter) 
        diseno.addWidget(etiqueta_titulo, 0, 0, 1, 2)

        # 2. Creamos etiquetas y campos de texto para Nombre, Apellido y DNI.
        
        etiqueta_nombre = QLabel("Nombre:")
        self.campo_nombre = QLineEdit()

        
        etiqueta_apellido = QLabel("Apellido:")
        self.campo_apellido = QLineEdit()

        
        etiqueta_dni = QLabel("DNI:")
        self.campo_dni = QLineEdit()
        
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
        self.boton_comprar.setStyleSheet("background-color: #4CAF50; color: white; font-weight: bold; padding: 10px; border-radius: 5px;")
        
        
        self.boton_comprar.clicked.connect(self.procesar_compra)
        
        
        diseno.addWidget(etiqueta_nombre, 1, 0)
        diseno.addWidget(self.campo_nombre, 1, 1)

        diseno.addWidget(etiqueta_apellido, 2, 0)
        diseno.addWidget(self.campo_apellido, 2, 1)

        diseno.addWidget(etiqueta_dni, 3, 0)
        diseno.addWidget(self.campo_dni, 3, 1)
        
        
        diseno.addWidget(etiqueta_origen, 4, 0)
        diseno.addWidget(self.combo_origen, 4, 1)
        
        diseno.addWidget(etiqueta_destino, 5, 0)
        diseno.addWidget(self.combo_destino, 5, 1)
        
        diseno.addWidget(etiqueta_fecha, 6, 0)
        diseno.addWidget(self.campo_fecha, 6, 1)
        
        
        diseno.addWidget(grupo_clase, 7, 0, 1, 2)
        diseno.addWidget(etiqueta_pasajeros, 8, 0)
        diseno.addWidget(self.spinbox_pasajeros, 8, 1)
        
        
        diseno.addWidget(self.boton_comprar, 9, 0, 1, 2)
        
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
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())