from flask import make_response
from flask_restful import Resource
from controller.token_required import token_required
from services.Petitioner_Services import Petitioner_Services
from services.Beneficiary_Services import Beneficiary_Services
from flask import request


class Beneficiary(Resource):
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


class BeneficiaryImmigrationTimeLine(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryImmigrationTimeLine(beneficiary_id)


class BeneficiaryQuickAssessmentForm(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryQuickAssessmentForm(beneficiary_id)


class BeneficiaryImmigrationStatusKeyDates(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryImmigrationStatusKeyDates(beneficiary_id)


class BeneficiaryProjects(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryProjects(beneficiary_id)


class BeneficiaryWorkAuthorizationInfo(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryWorkAuthorizationInfo(beneficiary_id)


class BeneficiaryPRProcessInfo(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryPRProcessInfo(beneficiary_id)


class BeneficiaryPriorityInfo(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryPriorityInfo(beneficiary_id)


class BeneficiaryEmploymentInfo(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryEmploymentInfo(beneficiary_id)


class BeneficiaryPassportTravel(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryPassportTravel(beneficiary_id)


class BeneficiaryPersonalInfo(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryPersonalInfo(beneficiary_id)


class BeneficiaryDMSWorkspaceLink(Resource):

    @token_required
    def get(currentUser, self, beneficiary_id):
        return Beneficiary_Services().getBeneficiaryDMSWorkspaceLink(beneficiary_id)

class BenSearch(Resource):

    @token_required
    def get(currentUser, self):
        args = request.args
        ben_name = args.get('ben_name')
        dob = args.get('dob')
        project_id = args.get('pet_id')
        pet_name = args.get('pet_name')
        return Beneficiary_Services().getBenificiaryBySearch(ben_name, dob, project_id, pet_name)
