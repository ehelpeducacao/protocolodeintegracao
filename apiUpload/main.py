from email.utils import localtime
import os
import zipfile 
from flask import Flask, request, jsonify, send_from_directory, send_file,render_template
from model.arquivo import ArquivoModel
import time
from zipfile import ZipFile
from io import BytesIO
import subprocess
import webbrowser
import sys, os

DIRETORIO = os.path.dirname(os.path.realpath(__file__)) + "\output\\"

api = Flask(__name__)

@api.route("/", methods=["GET"])
def lista_arquivos():
    arquivos = []
    for nome_do_arquivo in os.listdir(DIRETORIO):
        endereco_do_arquivo = os.path.join(DIRETORIO,nome_do_arquivo)
        if(os.path.isfile(endereco_do_arquivo)):
            extList = nome_do_arquivo.split(".")
            s= ArquivoModel(nome_do_arquivo,extList[(len(extList)-1)],os.path.getsize(endereco_do_arquivo), time.ctime(os.path.getctime(endereco_do_arquivo)))
            arquivos.append(s.json())

    return jsonify(arquivos)   


@api.route("/a/<nome_do_arquivo>", methods=["GET"])
def get_arquivo(nome_do_arquivo):
    return send_from_directory(DIRETORIO, nome_do_arquivo, as_attachment = True)


@api.route("/all")
def get_tudo():
    zf = zipfile.ZipFile('tudo.zip', mode='w')
    for nome_do_arquivo in os.listdir(DIRETORIO):
        
        endereco_do_arquivo = os.path.join(DIRETORIO,nome_do_arquivo)
        print(endereco_do_arquivo)
        zf.write(endereco_do_arquivo)
    zf.close()
    return '', 201


@api.route("/delete/<nome_do_arquivo>", methods=["DELETE"])
def delete_arquivo(nome_do_arquivo):
    arquivo = os.path.dirname(os.path.realpath(__file__)) + "\output\\" + nome_do_arquivo
    os.remove(arquivo)
    return '', 201


    

@api.route("/", methods=["POST"])
def post_arquivo():
    arquivo = request.files.get("meuArquivo")
    nomeArquivo= arquivo.filename
    arquivo.save(os.path.join(DIRETORIO, nomeArquivo))
    return '',201


@api.route("/patch/<nome_do_arquivo>", methods=["PUT"])
def patch_arquivo(nome_do_arquivo):
    
    url = 'file://' + os.path.dirname(os.path.realpath(__file__))  + '/index.html' + '#{}'.format(str(nome_do_arquivo))
    webbrowser.get().open(url)

    arquivoAux = os.path.dirname(os.path.realpath(__file__)) + "\output\\" + nome_do_arquivo
    os.remove(arquivoAux)
    arquivo = request.files.get("novoArquivo")
    arquivo.save(os.path.join(DIRETORIO,arquivoAux))

    return '',201





if __name__ == "__main__":
    api.run(debug=True, port=8000)