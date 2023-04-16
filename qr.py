import qrcode 

qr = qrcode.QRCode(
    version=15,
    box_size=10,
    border=5
)
data = "https://www.youtube.com/channel/UC2lrNnCSAA0j5qU1mUGNNYA"
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black" , back_color="white")
img.save('text.png')

#me = qrcode.make(
    #'https://www.youtube.com/channel/UC2lrNnCSAA0j5qU1mUGNNYA'
#)
#me.save('myQRcode.png')
#me.show()