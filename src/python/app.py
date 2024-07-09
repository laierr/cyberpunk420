from flask import Flask, jsonify
import random

# List of Roman names
roman_names = [
    "Aurelius", "Brutus", "Cassius", "Decimus", "Faustus",
    "Gaius", "Horatius", "Julius", "Lucius", "Marcus",
    "Nero", "Octavius", "Publius", "Quintus", "Romulus",
    "Sextus", "Tiberius", "Urbanus", "Valerius"
]

# Generate a random service name on startup
service_name = random.choice(roman_names)

app = Flask(__name__)

@app.route('/service_name', methods=['GET'])
def get_service_name():
    return jsonify({"service_name": service_name})

if __name__ == '__main__':
    app.run(debug=True)
