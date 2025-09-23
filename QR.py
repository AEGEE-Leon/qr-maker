import qrcode
from PIL import Image
import os


def create_qr_with_logo(url, logo_path, output_path, language, qr_color="#000000", bg_color="#FFFFFF"):

    if(language == "es"):
        logo_path = "ES_" + logo_path
        print("Logo path is set to:", logo_path )
    elif(language == "en"):
        logo_path = "EN_" + logo_path
        print("Logo path is set to:", logo_path)


    output_path = output_path + logo_path
    # Crear el código QR
    qr = qrcode.QRCode(
        version=4,  # Controla el tamaño del QR (más alto, más datos).
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Alta tolerancia a errores.
        box_size=20,  # Tamaño de cada "cuadro" del QR.
        border=2,  # Tamaño del borde del QR.
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Generar la imagen del QR con colores personalizados
    qr_image = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')

    # Abrir la imagen del logo
    logo = Image.open(logo_path)

    # Ajustar el tamaño del logo
    qr_width, qr_height = qr_image.size
    logo_size = qr_width // 3  # El logo ocupará aproximadamente 1/3 del ancho del QR.
    logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

    # Pegar el logo en el centro del QR
    pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)
    qr_image.paste(logo, pos, mask=logo if logo.mode == 'RGBA' else None)

    # Asegurar que la carpeta de salida existe
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Guardar el QR final
    qr_image.save(output_path)
    print(f"QR code guardado en: {output_path}")


# Configuración
language = ""  # Cambia a "en" para inglés
url = "paypal.me/aegeeleon"
logo_path = "logoPaypal.png"  # Ruta al archivo de la imagen (logo)
output_path = "output/qr_with_"  # Nombre del archivo de salida

# Especificar colores personalizados con hex
qr_color = "#000000"  # Azul brillante (DeepSkyBlue)
bg_color = "#f6f6f6"  # Amarillo claro (LightYellow)

# Generar el QR
create_qr_with_logo(url, logo_path, output_path, language, qr_color=qr_color, bg_color=bg_color)