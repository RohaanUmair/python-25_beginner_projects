import qrcode

data = 'My name is Rohaan.'

qr = qrcode.QRCode(version=1, box_size=15, border=5)
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image()

img.save('qrcode_encoder_decoder/qrcode.png')