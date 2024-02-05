from flask import Flask, render_template
import random

app = Flask(__name__)

def gerar_introducao():
    introducoes = ["Era uma vez", "Há muito tempo atrás", "Num reino distante"]
    return random.choice(introducoes)

def gerar_desenvolvimento():
    desenvolvimentos = ["um valente cavaleiro", "uma destemida guerreira", "um bravo guerreiro",
                        "uma poderosa feiticeira", "um sábio mago"]
    return random.choice(desenvolvimentos)

def gerar_final():
    finais = ["enfrentando dragões ferozes.", "derrotando um terrível vilão.",
              "descobrindo um tesouro escondido.", "salvando o reino da escuridão.",
              "encontrando um amor verdadeiro."]
    return random.choice(finais)

def gerar_historia():
    introducao = gerar_introducao()
    desenvolvimento = gerar_desenvolvimento()
    final = gerar_final()

    historia = f"{introducao} {desenvolvimento} {final}"

    return historia

@app.route('/')
def index():
    historia = gerar_historia()
    return render_template('index.html', historia=historia)

if __name__ == "__main__":
    app.run(debug=True)
