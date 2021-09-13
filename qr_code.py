import qrcode

qr_code = "https://bavinsblog.herokuapp.com/"

qr = qrcode.make(qr_code)
qr.save('img.jpg', scale=8)

