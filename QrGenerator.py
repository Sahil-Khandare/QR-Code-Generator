import qrcode

text = input("Enter any text: ").strip()
file_path = "qrcode.png"

qr = qrcode.QRCode()
qr.add_data(text)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("QR Code was generated!")