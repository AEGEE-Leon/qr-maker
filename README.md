
# 📘 Generador de Códigos QR Personalizados

Este proyecto permite generar códigos QR personalizados de dos maneras:

1. **QR con un bloque de texto en el centro**
2. **QR con una imagen insertada en el centro** (Ya con la imagen central hecha: [Ejemplos de Canva](https://www.canva.com/design/DAGx0s_7rsY/fZfj3gSCNGs4EhWNVfynfA/edit))

Incluye dos scripts independientes para que puedas generar fácilmente múltiples QR de forma automática.

# 🛠️ Requisitos

* Python 3.8 o superior
* Instalar dependencias:

```bash
pip install qrcode[pil] pillow
```

# 📦 Estructura esperada del proyecto

```
/
├── img/                 # Imágenes para los QR con iconos
├── output/              # Aquí se guardan todos los QR generados
├── QR_buildImage.py     # Script para QR con bloque + texto
├── QR_fullImage.py      # Script para QR con imagen central
└── README.md
```

Asegúrate de que las carpetas `img/` y `output/` existan.

---

# 📘 Uso del script: **QR_buildImage.py**

![alt text](demo_img/qr_output.png "Title")


### (QR con recuadro y texto central)

Este script genera códigos QR con un **bloque de color** en el centro que contiene un texto personalizado.

## ✅ Cómo usarlo

### 1️⃣ Edita la lista `data`

Dentro del script encontrarás algo así:

```python
# ------------------------
# CONFIGURATION
# ------------------------
url = "https://forms.gle/xvW9kUkar5P2o5VK6"
text = "LTCrossing Form"
output_path = "output/qr_output.png"
logo_path = "logoAEGEE.png"
```

Cada elemento significa:

* **url** → Enlace que contendrá el QR
* **text** → Texto que aparecerá en el cuadro central
* **output_path** → Nombre del PNG generado
* **logo_path** → Nombre de la imagen del logo de AEGEE-León


### 2️⃣ Ejecuta el script

```bash
python QR_buildImage.py
```

### 3️⃣ Revisa la carpeta `output/`

El QR aparecerán automáticamente como archivo `.png`.

---

# 📗 Uso del script: **QR_fullImage.py**

![alt text](demo_img/QR_002_actividades_locales.png "Title")

### (QR con imagen insertada en el centro)

Este script genera códigos QR que incorporan una **imagen o icono** al centro.

## ✅ Cómo usarlo

### 1️⃣ Prepara las imágenes en la carpeta `img/`

Coloca ahí las imágenes que quieras usar como icono (JPG o PNG).

Ejemplo:

```
img/002-actividades-locales.png
```

### 2️⃣ Edita la lista `data`

En el script encontrarás algo así:

```python
data = [
    "actividades_locales": (
        "https://uleaegee.unileon.es/actividades-locales",
        "002-actividades-locales.png"
    ),
]
```

Cada parámetro significa:

* **actividades_locales** → Nombre del archivo final -> QR_002_actividades_locales.png
* **https://uleaegee.unileon...** → Enlace que contendrá el QR
* **002-actividades-locales.png** → Imagen insertada en el centro (debe estar en `img/`)

Puedes añadir todas las entradas que necesites.

### 3️⃣ Ejecuta el script

```bash
python QR_fullImage.py
```

### 4️⃣ Revisa la carpeta `output/`

Los QR generados aparecerán en formato `.png`.