from flask import Flask, jsonify, request

app = Flask(__name__)

produtos = [
    {
        'id01':1,
        'nome01': 'Furadeira Bivolt',
        'descricao01': 'Furadeira Bivolt Power, ferramenta eletrica capaz de lhe ajudar nas tarefas do dia-a-dia.',
        'valor01': 'R$220,00'
    },
    {
        'id02':2,
        'nome02': 'Parafusadeira Eletrica',
        'descricao02': 'Parafusadeira Eletrica, equipamento potente.',
        'valor02': 'R$180,00'
    },
    {
        'id03':3,
        'nome03': 'Aspirador 220v',
        'descricao03': 'Aspirador 220v, capaz de aspirar qualquer tipo de poeira.',
        'valor03': 'R$110,00'
    },       
]

# Consultar TODOS
@app.route('/produtos',methods=['GET'])
def obter_produtos():
    return jsonify(produtos)
