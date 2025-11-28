import qrcode
from PIL import Image
import os

def create_qr_with_center_image(url, image_path, output_path,
                                qr_color="#000000", bg_color="#FFFFFF"):
    # Create QR
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Para logo grande
        box_size=20,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color=qr_color, back_color=bg_color).convert("RGB")

    # Insert center image
    center_img = Image.open(image_path).convert("RGBA")

    qr_w, qr_h = qr_image.size
    max_size = qr_w // 3  # Logo ocupa 1/3 del QR

    center_img.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)

    # Center position
    x = (qr_w - center_img.width) // 2
    y = (qr_h - center_img.height) // 2
    qr_image.paste(center_img, (x, y), center_img)

    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    qr_image.save(output_path)
    print(f"✅ QR generado en: {output_path}")


# -----------------------------------------
#   TUS DATOS (EJEMPLO)
# -----------------------------------------
data = {
#     "Nombre de archivo": (
#        "URL a la dirige",
#        "nombre-foto.png"
#    ),
    "aegee_leon_es": (
        "https://uleaegee.unileon.es/aegee-leon/",
        "000-aegee-leon.png"
    ),
    "aegee_leon_en": (
        "https://uleaegee.unileon.es/en/aegee-leon-2",
        "000-aegee-leon.png"
    ),
    "aegee_europe_es": (
        "https://uleaegee.unileon.es/aegee-europe/",
        "001-aegee-europe.png"
    ),
    "aegee_europe_en": (
        "https://uleaegee.unileon.es/en/aegee-europe-2/",
        "001-aegee-europe.png"
    ),
    "actividades_locales": (
        "https://uleaegee.unileon.es/actividades-locales",
        "002-actividades-locales.png"
    ),
    "local_activities": (
        "https://uleaegee.unileon.es/en/local-activities",
        "002-local-activities.png"
    ),
    "actividades_erasmus": (
        "https://uleaegee.unileon.es/actividades-erasmus",
        "003-actividades-erasmus.png"
    ),
    "erasmus_activities": (
        "https://uleaegee.unileon.es/en/erasmus-activities",
        "003-erasmus-activities.png"
    ),
    "socios_locales": (
        "https://uleaegee.unileon.es/socios",
        "004-socios-locales.png"
    ),
    "local_members": (
        "https://uleaegee.unileon.es/en/members",
        "004-local-members.png"
    ),
    "socios_erasmus": (
        "https://uleaegee.unileon.es/socios-erasmus",
        "005-socios-erasmus.png"
    ),
    "erasmus_members": (
        "https://uleaegee.unileon.es/en/erasmus-members",
        "005-erasmus-members.png"
    ),
    "descuentos": (
        "https://uleaegee.unileon.es/colaboradores/",
        "006-descuentos.png"
    ),
    "discounts": (
        "https://uleaegee.unileon.es/en/partners",
        "006-discounts.png"
    ),
    "descuentos_erasmus": (
        "https://uleaegee.unileon.es/descuentos-erasmus/",
        "007-descuentos-erasmus.png"
    ),
    "erasmus_discounts": (
        "https://uleaegee.unileon.es/en/erasmus-discounts",
        "007-erasmus-discounts.png"
    ),
    "contacto": (
        "http://uleaegee.unileon.es/contacto/",
        "008-contacto.png"
    ),
    "contact": (
        "https://uleaegee.unileon.es/en/contact",
        "008-contact.png"
    ),
    "devoluciones": (
        "http://uleaegee.unileon.es/devoluciones/",
        "009-devoluciones.png"
    ),
    "refunds": (
        "https://uleaegee.unileon.es/en/refunds",
        "009-refunds.png"
    ),
    "paypal": (
        "paypal.me/aegeeleon",
        "010-paypal.png"
    ),  
    "formulario_socios_locales": (
        "https://forms.gle/qGH1w9onDb3dkez87",
        "011-formulario-socios-locales.png"
    ),
    "whatsapp_aegee_leon": (
        "https://wa.me/message/ULSG2JHPSQBLH1?src=qr",
        "012-whatsapp-aegee-leon.png"
    ),

}

# -----------------------------------------
#   GENERACIÓN AUTOMÁTICA
# -----------------------------------------
for nombre, (url, img) in data.items():
    # Crear nombre del archivo correcto
    nombre_archivo = "QR_" + img[:3] + "_" + nombre.replace(" ", "_") + ".png"

    output_path = os.path.join("output", nombre_archivo)

    create_qr_with_center_image(url, "img/" + img, output_path)
