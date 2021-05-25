from flask import Flask, request
from flask_restx import Resource, Api
from model.residence_model import ResidenceModel, ResidenceModelLike, ModelLike
from werkzeug.exceptions import BadRequest
from controller.residences_controller import filter_residences, filter_average_price
from repository.repository import *
from cruds.generci_cruds import *

app = Flask(__name__)
api = Api(app)
Base.metadata.create_all(bind=engine)

def refined_response(model, schema):
    return schema(**model.__dict__).dict()


@api.route('/residencias')
class Residence(Resource):
    def get(self):
        parameters = request.args

        if len(parameters) > 2:
            return BadRequest("muitos parametros na URL")

        for parameter in parameters:
            if parameter in ResidenceModel.__dict__.keys():
                query = parameter
                value = parameters.get(query)

        residences = filter_residences(query, value)

        limit = int(parameters.get("limit")) if "limit" in parameters else None
        return residences[0:limit]

    def post(self):
        try:
            values_form = ModelLike(**request.form).dict()
            response = filter_residences('id', values_form['id'])[0]
            print(values_form)
            if response:
                db = SessionLocal()
                result = create_model(db, ResidenceModelLike, values_form)
                if result:
                    return refined_response(result, ModelLike)
                else:
                    return {"Error": "Error inesperado"}
        except Exception as e:
            return {'Error': str(e)}


@api.route('/preco-medio')
class AveragePrice(Resource):
    def get(self):
        neighbourhood_group = request.args.get("neighbourhood_group")
        room_type = request.args.get("room_type")

        average_price = filter_average_price("neighbourhood_group" if neighbourhood_group else "room_type",
                                             neighbourhood_group if neighbourhood_group else room_type)
        return average_price


if __name__ == '__main__':
    app.run(debug=True)
