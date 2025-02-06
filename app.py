from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_numbers')
def generate_numbers():
    numbers = [random.randint(1, 100) for _ in range(3)]
    return jsonify(numbers)

if __name__ == '__main__':
    app.run(debug=True)