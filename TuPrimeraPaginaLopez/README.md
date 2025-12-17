🧠 Sistema de Gestión Logístico-Comercial
📍 Nombre del proyecto

TuPrimeraPaginaLopez
Proyecto desarrollado como parte de la Entrega 3 del curso de Python & Django (Coderhouse).

🎯 Objetivo funcional

El objetivo de este proyecto es desarrollar una aplicación web integral para la gestión logística y comercial de una empresa.
El sistema permite administrar clientes, productos, vendedores, sucursales y ventas, concentrando toda la información en un entorno web claro, moderno y funcional.

Cada módulo incorpora formularios dinámicos que permiten crear, editar, eliminar y listar registros, con persistencia de datos en una base SQLite3.
Además, se implementan relaciones entre modelos, de modo que cada venta queda vinculada con su cliente, vendedor, sucursal y detalle de productos vendidos.

⚙️ Instalación y ejecución del proyecto
🔹 Clonar el repositorio
git clone https://github.com/estebanlopezlog/TuPrimeraPaginaLopez.git
cd TuPrimeraPaginaLopez

🔹 Instalar dependencias

Para que el proyecto funcione correctamente, instalá todas las librerías incluidas en el entorno original:

pip install Django==5.2.8
pip install django-select2==8.4.3
pip install asgiref==3.11.0
pip install sqlparse==0.5.3
pip install tzdata==2025.2
pip install pandas==2.3.3
pip install numpy==2.3.5
pip install matplotlib==3.10.7
pip install pillow==12.0.0
pip install requests==2.32.3
pip install python-dateutil==2.9.0.post0
pip install kiwisolver==1.4.9
pip install pyparsing==3.2.5
pip install fonttools==4.60.1
pip install packaging==25.0
pip install charset-normalizer==3.4.4
pip install idna==3.11
pip install urllib3==2.5.0
pip install six==1.17.0

👤 Usuarios de prueba (Django Admin)

Para acceder al panel o al sistema, se pueden utilizar las siguientes credenciales:

🧭 Superusuario – Dirección y Gerencia

Usuario: admin

Contraseña: admin123

💼 Grupo – Vendedores

Usuario: Vendedor

Contraseña: Junio.2020

📌 El superusuario posee permisos totales sobre el sistema.
El usuario Vendedor pertenece al grupo “Vendedores”, con permisos restringidos para crear y visualizar registros, pero sin posibilidad de eliminar o editar ciertos módulos.



🚀 Flujo de acceso

Ingresar al sistema:

http://127.0.0.1:8000/


Iniciar sesión con alguno de los usuarios anteriores.

Navegar por las secciones del panel lateral: Clientes, Productos, Vendedores, Sucursales y Ventas.

Cerrar sesión desde el botón “🔒 Cerrar sesión” ubicado en la esquina superior derecha.

🧩 Tecnologías utilizadas

Python 3.12.6

Django 5.2.8

Bootstrap 5 para la interfaz visual

SQLite3 como motor de base de datos local

📄 Autor

Esteban López
Desarrollado como proyecto académico dentro del curso Python & Django – Coderhouse (2025)