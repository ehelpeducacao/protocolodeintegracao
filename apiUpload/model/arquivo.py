class ArquivoModel:
    def __init__(self, nome, tipo,tamanho, data):
        #self.arquivo_id = arquivo_id
        self.nome = nome
        self.tipo = tipo
        self.tamanho = tamanho
        self.data = data
    def json(self):
        return {
            #'arquivo_id': self.arquivo_id,
            'nome': self.nome,
            'tipo': self.tipo,
            'tamanho': self.tamanho,
            'data': self.data
        }
