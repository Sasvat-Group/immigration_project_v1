from flask import make_response
from flask_restful import Resource
from controller.token_required import token_required
from services.Petitioner_Services import Petitioner_Services


class Petitioner(Resource):
    @token_required
    def get(currentUser, self):
        user_type = currentUser["UserType"]
        if user_type == 'Attorney':
            return Petitioner_Services().getPetitionerListForAttorney(currentUser["ID"])
        elif user_type == 'Paralegal':
            return Petitioner_Services().getPetitionerListForParalegal(currentUser["ID"])
        elif user_type == 'HR':
            return Petitioner_Services().getPetitionerListForHR(currentUser["ID"])
        elif user_type == 'GlobalMobility':
            return Petitioner_Services().getPetitionerListForGlobalMobility(currentUser["ID"])
        elif user_type == 'Beneficiary':
            return Petitioner_Services().getPetitionerListForBeneficiary(currentUser["ID"])
        return make_response({"Error": "User data is incorrect!"}, 400)


class PetitionerOverview(Resource):

    @token_required
    def get(currentUser, self, petitioner_id):
        return Petitioner_Services().getPetitionerOverview(petitioner_id)


class PetitionerIncorporation(Resource):

    @token_required
    def get(currentUser, self, petitioner_id):
        return Petitioner_Services().getPetitionerIncorporation(petitioner_id)


class PetitionerEmployeeRevenue(Resource):

    @token_required
    def get(currentUser, self, petitioner_id):
        return Petitioner_Services().getPetitionerEmployeeRevenue(petitioner_id)


class PetitionerImmigration(Resource):

    @token_required
    def get(currentUser, self, petitioner_id):
        return Petitioner_Services().getPetitionerImmigration(petitioner_id)


class PetitionerCompanyAuth(Resource):

    @token_required
    def get(currentUser, self, petitioner_id):
        return Petitioner_Services().getPetitionerCompanyAuth(petitioner_id)


class PetitionerCompanyContact(Resource):

    @token_required
    def get(currentUser, self, petitioner_id):
        return Petitioner_Services().getPetitionerCompanyContact(petitioner_id)
