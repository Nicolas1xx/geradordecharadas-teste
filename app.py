from flask import Flask, jsonify, request
import random
import firebase_admin
from firebase_admin import credentials, firestore
from flask_cors import CORS
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

load_dotenv()

FBKEY = json.loads(os.getenv('CONFIG_FIREBASE'))

cred = credentials.Certificate(FBKEY)
firebase_admin.initialize_app(cred)




#Conectando com o firestore da Firebase
db = firestore.client()




#---------ROTA PRINCIPAL DE TESTE---------#
@app.route('/')
def index():
    return "API TÁ ON", 200

#---------MÉTODO GET - CHARADA ALEATÓRIA---------#
@app.route('/charadas', methods=['GET'])
def charada_aleatoria():
    charadas = []
    lista = db.collection('charadas').stream()
    for item in lista:
        charadas.append(item.to_dict())
    if charadas:
        return jsonify(random.choice(charadas)), 200
    else:
        return jsonify({"error": "Nenhuma charada encontrada"}), 404


#---------MÉTODO GET - CHARADA POR ID   ---------#
@app.route('/charadas/<id>', methods=['GET'])
def busca(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if doc:
        return jsonify(doc.to_dict()), 200
    else:
        return jsonify({"error": "Charada não encontrada"}), 404


#---------MÉTODO POST - ADICIONAR CHARADAS---------#
@app.route('/charadas', methods=['POST'])
def adicionar_charada():
    print("entrou no post")
    dados = request.json

    if "pergunta" in dados and "resposta" not in dados:
        return jsonify({"error": "Campos pergunta e resposta são obrigatórios"}), 400

    #contador
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id = contador_doc.get('id')
    novo_id = int(ultimo_id) + 1
    contador_ref.update({'id': novo_id}) #Atualização d coleção

    db.collection('charadas').document(str(novo_id)).set({
        'id': novo_id,
        'pergunta': dados['pergunta'],
        'resposta': dados['resposta']
    })

    return jsonify({"message": "Charada adicionada com sucesso"}), 201

#---------MÉTODO PUT - ATUALIZAR CHARADA---------#
@app.route('/charadas/<id>', methods=['PUT'])
def atuliazar_charada(id):
    dados = request.json

    if "pergunta" not in dados and "resposta" not in dados:
        return jsonify({"error": "Necessário informar pergunta ou resposta"}), 400

    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            'pergunta': dados['pergunta'],
            'resposta': dados['resposta']
        })
        return jsonify({"message": "Charada atualizada com sucesso"}), 201
    else:
        return jsonify({"error": "Charada não encontrada"}), 404

#---------MÉTODO DELETE - REMOVER CHARADA---------#
@app.route('/charadas/<id>', methods=['DELETE'])
def excluir_charada(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({"error": "Charada não encontrada"}), 404
    else:
        doc_ref.delete()
        return jsonify({"message": "Charada removida com sucesso"}), 200



        
if __name__ == '__main__':
    app.run(debug=True)