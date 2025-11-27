import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

def create_qr_with_center_block(url, text, output_path,
                                logo_path="logoAEGEE.png",
                                qr_color="#000000", bg_color="#FFFFFF",
                                block_color="#0A3D91"):  # Blue rectangle background

    # Create QR
    qr = qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=20,
        border=2,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color=qr_color, back_color=bg_color).convert('RGB')

    # Open logo
    logo = Image.open(logo_path).convert("RGBA")

    # Resize logo while keeping proportions
    qr_width, qr_height = qr_image.size
    block_size = qr_width // 3  # central block ~1/3 QR size

    max_logo_width = block_size * 0.8
    max_logo_height = block_size // 2

    logo_ratio = logo.width / logo.height
    if logo.width > logo.height:
        new_width = int(max_logo_width)
        new_height = int(new_width / logo_ratio)
    else:
        new_height = int(max_logo_height)
        new_width = int(new_height * logo_ratio)

    if new_width > max_logo_width:
        new_width = int(max_logo_width)
        new_height = int(new_width / logo_ratio)
    if new_height > max_logo_height:
        new_height = int(max_logo_height)
        new_width = int(new_height * logo_ratio)

    logo = logo.resize((new_width, new_height), Image.Resampling.LANCZOS)

    # Create block (blue rectangle)
    block = Image.new("RGBA", (block_size, block_size), block_color)

    # Draw text
    draw = ImageDraw.Draw(block)
    try:
        # Use bold sans-serif font if available
        font = ImageFont.truetype("arialbd.ttf", size=block_size // 7)
    except:
        try:
            font = ImageFont.truetype("DejaVuSans-Bold.ttf", size=block_size // 7)
        except:
            font = ImageFont.load_default()

    # Add horizontal padding
    padding_x = block_size // 12
    max_text_width = block_size - 2 * padding_x

    # Wrap text to fit inside padded width
    words = text.split(" ")
    wrapped_lines = []
    current_line = ""

    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] - bbox[0] <= max_text_width:
            current_line = test_line
        else:
            wrapped_lines.append(current_line)
            current_line = word
    if current_line:
        wrapped_lines.append(current_line)

    # Calculate text block height
    line_height = font.getbbox("Ay")[3] - font.getbbox("Ay")[1]
    total_text_height = line_height * len(wrapped_lines)

    # Center text in top half
    start_y = (block_size // 2 - total_text_height) // 2
    for line in wrapped_lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        text_width = bbox[2] - bbox[0]
        x = (block_size - text_width) // 2
        draw.text((x, start_y), line, font=font, fill="white")
        start_y += line_height

    # Paste logo in bottom half, centered
    logo_x = (block_size - new_width) // 2
    logo_y = (block_size // 2) + ((block_size // 2 - new_height) // 2)
    block.paste(logo, (logo_x, logo_y), logo)

    # Paste block in the center of QR
    pos = ((qr_width - block_size) // 2, (qr_height - block_size) // 2)
    qr_image.paste(block, pos, block)

    # Save output
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    qr_image.save(output_path)
    print(f"✅ QR generated at: {output_path}")


# ------------------------
# CONFIGURATION
# ------------------------
url = "https://uleaegee.unileon.es/actividades-locales"
text = "Actividades locales"
output_path = "output/qr_output.png"
logo_path = "logoAEGEE.png"

# Generate QR
create_qr_with_center_block(url, text, output_path, logo_path,
                            qr_color="#000000", bg_color="#f6f6f6",
                            block_color="#163e7a")
