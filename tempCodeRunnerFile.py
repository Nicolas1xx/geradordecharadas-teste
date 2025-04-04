from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Lista de charadas sobre futebol
charadas_futebol = [
    {"id": 1, "charada": "Por que o Palmeiras não pode ser relojoeiro? Porque sempre fica esperando o momento certo para ganhar, mas o tempo nunca chega!"},
    {"id": 2, "charada": "O que o Corinthians faz quando a bola não entra? Chama o VAR e pede replay do último título... do século passado!"},
    {"id": 3, "charada": "Qual é a diferença entre o Flamengo e o Sherlock Holmes? O Sherlock resolve mistérios, e o Flamengo... só fica perdido na final!"},
    {"id": 4, "charada": "Por que o Botafogo nunca perde no Campeonato Carioca? Porque ele nunca está lá para perder... está sempre no rebaixamento!"},
    {"id": 5, "charada": "Qual time gosta de prometer o Mundial, mas nunca entrega? O Palmeiras, que já se acostumou a viver na promessa!"},
    {"id": 6, "charada": "O que o São Paulo e o Mundial têm em comum? Ambos estão no passado, ninguém mais lembra!"},
    {"id": 7, "charada": "Por que o Fluminense sempre é convidado para o churrasco? Porque sempre leva a carne... mas nunca aparece para assar!"},
    {"id": 8, "charada": "Como o Vasco celebra a vitória? Com um vídeo de 5 segundos no YouTube... antes de ser rebaixado de novo!"},
    {"id": 9, "charada": "Qual é o verdadeiro campeonato do Grêmio? O campeonato de 'Melhor Time de Vice'!"},
    {"id": 10, "charada": "Por que o Atlético-MG vai bem no mercado de trabalho? Porque, em toda negociação, ele é mestre em 'pesar' as derrotas!"},
    {"id": 11, "charada": "O que o Flamengo e o Titanic têm em comum? Ambos são gigantes, mas afundam quando a coisa esquenta!"},
    {"id": 12, "charada": "Qual a diferença entre o Neymar e um sorvete? O Neymar é o único que derrete rápido... e ainda cai sem ninguém tocar nele!"},
    {"id": 13, "charada": "O que é, o que é: tem camisa bonita, mas nunca ganha? O Fluminense, que vive de estilo e nunca de título!"},
    {"id": 14, "charada": "Por que o Grêmio adora uma 'guerra' psicológica? Porque é mais fácil ganhar na mente do que no campo!"},
    {"id": 15, "charada": "O que é um Vasco jogando na Copa do Brasil? Uma partida com final já pré-definido: rebaixamento garantido!"},
    {"id": 16, "charada": "O que o Palmeiras e o filme 'Rápido e Furioso' têm em comum? Ambos estão sempre acelerando, mas quando chega a hora de ganhar, não conseguem ultrapassar!"},
    {"id": 17, "charada": "Por que o Flamengo não precisa de espelho? Porque ele já sabe que está sempre refletindo sobre o título perdido!"},
    {"id": 18, "charada": "O que é o Atlético Mineiro e o futebol de botão? Ambos adoram girar, mas quando chega na final... param na última rodada!"},
    {"id": 19, "charada": "Como o São Paulo joga o Campeonato Brasileiro? Como uma maratona: começa forte, mas no final... ninguém mais lembra!"},
    {"id": 20, "charada": "Qual a diferença entre o Vasco e a estátua do Cristo Redentor? A estátua nunca cai, mas o Vasco sempre se arrasta para o rebaixamento!"},
    {"id": 21, "charada": "Por que o Palmeiras não tem Mundial? Porque sempre perde na final, até no PlayStation!"},
    {"id": 22, "charada": "Qual é o cheirinho do Flamengo? Cheiro de título, mas só no papel!"},
    {"id": 23, "charada": "O que o São Paulo e o Mundial têm em comum? Eles moram no mesmo lugar: no passado!"},
    {"id": 24, "charada": "Por que o time do Vasco leva o celular para o jogo? Para ver o placar, já que não consegue marcar gols!"},
    {"id": 25, "charada": "Qual é a diferença entre o Corinthians e o Wi-Fi? O Wi-Fi conecta todo mundo, o Corinthians só se conecta com a derrota!"},
    {"id": 26, "charada": "O que é, o que é: veste vermelho, tem uma grande torcida, mas não é capaz de ganhar uma Libertadores? O Flamengo!"},
    {"id": 27, "charada": "Por que o Atlético-MG não consegue guardar segredo? Porque todo ano ele promete ser campeão, mas nunca entrega!"},
    {"id": 28, "charada": "Qual é o time que leva o VAR no bolso? O Palmeiras, porque só ganha com ajuda!"},
    {"id": 29, "charada": "Como o Grêmio tenta sair da crise? Mandando para a Europa, já que aqui não consegue nada!"},
    {"id": 30, "charada": "O que é, o que é: tem uma torcida enorme, mas nunca consegue ganhar títulos internacionais? O Botafogo!"}
]

@app.route('/')
def index():
    # Escolhe uma charada aleatória
    charada_aleatoria = random.choice(charadas_futebol)
    return render_template('index.html', charada=charada_aleatoria)

@app.route('/nova_charada')
def nova_charada():
    # Escolhe uma nova charada aleatória
    charada_aleatoria = random.choice(charadas_futebol)
    return render_template('index.html', charada=charada_aleatoria)

if __name__ == '__main__':
    # Define a porta como 5003
    app.run(debug=True, port=5003)
