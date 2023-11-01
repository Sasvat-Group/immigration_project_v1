from flask_restful import Resource
from controller.token_required import token_required
from services.Services import Services


class RPAQuickFormAutomation(Resource):

    @token_required
    def get(currentUser, self):
        return Services().runRPAQuickFormAutomation()
