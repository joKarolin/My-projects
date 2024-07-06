from flask import Flask, render_template, request

app = Flask(__name__)

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def vigenere_encrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    key = key.lower()
    result = ""
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    plain_text = ""
    caesar_shift = ""
    vigenere_key = ""
    result_text = ""

    if request.method == 'POST':
        plain_text = request.form.get('plain_text', '')
        caesar_shift = request.form.get('caesar_shift', 0)
        vigenere_key = request.form.get('vigenere_key', '')
        action = request.form.get('action', 'Encrypt')

        if plain_text and caesar_shift and vigenere_key:
            caesar_shift = int(caesar_shift)
            if action == 'Encrypt':
                encrypted = caesar_encrypt(plain_text, caesar_shift)
                result_text = vigenere_encrypt(encrypted, vigenere_key)
            elif action == 'Decrypt':
                decrypted = vigenere_decrypt(plain_text, vigenere_key)
                result_text = caesar_decrypt(decrypted, caesar_shift)

    return render_template('enc_project/index.html', plain_text=plain_text, caesar_shift=caesar_shift, vigenere_key=vigenere_key, result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
