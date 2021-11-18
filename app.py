from flask import Flask, render_template, request
from functions import functions as fc

app = Flask(__name__)

@app.route("/")
def inicial():
    #Retornar a pagina inicial com as posicoes predefinidas em 1 e 1.
    posicao = [1, 1]
    return render_template("index.html", posicoes=posicao)

@app.route("/ligar_pontos", methods=['POST'])
def ligar_pontos():
    #Pegar as coordenadas X, Y do ponto de partida e de chegada:
    coordenadas = []
    coordenadas.append(request.form["X_1"])
    coordenadas.append(request.form["Y_1"])
    coordenadas.append(request.form["X_2"])
    coordenadas.append(request.form["Y_2"])
    metodo = request.form["metodo"]

    #Garantir que todos os valores sejam INT, se nao atribuir 1 por padrao:
    for i in range(len(coordenadas)):
        try:
            coordenadas[i] = int(coordenadas[i])
        except:
            coordenadas[i] = 1

    #Obter os pontos dentro do quadrado e gerar caminho entre eles.
    posicao = fc.ligar_os_pontos(coordenadas)
    caminho = fc.buscar_caminho(posicao, metodo)

    #Retornar a pagina inicial com os pontos do caminho, ou retorna uma lista com 0 (vai mostrar nada).
    if caminho == False:
        caminho = [0]
        return render_template("index.html", posicoes=caminho)
    else:
        return render_template("index.html", posicoes=caminho)

if __name__ == '__main__':
    app.run(debug=True)