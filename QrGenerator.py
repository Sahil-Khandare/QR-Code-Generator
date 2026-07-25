import qrcode

print("Enter your text (press Enter twice to finish):")

lines = []

while True:
    line = input()
    if line == "":
        break
    lines.append(line)

text = "\n".join(lines)

qr = qrcode.QRCode()
qr.add_data(text)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")

print("QR Code was generated!")