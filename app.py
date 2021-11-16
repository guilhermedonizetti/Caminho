from flask import Flask, render_template, request
from functions import functions as fc

app = Flask(__name__)

@app.route("/")
def inicial():
    posicao = [1, 1]
    return render_template("index.html", posicoes=posicao)

@app.route("/ligar_pontos", methods=['POST'])
def ligar_pontos():
    coordenadas = []
    coordenadas.append(request.form["X_1"])
    coordenadas.append(request.form["Y_1"])
    coordenadas.append(request.form["X_2"])
    coordenadas.append(request.form["Y_2"])

    for i in range(len(coordenadas)):
        try:
            coordenadas[i] = int(coordenadas[i])
        except:
            coordenadas[i] = 1

    posicao = fc.ligar_os_pontos(coordenadas)
    print("Posicoes: {}".format(posicao))
    caminho = fc.buscar_caminho(posicao)

    if caminho == False:
        caminho = [0]
        return render_template("index.html", posicoes=caminho)
    else:
        print("Caminho: {}".format(caminho))
        return render_template("index.html", posicoes=caminho)

if __name__ == '__main__':
    app.run(debug=True)