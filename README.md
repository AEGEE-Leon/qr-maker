# QR Maker

Generador de códigos QR personalizados con texto y logo para AEGEE-León.

## Requisitos
Instalar dependencias:
```bash
pip install qrcode[pil] pillow
````

## Uso

Ejemplo en Python:

```python
url = "https://forms.gle/xvW9kUkar5P2o5VK6"
text = "LTCrossing Form"
output_path = "output/qr_output.png"
logo_path = "logoAEGEE.png"
```

``` bash
python3 QR.py
```

El QR se guardará como `qr_output.png` en la carpeta output
