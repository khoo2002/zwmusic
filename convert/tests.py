import qrcode
from PIL import Image
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://zwmusic.herokuapp.com')
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
print(img)
Image.show(img)
img.save('zwapp.png')