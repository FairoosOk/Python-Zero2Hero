import pyqrcode
import eel

eel.init('web')

@eel.expose
def generate_qr(data):
    img = pyqrcode.create(data)
    img.png("web/qr.png", scale=8)
    print("QR code generation successful.")
    return "", 204

eel.start('index.html',mode='edge', size=(750, 800))


'''
pip install eel

Package install

pip install pyinstaller

python -m eel QRCode.py web --noconsole --onefile

with icon

python -m eel QRCode.py web --noconsole --onefile --icon=qrc.ico
'''