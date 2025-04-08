from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('qrcode_encoder_decoder/qrcode.png')

result = decode(img)

print(result)