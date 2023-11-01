import os
import pyodbc
import requests
import warnings
import subprocess
import threading
import re
from dateutil.relativedelta import relativedelta
from datetime import date
from datetime import datetime
import RPA_Process.sub_files_US.push_to_qf_I129 as i129
import RPA_Process.sub_files_US.push_to_qf_I131 as i131
import RPA_Process.sub_files_US.push_to_qf_I140 as i140
import RPA_Process.sub_files_US.push_to_qf_I485 as i485
import RPA_Process.sub_files_US.push_to_qf_I539 as i539
import RPA_Process.sub_files_US.push_to_qf_I765 as i765

warnings.filterwarnings(action='ignore')
parent_dir = os.path.dirname(os.path.realpath(__file__))
os.chdir(parent_dir)

conn = pyodbc.connect(
    'Driver={ODBC Driver 18 for SQL Server};Server=20.228.144.215;port=port;Network Library=DBMSSOCN;Database=Immilytics_IOP_V7;uid=sa;pwd=gskPraveen@123;TrustServerCertificate=Yes;MARS_Connection=Yes;')
username = "ImmilyticsLLC_AdminUser"
password = "wcqs9HscgI8StxrWBBeMTq"
api_url = "https://websvcs.quikforms.com/rest_authentication/token"
headersAuth = {'Content-Type': 'application/x-www-form-urlencoded', }
data = {"grant_type": "password", "username": username, "password": password}
response = requests.post(api_url, headers=headersAuth, data=data, verify=True)
response_auth = response.json()

headersAPI = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer ' + response_auth['access_token'],
}

source_dir = os.path.join(parent_dir, 'immiLytics/Certified PERMs')
processed_dir = os.path.join(parent_dir, 'processed')

US_keyword = re.compile('united states|united states of america|america|U\.S\.A|U\.S|U\.S\.AMERICA|usa|us',
                        flags=re.IGNORECASE)


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
            return 3
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
        command_string = command_string + '"' + str(pdf_name) + '"' + ' '
    command_string = command_string + f' -- "{folder_path3}\Final_{formtype}.pdf"'
    command_string.replace('\n', '')
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


