from flask import Flask, render_template, request
from pyDes import *
import base64
import binascii
from random import Random
app = Flask(__name__)


@app.route('/decode', methods=['POST', 'GET'])
def des_decrypt():
    if request.method == 'POST':
        cipher = request.form.get('cipher')
        secret_key = request.form.get('key')
        iv = secret_key
        k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(cipher), padmode=PAD_PKCS5)
        return render_template('des_decode.html', de=de)
    else:
        return render_template('des_decode.html')


@app.route('/encode', methods=['GET', 'POST'])
def des_encrypt():
    if request.method == 'POST':
        text = request.form.get('text')
        secret_key = request.form.get('key')
        iv = secret_key
        k = des(secret_key, ECB, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(text, padmode=PAD_PKCS5)
        return render_template('des_encode.html', en = base64.b64encode(en), en2 = binascii.b2a_hex(en))
    else:
        randomlength = 8
        str = ''
        chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            str += chars[random.randint(0, length)]
        return render_template('des_encode.html',str = str)


if __name__ == '__main__':
    app.run(debug=True)
