import os
import time
import glob
import shutil
import os.path as op
import traceback
import pandas as pd
import pyodbc
import requests
import warnings
import subprocess
import threading
import re
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import datetime

# for sahrepoint activities
from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
import os
from office365.runtime.auth.user_credential import UserCredential
from office365.runtime.auth.client_credential import ClientCredential
import RPA_Process.sub_files_US.push_to_qf_I140 as push_to_qf_I140

client_id = "6b0381e5-8dcb-44a9-a2bb-d9b9bc0f0a3d"
client_secret = "Wc+nwPNkSfJHPx+8UT4u2DUn8PncSECrxK2zGgF1rXQ="

# print('hi')
MODE_OF_RUN = 'local'  # local/server

warnings.filterwarnings(action='ignore')

parent_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(parent_dir)

conn = pyodbc.connect(
    '{connection string}')
username = "ImmilyticsLLC_AdminUser"
password = "wcqs9HscgI8StxrWBBeMTq"

api_url = "https://websvcs.quikforms.com/rest_authentication/token"
headersAuth = {
    'Content-Type': 'application/x-www-form-urlencoded',
}
data = {"grant_type": "password", "username": username, "password": password}
response = requests.post(api_url, headers=headersAuth, data=data, verify=True)
response_auth = response.json()

# print(response_auth)
headersAPI = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer '+response_auth['access_token'],
}

source_dir = os.path.join(parent_dir, 'immiLytics/Certified PERMs')
processed_dir = os.path.join(parent_dir, 'processed')

US_keyword = re.compile(
    'united states|united states of america|america|U\.S\.A|U\.S|U\.S\.AMERICA|usa|us', flags=re.IGNORECASE)


def get_gender(value):
    if value:
        value = value.lower().strip()
        if value == 'male':
            return '1'
        if value == 'female':
            return '2'
        else:
            return ''

    else:
        return ''


def clean_price(val):
    val = (re.sub("[^0-9]", "", str(val)))
    try:
        return int(val)
    except:
        return None


def clean_num(val):
    if val:
        return (re.sub("[^0-9]", "", str(val)))
    else:
        return ''


def bit_ans(value):
    try:
        value = value.strip().lower()
    except:
        pass

    if value in ('yes', '1', 'true', True, 1):
        return 'Yes'
    elif value in ('no', '0', 'false', 0, False):
        return 'No'
    else:
        return ''


def iff(value):
    if value:
        return value
    else:
        return ''


def AptSteFlr(value):
    if value:
        value = str(value).strip().lower()[0]
        if value == 'a':
            return 1
        if value == 's':
            return 2
        if value == 'f':
            return 3
    else:
        return ''


def change_date(dat):
    if dat not in ('', None, 'nan', 'Nan'):
        dat = dat.strftime('%m/%d/%Y')
        if not dat.__contains__('1900'):
            return dat
        else:
            return ''
    else:
        return ''


def calculate_age(birth_date):

    if isinstance(birth_date, str):

        birth_date = datetime.strptime(birth_date, '%Y/%m/%d')

    today = date.today()
    age = relativedelta(today, birth_date)
    return (int(age.years))


def return_high_salary(sal1, sal2):
    if sal1 and sal2:
        sal1 = float(str(sal1).replace(',', ''))
        sal2 = float(str(sal2).replace(',', ''))
        return sal1 if sal1 >= sal2 else sal2
    else:
        return sal1 if sal1 else ''


def qpdf_merger(pdfs, folder_path3, formtype):

    command_string = r'"qpdf_11.2.0\bin\qpdf.exe" --empty --pages '

    for pdf_name in pdfs:
        command_string = rf'{command_string}"{pdf_name}" '
    command_string = command_string + rf' -- "{folder_path3}\Final_{formtype}.pdf"'

    command_string.replace('\n', '')
    
    # for pdf_name in pdfs:
    #     command_string = command_string+'"' + str(pdf_name)+'"' + ' '
    # command_string = command_string + \
    #     rf' -- "{folder_path3}\Final_{formtype}.pdf"'

    # command_string.replace('\n', '')

    subprocess.Popen(command_string)

