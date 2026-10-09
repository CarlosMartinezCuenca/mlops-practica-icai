import joblib
import numpy as np

from flask import Flask, request, jsonify


# Cargar el modelo entrenado
try: 
    model = joblib.load('model.pkl')
except FileNotFoundError:
    model = None
    print("Error: 'model.pkl' no encontrado. Por favor, asegúrese de haber ejecutado el script de entrenamiento.")


# Inicializar la aplicación Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': "Modelo no cargado. Por favor, asegúrese de haber ejecutado el script de entrenamiento."}), 500

    try:
        # Obtener los datos en formato JSON
        data = request.get_json(force=True)
        features = np.array(data['features']).reshape(1, -1)

        # Realizar la predicción
        prediction = model.predict(features)

        # Devolver la predicción en formato JSON
        return jsonify({'prediction': int(prediction[0])})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)