def start():
    cursor = conn.cursor()
    project_list = cursor.execute('''select pro.ProjectID,pro.ProjectXref,pro.ProjectPetitionID,pt.FormsToBeGenerated
        from dbo.[Project] as pro 
        left join config.PetitionTemplate as pt on pro.ProjectPetitionID = pt.PetitionTemplateID
        where pro.RPADraftingRequestYesNo = 'True' ''').fetchall()

    for project in project_list:
        forms = project.FormsToBeGenerated.split(';')
        ProjectID = project.ProjectID

        thread1 = CustomThread(ProjectID)
        thread1.start()
        thread1.join()

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

        # from here you query from the query result
        marriage_history = cursor.execute(f'''select * from BeneficiaryMaritalInfo m 
        where m.BeneficiaryID = '{result.BeneficiaryID}'
        order by MarriageDate desc ''').fetchall()

        # ben's primary ben's,  ben level data
        prim_ben = cursor.execute(f'''select nd.ReceiptNumber,b.*
        from Beneficiary b left join dbo.NoticeDetail nd on nd.BeneficiaryID  = b.BeneficiaryID                                
        where b.BeneficiaryID = '{result.PrimaryBeneficiaryID}' ''').fetchone()

        ben_high_edu = cursor.execute(
            f'''select * from BeneficiaryEducation where BeneficiaryID = '{result.BeneficiaryID}' and IsHighestDegree = '1' and IsUSDegree = '1' ''').fetchone()

        ben_all_edu = cursor.execute(
            f'''select * from BeneficiaryEducation where BeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

        ben_family = cursor.execute(
            f'''select * from BeneficiaryFamily where PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

        most_recent_entry_rec = cursor.execute('''select bt.*,ci.* from BeneficiaryTravel bt
        left join config.I94Status ci on ci.I94StatusID  = bt.ImmigrationStatusOnI94ID
        where BeneficiaryID = ? and EntryMostRecent = ?
        ''', (result.BeneficiaryID, True)).fetchone()

        Ques_Responses = cursor.execute('''select r.ResponseFull,r.QuestionID from Response r
        left join Question q on q.QuestionID  = r.QuestionID
        where BeneficiaryID = ? order by r.QuestionID
        ''', result.BeneficiaryID).fetchall()

        resp_dic = {}
        for resp in Ques_Responses:
            try:
                resp_dic[f'{int(resp.QuestionID)}'] = int(resp.ResponseFull)
            except:
                resp_dic[f'{int(resp.QuestionID)}'] = resp.ResponseFull

        most_recent_notice = cursor.execute('''select * from NoticeDetail nd
        left join config.NoticeType nt on nt.NoticeTypeID  = nd.NoticeDetailID
        where ProjectID = ?''', result.ProjectID).fetchone()

        # last_five_years_residence_address
        l5_res = cursor.execute(
            f'''select *, DATEDIFF(DAY,cast(AddressToDate as varchar),GETDATE()) as days_from_now from dbo.BeneficiaryAddress
            where AddressType = 'residence' and
            IsCurrentResidenceAddress = 'False' and
            AddressFromDate is not null and 
            DATEDIFF(YEAR,cast(AddressFromDate as varchar),GETDATE()) <= 5 and
            BeneficiaryID = '{result.BeneficiaryID}'
            order by days_from_now asc''').fetchall()

        # last_five_years_employment_history
        l5_emp = cursor.execute(
            f'''select *, DATEDIFF(DAY,cast(TerminationDate as varchar),GETDATE()) as days_from_now from [dbo].[BeneficiaryEmployment]
            where HireDate is not null and DATEDIFF(YEAR,cast(HireDate as varchar),GETDATE()) <= 5 and
            BeneficiaryID = '{result.BeneficiaryID}' order by days_from_now asc''').fetchall()

        parents = cursor.execute(
            f'''select * from [dbo].[BeneficiaryFamily] where (lower(Relation) like '%father%' or lower(Relation) like '%mother%') and
            PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

        spouse = cursor.execute(
            f'''select * from [dbo].[Beneficiary] where (lower(RelationType) like '%spouse%' or
                lower(RelationType) like '%wife%' or
                lower(RelationType) like '%husband%' or
                lower(RelationType) like '%partner%') and
            PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()

        org_membership = cursor.execute(f'''select * from BeneficiaryOrganizationMembership ms  
        where ms.BeneficiaryID = '{result.BeneficiaryID}'
        order by MembershipStartDate desc ''').fetchall()

        ben_cur_emp = cursor.execute(
            f'''select * from BeneficiaryEmployment where BeneficiaryID = '{result.BeneficiaryID}' and IsCurrent = '1' ''').fetchone()
        cursor.close()

        other_objects = {
            'mailing_address': thread1.mailing_address,
            'current_res_address': thread1.current_res_address,
            'last_perm_address_abroad': thread1.last_perm_address_abroad,
            'perm_foreign_address': thread1.perm_foreign_address,
            'mail_addr_vs_phys_addr': thread1.mail_addr_vs_phys_addr,
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
            'results2': thread1.results2,
            'headersAPI': headersAPI,
            'US_keyword': US_keyword,
            'conn': conn,
            'parent_dir': parent_dir,
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
            'clean_price': clean_price
        }

        print("ProjectXref: {}".format(project.ProjectXref))
        for form_type in forms:
            if form_type.lower().strip() == 'i-765':
                print('Processing Form I-765')
                i765_thread = threading.Thread(target=i765.generate_765,
                                               args=(project.ProjectID, form_type, other_objects))
                i765_thread.start()

            elif form_type.lower().strip() == 'i-539':
                print('Processing Form I-539')
                i539_thread = threading.Thread(target=i539.generate_539,
                                               args=(project.ProjectID, form_type, other_objects))
                i539_thread.start()

            elif form_type.lower().strip() == 'i-140':
                print('Processing Form I-140')
                i140_thread = threading.Thread(target=i140.generate_140,
                                               args=(project.ProjectID, form_type, other_objects))
                i140_thread.start()

            elif form_type.lower().strip() == 'i-131':
                print('Processing Form I-131')
                i131_thread = threading.Thread(target=i131.generate_131,
                                               args=(project.ProjectID, form_type, other_objects))
                i131_thread.start()

            elif form_type.lower().strip() == 'i-485':
                print('Processing Form I-485')
                i485_thread = threading.Thread(target=i485.generate_485,
                                               args=(project.ProjectID, form_type, other_objects))
                i485_thread.start()

        for form_type in forms:
            if form_type.lower().strip() == 'i-765':
                i765_thread.join()
                print('Process Completed Form I-765')
            elif form_type.lower().strip() == 'i-539':
                i539_thread.join()
                print('Process Completed Form I-539')
            elif form_type.lower().strip() == 'i-140':
                i140_thread.join()
                print('Process Completed Form I-140')
            elif form_type.lower().strip() == 'i-131':
                i131_thread.join()
                print('Process Completed Form I-131')
            elif form_type.lower().strip() == 'i-485':
                i485_thread.join()
                print('Process Completed Form I-485')

        return get_files(other_objects["result"])


def get_files(result_data):
    result = result_data
    data_dict = {
        'organization_xref': result.OrganizationXref,
        'organization_name': result.OrganizationName,
        'petitioner_xref': result.PetitionerXref,
        'petitioner_name': result.PetitionerName,
        'beneficiary_xref': result.BeneficiaryXref,
        'project_xref': result.ProjectXref,
        'last_name': result.b_lastname,
        'first_name': result.b_firstname,
    }
    if data_dict['organization_xref']:
        target_dir = os.path.join(parent_dir, 'ImmiLytics',
                                  f"{data_dict['organization_xref']} - {data_dict['organization_name']}",
                                  f"{data_dict['petitioner_xref']} - {data_dict['petitioner_name']}",
                                  f"{data_dict['beneficiary_xref']} - {data_dict['last_name']}, {data_dict['first_name']}",
                                  f"{data_dict['project_xref']}")

    else:
        target_dir = os.path.join(parent_dir, 'ImmiLytics',
                                  f"{data_dict['petitioner_xref']} - {data_dict['petitioner_name']}",
                                  f"{data_dict['beneficiary_xref']} - {data_dict['last_name']}, {data_dict['first_name']}",
                                  f"{data_dict['project_xref']}")

    if os.path.exists(target_dir):
        file_list = [fp for fp in os.listdir(target_dir) if os.path.isfile(os.path.join(target_dir, fp))]
        return target_dir, file_list
    else:
        return []


def RPA_Quick_Form_Automation():
    try:
        target_dir, file_list = start()
        return True, target_dir, file_list
    except Exception as e:
        print(e)
        return False
