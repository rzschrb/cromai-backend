from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

# Rota para a página inicial
@app.route('/')
@cross_origin()
def index():
    return {"id":"200", "response":"Hello, World!"}

# Recebe os valores dos lados e da hipotenusa e calcula o valor que falta.
# Testa se os valores são validos e retorna o valor calculado.
# Erro 1: Irá ocorrer caso todos os lados sejam negativos ou igual a 0.
# Erro 2: Irá ocorrer caso os lados A e B sejam negativos ou igual a 0. 
# Erro 3: Irá ocorrer caso os lados A e C sejam negativos ou igual a 0.
# Erro 4: Irá ocorrer caso os lados B e C sejam negativos ou igual a 0.
# Erro: Irá ocorrer caso todos os lados sejam preenchidos.
@app.route('/calculate/<side_a>/<side_b>/<hipo_c>/')
def calculate(side_a, side_b, hipo_c):
    side_a = float(side_a)
    side_b = float(side_b)
    hipo_c = float(hipo_c)
    if side_a <= 0 and side_b <= 0 and hipo_c <= 0:
        return {"id":"404", "response":"Erro 1: Ao menos dois lados do triângulo devem ser positivos."}
    elif side_a <= 0 and side_b <= 0:
        return {"id":"404", "response":"Erro 2: Ao menos dois lados do triângulo devem ser positivos."}
    elif side_a <= 0 and hipo_c <= 0:
        return {"id":"404", "response":"Erro 3: Ao menos dois lados do triângulo devem ser positivos."}
    elif side_b <= 0 and hipo_c <= 0:
        return {"id":"404", "response":"Erro 4: Ao menos dois lados do triângulo devem ser positivos."}
    elif side_a == 0:
        if (hipo_c > side_b):
            result = "{:.2f}".format((hipo_c ** 2 - side_b ** 2) ** 0.5)
            return {"id":"200", "response":result}
        else:
            return {"id":"404", "response":"Erro 6: O lado B não pode ser igual ou maior que a hipotenusa."}
    elif side_b == 0:
        if (hipo_c > side_a):
            result = "{:.2f}".format((hipo_c ** 2 - side_a ** 2) ** 0.5)
            return {"id":"200", "response":result}
        else:
            return {"id":"404", "response":"Erro 7: O lado A não pode ser igual ou maior que a hipotenusa."}
    elif hipo_c == 0:
        result = "{:.2f}".format((side_a ** 2 + side_b ** 2) ** 0.5)
        return {"id":"200", "response":result}
    else:
        return {"id":"404", "response":"Para calcular, preencha apenas dois lados do triângulo."}

# Inicia o servidor.
if __name__ == '__main__':
    app.run(debug=True)