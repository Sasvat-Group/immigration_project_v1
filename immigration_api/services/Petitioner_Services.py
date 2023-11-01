from flask import make_response
from services.schemaServices import Database
from services.schemaServices.dbQuery import DBQueryForPetitioner


class Petitioner_Services:

    def getPetitionerById(self, pid):
        result = Database().executeOne(DBQueryForPetitioner().PET_BY_ID, (pid,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"petitioner": result[1]}, result[2])

    def getPetitionerListForAttorney(self, user_id):
        result = Database().executeAll(DBQueryForPetitioner().PET_BY_ATTORNEY, (user_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"petitioner": result[1]}, result[2])

    def getPetitionerListForParalegal(self, user_id):
        result = Database().executeAll(DBQueryForPetitioner().PET_BY_PARALEGAL, (user_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"petitioner": result[1]}, result[2])

    def getPetitionerListForHR(self, user_id):
        result = Database().executeAll(DBQueryForPetitioner().PET_BY_HR, (user_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"petitioner": result[1]}, result[2])

    def getPetitionerListForGlobalMobility(self, user_id):
        result = Database().executeAll(DBQueryForPetitioner().PET_BY_HR, (user_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"petitioner": result[1]}, result[2])

    def getPetitionerListForBeneficiary(self, user_id):
        result = Database().executeAll(DBQueryForPetitioner().PET_BY_HR, (user_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"petitioner": result[1]}, result[2])

    def getPetitionerOverview(self, pet_id):
        DB = Database()
        if not DB.DB_Conn:
            return make_response({"Error": "Database is not available!"}, 404)
        try:
            filed = DB.queryAll(DBQueryForPetitioner().OVERVIEW_PROJECT_FILED, (pet_id,))
            initiated = DB.queryAll(DBQueryForPetitioner().OVERVIEW_PROJECT_INITIATED, (pet_id,))
            total_beneficiary = DB.queryOne(DBQueryForPetitioner().TOTAL_BEN_BY_PET, (pet_id,))
            total_spend = DB.queryAll(DBQueryForPetitioner().TOTAL_IMMIGRATION_SPEND, (pet_id,))
            DB.DB_Conn.close()
            return make_response({"total_beneficiary": total_beneficiary["TotalBeneficiaryCount"],
                                  "filed": filed, "initiated": initiated, "total_spend": total_spend}, 200)
        except Exception as e:
            DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getPetitionerIncorporation(self, pet_id):
        result = Database().executeOne(DBQueryForPetitioner().INCORPORATION, (pet_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"incorporation": result[1]}, result[2])

    def getPetitionerEmployeeRevenue(self, pet_id):
        result = Database().executeOne(DBQueryForPetitioner().EMPLOYEE_REVENUE, (pet_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"employee_revenue": result[1]}, result[2])

    def getPetitionerImmigration(self, pet_id):
        result = Database().executeOne(DBQueryForPetitioner().IMMIGRATION, (pet_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"immigration": result[1]}, result[2])

    def getPetitionerCompanyAuth(self, pet_id):
        p = (pet_id,) * 2
        result = Database().executeAll(DBQueryForPetitioner().COMPANY_AUTH_SIGN, p)
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"authorized_signatory": result[1]}, result[2])

    def getPetitionerCompanyContact(self, pet_id):
        result = Database().executeOne(DBQueryForPetitioner().COMPANY_CONTACT, (pet_id,))
        if not result[0]:
            return make_response({"Error": result[1]}, result[2])
        return make_response({"contact": result[1]}, result[2])
