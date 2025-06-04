import qrcode
import qrcode.constants
data ="https://tasneem78899.wixstudio.com/openways1"

qr = qrcode.QRCode(
    version= 1 ,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(data)
qr.make(fit= True)

img = qr.make_image(fill_color ="black" , back_color ="white")
img.save("demo_qrcode.png")

print("Qr code i generated and saved as demo_qrcode.png")