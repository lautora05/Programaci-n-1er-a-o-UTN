# Ejercicio 3: Clase y cantidad de pasajeros
# -----------------------------------------------------------------------------
# Teoría:
# - QRadioButton permite seleccionar una opción (Ej: clase turista o ejecutiva).
# - QSpinBox permite elegir un número (Ej: cantidad de pasajeros).
#
# Consigna:
# - Agregar QRadioButton para “Turista” y “Ejecutiva”.
# - Agregar QLabel “Cantidad de pasajeros:” y QSpinBox (mínimo 1, máximo 10).

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QComboBox, QDateEdit, QRadioButton, QSpinBox, QGroupBox, QVBoxLayout
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
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())