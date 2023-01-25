# Crio uma API simples com Flask que recebe dois valores e retorna a hipotenusa

import math
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Crio a rota da API
@app.route('/api', methods=['GET'])
def api():
    # Pego os valores passados na URL e retorno a hipotenusa calculada
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    c = math.sqrt(float(a*a) + float(b*b))
    return str(c)


if __name__ == '__main__':
    app.run()