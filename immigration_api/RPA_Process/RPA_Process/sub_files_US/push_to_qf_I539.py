import os,json,shutil,glob,requests,base64
import os.path as op
import time

def generate_539(CaseID, formtype, other_objects):

    mailing_address = other_objects['mailing_address']
    current_res_address = other_objects['current_res_address']
    last_perm_address_abroad = other_objects['last_perm_address_abroad']
    perm_foreign_address = other_objects['perm_foreign_address']
    ben_cur_emp = other_objects['ben_cur_emp']
    bit_ans = other_objects['bit_ans']
    iff = other_objects['iff']
    result = other_objects['result']
    
    most_recent_entry_rec = other_objects['most_recent_entry_rec']

    most_recent_notice = other_objects['most_recent_notice']

    resp_dic = other_objects['resp_dic']



    cursor = other_objects['cursor']
    headersAPI = other_objects['headersAPI']
    qpdf_merger = other_objects['qpdf_merger']
    parent_dir = other_objects['parent_dir']
    change_date = other_objects['change_date']
    AptSteFlr = other_objects['AptSteFlr']
    iff = other_objects['iff']
    return_high_salary = other_objects['return_high_salary']
    results2 = other_objects['results2']
    clean_num = other_objects['clean_num']



    # for sharepoint activities
    get_files = other_objects['get_files']
    download_files = other_objects['download_files']
    upload_to_sharepoint = other_objects['upload_to_sharepoint']
   

    if result:

        if True:

            # old cond includes not only children

            # dependents = cursor.execute('''select *,DATEDIFF(YY,BirthDate,GETDATE()) as Age from [dbo].[Beneficiary] where PrimaryBeneficiaryID = '{}' and not (LOWER(BirthCountry) Like '%america%' or LOWER(BirthCountry) Like '%u.s.a%' or LOWER(BirthCountry) Like '%usa%' ) and not (LOWER(CitizenshipCountry) Like '%america%' or LOWER(CitizenshipCountry) Like '%u.s.a%' or LOWER(CitizenshipCountry) Like '%usa%' ) and ((LOWER(RelationType) in('husband','spouse','wife'))  or (lower(RelationType) in('child','son','daughter','biological son','biological daughter','biological child') and ((DATEDIFF(YY,BirthDate,GETDATE()))<21))) '''.format(result.BeneficiaryID)).fetchall()

            # new cond only for children >21 and country not in us

            dependents = cursor.execute('''select b.*,ci.*,

            bt.EntryDate as bt_EntryDate,
            bt.IssuingCountry as bt_IssuingCountry,
            bt.I94Number as bt_I94Number,
            bt.I94ExpirationDate, 
            bt.ValidTo as bt_ValidTo,
            bt.TravelDocumentNumber,

            pp.PassportNumber as pp_PassportNumber,
            pp.ValidTo as pp_ValidTo,

            DATEDIFF(YY,BirthDate,GETDATE()) as Age from [dbo].[Beneficiary] b
            
            left join BeneficiaryPassport pp on pp.BeneficiaryID = b.BeneficiaryID

            left join BeneficiaryTravel bt on bt.BeneficiaryID = b.BeneficiaryID

            left join config.I94Status ci on ci.I94StatusID  = bt.ImmigrationStatusOnI94ID


            where PrimaryBeneficiaryID = ? and
            pp.IsCurrent = 1 and
            bt.EntryMostRecent = 1 and not
            (LOWER(BirthCountry) Like '%america%' or 
            LOWER(BirthCountry) Like '%u.s.a%' or 
            LOWER(BirthCountry) Like '%usa%' ) and not 
            (LOWER(CitizenshipCountry) Like '%america%' or 
            LOWER(CitizenshipCountry) Like '%u.s.a%' or
            LOWER(CitizenshipCountry) Like '%usa%' ) and
            ((lower(RelationType) in('child','son','daughter','biological son','biological daughter','biological child') and
            ((DATEDIFF(YY,BirthDate,GETDATE()))<21))) 
            
            ''',(result.BeneficiaryID)).fetchall()

            p1 = {'FirstName': '', 'LastName': '', 'MiddleName': '',
                  'DateOfBirth': '', 'BirthCountry': '', 'Relation': ''}
            p2 = {'FirstName': '', 'LastName': '', 'MiddleName': '',
                  'DateOfBirth': '', 'BirthCountry': '', 'Relation': ''}
            p3 = {'FirstName': '', 'LastName': '', 'MiddleName': '',
                  'DateOfBirth': '', 'BirthCountry': '', 'Relation': ''}
            p4 = {'FirstName': '', 'LastName': '', 'MiddleName': '',
                  'DateOfBirth': '', 'BirthCountry': '', 'Relation': ''}
            p5 = {'FirstName': '', 'LastName': '', 'MiddleName': '',
                  'DateOfBirth': '', 'BirthCountry': '', 'Relation': ''}
            p6 = {'FirstName': '', 'LastName': '', 'MiddleName': '',
                  'DateOfBirth': '', 'BirthCountry': '', 'Relation': ''}

            persons = [p1, p2, p3, p4, p5, p6]

            p4q13 = []

            if result.IsInRemovalProceeding:
                p4q13.append(
                    {
                        'page_num': 3,

                        'part_num': 4,

                        'item_num': 13,

                        'rem_pers': f'Person in removal Proceeding: {result.b_firstname}, {result.b_lastname}',

                        'jur_inf': f'Jurisdiction info: {result.RemovalProceedingJurisdiction}',

                        'star_date': f"Proceeding start date: {result.RemovalProceedingStartDate.strftime('%m/%d/%Y') if result.RemovalProceedingStartDate else ''}",

                        'status': f'Status: {result.RemovalProceedingStatus}'
                    })

            for dependent, person in zip(dependents, persons):
                person['FirstName'] = dependent.FirstName
                person['LastName'] = dependent.LastName
                person['MiddleName'] = dependent.MiddleName
                person['DateOfBirth'] = dependent.BirthDate
                person['BirthCountry'] = dependent.BirthCountry
                person['Relation'] = dependent.RelationType

                if dependent.IsInRemovalProceeding:
                    p4q13.append({
                        'page_num': 3,

                        'part_num': 4,

                        'item_num': 13,

                        'rem_pers': f'Person in removal Proceeding: {dependent.FirstName}, {dependent.LastName}',

                        'jur_inf': f'Jurisdiction info: {dependent.RemovalProceedingJurisdiction}',

                        'star_date': f"Proceeding start date: {dependent.RemovalProceedingStartDate.strftime('%m/%d/%Y') if dependent.RemovalProceedingStartDate else ''}",

                        'status': f'Status: {dependent.RemovalProceedingStatus}'
                    })

            p4q14 = ''

            if resp_dic.get('36',''):
                # if True:
                # for yes case

                p4q14 = {
                    'page_num': 3,
                    'part_num': 4,
                    'item_num': 14,
                    'person_employed': f'Person employed: {result.b_firstname}, {result.b_lastname}',

                    'employer_name': f'Name of employer: {ben_cur_emp.EmployerName}',

                    'employer_address': f'The address of employer: {ben_cur_emp.Address1}',
                    'Income': f'Income: {ben_cur_emp.SalaryAmount} per {ben_cur_emp.SalaryPer}',
                    'USCIS_Authorized': 'USCIS Authorization: See attached copy of EAD/I-797'
                }

            else:
                # for no case
                p4q14 = {
                    'page_num': 3,
                    'part_num': 4,
                    'item_num': 14,
                    'evidence_l0': 'Documentary evidence of the source:',
                    'evidence_l1': 'I will be supported by my spouse who is employed pursuant to a',
                    'evidence_l2': 'employment-based nonimmigrant status/visa. Please see attached',
                    'evidence_l3': "my spouse's relevant immigration and financial documents.",
                }

            J1ExchangeVisitor = ((str(most_recent_entry_rec.I94StatusType.lower() in (
                'j1', 'j2'))) or (result.HasPreviouslyHeldJVisaStatus == 1))

            # p4q15
            p4q15 = ''
            # if J1ExchangeVisitor:
            if True:
                p4q15 = {
                    'page_num': 3,
                    'part_num': 4,
                    'item_num': 15,
                    'start_date': 'Start date: 12/12/2020',
                    'end_date': 'End date:12/12/2023',
                    'J2Dependents': 'Some dependent here'
                }

            allcitizenship_countries = (result.AllCitizenshipCountries).split(';')

            extension_vs_changeofstatus = ''
            if result.PTag1_Val:
                word = result.PTag1_Val.strip().lower()
                if word in ('ext', 'extn', 'extension', 'extn.'):
                    extension_vs_changeofstatus = 2

                elif (word in ('cos', 'change of status')) or (result.IsCOSRequested):
                    extension_vs_changeofstatus = 3
                else:
                    extension_vs_changeofstatus = 1

            result_priority_category_chkbox_val = ''
            if str(result.ProjectPriorityCategory) in ["EB2", "EB-2", "Employment-Based 2nd", "Employment Based 2nd", "203(b)(2)"]:
                result_priority_category_chkbox_val = 4
            if str(result.ProjectPriorityCategory) in ["EB3", "EB-3", "Employment-Based 3rd", "Employment Based 3rd", "203(b)(3)(A)(ii)"]:
                result_priority_category_chkbox_val = 5

            part_4_checkbox_text = perm_foreign_address.AddressUnitType if str(
                mailing_address.Country).lower() in ('usa', 'u.s.a', 'america', 'united states of america') else ''

            # data_dict = []

            data_dict = [
                {
                    "FieldName": "1lawyer.ELISNumComb",
                    "FieldValue": clean_num(result.l_USCISNumber)
                },
                {
                    "FieldName": "User.D937.AdditionalInfo3.multiline.1",
                    "FieldValue": 'Dates maintained status as a J-1 exchange visitor or J-2dependent: '
                },
                {  
                    "FieldName": "USIMM84658.txt1.67",
                    "FieldValue": iff(result.COSNewStatusRequested)
                },
                { 
                    "FieldName": "USIMM84658.txt1.66",
                    "FieldValue": result.COSNewStatusEffectiveDate.strftime('%Y/%m/%d') if result.IsCOSRequested else ''
                },

                {
                    "FieldName": "1ben.SSNComb",
                    "FieldValue": iff(result.b_USCISNumber)
                },
                {
                    "FieldName": "USIMM84658.chk1.06",
                    "FieldValue": iff(extension_vs_changeofstatus)
                },
                {
                    "FieldName": "USIMM84658.chk1.00",  # p2 4
                    "FieldValue": '2' if dependents else '1'
                },
                {
                    "FieldName": "USIMM84658.txt1.71",
                    "FieldValue": str(len(dependents)+1) if dependents else '1'
                },
                {
                    "FieldName": "User.F84658.EmployedSinceExtension",
                    "FieldValue": bit_ans(resp_dic.get('36',''))
                },
                {
                    "FieldName": "1ben.O.Phone",
                    "FieldValue": iff(result.ben_WorkPhone)
                },
                {
                    "FieldName": "1ben.H.Mobile",
                    "FieldValue": iff(result.b_Mobile)
                },
                {
                    "FieldName": "1ben.TD.ID",
                    "FieldValue": iff(most_recent_entry_rec.TravelDocumentNumber)
                },
                {
                    "FieldName": "USIMM84658.chk1.21",
                    "FieldValue": '1' if (str(most_recent_entry_rec.I94StatusType.lower() in ('j1', 'j2', 'f1', 'f2'))) else '0'
                },
                {
                    "FieldName": "1ben.H.Email",
                    "FieldValue": iff(result.ben_WorkEmail)
                },
                {
                    "FieldName": "1ben.H.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(current_res_address.Address1)
                },
                {
                    "FieldName": "1ben.H.AddrUnitType",
                    "FieldValue": AptSteFlr(current_res_address.AddressUnitType) if AptSteFlr(current_res_address.AddressUnitType) else ''
                },                            
                {
                    "FieldName": "1ben.H.Addr4",
                    "FieldValue": iff(current_res_address.AddressUnitNumber)
                },

                {
                    "FieldName": "1ben.H.City",
                    "FieldValue":iff(current_res_address.City)
                },
                {
                    "FieldName": "1ben.H.State",
                    "FieldValue": iff(current_res_address.StateProvince)
                },
                {
                    "FieldName": "1ben.H.Zip",
                    "FieldValue":iff( current_res_address.PostalZipCode)
                },

                {
                    "FieldName": "USIMM84658.txt3.178",  # p42b
                    "FieldValue": current_res_address.Country if str(current_res_address.Country).lower().strip() not in ('usa', 'u.s.a', 'america', 'united states of america') else last_perm_address_abroad.Country
                },
                {
                    "FieldName": "1ben.F.Addr123",  # p43a
                    "FieldCalcOverride": True,
                    "FieldValue": perm_foreign_address.Address1 if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.F.AddrUnitType",  # p43b checkbox
                    "FieldValue": AptSteFlr(part_4_checkbox_text)
                },
                {
                    "FieldName": "1ben.F.Addr4",  # p43b blankbx
                    "FieldValue": perm_foreign_address.AddressUnitNumber if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.F.City",  # p43c blankbx
                    "FieldValue": perm_foreign_address.City if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.F.County",  # p43d blankbx
                    "FieldValue": perm_foreign_address.StateProvince if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.F.ForeignRoute",  # p43e blankbx
                    "FieldValue": perm_foreign_address.PostalZipCode if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.F.Country",  # p43f blankbx
                    "FieldValue": perm_foreign_address.Country if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "USIMM84658.txt1.01",
                    "FieldValue": iff(results2.WorkLocationAddress1)
                },

                {
                    "FieldName": "USIMM84658.txt1.02",
                    "FieldValue": iff(results2.WorkLocationAddress2)
                },
                {
                    "FieldName": "USIMM84658.txt1.03",
                    "FieldValue": iff(results2.WorkLocationCity)
                },
                {
                    "FieldName": "USIMM84658.txt1.04",
                    "FieldValue": iff(results2.WorkLocationState)
                },
                {
                    "FieldName": "USIMM84658.txt1.05",
                    "FieldValue": iff(results2.WorkLocationZipCode)
                },
                {
                    "FieldName": "1spou.FName",
                    "FieldValue":iff(p1['FirstName'])
                },
                {
                    "FieldName": "1spou.LName",
                    "FieldValue": iff(p1['LastName'])
                },
                {
                    "FieldName": "1spou.MName",
                    "FieldValue": iff(p1['MiddleName'])
                },
                {
                    "FieldName": "1spou.DOB",
                    "FieldValue": change_date(p1['DateOfBirth'])
                },
                {
                    "FieldName": "1spou.BP.Country",
                    "FieldValue": iff(p1['BirthCountry'])
                },
                {
                    "FieldName": "1spou.RelToClient",
                    "FieldValue": iff(p1['Relation'])
                },
                {
                    "FieldName": "1child.FName",
                    "FieldValue": iff(p2['FirstName'])
                },
                {
                    "FieldName": "1child.LName",
                    "FieldValue": iff(p2['LastName'])
                },
                {
                    "FieldName": "1child.MName",
                    "FieldValue": iff(p2['MiddleName'])
                },
                {
                    "FieldName": "1child.DOB",
                    "FieldValue": change_date(p2['DateOfBirth'])
                },
                {
                    "FieldName": "1child.BP.Country",
                    "FieldValue": iff(p2['BirthCountry'])
                },
                {
                    "FieldName": "1child.RelToClient",
                    "FieldValue": iff(p2['Relation'])
                },
                {
                    "FieldName": "2child.FName",
                    "FieldValue": iff(p3['FirstName'])
                },
                {
                    "FieldName": "2child.LName",
                    "FieldValue": iff(p3['LastName'])
                },
                {
                    "FieldName": "2child.MName",
                    "FieldValue": iff(p3['MiddleName'])
                },
                {
                    "FieldName": "2child.DOB",
                    "FieldValue": change_date(p3['DateOfBirth'])
                },
                {
                    "FieldName": "2child.BP.Country",
                    "FieldValue": iff(p3['BirthCountry'])
                },
                {
                    "FieldName": "2child.RelToClient",
                    "FieldValue": iff(p3['Relation'])
                },
                {
                    "FieldName": "3child.FName",
                    "FieldValue": iff(p4['FirstName'])
                },
                {
                    "FieldName": "3child.LName",
                    "FieldValue": iff(p4['LastName'])
                },
                {
                    "FieldName": "3child.MName",
                    "FieldValue": iff(p4['MiddleName'])
                },
                {
                    "FieldName": "3child.DOB",
                    "FieldValue": change_date(p4['DateOfBirth'])
                },
                {
                    "FieldName": "3child.BP.Country",
                    "FieldValue": iff(p4['BirthCountry'])
                },
                {
                    "FieldName": "3child.RelToClient",
                    "FieldValue": iff(p4['Relation'])
                },
                {
                    "FieldName": "4child.FName",
                    "FieldValue": iff(p5['FirstName'])
                },
                {
                    "FieldName": "4child.LName",
                    "FieldValue": iff(p5['LastName'])
                },
                {
                    "FieldName": "4child.MName",
                    "FieldValue": iff(p5['MiddleName'])
                },
                {
                    "FieldName": "4child.DOB",
                    "FieldValue": change_date(p5['DateOfBirth'])
                },
                {
                    "FieldName": "4child.BP.Country",
                    "FieldValue": iff(p5['BirthCountry'])
                },
                {
                    "FieldName": "4child.RelToClient",
                    "FieldValue": iff(p5['Relation'])
                },
                {
                    "FieldName": "5child.FName",
                    "FieldValue": iff(p6['FirstName'])
                },
                {
                    "FieldName": "5child.LName",
                    "FieldValue": iff(p6['LastName'])
                },
                {
                    "FieldName": "5child.MName",
                    "FieldValue": iff(p6['MiddleName'])
                },
                {
                    "FieldName": "5child.DOB",
                    "FieldValue": change_date(p6['DateOfBirth'])
                },
                {
                    "FieldName": "5child.BP.Country",
                    "FieldValue": iff(p6['BirthCountry'])
                },
                {
                    "FieldName": "5child.RelToClient",
                    "FieldValue": iff(p6['Relation'])
                },
                {
                    "FieldName": "1lawyer.G28Attached",
                    "FieldValue": 1
                },
                {
                    "FieldName": "USIMM84658.txt3.83",
                    "FieldValue": iff(results2.OfferedWageType)
                },
                {
                    "FieldName": "USIMM84658.txt3.79",
                    "FieldValue": results2.OfferedWageFrom if float(results2.OfferedWageFrom.replace(',', '')) >= float(ben_cur_emp.CurrentAnnualSalary.replace(',', '')) else ben_cur_emp.CurrentAnnualSalary
                },
                {
                    "FieldName": "USIMM84658.txt3.74",
                    "FieldValue": iff(results2.JobTitle)
                },
                {
                    "FieldName": "USIMM84658.txt3.78.0",
                    "FieldValue": iff(results2.SOCCODE.split('-')[0].strip())
                },
                {
                    "FieldName": "USIMM84658.txt3.78.1",
                    "FieldValue": iff(results2.SOCCODE.split('-')[1].strip())
                },
                {
                    "FieldName": "USIMM84658.txt3.68.0",
                    "FieldValue": change_date(results2.PERMFilingDate)
                },
                {
                    "FieldName": "USIMM84658.txt3.68.1",
                    "FieldValue": change_date(results2.PERMValidTo)
                },
                {
                    "FieldName": "USIMM84658.txt3.38",
                    # if results.PERMDOLCaseNumber #is not None else results2.PERMDOLCaseNumber
                    "FieldValue": iff(result.ReceiptNumber)
                },
                {
                    "FieldName": "1lawyer.LicNum",
                    "FieldValue": iff(result.l_BarNumber)
                },
                {
                    "FieldName": "1petitioner.LName",
                    "FieldValue": result.LastName if result.LastName is not None else results2.PetitionerContactLastName
                },
                {
                    "FieldName": "1petitioner.FName",
                    "FieldValue": result.FirstName if result.FirstName is not None else results2.PetitionerContactFirstName
                },
                {
                    "FieldName": "1petitioner.MName",
                    "FieldValue": result.MiddleName if result.MiddleName is not None else iff(results2.PetitionerContactMiddleInitial)
                },
                {
                    "FieldName": "1contact.SEmp.Company",
                    "FieldValue": result.PetitionerName if result.PetitionerName is not None else (str(results2.PetitionerContactLastName)+', '+str(results2.PetitionerContactFirstName)+' '+str(results2.PetitionerContactMiddleInitial)).strip()
                },
                {
                    "FieldName": "1contact.EO.Attn",
                    "FieldValue": (str(result.FirstName if result.FirstName is not None else results2.PetitionerContactFirstName)+' '+str(result.LastName if result.LastName is not None else results2.PetitionerContactLastName)).strip()
                },
                {
                    "FieldName": "txtCalcEO.Addr1",
                    "FieldValue": result.Address1 if result.Address1 is not None else results2.PetitionerContactAddress1
                },
                {
                    "FieldName": "USIMM84658.chk3.11.6",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "USIMM84658.chk3.11.0",
                    "FieldValue": 'No'
                },
                {  # part4 2a
                    "FieldName": "USIMM84658.chk3.07",
                    "FieldValue": '2'
                },
                {  # part4 6a
                    "FieldName": "USIMM84658.chk3.10",
                    "FieldValue": 'No'
                },

                {
                    "FieldName": "1contact.EO.Addr123",  # overwri 1contact.EO.Addr123
                    "FieldCalcOverride": True,
                    "FieldValue": iff(result.Address1)
                },
                {  # peculiar
                    "FieldName": "1contact.EO.Addr4",
                    "FieldValue": result.AddressUnitNumber if result.AddressUnitNumber is not None else results2.PetitonerContactAddress2
                },

                {
                    "FieldName": "1contact.EO.AddrUnitType",
                    "FieldValue": AptSteFlr(result.AddressUnitType)
                },
                {
                    "FieldName": "User.D937.AttorneyOrAccreditedRep",
                    "FieldValue": '1'
                },
                {
                    "FieldName": "USIMM84658.chk3.27.0",
                    "FieldValue": 'No' if p1['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk3.26.0",
                    "FieldValue": 'Yes' if p1['FirstName'] else ''
                },

                {
                    "FieldName": "USIMM84658.chk2.54.1.0",
                    "FieldValue": '1'
                },
                {
                    "FieldName": "USIMM84658.chk3.26.1",
                    "FieldValue": 'Yes' if p2['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk3.27.1",
                    "FieldValue": 'No' if p2['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.26.0.0",
                    "FieldValue": 'Yes' if p3['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.27.0.0",
                    "FieldValue": 'No' if p3['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.54.1.2",
                    "FieldValue": '1'
                },
                {
                    "FieldName": "USIMM84658.chk2.26.0.1",
                    "FieldValue": 'Yes' if p4['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.27.0.1",
                    "FieldValue": 'No' if p4['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.26.1.0",
                    "FieldValue": 'Yes' if p5['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.27.1.0",
                    "FieldValue": 'No' if p5['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.26.1.1",
                    "FieldValue": 'Yes' if p6['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.27.1.1",
                    "FieldValue": 'No' if p6['FirstName'] else ''
                },
                {
                    "FieldName": "USIMM84658.chk2.54.0",
                    "FieldValue": '1'
                },
                {
                    "FieldName": "User.D937.NontechnicalDescriptionOfJob.multiline.1",
                    "FieldValue": "See attached Certified ETA Form 9089"
                },
                {
                    "FieldName": "1contact.EO.City",
                    "FieldValue": result.City if result.City is not None else results2.PetitionerContactCity
                },
                {
                    "FieldName": "USIMM84658.chk3.22",
                    "FieldValue": '1'
                },
                {
                    "FieldName": "USIMM84658.chk3.24",
                    "FieldValue": 'Yes'
                },
                {
                    "FieldName": "USIMM84658.chk3.23.0",
                    "FieldValue": 'Yes'
                },
                {
                    "FieldName": "1contact.EO.State",
                    "FieldValue": result.StateProvince if result.StateProvince is not None else results2.PetitionerContactState
                },
                {
                    "FieldName": "1contact.EO.Zip",
                    "FieldValue": result.PostalZipCode if result.PostalZipCode is not None else results2.PetitionerContactZipCode
                },
                {
                    "FieldName": "1contact.EO.Country",
                    "FieldValue": result.Country if result.Country is not None else results2.PetitionerContactCountry
                },
                {
                    "FieldName": "1contact.SEmp.TaxIDComb",
                    "FieldValue": result.FederalEmployerId.replace('-', '') if result.FederalEmployerId is not None else str(results2.FEIN).replace('-', '')
                },
                {
                    "FieldName": "USIMM84658.chk1.04",
                    "FieldValue": iff(result_priority_category_chkbox_val)
                },
                {
                    "FieldName": "1ben.LName",
                    "FieldValue": result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName
                },
                {
                    "FieldName": "1ben.FName",
                    "FieldValue": result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName
                },
                {
                    "FieldName": "1ben.MName",
                    "FieldValue": result.b_middlename if result.b_middlename is not None else iff(results2.BeneficiaryMiddleName)
                },
                {
                    "FieldName": "1ben.M.Attn",
                    "FieldValue": (str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)).strip()
                },
                {
                    "FieldName": "1ben.M.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": mailing_address.Address1 if mailing_address.Address1 is not None else results2.BeneficiaryAddress1
                },
                {
                    "FieldName": "1ben.M.AddrUnitType",
                    "FieldValue": AptSteFlr(mailing_address.AddressUnitType)
                },
                {
                    "FieldName": "1ben.M.Addr4",
                    "FieldValue": mailing_address.AddressUnitNumber if mailing_address.AddressUnitNumber is not None else results2.BeneficiaryAddress2
                },
                {
                    "FieldName": "1ben.M.City",
                    "FieldValue": mailing_address.City if mailing_address.City is not None else results2.BeneficiaryAddressCity
                },
                {
                    "FieldName": "1ben.M.State",
                    "FieldValue": mailing_address.StateProvince if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.M.County",
                    "FieldValue": mailing_address.StateProvince if str(mailing_address.Country).lower().strip() not in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.M.Zip",
                    "FieldValue": mailing_address.PostalZipCode if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.M.ForeignRoute",
                    "FieldValue": mailing_address.PostalZipCode if str(mailing_address.Country).lower().strip() not in ('usa', 'u.s.a', 'america', 'united states of america') else ''
                },
                {
                    "FieldName": "1ben.M.Country",
                    "FieldValue": mailing_address.Country if mailing_address.Country is not None else results2.BeneficiaryAddressCountry
                },
                {
                    "FieldName": "1ben.DOB",
                    "FieldValue": result.BirthDate.strftime('%m/%d/%Y') if result.BirthDate is not None else results2.BeneficiaryDateofBirth.strftime('%m/%d/%Y')
                },
                {
                    "FieldName": "1ben.BP.City",
                    "FieldValue": iff(result.BirthCity)
                },
                {
                    "FieldName": "1ben.BP.State",
                    "FieldValue": iff(result.BirthStateProvince)
                },
                {
                    "FieldName": "1ben.BP.Country",
                    "FieldValue": result.BirthCountry if result.BirthCountry is not None else results2.BeneficiaryCountryofBirth
                },
                {
                    "FieldName": "1ben.Citizenship",
                    "FieldValue": result.CitizenshipCountry if result.CitizenshipCountry is not None else results2.BeneficiaryCountryofCitizenship
                },
                {
                    "FieldName": "1ben.AlienRegNumComb",
                    "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
                },
                {
                    "FieldName": "1ben.SSNComb",
                    "FieldValue": clean_num(result.SSNNumber)
                },
                {
                    "FieldName": "1ben.I94.ArrivalDate",
                    "FieldValue": change_date(most_recent_entry_rec.EntryDate)
                },
                {
                    "FieldName": "1ben.I94.ID",
                    "FieldValue": most_recent_entry_rec.I94Number if most_recent_entry_rec.I94Number is not None else results2.BeneficiaryI94Number
                },
                {
                    "FieldName": "1ben.I94.IDExpire",
                    "FieldValue": change_date(most_recent_entry_rec.I94ExpirationDate)
                },
                {
                    "FieldName": "1ben.I94.IDStatus",
                    "FieldValue": iff(most_recent_entry_rec.I94StatusType)
                },
                {
                    "FieldName": "1alt.GOV.ID",
                    "FieldValue": iff(result.PassportNumber)
                },
                {
                    "FieldName": "1alt.GOV.IDCountry",
                    "FieldValue": iff(result.pp_IssuingCountry)
                },
                {
                    "FieldName": "1alt.GOV.IDExpire",
                    "FieldValue": change_date(result.pp_ValidTo)
                },
                {
                    "FieldName": "1ben.GOV.ID",
                    "FieldValue": iff(result.PassportNumber)
                },
                {
                    "FieldName": "1ben.GOV.IDCountry",
                    "FieldValue": iff(most_recent_entry_rec.IssuingCountry)
                },
                {
                    "FieldName": "1ben.GOV.IDExpire",
                    "FieldValue": change_date(result.pp_ValidTo)
                },
                {
                    "FieldName": "USIMM84658.txt3.19.1",
                    "FieldValue": (str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)).strip()
                },
                {
                    "FieldName": "USIMM84658.txt3.19.0",
                    "FieldValue": mailing_address.Address1 if mailing_address.Address1 is not None else results2.BeneficiaryAddress1
                },
                {
                    "FieldName": "USIMM84658.txt3.24.0",
                    "FieldValue": mailing_address.AddressUnitNumber if mailing_address.AddressUnitNumber is not None else results2.BeneficiaryAddress2
                },
                {
                    "FieldName": "USIMM84658.chk3.09",
                    "FieldValue": AptSteFlr(mailing_address.AddressUnitType)
                },
                {
                    "FieldName": "USIMM84658.txt3.29.0",
                    "FieldValue": mailing_address.City if mailing_address.City is not None else results2.BeneficiaryAddressCity
                },
                {
                    "FieldName": "USIMM84658.txt3.29.2",
                    "FieldValue": mailing_address.StateProvince if mailing_address.StateProvince is not None else results2.BeneficiaryAddressState
                },
                {
                    "FieldName": "USIMM84658.txt3.29.3",
                    "FieldValue": mailing_address.PostalZipCode if mailing_address.PostalZipCode is not None else results2.BeneficiaryAddressZipCode
                },
                {
                    "FieldName": "USIMM84658.txt3.34",
                    "FieldValue": mailing_address.Country if mailing_address.Country is not None else results2.BeneficiaryAddressCountry
                },
                {
                    "FieldName": "1contact.SEmp.BusType",
                    "FieldValue": iff(result.p_BusinessType)
                },
                {
                    "FieldName": "1contact.SEmp.YearEst",
                    "FieldValue": result.p_YearEstablished if result.p_YearEstablished is not None else results2.YearCommencedBusiness
                },
                {
                    "FieldName": "User.D937.1contact.SEmp.NumEmployeesUS",
                    "FieldValue": result.p_EmployeeCountUS if result.p_EmployeeCountUS is not None else results2.NumberOfEmployees
                },
                {
                    "FieldName": "1contact.SEmp.GrossIncome",
                    "FieldValue": iff(result.p_AnnualIncomeGrossUS)
                },
                {
                    "FieldName": "1contact.SEmp.NetIncome",
                    "FieldValue": iff(result.p_AnnualIncomeNetUS)
                },
                {
                    "FieldName": "1contact.SEmp.NAICSComb",
                    "FieldValue": result.p_NaicsCode if result.p_NaicsCode is not None else results2.NAICSCode
                },
                {
                    "FieldName": "USIMM84658.txt3.01.1",
                    "FieldValue": (str(iff(result.l_firstname))+' '+str(iff(result.l_lastname))).strip()
                },
                {
                    "FieldName": "1authind.LName",
                    "FieldValue": result.LastName if result.LastName is not None else results2.PetitionerContactLastName
                },
                {
                    "FieldName": "1authind.FName",
                    "FieldValue": result.FirstName if result.FirstName is not None else results2.PetitionerContactFirstName
                },
                {
                    "FieldName": "1authind.SignTitle",
                    "FieldValue": result.JobTitle if result.JobTitle is not None else results2.JobTitle
                },
                {
                    "FieldName": "1authind.O.Phone",
                    "FieldValue": result.PhoneNumber if result.PhoneNumber is not None else results2.PetitionerContactPhoneNumber
                },
                {
                    "FieldName": "USIMM84658.txt3.525",
                    "FieldValue": iff(result.MobilePhone)
                },
                {
                    "FieldName": "1authind.O.Email",
                    "FieldValue": result.Email if result.Email is not None else results2.PetitionerContactEmail
                },
                {
                    "FieldName": "1lawyer.LName",
                    "FieldValue": result.l_lastname if result.l_lastname is not None else results2.AttorneyAgentLastName
                },
                {
                    "FieldName": "1lawyer.FName",
                    "FieldValue": result.l_firstname if result.l_firstname is not None else results2.AttorneyAgentFirstName
                },
                {
                    "FieldName": "1lawfirm.Company",
                    "FieldValue": result.l_firmname if result.l_firmname is not None else results2.AttorneyAgentFirmName
                },
                {
                    "FieldName": "1lawfirm.O.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": result.l_address1 if result.l_address1 is not None else results2.AttorneyAgentAddress1
                },
                {
                    "FieldName": "1lawfirm.O.AddrUnitType",
                    "FieldValue": AptSteFlr(result.l_addressunittype)
                },
                {
                    "FieldName": "1lawfirm.O.Addr4",
                    "FieldValue": result.l_addressunitnumber if result.l_addressunitnumber is not None else results2.AttorneyAgentAddress2
                },
                {
                    "FieldName": "1lawfirm.O.City",
                    "FieldValue": result.l_city if result.l_city is not None else results2.AttorneyAgentCity
                },
                {
                    "FieldName": "1lawfirm.O.State",
                    "FieldValue": result.l_state if result.l_state is not None else results2.AttorneyAgentState
                },
                {
                    "FieldName": "1lawfirm.O.Zip",
                    "FieldValue": result.l_zipcode if result.l_zipcode is not None else results2.AttorneyAgentZipCode
                },
                {
                    "FieldName": "1lawfirm.O.Country",
                    "FieldValue": result.l_country if result.l_country is not None else results2.AttorneyAgentCountry
                },
                {
                    "FieldName": "1lawyer.O.Phone",
                    "FieldValue": result.l_phonenumber if result.l_phonenumber is not None else results2.AttorneyAgentPhoneNumber
                },
                {
                    "FieldName": "1lawyer.O.Mobile",
                    "FieldValue": iff(result.l_mobilenumber)
                },
                {
                    "FieldName": "1lawyer.O.Email",
                    "FieldValue": result.l_email if result.l_email is not None else results2.AttorneyAgentEmail
                },
                # new from here
                {
                    "FieldName": "1ben.AppVisaAbroad",
                    "FieldValue": 'Yes' if result.IsImmigrantVisaApplicant else 'No'
                },
                {
                    "FieldName": "User.F84658.ImmigrantPetitionFiled",
                    "FieldValue": 'Yes' if result.HasAnyImmigrantVisaPetitionBeenFiledOnYourBehalf else 'No'
                },
                {
                    "FieldName": "User.F84658.I485PreviouslyFiled",
                    "FieldValue": 'Yes' if result.AosProjectFiledDate or (result.ServiceType.lower().strip() in ('aos application', 'adjustment of status', '485')) else 'No'
                },
                {
                    "FieldName": "1ben.BeenArrested",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.InvolvedInTorture",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.InvolvedInKilling",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.InvolvedInSevereInjury",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.CommittedRape",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.DenyingReligiousBeliefs",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.ServedUSMilitary",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.WorkedPrison",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.UsedWeapon",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.BeenWeaponsDealer",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.CombatTraining",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.ViolatedTerms",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "1ben.PendingProceedings",
                    "FieldValue": 'Yes' if result.IsInRemovalProceeding else 'No'
                },
                {
                    "FieldName": "1ben.UnderstandLanguage",
                    "FieldValue": 1
                },
                {
                    "FieldName": "1ben.CurrentStatus",
                    "FieldValue": iff(most_recent_entry_rec.I94StatusType)
                },
                {
                    "FieldName": "1ben.J1StatusInUS",
                    "FieldValue": 'Yes' if J1ExchangeVisitor else 'No'
                },
                {
                    "FieldName": "1lawyer.ExtendsPrepApp",
                    "FieldValue": 1
                },
                {
                    "FieldName": "1lawyer.FullName",
                    "FieldValue": f'{result.l_lastname}, {iff(result.l_firstname)}' 
                },
                {
                    "FieldName": "1ben.PreparerPreparedApp",
                    "FieldValue": 1
                },
                {
                    "FieldName": "1ben.NonImmigExpiry",
                    "FieldValue": most_recent_entry_rec.I94ExpirationDate.strftime('%m/%d/%Y') if str(most_recent_entry_rec.I94StatusType).lower() not in ('j1', 'j2', 'f1', 'f2') else 'N/A'
                }
            ]

            place_1 = ''
            place_2 = ''
            place_3 = ''
            place_4 = ''
            place_5 = ''

            if len(p4q13) > 0:

                place_1 = 'full'

                data_dict.extend([
                    {
                        "FieldName": "USIMM84658.txt2.47.0",
                        "FieldValue": p4q13[0].get('page_num', '')
                    },
                    {
                        "FieldName": "USIMM84658.txt2.48.0",
                        "FieldValue": p4q13[0].get('part_num', '')
                    },
                    {
                        "FieldName": "USIMM84658.txt2.49.0",
                        "FieldValue": p4q13[0].get('item_num', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.1",
                        "FieldValue": p4q13[0].get('rem_pers', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.2",
                        "FieldValue": p4q13[0].get('jur_inf', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.3",
                        "FieldValue": p4q13[0].get('star_date', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.4",
                        "FieldValue": p4q13[0].get('status', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.5",
                        "FieldValue": ''
                    }])

            if len(p4q13) > 1:
                data_dict.extend([
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.6",
                        "FieldValue": p4q13[1].get('rem_pers', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.7",
                        "FieldValue": p4q13[1].get('jur_inf', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.8",
                        "FieldValue": p4q13[1].get('star_date', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.9",
                        "FieldValue": p4q13[1].get('status', '')
                    }])

            if len(p4q13) > 2:
                place_2 = 'full'

                data_dict.extend([
                    {
                        "FieldName": "USIMM84658.txt2.47.1.0",
                        "FieldValue": p4q13[2].get('page_num', '')
                    },
                    {
                        "FieldName": "USIMM84658.txt2.48.1.0",
                        "FieldValue": p4q13[2].get('part_num', '')
                    },
                    {
                        "FieldName": "USIMM84658.txt2.49.1.0",
                        "FieldValue": p4q13[2].get('item_num', '')
                    },
                    {

                        "FieldName": "User.D937.AdditionalInfo2.multiline.1",
                        "FieldValue": p4q13[2].get('rem_pers', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.2",
                        "FieldValue": p4q13[2].get('jur_inf', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.3",
                        "FieldValue": p4q13[2].get('star_date', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.4",
                        "FieldValue": p4q13[2].get('status', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.5",
                        "FieldValue": ''
                    }])

            if len(p4q13) > 3:
                data_dict.extend([
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.6",
                        "FieldValue": p4q13[3].get('rem_pers', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.7",
                        "FieldValue": p4q13[3].get('jur_inf', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.8",
                        "FieldValue": p4q13[3].get('star_date', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo2.multiline.9",
                        "FieldValue": p4q13[3].get('status', '')
                    }])

            if len(p4q13) > 4:
                place_3 = 'full'
                data_dict.extend([
                    {
                        "FieldName": "USIMM84658.txt2.47.1.1.0",
                        "FieldValue": p4q13[4].get('page_num', '')
                    },
                    {
                        "FieldName": "USIMM84658.txt2.48.1.1.0",
                        "FieldValue": p4q13[4].get('part_num', '')
                    },
                    {
                        "FieldName": "USIMM84658.txt2.49.1.1.0",
                        "FieldValue": p4q13[4].get('item_num', '')
                    },
                    {

                        "FieldName": "User.D937.AdditionalInfo3.multiline.1",
                        "FieldValue": p4q13[4].get('rem_pers', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.2",
                        "FieldValue": p4q13[4].get('jur_inf', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.3",
                        "FieldValue": p4q13[4].get('star_date', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.4",
                        "FieldValue": p4q13[4].get('status', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.5",
                        "FieldValue": ''
                    }])

            if len(p4q13) > 5:
                data_dict.extend([
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.6",
                        "FieldValue": p4q13[5].get('rem_pers', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.7",
                        "FieldValue": p4q13[5].get('jur_inf', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.8",
                        "FieldValue": p4q13[5].get('star_date', '')
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo3.multiline.9",
                        "FieldValue": p4q13[5].get('status', '')
                    }])

            if p4q14:
                if place_1 != 'full':
                    place_1 = 'full'
                    data_dict.extend([

                        {
                            "FieldName": "USIMM84658.txt2.47.0",
                            "FieldValue": p4q14.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.0",
                            "FieldValue": p4q14.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.0",
                            "FieldValue": p4q14.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.1",
                            "FieldValue": p4q14.get('person_employed', p4q14.get('evidence_l0', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.2",
                            "FieldValue": p4q14.get('employer_name', p4q14.get('evidence_l1', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.3",
                            "FieldValue": p4q14.get('employer_address', p4q14.get('evidence_l2', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.4",
                            "FieldValue": p4q14.get('Income', p4q14.get('evidence_l3', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.5",
                            "FieldValue": p4q14.get('USCIS_Authorized', '')
                        }])

                elif place_2 != 'full':
                    place_2 = 'full'
                    data_dict.extend([

                        {
                            "FieldName": "USIMM84658.txt2.47.1.0",
                            "FieldValue": p4q14.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.0",
                            "FieldValue": p4q14.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.0",
                            "FieldValue": p4q14.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.1",
                            "FieldValue": p4q14.get('person_employed', p4q14.get('evidence_l0', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.2",
                            "FieldValue": p4q14.get('employer_name', p4q14.get('evidence_l1', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.3",
                            "FieldValue": p4q14.get('employer_address', p4q14.get('evidence_l2', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.4",
                            "FieldValue": p4q14.get('Income', p4q14.get('evidence_l3', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.5",
                            "FieldValue": p4q14.get('USCIS_Authorized', '')
                        }])

                elif place_3 != 'full':
                    place_3 = 'full'
                    data_dict.extend([

                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.0",
                            "FieldValue": p4q14.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.0",
                            "FieldValue": p4q14.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.0",
                            "FieldValue": p4q14.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.1",
                            "FieldValue": p4q14.get('person_employed', p4q14.get('evidence_l0', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.2",
                            "FieldValue": p4q14.get('employer_name', p4q14.get('evidence_l1', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.3",
                            "FieldValue": p4q14.get('employer_address', p4q14.get('evidence_l2', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.4",
                            "FieldValue": p4q14.get('Income', p4q14.get('evidence_l3', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.5",
                            "FieldValue": p4q14.get('USCIS_Authorized', '')
                        }])

                elif place_4 != 'full':
                    place_4 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.1",
                            "FieldValue": p4q14.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.1",
                            "FieldValue": p4q14.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.1",
                            "FieldValue": p4q14.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.1",
                            "FieldValue": p4q14.get('person_employed', p4q14.get('evidence_l0', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.2",
                            "FieldValue": p4q14.get('employer_name', p4q14.get('evidence_l1', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.3",
                            "FieldValue": p4q14.get('employer_address', p4q14.get('evidence_l2', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.4",
                            "FieldValue": p4q14.get('Income', p4q14.get('evidence_l3', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.5",
                            "FieldValue": p4q14.get('USCIS_Authorized', '')
                        }])

                elif place_5 != 'full':
                    place_5 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.2",
                            "FieldValue": p4q14.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.2",
                            "FieldValue": p4q14.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.2",
                            "FieldValue": p4q14.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.1",
                            "FieldValue":  p4q14.get('person_employed', p4q14.get('evidence_l0', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.2",
                            "FieldValue":  p4q14.get('employer_name', p4q14.get('evidence_l1', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.3",
                            "FieldValue": p4q14.get('employer_address', p4q14.get('evidence_l2', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.4",
                            "FieldValue": p4q14.get('Income', p4q14.get('evidence_l3', ''))
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.5",
                            "FieldValue": p4q14.get('USCIS_Authorized', '')
                        }])

            if p4q15:
                if place_1 != 'full':
                    place_1 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.0",
                            "FieldValue": p4q15.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.0",
                            "FieldValue": p4q15.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.0",
                            "FieldValue": p4q15.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.1",
                            "FieldValue": p4q15.get('start_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.2",
                            "FieldValue": p4q15.get('end_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.3",
                            "FieldValue": p4q15.get('J2Dependents', '')
                        }])

                elif place_2 != 'full':
                    place_2 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.0",
                            "FieldValue": p4q15.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.0",
                            "FieldValue": p4q15.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.0",
                            "FieldValue": p4q15.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.1",
                            "FieldValue": p4q15.get('start_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.2",
                            "FieldValue": p4q15.get('end_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.3",
                            "FieldValue": p4q15.get('J2Dependents', '')
                        }])

                elif place_3 != 'full':
                    place_3 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.0",
                            "FieldValue": p4q15.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.0",
                            "FieldValue": p4q15.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.0",
                            "FieldValue": p4q15.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.1",
                            "FieldValue": p4q15.get('start_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.2",
                            "FieldValue": p4q15.get('end_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.3",
                            "FieldValue": p4q15.get('J2Dependents', '')
                        }])

                elif place_4 != 'full':
                    place_4 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.1",
                            "FieldValue": p4q15.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.1",
                            "FieldValue": p4q15.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.1",
                            "FieldValue": p4q15.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.1",
                            "FieldValue": p4q15.get('start_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.2",
                            "FieldValue": p4q15.get('end_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.3",
                            "FieldValue": p4q15.get('J2Dependents', '')
                        }])

                elif place_5 != 'full':
                    place_5 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.2",
                            "FieldValue": p4q15.get('page_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.2",
                            "FieldValue": p4q15.get('part_num', '')
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.2",
                            "FieldValue": p4q15.get('item_num', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.1",
                            "FieldValue": p4q15.get('start_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.2",
                            "FieldValue": p4q15.get('end_date', '')
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.3",
                            "FieldValue": p4q15.get('J2Dependents', '')
                        }])

            if len(allcitizenship_countries) > 1:
                if place_1 != 'full':
                    place_1 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.0",
                            "FieldValue": 2
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.0",
                            "FieldValue": 4
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.0",
                            "FieldValue": '2f'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.1",
                            "FieldValue": 'All countries of citizenship:'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.2",
                            "FieldValue": allcitizenship_countries[0]
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.3",
                            "FieldValue": allcitizenship_countries[1] if len(allcitizenship_countries) > 2 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.4",
                            "FieldValue":  allcitizenship_countries[2] if len(allcitizenship_countries) > 3 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.5",
                            "FieldValue":  allcitizenship_countries[3] if len(allcitizenship_countries) > 4 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.6",
                            "FieldValue":  allcitizenship_countries[4] if len(allcitizenship_countries) > 5 else ''
                        },

                    ])

                elif place_2 != 'full':

                    place_2 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.0",
                            "FieldValue": '2'
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.0",
                            "FieldValue": '4'
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.0",
                            "FieldValue": '2f'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.1",
                            "FieldValue": 'All countries of citizenship:'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.2",
                            "FieldValue": allcitizenship_countries[0]
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.3",
                            "FieldValue": allcitizenship_countries[1] if len(allcitizenship_countries) > 2 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.4",
                            "FieldValue":  allcitizenship_countries[2] if len(allcitizenship_countries) > 3 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.5",
                            "FieldValue":  allcitizenship_countries[3] if len(allcitizenship_countries) > 4 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo2.multiline.6",
                            "FieldValue":  allcitizenship_countries[4] if len(allcitizenship_countries) > 5 else ''
                        }
                    ])

                elif place_3 != 'full':

                    place_3 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.0",
                            "FieldValue": 2
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.0",
                            "FieldValue": 4
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.0",
                            "FieldValue": '2f'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.1",
                            "FieldValue": 'All countries of citizenship:'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.2",
                            "FieldValue": allcitizenship_countries[0]
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.3",
                            "FieldValue": allcitizenship_countries[1] if len(allcitizenship_countries) > 2 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.4",
                            "FieldValue":  allcitizenship_countries[2] if len(allcitizenship_countries) > 3 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.5",
                            "FieldValue":  allcitizenship_countries[3] if len(allcitizenship_countries) > 4 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo3.multiline.6",
                            "FieldValue":  allcitizenship_countries[4] if len(allcitizenship_countries) > 5 else ''
                        }])

                elif place_4 != 'full':

                    place_4 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.1",
                            "FieldValue": 2
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.1",
                            "FieldValue": 4
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.1",
                            "FieldValue": '2f'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.1",
                            "FieldValue": 'All countries of citizenship:'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.2",
                            "FieldValue": allcitizenship_countries[0]
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.3",
                            "FieldValue": allcitizenship_countries[1] if len(allcitizenship_countries) > 2 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.4",
                            "FieldValue":  allcitizenship_countries[2] if len(allcitizenship_countries) > 3 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.5",
                            "FieldValue":  allcitizenship_countries[3] if len(allcitizenship_countries) > 4 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo4.multiline.6",
                            "FieldValue":  allcitizenship_countries[4] if len(allcitizenship_countries) > 5 else ''
                        }
                    ])

                elif place_5 != 'full':

                    place_5 = 'full'
                    data_dict.extend([
                        {
                            "FieldName": "USIMM84658.txt2.47.1.1.2",
                            "FieldValue": '2'
                        },
                        {
                            "FieldName": "USIMM84658.txt2.48.1.1.2",
                            "FieldValue": '4'
                        },
                        {
                            "FieldName": "USIMM84658.txt2.49.1.1.2",
                            "FieldValue": '2f'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.1",
                            "FieldValue": 'All countries of citizenship:'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.2",
                            "FieldValue": allcitizenship_countries[0]
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.3",
                            "FieldValue": allcitizenship_countries[1] if len(allcitizenship_countries) > 2 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.4",
                            "FieldValue":  allcitizenship_countries[2] if len(allcitizenship_countries) > 3 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.5",
                            "FieldValue":  allcitizenship_countries[3] if len(allcitizenship_countries) > 4 else ''
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo5.multiline.6",
                            "FieldValue":  allcitizenship_countries[4] if len(allcitizenship_countries) > 4 else ''
                        }
                    ])

            params = {
                "HostFormOnQuik": True,
                "FormFields": data_dict,
                "QuikFormID": "84658",
                "PrintEditablePDF": True
            }

            # return False
            data_json = json.dumps(params)

            response = requests.post(
                'https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)

            # response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/html', headers=headersAPI, data=data_json)

            api_response = response.json()

            # print(api_response)
            # quit()

            pdf_base64 = api_response['ResultData']['PDF']
            with open('Form I-539.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))

            # if False:
            if len(dependents) > 0:
                print('\nProcessing for I-539-A dependents')
                for dep in dependents:

                    data_539A = [

                        {
                            "FieldName": "1lawyer.O.Fax",
                            "FieldValue": iff(result.l_mobilenumber)
                        },
                        {
                            "FieldName": "1lawyer.G28Attached",
                            "FieldValue": 1
                        },

                        {
                            "FieldName": "USIMM82459.txt1.01",
                            "FieldValue": iff(result.b_lastname)
                        },
                        {
                            "FieldName": "USIMM82459.txt1.02",
                            "FieldValue": iff(result.b_firstname)
                        },
                        {
                            "FieldName": "USIMM82459.txt1.03",
                            "FieldValue":iff(result.b_middlename)
                        },
                        {
                            "FieldName": "USIMM82459.txt1.46",
                            "FieldValue": iff(dep.TravelDocumentNumber)
                        },

                        {
                            "FieldName": "USIMM82459.txt1.45",
                            "FieldValue": iff(dep.USCISNumber)

                        },

                        {
                            "FieldName": "1ben.UnderstandLanguage",
                            "FieldValue": '1'
                        },
                        {
                            "FieldName": "1ben.PreparerPreparedApp",
                            "FieldValue": '1'
                        },
                        {
                            "FieldName": "1lawyer.FullName",
                            "FieldValue": f'{result.l_lastname}, {iff(result.l_firstname)}' 
                        },


                        {
                            "FieldName": "1ben.LName",
                            "FieldValue": iff(dep.LastName)
                        },

                        {
                            "FieldName": "1ben.FName",
                            "FieldValue": iff(dep.FirstName)
                        },

                        {
                            "FieldName": "1ben.MName",
                            "FieldValue": iff(dep.MiddleName)
                        },

                        {
                            "FieldName": "1ben.DOB",
                            "FieldValue": change_date(dep.BirthDate)
                        },

                        {
                            "FieldName": "1ben.BP.Country",
                            "FieldValue": iff(dep.BirthCountry)
                        },

                        {
                            "FieldName": "1ben.Citizenship",
                            "FieldValue": iff(dep.CitizenshipCountry)
                        },

                        {
                            "FieldName": "1ben.SSNComb",
                            "FieldValue": iff(dep.SSNNumber)
                        },

                        {
                            "FieldName": "1ben.AlienRegNumComb",
                            "FieldValue": iff(dep.AlienNumber1)
                        },
                        {
                            "FieldName": "1ben.LastEntryDate",
                            "FieldValue": change_date(dep.bt_EntryDate)
                        },

                        {
                            "FieldName": "1ben.I94.IDComb",
                            "FieldValue": iff(dep.bt_I94Number)
                        },

                        {
                            "FieldName": "1ben.GOV.ID",
                            "FieldValue": iff(dep.pp_PassportNumber)
                        },

                        {
                            "FieldName": "1ben.GOV.IDCountry",
                            "FieldValue": iff(dep.bt_IssuingCountry)
                        },

                        {
                            "FieldName": "1ben.GOV.IDExpire",
                            "FieldValue": change_date(dep.bt_ValidTo)
                        },
                        {
                            "FieldName": "1ben.CurrentStatus",
                            "FieldValue": iff(dep.I94StatusType)
                        },

                        {
                            "FieldName": "1ben.NonImmigExpiry",
                            "FieldValue": dep.I94ExpirationDate.strftime('%m/%d/%Y') if str(dep.I94StatusType).lower() not in ('j1', 'j2', 'f1', 'f2') else 'N/A'
                        },
                        {
                            "FieldName": "1ben.H.Phone",
                            "FieldValue": iff(result.ben_WorkPhone)
                        },
                        {
                            "FieldName": "1ben.H.Mobile",
                            "FieldValue": iff(result.b_Mobile)
                        },

                        {
                            "FieldName": "1ben.H.Email",
                            "FieldValue": iff(result.ben_WorkEmail)
                        },

                        {
                            "FieldName": "1lawyer.LName",
                            "FieldValue": iff(result.l_lastname)
                        },

                        {
                            "FieldName": "1lawyer.FName",
                            "FieldValue": iff(result.l_firstname)
                        },

                        {
                            "FieldName": "1lawfirm.Company",
                            "FieldValue": iff(result.l_firmname)
                        },
                        {
                            "FieldName": "1lawfirm.O.Addr123",
                            "FieldCalcOverride": True,
                            "FieldValue": result.l_address1 if result.l_address1 is not None else results2.AttorneyAgentAddress1
                        },


                        {
                            "FieldName": "1lawfirm.O.AddrUnitType",
                            "FieldValue": AptSteFlr(result.l_addressunittype)
                        },

                        {
                            "FieldName": "1lawfirm.O.Addr4",
                            "FieldValue": iff(result.l_addressunitnumber)
                        },

                        {
                            "FieldName": "1lawfirm.O.City",
                            "FieldValue": iff(result.l_city)
                        },
                        {
                            "FieldName": "1lawfirm.O.State",
                            "FieldValue": iff(result.l_state)
                        },

                        {
                            "FieldName": "1lawfirm.O.Zip",
                            "FieldValue": iff(result.l_zipcode)
                        },
                        {
                            "FieldName": "1lawfirm.O.Country",
                            "FieldValue": iff(result.l_country)
                        },

                        {
                            "FieldName": "1lawyer.O.Phone",
                            "FieldValue": iff(result.l_phonenumber)
                        },

                        {
                            "FieldName": "1lawyer.O.Email",
                            "FieldValue": iff(result.l_email)
                        },

                        {
                            "FieldName": "User.D937.AttorneyOrAccreditedRep",
                            "FieldValue": '1'
                        },

                        {
                            "FieldName": "1ben.AlienRegNumComb",
                            "FieldValue": iff(dep.AlienNumber1)
                        },

                        {
                            "FieldName": "3altclientLName",
                            "FieldValue": iff(result.b_lastname)
                        },
                        {
                            "FieldName": "3ben.FName",
                            "FieldValue": iff(result.b_firstname)
                        },
                        {
                            "FieldName": "3ben.MName",
                            "FieldValue": iff(result.b_middlename)
                        },
                        {
                            "FieldName": "1lawyer.ELISNumComb",
                            "FieldValue": clean_num(result.l_USCISNumber)
                        },
                        {
                            "FieldName": "USIMM82459.txt2.45",
                            "FieldValue": iff(dep.USCISNumber)
                        },
                        {
                            "FieldName": "1lawyer.ExtendsPrepApp",
                            "FieldValue": 1
                        },
                        {
                            "FieldName": "1ben.TD.ID",
                            "FieldValue": iff(dep.TravelDocumentNumber)
                        }

                    ]

                    params = {
                        "HostFormOnQuik": True,
                        "FormFields": data_539A,
                        "QuikFormID": "82459",
                        "PrintEditablePDF": True
                    }

                    data_json = json.dumps(params)

                    response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)

                    # response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/html', headers=headersAPI, data=data_json)

                    api_response = response.json()

                    # print(api_response)
                    # quit()

                    pdf_base64 = api_response['ResultData']['PDF']
                    with open(f'Form I-539A_{dep.FirstName}.pdf', 'wb') as pdf:
                        pdf.write(base64.b64decode(pdf_base64))

            #fd


            data_dict2 = [
                 {
                    "FieldName": "1ben.AlienRegNumComb",
                    "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
                },
                {
                    "FieldName": "1lawyer.ELISNumComb",
                    "FieldValue": clean_num(result.l_USCISNumber)
                },
                {
                    "FieldName": "1lawyer.LName",
                    "FieldValue": result.l_lastname if result.l_lastname is not None else results2.AttorneyAgentLastName
                },
                {
                    "FieldName": "1lawyer.FName",
                    "FieldValue": result.l_firstname if result.l_firstname is not None else results2.AttorneyAgentFirstName
                },
                {
                    "FieldName": "1lawyer.MName",
                    "FieldValue": result.l_middlename if result.l_middlename is not None else iff(results2.AttorneyAgentMiddleInitial)
                },
                {
                    "FieldName": "1lawfirm.O.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": result.l_address1 if result.l_address1 is not None else results2.AttorneyAgentAddress1
                },
                {
                    "FieldName": "1lawfirm.O.AddrUnitType",
                    "FieldValue": AptSteFlr(result.l_addressunittype)
                },
                {
                    "FieldName": "1lawfirm.O.Addr4",
                    "FieldValue": result.l_addressunitnumber if result.l_addressunitnumber is not None else results2.AttorneyAgentAddress2
                },
                {
                    "FieldName": "1lawfirm.O.City",
                    "FieldValue": result.l_city if result.l_city is not None else results2.AttorneyAgentCity
                },
                {
                    "FieldName": "1lawfirm.O.State",
                    "FieldValue": result.l_state if result.l_state is not None else results2.AttorneyAgentState
                },
                {
                    "FieldName": "1lawfirm.O.Zip",
                    "FieldValue": result.l_zipcode if result.l_zipcode is not None else results2.AttorneyAgentZipCode
                },
                {
                    "FieldName": "1lawfirm.O.Country",
                    "FieldValue": result.l_country if result.l_country is not None else results2.AttorneyAgentCountry
                },
                {
                    "FieldName": "1lawyer.O.Phone",
                    "FieldValue": result.l_phonenumber if result.l_phonenumber is not None else results2.AttorneyAgentPhoneNumber
                },
                {
                    "FieldName": "1lawyer.O.Mobile",
                    "FieldValue": iff(result.l_mobilenumber)
                },
                {
                    "FieldName": "1lawyer.O.Email",
                    "FieldValue": result.l_email if result.l_email is not None else results2.AttorneyAgentEmail
                },
                {
                    "FieldName": "1lawyer.LicNum",
                    "FieldValue": iff(result.l_BarNumber)
                },
                {
                    "FieldName": "1lawfirm.Company",
                    "FieldValue": result.l_firmname if result.l_firmname is not None else results2.AttorneyAgentFirmName
                },
                {
                    "FieldName": "USIMM82463.txt1.21.0",
                    "FieldValue": ('Form I-539 - '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)+', '+str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_middlename if result.b_middlename is not None else iff(results2.BeneficiaryMiddleName))).strip()
                },
                {
                    "FieldName": "1ben.LName",
                    "FieldValue": iff(result.LastName)
                },
                {
                    "FieldName": "1ben.FName",
                    "FieldValue": iff(result.FirstName)
                },
                {
                    "FieldName": "1ben.MName",
                    "FieldValue": iff(result.MiddleName)
                },
                {
                    "FieldName": "1ben.SEmp.Company",
                    "FieldValue": result.PetitionerName if result.PetitionerName is not None else results2.PetitionerName
                },
                {
                    "FieldName": "1ben.SignTitle",
                    "FieldValue": result.JobTitle if result.JobTitle is not None else results2.JobTitle
                },
                {
                    "FieldName": "1ben.M.Phone",
                    "FieldValue": result.PhoneNumber if result.PhoneNumber is not None else results2.PetitionerPhone
                },
                {
                    "FieldName": "1ben.M.Mobile",
                    "FieldValue": iff(result.MobilePhone)
                },
                {
                    "FieldName": "1ben.M.Email",
                    "FieldValue": iff(result.Email)
                },
                {
                    "FieldName": "1ben.M.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": result.Address1 if result.Address1 is not None else results2.PetitionerAddress1
                },
                {
                    "FieldName": "1ben.M.Addr4",
                    "FieldValue": iff(result.AddressUnitNumber)
                },
                {
                    "FieldName": "1ben.M.City",
                    "FieldValue": result.City if result.City is not None else results2.PetitionerCity
                },
                {
                    "FieldName": "1ben.M.State",
                    "FieldValue": result.StateProvince if result.StateProvince is not None else results2.PetitionerState
                },
                {
                    "FieldName": "1ben.M.Zip",
                    "FieldValue": result.PostalZipCode if result.PostalZipCode is not None else results2.PetitionerZipCode
                },
                {
                    "FieldName": "1ben.M.Country",
                    "FieldValue": result.Country if result.Country is not None else results2.PetitionerPhone
                },

                {
                    "FieldName": "User.D937.AttorneyEligiblePracticeLawIn",
                    "FieldValue": 1
                },
                {
                    "FieldName": "User.D937.AmNotAmSubjectToAnyOrder",
                    "FieldValue": 1
                },
                {
                    "FieldName": "USIMM82463.chk1.02",
                    "FieldValue": 1
                },
                {
                    "FieldName": "USIMM82463.chk1.03",
                    "FieldValue": 2
                },
                {
                    "FieldName": "1altclient.EO.AddrUnitType",
                    "FieldValue": AptSteFlr(result.AddressUnitType)
                },
                {
                    "FieldName": "1lawyer.O.Fax",
                    "FieldValue": iff(result.l_Faxnumber)
                },
                {
                    "FieldName": "USIMM82463.chk1.25",
                    "FieldValue": 1
                },
                {
                    "FieldName": "1lawyer.PracticeJurisidiction",
                    "FieldValue": iff(result.l_LicensingAuthority)
                }
            ]




            params = {
                "HostFormOnQuik": True,
                "FormFields": data_dict2,
                "QuikFormID": "82463",
                "PrintEditablePDF": True
            }

            data_json = json.dumps(params)

            response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)

            # response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/html', headers=headersAPI, data=data_json)
            
            api_response = response.json()

            pdf_base64 = api_response['ResultData']['PDF']
            # print()
            with open('Form G-28_for_I-539.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))

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

        pdf_merge_sp(data_dict, formtype, result, results2,most_recent_entry_rec,most_recent_notice,parent_dir,iff,change_date,qpdf_merger,get_files,download_files,upload_to_sharepoint)

        # print(result)
        # shutil.move(os.path.join(source_dir, file_name), os.path.join(processed_dir, file_name))

    else:
        print('No Matching record in db to Process..')





def pdf_merge_sp(data_dict, formtype, result, results2,most_recent_entry_rec,most_recent_notice,parent_dir,iff,change_date,qpdf_merger,get_files,download_files,upload_to_sharepoint):

    os.chdir(parent_dir)

    if data_dict['organization_xref']:

        target_dir = op.join(parent_dir,
                             'ImmiLytics',
                             f"{data_dict['organization_xref']} - {data_dict['organization_name']}",
                             f"{data_dict['petitioner_xref']} - {data_dict['petitioner_name']}",
                             f"{data_dict['beneficiary_xref']} - {data_dict['last_name']}, {data_dict['first_name']}",
                             f"{data_dict['project_xref']}")
        
    else:
        target_dir = op.join(parent_dir,
                             'ImmiLytics',
                             f"{data_dict['petitioner_xref']} - {data_dict['petitioner_name']}",
                             f"{data_dict['beneficiary_xref']} - {data_dict['last_name']}, {data_dict['first_name']}",
                             f"{data_dict['project_xref']}")
        
    support_doc_dir = op.join(target_dir,'Supporting Docs')

    if not op.exists(support_doc_dir):

        os.makedirs(support_doc_dir)

        
    pdfs = []

    shutil.move(op.join(parent_dir, 'Form G-28_for_I-539.pdf'),
                op.join(target_dir, 'Form G-28_for_I-539.pdf'))
    
    shutil.move(op.join(parent_dir, 'Form I-539.pdf'),
                op.join(target_dir, 'Form I-539.pdf'))


    print("Getting supporting docs from sharepoint..")
    get_files(
        site_url=f"https://immilytics.sharepoint.com/sites/{data_dict['beneficiary_xref']}-{data_dict['last_name']}{data_dict['first_name']}",
        sp_folder=f"Shared Documents/Document Library/Project Specific Supporting Docs/{data_dict['project_xref']}",
        dwd_dir = support_doc_dir)
    
    # wait to download file 
    time.sleep(10)

    pdfs.append(op.join(target_dir, 'Form G-28_for_I-539.pdf'))
    pdfs.append(op.join(target_dir, 'Form I-539.pdf'))
   

    if op.exists(op.join(support_doc_dir, 'ETA 9089.pdf')):
        pdfs.append(op.join(support_doc_dir, 'ETA 9089.pdf'))
    

    pdfs.append(op.join(support_doc_dir, 'I-539 Supporting Docs Final Packet.pdf'))

    os.chdir(parent_dir)

    indiv_finals_dir = op.join(target_dir,"indiv_finals_dir")
    
    if not op.exists(indiv_finals_dir):
        os.mkdir(indiv_finals_dir)
    qpdf_merger(pdfs, indiv_finals_dir, formtype)
    time.sleep(5)

    # removing individual files
    os.remove(op.join(target_dir, 'Form G-28_for_I-539.pdf'))
    os.remove(op.join(target_dir, 'Form I-539.pdf'))

    # qpdf_merger(pdfs, target_dir, formtype)

