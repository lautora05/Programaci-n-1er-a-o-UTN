import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class VentanaFormulario(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Afiliados - Chacarita Juniors")
        self.setGeometry(100, 100, 500, 350)
        
        layout = QGridLayout()
        self.setLayout(layout)
        
        # Ejercicio 1: Crear la ventana de contexto (formulario de afiliados)
        titulo = QLabel("Formulario de Afiliación")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;")
        layout.addWidget(titulo, 0, 0, 1, 2, alignment=Qt.AlignCenter)
        

        
        self.nombre_label = QLabel("Nombre:")
        self.apellido_label = QLabel("Apellido:")
        self.dni_label = QLabel("DNI:")
        self.fecha_label = QLabel("Fecha de nacimiento:")
        
        self.nombre_input = QLineEdit()
        self.apellido_input = QLineEdit()
        self.dni_input = QLineEdit()
        self.fecha_input = QLineEdit()  

        
        self.nombre_input.setStyleSheet("padding: 4.5px;")
        self.apellido_input.setStyleSheet("padding: 4.5px;")
        self.dni_input.setStyleSheet("padding: 4.5px;")
        self.fecha_input.setStyleSheet("padding: 4.5px;")

        
        layout.addWidget(self.nombre_label, 1, 0)
        layout.addWidget(self.nombre_input, 1, 1)
        layout.addWidget(self.apellido_label, 2, 0)
        layout.addWidget(self.apellido_input, 2, 1)
        layout.addWidget(self.dni_label, 3, 0)
        layout.addWidget(self.dni_input, 3, 1)
        layout.addWidget(self.fecha_label, 4, 0)
        layout.addWidget(self.fecha_input, 4, 1)

    def mostrar_datos(self):
        
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        dni = self.dni_input.text()
        fecha = self.fecha_input.text()

        
        if not nombre or not apellido or not dni or not fecha:
            QMessageBox.warning(self, "Error", "Todos los campos son obligatorios")
            return
        
        mensaje = f"Datos guardados:\nNombre: {nombre}\nApellido: {apellido}\nDNI: {dni}\nFecha de nacimiento: {fecha}"
        QMessageBox.information(self, "Datos guardados", mensaje) 
# Ejercicio 2: Crear la ventana de herramientas
class VentanaHerramientas(QWidget):
    def __init__(self, ventana_form):
        super().__init__()
        self.setWindowTitle("Herramientas")
        self.setGeometry(650, 100, 200, 300)
        
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
       # Ejercicio 5: Personalización visual y validaciones
        self.boton_guardar = QPushButton("Guardar")
        self.boton_guardar.setStyleSheet("background-color: #c21c2c; color: white; padding: 10px; margin: 5px;")
        self.boton_guardar.clicked.connect(ventana_form.mostrar_datos)
        
        self.boton_abrir = QPushButton("Abrir")
        self.boton_abrir.setStyleSheet("background-color: #25292e; color: white; padding: 10px; margin: 5px;")
        
        self.boton_buscar = QPushButton("Buscar")
        self.boton_buscar.setStyleSheet("background-color: #eff2f5; color: black; padding: 10px; margin: 5px;")
        
        self.boton_salir = QPushButton("Salir")
        self.boton_salir.setStyleSheet("background-color: #f44336; color: white; padding: 10px; margin: 5px;")
        self.boton_salir.clicked.connect(self.close)
        
        #4 Conectar botones de herramientas con el formulario
        
        layout.addWidget(self.boton_guardar)
        layout.addWidget(self.boton_abrir)
        layout.addWidget(self.boton_buscar)
        layout.addWidget(self.boton_salir)
# Ejercicio 3: Mostrar ambas ventanas a la vez
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    
    ventana_form = VentanaFormulario()
    ventana_herr = VentanaHerramientas(ventana_form)
    
    
    ventana_form.show()
    ventana_herr.show()
    
    sys.exit(app.exec_())
