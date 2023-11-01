from flask import make_response
from flask_restful import Resource
from controller.token_required import token_required
from services.Dashboard_Services import Dashboard_Service
from services.schemaServices.dbQuery import DBQueryForDashboardAttorney, DBQueryForDashboardHR, DBQueryForDashboardParalegal, DBQueryForDashboardBeneficiary


class Dashboard(Resource):

    @token_required
    def get(currentUser, self):
        user_type = currentUser["UserType"]
        if user_type == "Attorney":
            DBQuery = DBQueryForDashboardAttorney()
        elif user_type == "Paralegal":
            DBQuery = DBQueryForDashboardParalegal()
        elif user_type == "HR":
            DBQuery = DBQueryForDashboardHR()
        elif user_type == "GlobalMobility":
            user_type = "HR"
            DBQuery = DBQueryForDashboardHR()
        elif user_type == "Beneficiary":
            DBQuery = DBQueryForDashboardBeneficiary()
        else:
            return make_response({"Error": "User data is incorrect!"}, 400)
        return Dashboard_Service(currentUser["ID"], user_type, DBQuery).getDashboardData()
