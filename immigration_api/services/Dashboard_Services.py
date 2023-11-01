from flask import make_response
from services.schemaServices import Database


class Dashboard_Service:

    def __init__(self, user_id, user_type, DBQuery):
        self.user_id = user_id
        self.user_type = user_type
        self.DBQueryForDashboard = DBQuery
        self.DB = Database()
        if not self.DB.DB_Conn:
            return make_response({"Error": "Database is not available!"}, 404)

    def getDashboardData(self):
        project_data = self.getProjects()
        petitioner = self.getPetitioner()
        beneficiary_data = self.getBeneficiary()
        project_graph = self.getProjectGraph()
        open_project_para = self.getOpenProjectPara()
        self.DB.DB_Conn.close()
        if project_data[0] and petitioner[0] and beneficiary_data[0] and project_graph[0]:
            return make_response({"total_projects": project_data[1], "total_petitioner": petitioner[1],
                                  "total_beneficiary": beneficiary_data[1], "project_graph": project_graph[1],
                                  "open_project_para": open_project_para[1]}, 200)
        return make_response({"Error": "Something Went Wrong!"}, 400)

    def getProjects(self):
        try:
            p = (self.user_id,)
            my_projects = self.DB.queryOne(self.DBQueryForDashboard.MY_OPEN_PROJECTS, p)
            firm_projects = self.DB.queryOne(self.DBQueryForDashboard.FIRM_OPEN_PROJECTS)
            return True, {"total_my_projects": my_projects["TotalProjectCount"],
                          "total_firm_projects": firm_projects["TotalProjectCount"]}, 200
        except Exception as e:
            print(1, e)
            return False, "Bad Request", 400

    def getPetitioner(self):
        try:
            p = (self.user_id,)
            my_petitioner = self.DB.queryOne(self.DBQueryForDashboard.MY_PETITIONER, p)
            firm_petitioner = self.DB.queryOne(self.DBQueryForDashboard.FIRM_PETITIONER)
            my_new_petitioner = self.DB.queryOne(self.DBQueryForDashboard.NEW_MY_PETITIONER, p)
            firm_new_petitioner = self.DB.queryOne(self.DBQueryForDashboard.NEW_FIRM_PETITIONER)
            return True, {"total_my_petitioner": my_petitioner["TotalPetitionerCount"],
                          "total_firm_petitioner": firm_petitioner["TotalPetitionerCount"],
                          "total_new_my_petitioner": my_new_petitioner["TotalPetitionerCount"],
                          "total_new_firm_petitioner": firm_new_petitioner["TotalPetitionerCount"]}, 200
        except Exception as e:
            print(2, e)
            return False, "Bad Request", 400

    def getBeneficiary(self):
        try:
            p = (self.user_id,)
            my_beneficiary = self.DB.queryOne(self.DBQueryForDashboard.MY_BENEFICIARY, p)
            firm_beneficiary = self.DB.queryOne(self.DBQueryForDashboard.FIRM_BENEFICIARY)
            my_new_beneficiary = self.DB.queryOne(self.DBQueryForDashboard.NEW_MY_BENEFICIARY, p)
            p = (self.user_id,) if self.user_type in ["Beneficiary"] else None
            firm_new_beneficiary = self.DB.queryOne(self.DBQueryForDashboard.NEW_FIRM_BENEFICIARY, p)
            return True, {"total_my_beneficiary": my_beneficiary["TotalBeneficiaryCount"],
                          "total_firm_beneficiary": firm_beneficiary["TotalBeneficiaryCount"],
                          "total_new_my_beneficiary": my_new_beneficiary["TotalBeneficiaryCount"],
                          "total_new_firm_beneficiary": firm_new_beneficiary["TotalBeneficiaryCount"]}, 200
        except Exception as e:
            print(3, e)
            return False, "Bad Request", 400

    def getOpenProjectPara(self):
        try:
            p = (self.user_id,) * 2
            open_projects_para = self.DB.queryAll(self.DBQueryForDashboard.OPEN_PROJECTS_PARA, p)
            return True, open_projects_para, 200
        except Exception as e:
            print(3, e)
            return False, "Bad Request", 400

    def getProjectGraph(self):
        try:
            p = (self.user_id,) if self.user_type in ["HR", "Beneficiary", "Paralegal"] else None
            filed_this = self.DB.queryAll(self.DBQueryForDashboard.PROJECT_FILED_THIS, p)
            filed_prev = self.DB.queryAll(self.DBQueryForDashboard.PROJECT_FILED_PREV, p)
            init_this = self.DB.queryAll(self.DBQueryForDashboard.PROJECT_INITIATED_THIS, p)
            init_prev = self.DB.queryAll(self.DBQueryForDashboard.PROJECT_INITIATED_PREV, p)
            return True, {"filed": {"this_filed": filed_this, "previous_filed": filed_prev},
                          "initiated": {"this_initiated": init_this, "previous_initiated": init_prev}}, 200
        except Exception as e:
            print(4, e)
            return False, "Bad Request", 400
