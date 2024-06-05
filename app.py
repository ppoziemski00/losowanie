from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random_number')
def random_number():
    number = random.randint(1, 100)
    return jsonify(number=number)

if __name__ == '__main__':
    app.run(debug=True)
