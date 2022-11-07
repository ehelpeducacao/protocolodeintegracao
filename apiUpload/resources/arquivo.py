from flask_restful import Resource, reqparse
from model.arquivo import ArquivoModel

arquivos = [
        
]


class Arquivos(Resource):
    def get(self):
        return {'arquivos': arquivos}

class Arquivo(Resource):
    atributos = reqparse.RequestParser()
    atributos.add_argument('nome')
    atributos.add_argument('tamanho')
    atributos.add_argument('data')

    def find_hotel(arquivo_id):
        for arquivo in arquivos:
            if arquivo['arquivo_id'] == arquivo_id:
                return arquivo
        return False

    def get(self, arquivo_id):
        arquivo = Arquivo.find_arquivo(arquivo_id)
        if arquivo:
            return arquivo
        return {'message': 'file not found.'}, 404

    def post(self, hotel_id):
        dados = Arquivo.atributos.parse_args()
        arquivo_objeto = ArquivoModel(arquivo_id, **dados)
        novo_arquivo = arquivo_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def put(self, hotel_id):
        dados = Hotel.atributos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201

    def delete(self, hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        return {'message': 'Hotel deleted.'}
