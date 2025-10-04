import sys
import traceback
import mysql.connector
from mysql.connector import Error
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pagina_actual = 0
        self.registros_por_pagina = 10
        self.total_registros = 0
        self.initUI()
        self.calcular_total_registros()
        self.mostrar_registros()

    def initUI(self):
        # Configuración básica de la ventana
        self.setWindowTitle("Sistema de Gestión Escolar - Registro de Estudiantes")
        self.setGeometry(250, 200, 800, 500)
        
        # Agregamos color celeste a la interfase
        self.setStyleSheet("""
            QMainWindow {
                background-color: #e6f7ff;
            }
            QLabel#titulo {
                font-size: 18px;
                font-weight: bold;
                color: #0066cc;
                padding: 10px;
                background-color: #b3e0ff;
                border-radius: 8px;
                margin: 10px;
            }
            QPushButton {
                background-color: #4da6ff;
                color: white;
                border: none;
                padding: 8px 15px;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #3399ff;
            }
            QPushButton:disabled {
                background-color: #99ccff;
                color: #cccccc;
            }
            QTableWidget {
                background-color: white;
                border: 2px solid #99ccff;
                border-radius: 5px;
                gridline-color: #cce6ff;
            }
            QTableWidget::item {
                padding: 5px;
                border-bottom: 1px solid #e6f2ff;
            }
            QTableWidget::item:selected {
                background-color: #99ccff;
                color: black;
            }
            QHeaderView::section {
                background-color: #4da6ff;
                color: white;
                font-weight: bold;
                padding: 8px;
                border: none;
            }
        """)
        
        # Widget central y layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout_principal = QVBoxLayout(central_widget)
        
        # Título de la ventana
        titulo = QLabel("REGISTRO DE ESTUDIANTES - INSTITUCIÓN EDUCATIVA")
        titulo.setObjectName("titulo")
        titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(titulo)
        
        # Tabla donde van a aparecer los estudiantes
        self.tabla = QTableWidget()
        layout_principal.addWidget(self.tabla)
        
        # Los botones para cambiar de página
        layout_controles = QHBoxLayout()
        self.btn_anterior = QPushButton("← Página Anterior")
        self.btn_anterior.clicked.connect(self.pagina_anterior)
        layout_controles.addWidget(self.btn_anterior)
        
        layout_controles.addStretch()
        
        # Etiqueta que muestra en qué página estamos
        self.lbl_pagina = QLabel("Página 0 de 0")
        self.lbl_pagina.setStyleSheet("font-weight: bold; color: #0066cc;")
        layout_controles.addWidget(self.lbl_pagina)
        
        layout_controles.addStretch()
        
        self.btn_siguiente = QPushButton("Página Siguiente →")
        self.btn_siguiente.clicked.connect(self.pagina_siguiente)
        layout_controles.addWidget(self.btn_siguiente)
        
        layout_principal.addLayout(layout_controles)
        self.actualizar_botones()

    def conectar_db(self):
        # Se conecta a la base de datos
        try:
            return mysql.connector.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='password',
                database='colegio'
            )
        except Error as e:
            QMessageBox.critical(self, "Error", f"No pude conectarme a la base de datos: {str(e)}")
            return None

    def calcular_total_registros(self):
        # Cuenta cuántos estudiantes hay en total para la paginación
        conexion = self.conectar_db()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("SELECT COUNT(*) FROM alumno")
                self.total_registros = cursor.fetchone()[0]
            except Error as e:
                # Log completo para depuración
                print("Error al contar estudiantes:", e)
                traceback.print_exc()
                QMessageBox.critical(self, "Error", f"Error al contar estudiantes: {str(e)}")
            finally:
                conexion.close()

    def mostrar_registros(self):
        # Se cargan los estudiantes de la página actual
        conexion = self.conectar_db()
        if not conexion:
            return
        try:
            cursor = conexion.cursor()
            offset = self.pagina_actual * self.registros_por_pagina
            cursor.execute("""
                SELECT id, nombre, apellido, edad, grado, promedio 
                FROM alumno 
                ORDER BY id 
                LIMIT %s OFFSET %s
            """, (self.registros_por_pagina, offset))
            registros = cursor.fetchall()
            
            # Se configura la tabla con las columnas que se necesita
            self.tabla.setRowCount(len(registros))
            self.tabla.setColumnCount(6)
            self.tabla.setHorizontalHeaderLabels(['ID', 'Nombre', 'Apellido', 'Edad', 'Grado', 'Promedio'])
            
            # Le damos ancho apropiado para cada columna
            self.tabla.setColumnWidth(0, 50)   # ID
            self.tabla.setColumnWidth(1, 150)  # Nombre
            self.tabla.setColumnWidth(2, 150)  # Apellido
            self.tabla.setColumnWidth(3, 80)   # Edad
            self.tabla.setColumnWidth(4, 100)  # Grado
            self.tabla.setColumnWidth(5, 100)  # Promedio
            
            # Se llena la tabla con los datos de los estudiantes
            for fila, registro in enumerate(registros):
                for columna, valor in enumerate(registro):
                    # Muestra la cadena vacía en lugar de 'None' para valores NULL
                    if valor is None:
                        display = ''
                    else:
                        # Formateos específicos por columna
                        if columna == 5:  # Promedio -> formato con 2 decimales
                            try:
                                display = f"{float(valor):.2f}"
                            except Exception:
                                display = str(valor)
                        elif columna == 3:  # Edad -> entero
                            try:
                                display = str(int(valor))
                            except Exception:
                                display = str(valor)
                        else:
                            display = str(valor)

                    item = QTableWidgetItem(display)

                    # La alineación para columnas numéricas
                    if columna in (0, 3, 5):
                        item.setTextAlignment(Qt.AlignCenter)

                    # Se pone de verde los promedios altos y de rojo los bajos (si hay valor)
                    if columna == 5 and valor is not None:
                        try:
                            promedio = float(valor)
                            if promedio >= 9.0:
                                item.setBackground(QColor('#ccffcc'))  # Verde para buenas notas
                            elif promedio <= 6.0:
                                item.setBackground(QColor('#ffcccc'))  # Rojo para notas bajas
                        except Exception:
                            pass

                    self.tabla.setItem(fila, columna, item)
                    
        except Exception as e:
            # Mostrar y registrar traceback completo para saber por qué falla la carga
            print("Error al cargar los estudiantes:", e)
            traceback.print_exc()
            QMessageBox.critical(self, "Error", f"Error al cargar los estudiantes: {str(e)}\n\nVer consola para más detalles.")
        finally:
            conexion.close()
            self.actualizar_etiqueta_pagina()
            self.actualizar_botones()

    def actualizar_etiqueta_pagina(self):
        # Actualizo la etiqueta que muestra la página actual
        total_paginas = max(1, (self.total_registros + self.registros_por_pagina - 1) // self.registros_por_pagina)
        self.lbl_pagina.setText(f"Página {self.pagina_actual + 1} de {total_paginas}")

    def actualizar_botones(self):
        # Activa o desactiva los botones según si hay más páginas
        total_paginas = max(1, (self.total_registros + self.registros_por_pagina - 1) // self.registros_por_pagina)
        self.btn_anterior.setEnabled(self.pagina_actual > 0)
        self.btn_siguiente.setEnabled(self.pagina_actual < total_paginas - 1)

    def pagina_anterior(self):
        # Va a la página anterior
        self.pagina_actual -= 1
        self.mostrar_registros()

    def pagina_siguiente(self):
        # Va a la página siguiente
        self.pagina_actual += 1
        self.mostrar_registros()

# Esta función prepara la base de datos cuando inicia el programa
def configurar_base_datos():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='sharktopus12'  
        )
        
        if connection.is_connected():
            print("Conectado a MySQL")
            cursor = connection.cursor()
            
            # Crea la base de datos si no existe
            cursor.execute("CREATE DATABASE IF NOT EXISTS colegio")
            print("Base de datos 'colegio' lista")
            
            cursor.execute("USE colegio")
            
            # Crea la tabla de estudiantes con más campos
            create_alumno_table = """
            CREATE TABLE IF NOT EXISTS alumno (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                apellido VARCHAR(50) NOT NULL,
                edad INT,
                grado VARCHAR(20),
                promedio DECIMAL(3,2)
            );
            """
            cursor.execute(create_alumno_table)
            print("Tabla de estudiantes lista")
            # Asegura que las columnas necesarias existen (por si la tabla antigua no las tiene)
            try:
                cursor.execute("SHOW COLUMNS FROM alumno")
                existing_cols = [row[0] for row in cursor.fetchall()]
                columnas_necesarias = {
                    'edad': 'INT',
                    'grado': 'VARCHAR(20)',
                    'promedio': 'DECIMAL(3,2)'
                }
                for col, col_type in columnas_necesarias.items():
                    if col not in existing_cols:
                        cursor.execute(f"ALTER TABLE alumno ADD COLUMN {col} {col_type}")
                        print(f"Columna '{col}' agregada a 'alumno'")
            except Error as e:
                print("No pude verificar/alterar columnas de 'alumno':", e)
                traceback.print_exc()
            
            # Si la tabla está vacía, se agrega algunos estudiantes de ejemplo
            cursor.execute("SELECT COUNT(*) FROM alumno")
            count = cursor.fetchone()[0]
            
            if count == 0:
                estudiantes_ejemplo = [
                    ('María', 'Gonzales', 15, '10mo Grado', 9.2),
                    ('Carlos', 'Rodríguez', 16, '11vo Grado', 8.7),
                    ('Ana', 'Martínez', 14, '9no Grado', 9.5),
                    ('Luis', 'Fernández', 15, '10mo Grado', 7.8),
                    ('Sofía', 'López', 17, '12vo Grado', 9.8),
                    ('Diego', 'Pérez', 16, '11vo Grado', 8.9),
                    ('Valeria', 'García', 15, '10mo Grado', 9.1),
                    ('Javier', 'Silva', 14, '9no Grado', 8.4),
                    ('Camila', 'Torres', 17, '12vo Grado', 9.6),
                    ('Andrés', 'Ramírez', 16, '11vo Grado', 8.2),
                    ('Isabella', 'Díaz', 15, '10mo Grado', 9.3),
                    ('Mateo', 'Herrera', 14, '9no Grado', 7.9),
                    ('Lucía', 'Rojas', 17, '12vo Grado', 9.7),
                    ('Sebastián', 'Morales', 16, '11vo Grado', 8.6),
                    ('Emma', 'Ortega', 15, '10mo Grado', 9.0)
                ]
                
                insert_query = "INSERT INTO alumno (nombre, apellido, edad, grado, promedio) VALUES (%s, %s, %s, %s, %s)"
                cursor.executemany(insert_query, estudiantes_ejemplo)
                connection.commit()
                print(f"Agregados {len(estudiantes_ejemplo)} estudiantes de ejemplo")
            
            # También se crea las otras tablas por si las necesitamos después
            create_materia_table = """
            CREATE TABLE IF NOT EXISTS materia (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL
            );
            """
            cursor.execute(create_materia_table)
            
            create_cursado_table = """
            CREATE TABLE IF NOT EXISTS cursado (
                id_alumno INT,
                id_materia INT,
                PRIMARY KEY (id_alumno, id_materia),
                FOREIGN KEY (id_alumno) REFERENCES alumno(id) ON DELETE CASCADE,
                FOREIGN KEY (id_materia) REFERENCES materia(id) ON DELETE CASCADE
            );
            """
            cursor.execute(create_cursado_table)
            print("Todas las tablas creadas correctamente")

            # Actualizar registros existentes para tener datos completos
            cursor.execute("UPDATE alumno SET edad = 15 WHERE edad IS NULL")
            cursor.execute("UPDATE alumno SET grado = '10mo Grado' WHERE grado IS NULL")
            cursor.execute("UPDATE alumno SET promedio = 8.00 WHERE promedio IS NULL")
            connection.commit()
            print("Registros existentes actualizados")

    except Error as e:
        print(f"Error con la base de datos: {e}")
        
    finally: 
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión cerrada")

# Aquí empieza el programa
if __name__ == '__main__':
    # Primero se prepara la base de datos
    configurar_base_datos()
    
    # Luego arrancamos la aplicación de escritorio
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec_())