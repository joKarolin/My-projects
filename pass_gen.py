from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Define the specific special characters you want to include
SPECIAL_CHARACTERS = "!@#$%^&*()+=-"

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = SPECIAL_CHARACTERS
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Ensure the password meets the criteria by using a list
    pwd = []
    while len(pwd) < min_length or not meets_criteria(pwd, numbers, special_characters):
        new_char = random.choice(characters)
        pwd.append(new_char)

    random.shuffle(pwd)
    return ''.join(pwd)

def meets_criteria(pwd, numbers, special_characters):
    has_number = any(char in string.digits for char in pwd)
    has_special = any(char in SPECIAL_CHARACTERS for char in pwd)

    if numbers and not has_number:
        return False
    if special_characters and not has_special:
        return False
    return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password_route():
    min_length = int(request.form['min_length'])
    has_number = request.form['has_number'].lower() == 'y'
    has_special = request.form['has_special'].lower() == 'y'

    pwd = generate_password(min_length, has_number, has_special)
    return render_template('result.html', password=pwd)

if __name__ == '__main__':
    app.run(debug=True)
