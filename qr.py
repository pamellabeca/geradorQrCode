import qrcode

imagem = qrcode.make('https://www.efset.org/cert/nhSUMo')
imagem.save('qrcode-certificado.png')
