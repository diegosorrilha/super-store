from flask import Flask
import os
from flask import jsonify

app = Flask(__name__)

@app.route("/products")
def get_produtcs():
    products = [
        {
            'id': '1',
            'nome': 'Moto X 4',
            'descricao': 'Celular Moto X 4',
            'categoria': 'celular',
            'preco': 2000.00
        }, 
        {
            'nome': 'Moto G 3',
            'descricao': 'Celular Moto G 3',
            'categoria': 'celular',
            'preco': 1299.59
        }, 
        {
            'nome': 'Iphone 10',
            'descricao': 'Celular Iphone 10',
            'categoria': 'celular',
            'preco': 1499.99
        }, 
        {
            'nome': 'Caneca PyCharm',
            'descricao': 'Caneca da melhor IDE do mundo',
            'categoria': 'utilidades',
            'preco': 50.00
        }, 
        {
            'nome': 'Kit 10 Post-It',
            'descricao': 'Kit com 10 Post-It coloridos',
            'categoria': 'papelaria',
            'preco': 30.00
        }, 
    ]

    print(os.getenv('NAME'))

    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)

