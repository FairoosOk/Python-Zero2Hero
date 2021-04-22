import pyqrcode
import png
qr = pyqrcode.create('www.google.com')
qr.png('QRT1.png',scale=4)
