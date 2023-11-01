from controller.project import RPAQuickFormAutomation
from main import app
from flask_restful import Api
from controller.hello import Hello
from controller.petitioner import *
from controller.benificiary import *
from controller.signin import SignIn
from controller.dashboard import Dashboard


api = Api(app)

api.add_resource(Hello, "/hello", methods=['GET', 'POST'])
api.add_resource(SignIn, "/signin", methods=['GET'])
api.add_resource(Dashboard, "/dashboard", methods=['GET'])

# Petitioner
api.add_resource(Petitioner, "/petitioner", methods=['GET'])
api.add_resource(PetitionerOverview, "/petitioner/overview/<petitioner_id>", methods=['GET'])
api.add_resource(PetitionerIncorporation, "/petitioner/incorporation/<petitioner_id>", methods=['GET'])
api.add_resource(PetitionerEmployeeRevenue, "/petitioner/employee_revenue/<petitioner_id>", methods=['GET'])
api.add_resource(PetitionerImmigration, "/petitioner/immigration/<petitioner_id>", methods=['GET'])
api.add_resource(PetitionerCompanyAuth, "/petitioner/company_auth/<petitioner_id>", methods=['GET'])
api.add_resource(PetitionerCompanyContact, "/petitioner/contact/<petitioner_id>", methods=['GET'])

# Beneficiary
api.add_resource(Beneficiary, "/beneficiary", methods=['GET'])
api.add_resource(BeneficiaryImmigrationTimeLine, "/beneficiary/immigration_timeline/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryQuickAssessmentForm, "/beneficiary/quick_assessment_form/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryImmigrationStatusKeyDates, "/beneficiary/immigration_status_key_dates/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryProjects, "/beneficiary/projects/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryWorkAuthorizationInfo, "/beneficiary/work_authorization_info/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryPRProcessInfo, "/beneficiary/pr_process_info/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryPriorityInfo, "/beneficiary/priority_info/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryEmploymentInfo, "/beneficiary/employment_info/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryPassportTravel, "/beneficiary/passport_travel/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryPersonalInfo, "/beneficiary/personal_info/<beneficiary_id>", methods=['GET'])
api.add_resource(BeneficiaryDMSWorkspaceLink, "/beneficiary/dms_workspace_link/<beneficiary_id>", methods=['GET'])
api.add_resource(BenSearch, "/beneficiary/search", methods=['GET'])

# RPA
api.add_resource(RPAQuickFormAutomation, "/rpa_quick_form_automation", methods=['GET'])

