from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    # Simula predicción de rendimiento académico
    # (en una versión real, aquí cargarías tu modelo .h5)
    rendimiento = round(random.uniform(10, 20), 2)
    return jsonify({'resultado': f'{rendimiento} puntos'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7860)