class CustomThread(threading.Thread):
    def __init__(self, ProjectID):
        threading.Thread.__init__(self)
        self.ProjectID = ProjectID
        self.results2 = self.mailing_address = self.current_res_address = self.last_perm_address_abroad = self.perm_foreign_address = self.mail_addr_vs_phys_addr = self.mail_addr_vs_phys_addr = None

    def run(self):
        cursor1 = conn.cursor()
        self.results2 = cursor1.execute(
            '''Select * from ProjectETA9089 et
        right join dbo.[Project] as pro on et.PERMDOLProjectNumber = pro.ReceiptNumber
        where pro.ProjectID='{}' '''.format(self.ProjectID)).fetchone()

        self.mailing_address = cursor1.execute(f'''select * from BeneficiaryAddress a
                left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
                left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID
                where a.IsMailingAddress = 1 and pro.ProjectID = '{self.ProjectID}' ''').fetchone()
        self.mail_addr_vs_phys_addr = True if self.mailing_address.IsMailingAddress == self.mailing_address.IsCurrentResidenceAddress else False

        self.current_res_address = cursor1.execute(f'''select a.* from BeneficiaryAddress a
                left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
                left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID
                where a.IsCurrentResidenceAddress = 1 and pro.ProjectID = '{self.ProjectID}' ''').fetchone()

        self.last_perm_address_abroad = cursor1.execute(f'''select a.* from BeneficiaryAddress a
                left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
                left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID
                where a.IsLastPermanentResidenceAddressAbroad = 1 and pro.ProjectID = '{self.ProjectID}' ''').fetchone()

        self.perm_foreign_address = cursor1.execute(f'''select * from BeneficiaryAddress a
                left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
                left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID
                where a.IsPermanentForeignAddress = 1 and pro.ProjectID = '{self.ProjectID}' ''').fetchone()
        cursor1.close()


# sharepoint related functions

def download_files(ctx,sp_file_path,dwd_to):
    
    # print(f"Downloading file from {sp_file_path} to {dwd_to}\n" )

    with open(dwd_to, "wb") as local_file:
        file = ctx.web.get_file_by_server_relative_url(sp_file_path)
        file.download(local_file)
        ctx.execute_query()


def get_files(site_url,sp_folder,dwd_dir):
    try:
        print(f"Downloading supporting files from sharepoint..")
        ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))

        list_source = ctx.web.get_folder_by_server_relative_url(sp_folder)
        files = list_source.files
        ctx.load(files)
        ctx.execute_query()
        for file in files:
            sp_file_path = file.properties["ServerRelativeUrl"]
            sp_file_name = file.properties["Name"]
            download_files(ctx,sp_file_path = sp_file_path,dwd_to = op.join(dwd_dir,sp_file_name))
        
    except Exception as e:
        print(e)


def upload_to_sharepoint(site_url, local_file_path, sp_folder: str):
    ctx = ClientContext(site_url).with_credentials(
        ClientCredential(client_id, client_secret))
    print(f"Uploading files to sharepoint.." )
    # print(f"Uploading file from {local_file_path} to {sp_folder}\n")
    target_folder = ctx.web.get_folder_by_server_relative_url(sp_folder)
    local_file_name = os.path.basename(local_file_path)

    with open(local_file_path, 'rb') as content_file:
        file_content = content_file.read()
        target_folder.upload_file(
            local_file_name, file_content).execute_query()


