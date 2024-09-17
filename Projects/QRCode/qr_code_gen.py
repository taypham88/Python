'''Python has a qr code library'''

import os
import qrcode


def generate_qrcode(obj, path, filename='QRcodeoutput.png'):
    '''generates QR code in QRcode folder'''

    temppath = os.path.join(path,filename)
    base, ext = os.path.splitext(filename)

    counter = 1
    while os.path.exists(temppath):
        temppath = os.path.join(path, f"{base}_{counter}{ext}")
        counter += 1

    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(obj)
    qr.make(fit=False)

    img = qr.make_image(fill_color="red", back_color="blue")
    img.save(temppath)

if __name__== '__main__':
    Path = '/Users/taypham/Documents/GitHub/Python/Projects/QRCode'
    Text = 'www.linkedin.com/in/tay-pham1988'
    generate_qrcode(Text, Path)
