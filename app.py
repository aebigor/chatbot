from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Simulación de base de datos de paquetes
paquetes = {
    "123456": {
        "nombre": "Paquete A",
        "tipo_cobro": "Estandar",
        "monto_cobro": 100,
        "motivo_devolucion": "direccion erronea",
        "observacion": "",
        "justifica": False,
        "llamado": True,
        "telefono": "3174875518"  # Número telefónico
    },
    "654321": {
        "nombre": "Paquete B",
        "tipo_cobro": "Urgente",
        "monto_cobro": 200,
        "motivo_devolucion": "No reclamado",
        "observacion": "Contactar al cliente",
        "justifica": True,
        "llamado": False,
        "telefono": "3178773186"  # Número telefónico
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar_paquete', methods=['POST'])
def buscar_paquete():
    numero_guia = request.form.get('numero_guia')
    paquete = paquetes.get(numero_guia)
    if paquete:
        return jsonify(paquete), 200
    else:
        return jsonify({"error": "Paquete no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)