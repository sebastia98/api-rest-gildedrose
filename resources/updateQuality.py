from flask_restful import Resource, Api
from config import tienda
from services.service import Service
from domain.types import GildedRose

class UpdateQuality(Resource):
    def get(self):
        tienda.update_quality()
        return Service.getInventario(tienda)
