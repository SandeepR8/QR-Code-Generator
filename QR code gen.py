import qrcode
data="www.linkedin.com/in/sandeep-rokkala-68839b259"
qr=qrcode.make(data)
qr.save("linkedin_qrcode.png")
print("successful")