def start():
    cursor = conn.cursor()
    project_list = cursor.execute('''select pro.ProjectID,pro.ProjectXref,pro.ProjectPetitionID,pt.FormsToBeGenerated
        from dbo.[Project] as pro 
        left join config.PetitionTemplate as pt on pro.ProjectPetitionID = pt.PetitionTemplateID
        where pro.RPADraftingRequestYesNo = 'True' ''').fetchall()
    
    for project in project_list:
        forms = project.FormsToBeGenerated.split(';')
        ProjectID = project.ProjectID
        ProjectXref = project.ProjectXref
        # thread1 = CustomThread(ProjectID)
        # thread1.start()
        # thread1.join()

        if True:

            result = cursor.execute(f""" select ct.*,
            b.BeneficiaryType,
            b.Lastname as b_lastname,
            b.FirstName as b_firstname,
            b.MiddleName as b_middlename,
            b.OtherFirstName1,
            b.OtherMiddleName1,
            b.OtherLastName1,
            b.BeneficiaryID,
            b.BeneficiaryXref,
            b.PrimaryBeneficiaryID,
            b.BirthDate,
            b.BirthCity,
            b.BirthCountry,
            b.BirthStateProvince,
            b.CitizenshipCountry,
            b.AlienNumber1,
            b.SSNNumber,
            b.USCISNumber as b_USCISNumber,
            b.IsInRemovalProceeding,
            b.RemovalProceedingStartDate,
            b.RemovalProceedingJurisdiction,
            b.RemovalProceedingStatus,
            b.Salutation as ben_Salutation,
            b.gender as ben_gender,
            b.FinalNivDate,
            b.Mobile as b_Mobile,
            b.WorkEmail as ben_WorkEmail,
            b.WorkPhone as ben_WorkPhone,
            b.AllCitizenshipCountries,
            b.HasAnyImmigrantVisaPetitionBeenFiledOnYourBehalf,
            b.HasPreviouslyHeldJVisaStatus,
            b.IsImmigrantVisaApplicant,
            b.ImmigrantVisaApplicationDecision,
            b.ImmigrantVisaApplicationDecisionDate,
            b.AosProjectFiledDate,
            b.AsylumPersecutionCountry,
            b.AsylumReportedDHSLocation,
            b.AsylumReportedDateToDHS,
            b.AsylumReportedToDHS,
            b.SevisNumber1,
            b.CurrentOtherEADExpirationDate,
            b.EADApExpirationDate,
            b.MaritalStatus as ben_mari_stat,
            b.IsSpouseCurrentMemberOfUSArmedForcesOrCoastGuard,
            b.JVisaStatusValidFromDate,
            b.JVisaStatusExpirationDate,
            b.JVisaHomeStayRequirementComplied,
            b.JVisaHomeStayRequirementWaiverReceived,
            b.NonimmigrantVisaNumber,
            
            b.Ethnicity,
            b.Race,
            b.EyeColor,
            b.HeightFeet,
            b.HeightInches,
            b.HairColor,
            b.WeightLbs,
            b.InitialHlEntryDate,

            edt.EADType,

            p.PetitionerXref,
            p.PetitionerID,
            p.PetitionerName,
            p.FederalEmployerId,
            p.BusinessType as p_BusinessType,
            p.YearEstablished as p_YearEstablished,
            p.EmployeeCountUS as p_EmployeeCountUS,
            p.AnnualIncomeGrossUS as p_AnnualIncomeGrossUS,
            p.AnnualIncomeNetUS as p_AnnualIncomeNetUS,
            p.NaicsCode as p_NaicsCode,
            p.BusinessInfo as p_BusinessInfo,
            p.EmployerEVerifyName as p_EmployerEVerifyName,
            p.EmployerEVerifyNumber as p_EmployerEVerifyNumber,
            p.HigherEducationInstitution as p_HigherEducationInstitution,
            p.PrimarySecondaryEducationInstitution as p_PrimarySecondaryEducationInstitution,
            p.NonprofitCurriculumRelatedTraining as p_NonprofitCurriculumRelatedTraining,
            p.NonprofitGovernmentResearch as p_NonprofitGovernmentResearch,
            p.NonprofitOrganizationEntity as p_NonprofitOrganizationEntity,
            p.Over50PercentEEsinH1BL1AL1BStatus as p_Over50PercentEEsinH1BL1AL1BStatus,
            p.PetGUAMCNMICapExempt as p_PetGUAMCNMICapExempt,
            p.H1BDependentEmployer as p_H1BDependentEmployer,
            p.PetitionerWillfulViolator as p_PetitionerWillfulViolator,

            o.OrganizationID,
            o.OrganizationXref,
            o.OrganizationName,

            l.BarNumber as l_BarNumber,
            l.FirstName as l_firstname,
            l.LastName as l_lastname,
            l.MiddleName as l_middlename,
            l.FirmName as l_firmname,
            l.Address1 as l_address1,
            l.AddressUnitType as l_addressunittype,
            l.AddressUnitNumber as l_addressunitnumber,
            l.City as l_city,
            l.StateProvince as l_state,
            l.PostalZipCode as l_zipcode,
            l.Country as l_country,
            l.PostalZipCode as l_zipcode,
            l.PhoneNumber as l_phonenumber,
            l.PhoneNumberExt as l_PhoneNumberExt,
            l.MobileNumber as l_mobilenumber,
            l.Email as l_email,
            l.Faxnumber as l_Faxnumber,
            l.USCISNumber as l_USCISNumber,
            l.LicensingAuthority as l_LicensingAuthority,
            l.LegalResourceTitle as l_JobTitle,
            
            lca.LCAIntendedEmploymentEndDate,
            LCAIntendedEmploymentStartDate,
            lca.LCAIntendedEmploymentStartDate,
            lca.LCAJobTitle,
            lca.LCAProjectNumber,
            lca.LCAWorkLocation1_Address1,
            lca.LCAWorkLocation1_Address2,
            lca.LCAWorkLocation1_City,
            lca.LCAWorkLocation1_PrevailingWageRate,
            lca.LCAWorkLocation1_PrevailingWageRateType,
            lca.LCAWorkLocation1_State,
            lca.LCAWorkLocation1_ZipCode,

            pro.ProjectPriorityCategory,
            pro.ReceiptNumber,
            pro.ProjectXref,
            pro.ProjectID,
            pro.ServiceType,
            pro.ProjectFiledDate,
            pro.COSNewStatusEffectiveDate,
            pro.IsCOSRequested,
            pro.COSNewStatusRequested,

            pta1.ProjectTagValue as PTag1_Val,
            pta2.ProjectTagValue as PTag2_Val,
            pta3.ProjectTagValue as PTag3_Val,
            pta4.ProjectTagValue as PTag4_Val,

            ptt.ProjectPetitionName,

            vi.ValidTo as vi_ValidTo,

            pp.ValidFrom as pp_ValidFrom,
            pp.ValidTo as pp_ValidTo,
            pp.PassportNumber,
            pp.IssuingCountry as pp_IssuingCountry,

            (select IsRequired from ProjectJobRequirement where ProjectID = {ProjectID} and RequirementDescription like '%EarItar%') as IsEarItarRequired,

            DATEDIFF(DAY,GETDATE(),CAST(pp.ValidTo as varchar)) as passport_validity,

            '' as EADAPType,
            '' as EadNumber,
            
            '' as USEmbassyConsulateCity,
            '' as USEmbassyConsulateCountry,
            '' as UnderlyingImmigrantClassification,


            'yes' as AcquiredNewNationality,
            '' as AppliedOrReceivedBenefitsFromRefugeeOrAsyleeCountry,
            '' as AppliedOrRenewedPassportOrEntryPermitToRefugeeOrAsyleeCountry,
            '' as  BeenGrantedAsyleeOrRefugeeStatus,
            '' as  FiledFederalIncomeTaxReturn,
            '' as  IntendedDepartureDate,
            '' as  IntendedReturnDate,
            '' as  PlanningToTravelToRefugeeOrAsyleeCountry,
            '' as  PurposeOfTravel,
            '' as  ReEntryPermitIssueDate,
            '' as  RefugeeOrAsyleeCountry,
            '' as  RefugeeTravelDocumentIssueDate,
            '' as  ReturnedToRefugeeOrAsyleeCountry,
            '' as  TotalTimeAbroadSincePermanentUSResidence,
            '' as  VisitingCountries

            FROM dbo.[Project] as pro 

            LEFT JOIN config.ProjectTag as pta1 ON pta1.ProjectTagID = pro.ProjectTag1ID 
            LEFT JOIN config.ProjectTag as pta2 ON pta2.ProjectTagID = pro.ProjectTag2ID 
            LEFT JOIN config.ProjectTag as pta3 ON pta3.ProjectTagID = pro.ProjectTag3ID 
            LEFT JOIN config.ProjectTag as pta4 ON pta4.ProjectTagID = pro.ProjectTag4ID 

            LEFT JOIN config.PetitionTemplate ptt ON ptt.PetitionTemplateID = pro.ProjectPetitionID 

            LEFT JOIN dbo.Beneficiary b ON pro.BeneficiaryID = b.BeneficiaryID 
            LEFT JOIN dbo.Petitioner p ON p.PetitionerID=b.PetitionerID 
            LEFT JOIN dbo.Organization o ON o.OrganizationID =p.OrganizationID 
            LEFT JOIN dbo.Contact ct ON ct.ContactID=p.AuthorizedSignatory1ContactID 
            LEFT JOIN dbo.LegalResource l ON l.LegalResourceID=pro.LegalResourceAttorneyID1
            LEFT JOIN dbo.Beneficiary b2 ON b.PrimaryBeneficiaryID = b2.BeneficiaryID
            LEFT JOIN dbo.ProjectLCA lca ON lca.LCAProjectNumber = pro.LCANumber
            LEFT JOIN dbo.BeneficiaryVisa vi ON vi.BeneficiaryID = b.BeneficiaryID
            LEFT JOIN dbo.BeneficiaryPassport pp ON pp.BeneficiaryID = b.BeneficiaryID
            LEFT JOIN dbo.ProjectJobRequirement jr ON jr.ProjectID = pro.ProjectID
            LEFT JOIN config.EADType edt ON edt.EADTypeID = b.EADTypeID


            WHERE pro.ProjectID= '{ProjectID}' and 
            vi.IsCurrent = '{True}' and 
            pp.IsCurrent = '{True}'

            """).fetchone()

            results2 = cursor.execute(
                '''Select * from ProjectETA9089 et
            right join dbo.[Project] as pro on et.PERMDOLProjectNumber = pro.ReceiptNumber
            where pro.ProjectID='{}' '''.format(ProjectID)).fetchone()

            mailing_address = cursor.execute(f'''select * from BeneficiaryAddress a
            left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
            left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID

            where a.IsMailingAddress = 1 and pro.ProjectID = '{ProjectID}' ''').fetchone()

            current_res_address = cursor.execute(f'''select a.* from BeneficiaryAddress a
            left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
            left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID

            where a.IsCurrentResidenceAddress = 1 and pro.ProjectID = '{ProjectID}' ''').fetchone()

            last_perm_address_abroad = cursor.execute(f'''select a.* from BeneficiaryAddress a
            left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
            left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID

            where a.IsLastPermanentResidenceAddressAbroad = 1 and pro.ProjectID = '{ProjectID}' ''').fetchone()

            perm_foreign_address = cursor.execute(f'''select * from BeneficiaryAddress a
            left join Beneficiary b on b.BeneficiaryID = a.BeneficiaryID
            left join [Project] pro on pro.BeneficiaryID= b.BeneficiaryID

            where a.IsPermanentForeignAddress = 1 and pro.ProjectID = '{ProjectID}' ''').fetchone()

            # from here you query from the query result
            marriage_history = cursor.execute(f'''select * from BeneficiaryMaritalInfo m 
            where m.BeneficiaryID = '{result.BeneficiaryID}'
            order by MarriageDate desc ''').fetchall()

            # ben's primary ben's,  ben level data
            prim_ben = cursor.execute(f'''select nd.ReceiptNumber,b.*
            from Beneficiary b
                                      
            left join dbo.NoticeDetail nd on nd.BeneficiaryID  = b.BeneficiaryID                                
            where b.BeneficiaryID = '{result.PrimaryBeneficiaryID}' ''').fetchone()

            ben_high_edu = cursor.execute(
                f'''select * from BeneficiaryEducation where BeneficiaryID = '{result.BeneficiaryID}' and IsHighestDegree = '1' and IsUSDegree = '1' ''').fetchone()

            ben_all_edu = cursor.execute(
                f'''select * from BeneficiaryEducation where BeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

            ben_family = cursor.execute(
                f'''select * from BeneficiaryFamily where PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

            # doubt
            most_recent_entry_rec = cursor.execute('''select datediff(DAY,bt.TentativeArrivalDate,bt.TentativeDepartureDate) as 'trip_length', bt.*,ci.* from BeneficiaryTravel bt
            left join config.I94Status ci on ci.I94StatusID  = bt.ImmigrationStatusOnI94ID
            
            where BeneficiaryID = ? and 
            EntryMostRecent = ?

            ''', (result.BeneficiaryID, True)).fetchone()

            Ques_Responses = cursor.execute('''select r.ResponseFull,r.QuestionID from Response r
            left join Question q on q.QuestionID  = r.QuestionID
            
            where BeneficiaryID = ?
            order by r.QuestionID

            ''', (result.BeneficiaryID)).fetchall()

            resp_dic = {}

            for resp in Ques_Responses:
                try:
                    resp_dic[f'{int(resp.QuestionID)}'] = int(
                        resp.ResponseFull)
                except:
                    resp_dic[f'{int(resp.QuestionID)}'] = resp.ResponseFull

            most_recent_notice = cursor.execute('''select * from NoticeDetail nd
            left join config.NoticeType nt on nt.NoticeTypeID  = nd.NoticeDetailID
            
            where ProjectID = ?

            ''', (result.ProjectID)).fetchone()

            # last_five_years_residence_address
            l5_res = cursor.execute(
                f'''
            select *,
            DATEDIFF(DAY,cast(AddressToDate as varchar),GETDATE()) as days_from_now
            
            from dbo.BeneficiaryAddress
            where AddressType = 'residence' and
            IsCurrentResidenceAddress = 'False' and
            AddressFromDate is not null and 

            DATEDIFF(YEAR,cast(AddressFromDate as varchar),GETDATE()) <= 5 and
            
            BeneficiaryID = '{result.BeneficiaryID}'

            order by days_from_now asc''').fetchall()

            # last_five_years_employment_history
            l5_emp = cursor.execute(
                f'''
            select *,
            DATEDIFF(DAY,cast(TerminationDate as varchar),GETDATE()) as days_from_now
            
            from [dbo].[BeneficiaryEmployment]
            where
            
            HireDate is not null and 

            DATEDIFF(YEAR,cast(HireDate as varchar),GETDATE()) <= 5 and
            
            BeneficiaryID = '{result.BeneficiaryID}'

            order by days_from_now asc''').fetchall()

            parents = cursor.execute(
                f'''
            select *
            
            from [dbo].[BeneficiaryFamily]
            where (lower(Relation) like '%father%' or
                    lower(Relation) like '%mother%') and
            
            PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

            spouse = cursor.execute(
                f'''
            select *
            from [dbo].[Beneficiary]
            where (lower(RelationType) like '%spouse%' or
                    lower(RelationType) like '%wife%' or
                    lower(RelationType) like '%husband%' or
                    lower(RelationType) like '%partner%') and
            
            PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

            org_membership = cursor.execute(f'''select * from BeneficiaryOrganizationMembership ms  
            where ms.BeneficiaryID = '{result.BeneficiaryID}'
            order by MembershipStartDate desc ''').fetchall()

            ben_cur_emp = cursor.execute(
                f'''select * from BeneficiaryEmployment where BeneficiaryID = '{result.   BeneficiaryID}' and IsCurrent = '1' ''').fetchone()

            mail_addr_vs_phys_addr = True if mailing_address.IsMailingAddress == mailing_address.IsCurrentResidenceAddress else False

            os.chdir(parent_dir)
            cursor.close()
            if result.OrganizationXref:
                target_dir = op.join(parent_dir,
                                'ImmiLytics',
                                f"{result.OrganizationXref} - {result.OrganizationName}",
                                f"{result.PetitionerXref} - {result.PetitionerName}",
                                f"{result.BeneficiaryXref} - {result.b_lastname}, {result.b_firstname}",
                                f"{result.ProjectXref}")

            else:
                target_dir = op.join(parent_dir,
                                'ImmiLytics',
                                f"{result.PetitionerXref} - {result.PetitionerName}",
                                f"{result.BeneficiaryXref} - {result.b_lastname}, {result.b_firstname}",
                                f"{result.ProjectXref}")
            
            other_objects = {
                'mailing_address': mailing_address,
                'current_res_address': current_res_address,
                'last_perm_address_abroad': last_perm_address_abroad,
                'perm_foreign_address': perm_foreign_address,
                'mail_addr_vs_phys_addr': mail_addr_vs_phys_addr,
                'marriage_history': marriage_history,
                'ben_family': ben_family,
                'most_recent_entry_rec': most_recent_entry_rec,
                'most_recent_notice': most_recent_notice,
                'l5_res': l5_res,
                'l5_emp': l5_emp,
                'parents': parents,
                'spouse': spouse,
                'org_membership': org_membership,
                'ben_cur_emp': ben_cur_emp,
                'prim_ben': prim_ben,
                'ben_high_edu': ben_high_edu,
                'ben_all_edu': ben_all_edu,
                'result': result,
                'results2': results2,
                'headersAPI': headersAPI,
                'US_keyword': US_keyword,
                'conn': conn,
                'cursor': cursor,
                'parent_dir': parent_dir,
                'target_dir': target_dir,
                'resp_dic': resp_dic,

                # passing all functions
                'get_gender': get_gender,
                'bit_ans': bit_ans,
                'iff': iff,
                'AptSteFlr': AptSteFlr,
                'change_date': change_date,
                'calculate_age': calculate_age,
                'qpdf_merger': qpdf_merger,
                'return_high_salary': return_high_salary,
                'clean_price': clean_price,
                'clean_num': clean_num,
                'get_files': get_files,
                'download_files': download_files,
                'upload_to_sharepoint': upload_to_sharepoint,

            }
        for form_type in forms:

            # if form_type.lower().strip() == '485':
            #     print(f'\nProcessing Form I-485 for - {project.ProjectXref}')
            #     import sub_files_US.push_to_qf_I485 as push_to_qf_I485
            #     push_to_qf_I485.generate_485(
            #         project.ProjectID, form_type, other_objects)

            # if form_type.lower().strip() == '765':
            #     print(f'\nProcessing Form I-765 for - {project.ProjectXref}')
            #     import sub_files_US.push_to_qf_I765 as push_to_qf_I765
            #     push_to_qf_I765.generate_765(project.ProjectID,form_type,other_objects)

            # if form_type.lower().strip() == '539':
            #     print(f'\nProcessing Form I-539 for - {project.ProjectXref}')
            #     import sub_files_US.push_to_qf_I539 as push_to_qf_I539
            #     push_to_qf_I539.generate_539(project.ProjectID,form_type,other_objects)
            if form_type.lower().strip() == '140':
                print(f'\nProcessing Form I-140 for - {project.ProjectXref}')
                push_to_qf_I140.generate_140(
                    project.ProjectID, form_type, other_objects)            
            # if form_type.lower().strip() == '140':
            #     print(f'\nProcessing Form I-140 for - {project.ProjectXref}')
                
            #     i140_thread = threading.Thread(target=push_to_qf_I140.generate_140,
            #                                    args=(project.ProjectID, form_type, other_objects))
            #     i140_thread.start()

            # if form_type.lower().strip() == '131':
            #     print(f'\nProcessing Form I-131 for - {project.ProjectXref}')
            #     import sub_files_US.push_to_qf_I131 as push_to_qf_I131
            #     push_to_qf_I131.generate_131(
            #         project.ProjectID, form_type, other_objects)

            # if form_type.lower().strip() == '129':
            #     print(f'\nProcessing Form I-129 for - {project.ProjectXref}')
            #     import sub_files_US.push_to_qf_I129 as push_to_qf_I129
            #     push_to_qf_I129.generate_129(
            #         project.ProjectID, form_type, other_objects)

            # if form_type.lower().strip() == '485j':
            #     print(f'\nProcessing Form I-485J for - {project.ProjectXref}')
            #     import sub_files_US.push_to_qf_I485J as push_to_qf_I485J
            #     push_to_qf_I485J.generate_485J(
            #         project.ProjectID, form_type, other_objects)

        #     # if form_type.lower().strip() == '907':
        #     #     print(f'\nProcessing Form I-907 for - {project.ProjectXref}')
        #     #     import sub_files_US.push_to_qf_I907 as push_to_qf_I907
        #     #     push_to_qf_I907.generate_907(
        #     #         project.ProjectID, form_type, other_objects)

        
        # for form_type in forms:
        #     # if form_type.lower().strip() == 'i-765':
        #     #     i765_thread.join()
        #     #     print('Process Completed Form I-765')
        #     # elif form_type.lower().strip() == 'i-539':
        #     #     i539_thread.join()
        #     #     print('Process Completed Form I-539')
            # if form_type.lower().strip() == 'i-140':
            #     i140_thread.join()
            #     print('Process Completed Form I-140')
        #     # elif form_type.lower().strip() == 'i-131':
            #     i131_thread.join()
            #     print('Process Completed Form I-131')
            # elif form_type.lower().strip() == 'i-485':
            #     i485_thread.join()
            #     print('Process Completed Form I-485')
        return get_final_files(target_dir, ProjectID, ProjectXref, other_objects["result"])
    
def get_final_files(target_dir, ProjectID, ProjectXref, result):

        
    if os.path.exists(target_dir):
        cursor = conn.cursor()
        indiv_finals_dir = op.join(target_dir, "indiv_finals_dir")

        indiv_finals_pdfs = []

        pet_temp_data = cursor.execute('''select * from Config.PetitionTemplate pt 
        right join dbo.Project p on
        pt.PetitionTemplateID  =  p.ProjectPetitionID

        where p.ProjectID = ? ''', (ProjectID)).fetchone()
        cursor.close()
        sequence = pet_temp_data.FormsToBeGenerated.split(";")
        packet_name = pet_temp_data.ProjectPetitionTemplateDescription

        ind_final_files = os.listdir(indiv_finals_dir)

        for seq in sequence:
            for ind_fil in ind_final_files:
                if str(ind_fil).__contains__(seq):
                    indiv_finals_pdfs.append(op.join(indiv_finals_dir, ind_fil))
                

        qpdf_merger(indiv_finals_pdfs, indiv_finals_dir, packet_name)
        print("\nCreating final packet..")
        time.sleep(30)

        site_url_temp = f"https://immilytics.sharepoint.com/sites/{result.BeneficiaryXref}-{result.b_lastname}{result.b_firstname}"
        file_list = []
        for file in glob.glob(f"{indiv_finals_dir}\*{packet_name}*"):
            file_list.append(os.path.basename(file))
            upload_to_sharepoint(
                site_url = f"https://immilytics.sharepoint.com/sites/{result.BeneficiaryXref}-{result.b_lastname}{result.b_firstname}",
                local_file_path = file,
                sp_folder = f"Shared Documents/Document Library/{ProjectXref}")

            # shutil.move(op.join(indiv_finals_dir, op.basename(file)),
            #             op.join(target_dir, op.basename(file))) 
        shutil.rmtree(op.join(parent_dir,'ImmiLytics'))
        return  site_url_temp, file_list
    else:
        site_url_temp = f"https://immilytics.sharepoint.com/sites/{result.BeneficiaryXref}-{result.b_lastname}{result.b_firstname}"
        return site_url_temp, []

def RPA_Quick_Form_Automation():
    try:
        target_dir, file_list = start()
        return True, target_dir, file_list
    except Exception as e:
        print(e)
        return traceback.format_exc()
