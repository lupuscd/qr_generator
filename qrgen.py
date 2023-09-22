import qrcode, os

def qr_gen(text, filename):

    qr = qrcode.QRCode(
    version=1, 
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    os.makedirs('imgs', exist_ok=True)
    img.save(f'imgs/{filename}.png')

text_input = input('Enter the text to be converted to qr code: ')
filename_input = input('Enter the name of the qr code: ')

qr_gen(text_input, filename_input)
