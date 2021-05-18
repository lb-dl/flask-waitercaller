import qrcode


class QRHelper:
    def make_qrcode(self, url, tableid):
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save('static/media/' + str(tableid) + '.png')
            return img
        except Exception as e:
            return e
