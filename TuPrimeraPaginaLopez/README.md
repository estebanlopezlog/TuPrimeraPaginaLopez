

<h1 align="center">🧠 Sistema de Gestión Logístico-Comercial</h1>
<p align="center">
  <strong>Proyecto Final - Python & Django (Coderhouse 2025)</strong><br>
  Desarrollado por <a href="https://www.linkedin.com/in/estebanlopezlog" target="_blank">Esteban López</a>  
</p>

---

### 📦 Tecnologías principales

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Django-5.2.8-092E20?logo=django&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Bootstrap-5.3-7952B3?logo=bootstrap&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/SQLite-DB-003B57?logo=sqlite&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white&style=for-the-badge" />
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-005C7A?logo=plotly&logoColor=white&style=for-the-badge" />
</p>

---

## 🎯 Objetivo del proyecto  

> Desarrollar una **aplicación web integral** que permita la **gestión logística y comercial** de una empresa, centralizando los datos de clientes, productos, sucursales, vendedores y ventas en una interfaz web moderna, intuitiva y segura.  

Cada módulo incluye formularios dinámicos para **crear, editar, eliminar y listar registros**, con persistencia de datos en una base **SQLite3**.  
Además, el sistema incluye un **Dashboard analítico**, con indicadores visuales de rendimiento.

---

## ⚙️ Instalación y ejecución

### 🧩 1️⃣ Clonar el repositorio  
git clone https://github.com/estebanlopezlog/TuPrimeraPaginaLopez.git
cd TuPrimeraPaginaLopez


### 📦 2️⃣ Instalar dependencias
> pip install -r requirements.txt

### 🚀 3️⃣ Ejecutar el servidor
> python manage.py runserver
> Luego, ingresar a 👉 http://127.0.0.1:8000/

### 👤 Usuarios de prueba
Rol	Usuario	Contraseña	Permisos

- 🧭 Superusuario (Dirección y Gerencia) user: admin | pass: Perros123	(Acceso total)
- 💼 Vendedor (Grupo Vendedores) user: Vendedor | pass: Junio.2020	(Permisos limitados)
- 👩‍💻 Vendedora (Grupo Vendedores) user: Malena | pass: maradona	(Permisos limitados)

⚠️ Los vendedores pueden crear y consultar registros, pero no eliminarlos ni modificarlos.

### 🖥️ Funcionalidades principales

- ✅ Gestión completa de entidades: Clientes, Productos, Sucursales, Vendedores y Ventas.
- ✅ Video instructivo disponible en la pestaña Inicio.
- ✅ Dashboard analítico con KPIs dinámicos.
- ✅ Registro, edición de perfil y cambio de contraseña.
- ✅ Filtros dinámicos para búsquedas instantáneas.
- ✅ Gestión de permisos diferenciada (admin / vendedor).
- ✅ Control de errores 403 y 404 personalizados.

### 📊 Dashboard incluido
> El sistema incluye un panel de control visual con los siguientes indicadores:
- 📈 Altas de clientes por día
- 💳 Ventas registradas por rango de fecha
- 💰 Total vendido por forma de pago
- 🏆 Ranking de vendedores con más ventas
- 📉 Tendencias de negocio

Todos los gráficos se actualizan automáticamente según el período seleccionado.

🧾 Dependencias
>- asgiref==3.11.0
>- Django==5.2.8
>- django-select2==8.4.3
>- pandas==2.3.3
>- numpy==2.3.5
>- matplotlib==3.10.7
>- Pillow==12.0.0
>- sqlparse==0.5.3
>- tzdata==2025.2
>- python-dateutil==2.9.0.post0
>- kiwisolver==1.4.9
>- pyparsing==3.2.5
>- fonttools==4.60.1
>- packaging==25.0
>- charset-normalizer==3.4.4
>- idna==3.11
>- urllib3==2.5.0
>- six==1.17.0
>- requests==2.32.3


👨‍💻 Autor
> Esteban López
> 📍 Buenos Aires, Argentina

<p align="center"> <img src="https://img.shields.io/badge/Proyecto_Final-Coderhouse_2025-ff5733?style=for-the-badge&logo=github&logoColor=white" /> </p> <p align="center"> ⭐ *TuPrimeraPaginaLopez — desarrollado por Esteban López* ⭐ </p>
