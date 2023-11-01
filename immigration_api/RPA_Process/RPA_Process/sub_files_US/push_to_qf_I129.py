import os
import os.path as op
import json
import shutil
import glob
import requests
import base64
import re,time


def generate_129(ProjectID, formtype, other_objects):
   

    mailing_address = other_objects['mailing_address']
    current_res_address = other_objects['current_res_address']
    last_perm_address_abroad = other_objects['last_perm_address_abroad']
    perm_foreign_address = other_objects['perm_foreign_address']
    mail_addr_vs_phys_addr = other_objects['mail_addr_vs_phys_addr']
    marriage_history = other_objects['marriage_history']
    ben_high_edu = other_objects['ben_high_edu']
    ben_all_edu = other_objects['ben_all_edu']
    ben_cur_emp = other_objects['ben_cur_emp']
    ben_family = other_objects['ben_family']
    l5_res = other_objects['l5_res']
    l5_emp = other_objects['l5_emp']
    parents = other_objects['parents']
    spouse = other_objects['spouse']
    org_membership = other_objects['org_membership']
    prim_ben = other_objects['prim_ben']
    most_recent_entry_rec = other_objects['most_recent_entry_rec']
    most_recent_notice = other_objects['most_recent_notice']
    resp_dic = other_objects['resp_dic']
    result = other_objects['result']

    cursor = other_objects['cursor']
    bit_ans = other_objects['bit_ans']
    headersAPI = other_objects['headersAPI']
    qpdf_merger = other_objects['qpdf_merger']
    parent_dir = other_objects['parent_dir']
    change_date = other_objects['change_date']
    AptSteFlr = other_objects['AptSteFlr']
    iff = other_objects['iff']
    calculate_age = other_objects['calculate_age']
    get_gender = other_objects['get_gender']
    US_keyword = other_objects['US_keyword']
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
            dependents = cursor.execute('''select *,DATEDIFF(YY,BirthDate,GETDATE()) as Age from [dbo].[Beneficiary] where PrimaryBeneficiaryID = '{}' and not (LOWER(BirthCountry) Like '%america%' or LOWER(BirthCountry) Like '%u.s.a%' or LOWER(BirthCountry) Like '%usa%' ) and not (LOWER(CitizenshipCountry) Like '%america%' or LOWER(CitizenshipCountry) Like '%u.s.a%' or LOWER(CitizenshipCountry) Like '%usa%' ) and ( (lower(RelationType) in('child','son','daughter','biological son','biological daughter','biological child') and ((DATEDIFF(YY,BirthDate,GETDATE()))<21))) '''.format(result.BeneficiaryID)).fetchall()

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
                pass

            for dependent, person in zip(dependents, persons):
                person['FirstName'] = dependent.FirstName
                person['LastName'] = dependent.LastName
                person['MiddleName'] = dependent.MiddleName
                person['DateOfBirth'] = dependent.BirthDate
                person['BirthCountry'] = dependent.BirthCountry
                person['Relation'] = dependent.RelationType

            part_4_checkbox_text = perm_foreign_address.AddressUnitType if str(
                mailing_address.Country).lower() in ('usa', 'u.s.a', 'america', 'united states of america') else ''

            ben_gender = ''
            if result.ben_gender.lower().strip() == 'male':
                ben_gender = '1'
            elif result.ben_gender.lower().strip() == 'female':
                ben_gender = '2'

            data_dict = [
                {  # by default it will be no
                    "FieldName": "USIMM82468.chk7.41.2",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "USIMM82468.txt1.61",
                    "FieldValue": iff(most_recent_notice.ReceiptNumber)
                },
                {
                    "FieldName": "1contact.SEmp.Company",
                    "FieldValue": result.PetitionerName if result.PetitionerName is not None else (str(results2.PetitionerContactLastName)+', '+str(results2.PetitionerContactFirstName)+' '+str(results2.PetitionerContactMiddleInitial)).strip()
                },
                {
                    "FieldName": "1contact.EO.Attn",
                    "FieldValue": (str(result.FirstName if result.FirstName is not None else results2.PetitionerContactFirstName)+' '+str(result.LastName if result.LastName is not None else results2.PetitionerContactLastName)).strip()
                },
                {  # doubt this field is not pop though everything is right # pet for non immi worker p1 q3
                    "FieldName": "1contact.EO.AddrUnitType",
                    "FieldValue": AptSteFlr(result.AddressUnitType)
                },
                {
                    "FieldName": "1contact.EO.Addr4",
                    "FieldValue": result.AddressUnitNumber if result.AddressUnitNumber else results2.PetitonerContactAddress2
                },
                {
                    "FieldName": "1contact.EO.City",
                    "FieldValue": result.City if result.City is not None else results2.PetitionerContactCity
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
                    "FieldName": "1ben.J1StatusInUS",
                    "FieldValue": 'Yes' if result.HasPreviouslyHeldJVisaStatus else 'No'
                },

                {
                    "FieldName": "1contact.EO.Country",
                    "FieldValue": result.Country if result.Country is not None else results2.PetitionerContactCountry
                },
                {
                    "FieldName": "USIMM82468.txt1.57",
                    "FieldValue": 'H1-B'
                },
                {
                    "FieldName": "USIMM82468.chk1.04",
                    "FieldValue": AptSteFlr(result.ProjectPriorityCategory)
                },
                # {
                #     "FieldName": "USIMM82468.txt1.66",
                #     "FieldValue": result.COSNewStatusEffectiveDate.strftime('%Y/%m/%d') if result.IsCOSRequested else ''
                # },
                {
                    "FieldName": "1ben.MName",
                    "FieldValue": iff(result.b_middlename)
                },
                {
                    "FieldName": "1ben.DOB",
                    "FieldValue": result.BirthDate.strftime('%m/%d/%Y') if result.BirthDate is not None else results2.BeneficiaryDateofBirth.strftime('%m/%d/%Y')
                },
                {
                    "FieldName": "1ben.Gender",
                    "FieldValue": iff(ben_gender)
                },
                {
                    "FieldName": "1ben.AlienRegNumComb1",
                    "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
                },

                {
                    "FieldName": "1ben.BP.State",
                    "FieldValue": iff(result.BirthStateProvince)
                },
                {
                    "FieldName": "1ben.Citizenship",
                    "FieldValue": result.CitizenshipCountry if result.CitizenshipCountry is not None else results2.BeneficiaryCountryofCitizenship
                },
                {
                    "FieldName": "1ben.I94.ArrivalDate",
                    "FieldValue": change_date(most_recent_entry_rec.EntryDate)
                },
                {
                    "FieldName": "1ben.I94.IDComb",
                    "FieldValue": most_recent_entry_rec.I94Number if most_recent_entry_rec.I94Number is not None else results2.BeneficiaryI94Number
                },
                {
                    "FieldName": "1ben.GOV.IDCountry",
                    "FieldValue": iff(result.pp_IssuingCountry)
                },
                {
                    "FieldName": "1ben.CurrentStatus",
                    "FieldValue": iff(most_recent_entry_rec.I94StatusType)
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
                    "FieldValue": iff(current_res_address.City)
                },
                {
                    "FieldName": "1ben.H.State",
                    "FieldValue": iff(current_res_address.StateProvince)
                },
                {
                    "FieldName": "1ben.H.Zip",
                    "FieldValue": iff(current_res_address.PostalZipCode)
                },
                {
                    "FieldName": "1ben.F.AddrUnitType",
                    "FieldValue": AptSteFlr(part_4_checkbox_text)
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
                    "FieldName": "1authind.O.Email",
                    "FieldValue": result.Email if result.Email is not None else results2.PetitionerContactEmail
                },
                {
                    "FieldName": "1lawyer.LName",
                    "FieldValue": iff(result.l_lastname)
                },
                {
                    "FieldName": "1lawyer.FName",
                    "FieldValue": result.l_firstname if result.l_firstname is not None else results2.AttorneyAgentFirstName
                },
                {
                    "FieldName": "1lawfirm.Company",
                    "FieldValue": iff(result.l_firmname)
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
                    "FieldName": "1lawyer.O.Fax",
                    "FieldValue": iff(result.l_mobilenumber)
                },
                {
                    "FieldName": "1lawyer.O.Email",
                    "FieldValue": result.l_email if result.l_email is not None else results2.AttorneyAgentEmail
                },
                {
                    "FieldName": "1ben.AlienRegNumComb",
                    "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
                },
                {
                    "FieldName": "USIMM82468.chk7.41.0",
                    "FieldValue": bit_ans(result.p_H1BDependentEmployer)
                },
                {
                    "FieldName": "USIMM82468.chk7.41.1",
                    "FieldValue": bit_ans(result.p_PetitionerWillfulViolator)
                },



                ############### ppppppp############

                {
                    "FieldName": "1contact.EO.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": result.Address1 if result.Address1 else results2.PetitionerContactAddress1
                },
                {
                    "FieldName": "1contact.EO.Addr4",
                    "FieldValue": iff(result.AddressUnitNumber)
                },
                {
                    "FieldName": "1contact.EO.Phone",
                    "FieldValue": result.PhoneNumber if result.PhoneNumber is not None else results2.PetitionerContactPhoneNumber
                },
                {
                    "FieldName": "1contact.EO.Mobile",
                    "FieldValue": iff(result.MobilePhone)
                },
                {
                    "FieldName": "1contact.EO.Email",
                    "FieldValue": result.Email if result.Email is not None else results2.PetitionerContactEmail
                },
                {
                    "FieldName": "1contact.SEmp.TaxID",
                    "FieldValue": result.FederalEmployerId.replace('-', '') if result.FederalEmployerId is not None else str(results2.FEIN).replace('-', '')
                },
                {
                    "FieldName": "USIMM82468.txt1.62",
                    "FieldValue": 1
                },
                {
                    "FieldName": "1ben.LName",
                    "FieldValue": iff(result.b_lastname)
                },
                {
                    "FieldName": "1ben.FName",
                    "FieldValue": iff(result.b_firstname)
                },
                {
                    "FieldName": "1ben.AliasLName",
                    "FieldValue": iff(result.OtherLastName1)
                },
                {
                    "FieldName": "1ben.AliasFName",
                    "FieldValue": iff(result.OtherFirstName1)
                },
                {
                    "FieldName": "1ben.AliasMName",
                    "FieldValue": iff(result.OtherMiddleName1)
                },
                {
                    "FieldName": "1ben.SSNComb",
                    "FieldValue": clean_num(result.SSNNumber)
                },
                {
                    "FieldName": "1ben.BP.Country",
                    "FieldValue": iff(result.BirthCountry)
                },

                {
                    "FieldName": "1ben.GOV.ID",
                    "FieldValue": iff(result.PassportNumber)
                },
                {
                    "FieldName": "1ben.GOV.IDIssueDate",
                    "FieldValue": change_date(result.pp_ValidFrom)
                },
                {
                    "FieldName": "1ben.GOV.IDExpire",
                    "FieldValue": change_date(most_recent_entry_rec.ValidTo) 
                },
                {
                    "FieldName": "1ben.CurrentStayExpiry",
                    "FieldValue": change_date(most_recent_entry_rec.I94ExpirationDate)
                },
                {
                    "FieldName": "User.D937.SEVISNumber",
                    "FieldValue": iff(result.SevisNumber1)
                },
                {
                    "FieldName": "1ben.FilingOtherPetitions",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "USIMM82468.chk1.10.5",
                    "FieldValue": 'No'
                },
                {
                    "FieldName": "USIMM82468.chk1.10.7",
                    "FieldValue": 'No' if not result.ben_mari_stat.lower() == 'married' else ''
                },

                {
                    "FieldName": "USIMM82468.chk1.09",
                    "FieldValue": 'Yes' if int(result.passport_validity) > 0 else 'No'
                },
                {
                    "FieldName": "1ben.PendingProceedings",
                    "FieldValue": bit_ans(result.IsInRemovalProceeding)
                },

                {
                    "FieldName": "1ben.EAD.ID",
                    "FieldValue": iff(result.EadNumber)
                },
                {
                    "FieldName": "1ben.H.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(ben_cur_emp.Address1)
                },
                # Part 4
                {
                    "FieldName": "1ben.F.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(perm_foreign_address.Address1)
                },
                {
                    "FieldName": "1ben.F.Addr4",
                    "FieldValue": iff(perm_foreign_address.AddressUnitNumber)
                },
                {
                    "FieldName": "1ben.F.City",
                    "FieldValue": iff(perm_foreign_address.City)
                },
                {
                    "FieldName": "1ben.F.State",
                    "FieldValue": iff(perm_foreign_address.StateProvince)
                },
                {
                    "FieldName": "1ben.F.ForeignRoute",
                    "FieldValue": iff(perm_foreign_address.PostalZipCode)
                },
                {
                    "FieldName": "1ben.F.Country",
                    "FieldValue": iff(perm_foreign_address.Country)
                },
                {
                    "FieldName": "USIMM82468.txt1.59.1",
                    "FieldValue": iff(result.LCAJobTitle)
                },
                {
                    "FieldName": "USIMM82468.txt1.59.0",
                    "FieldValue": iff(result.LCAProjectNumber)
                },

                {
                    "FieldName": "1ben.M.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": f'{iff(result.LCAWorkLocation1_Address1)} {iff(result.LCAWorkLocation1_Address2)}'
                },
                {
                    "FieldName": "1ben.M.City",
                    "FieldValue": iff(result.LCAWorkLocation1_City) + '   -   See attached LCA for additional work locations' if (result.LCAWorkLocation1_Address1) else ''
                },
                {
                    "FieldName": "1ben.M.State",
                    "FieldValue": iff(result.LCAWorkLocation1_State)
                },
                {
                    "FieldName": "1ben.M.Zip",
                    "FieldValue": iff(result.LCAWorkLocation1_ZipCode)
                },
                {
                    "FieldName": "USIMM82468.txt1.78",
                    "FieldValue": iff(result.LCAWorkLocation1_PrevailingWageRate)
                },
                {
                    "FieldName": "USIMM82468.txt1.79",
                    "FieldValue": iff(result.LCAWorkLocation1_PrevailingWageRateType)
                },
                {
                    "FieldName": "User.D937.OtherCompensation.multiline.1",
                    "FieldValue": 'STANDARD COMPANY BENEFITS'
                },
                {
                    "FieldName": "USIMM82468.chk2.05",
                    "FieldValue": '1' if result.IsEarItarRequired == True else '2' if result.IsEarItarRequired == False else ''
                },
                {
                    "FieldName": "USIMM82468.txt1.12",
                    "FieldValue": change_date(result.LCAIntendedEmploymentStartDate)
                },
                {
                    "FieldName": "USIMM82468.txt1.14",
                    "FieldValue": change_date(result.LCAIntendedEmploymentEndDate)
                },
                {
                    "FieldName": "1lawfirm.O.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": result.l_address1 if result.l_address1 is not None else results2.AttorneyAgentAddress1
                }

            ]

            # logics for H Classification Supplement to Form I-129 page

            if result.ProjectPetitionName:
                word = result.ProjectPetitionName.lower().strip().split()[0]

                if word == 'h-1b':
                    value = 1
                elif word == 'h-1b1':
                    value = 2
                elif word == 'h-1b2':
                    value = 3
                elif word == 'h-1b4':
                    value = 4
                elif word == 'h-2a':
                    value = 5
                elif word == 'h-2b':
                    value = 6
                elif result.ProjectPetitionName.lower().__contains__('h-3 trainee'):
                    value = 7
                elif result.ProjectPetitionName.lower().__contains__('h-3 special'):
                    value = 8
                else:
                    value = ''

                data_dict.append(
                    {
                        "FieldName": "USIMM82468.chk10.26",
                        "FieldValue": value
                    }
                )

            if True:
                # under a condition when H Classification Supplement to Form I-129 has to populate
                # need to do everything fresh mapping nothing overlapping

                data_dict.extend([

                    {
                        "FieldName": "USIMM82468.txt11.59",
                        "FieldValue": '1'
                    },
                    {
                        "FieldName": "USIMM82468.chk10.27",
                        "FieldValue": 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk10.28",
                        "FieldValue": 'No'
                    },
                    {
                        "FieldName": "1altclient.SEmp.Company",
                        "FieldValue": iff(result.PetitionerName)
                    },

                    {
                        "FieldName": "1ben.FullName",
                        "FieldCalcOverride": True,
                        "FieldValue": (str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)).strip()
                    },
                    {
                        "FieldName": "USIMM82468.txt11.63.0",
                        "FieldValue": (str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)).strip()
                    },
                    {
                        "FieldName": "USIMM82468.txt11.64.0",
                        "FieldValue": change_date(result.InitialHlEntryDate)
                    },
                    {
                        "FieldName": "USIMM82468.chk10.29",
                        "FieldValue": 'No'
                    },
                    {
                        "FieldName": "User.D937.Explanation.multiline.1",
                        "FieldValue": 'N/A'
                    },
                    {
                        "FieldName": "User.D937.ProposedDuties.multiline.1",
                        "FieldValue": 'See attached support statement'
                    },
                    {
                        "FieldName": "User.D937.PresentOccupation.multiline.1",
                        "FieldValue": 'See attached support statement'
                    },
                    {
                        "FieldName": "1authind.Title",
                        "FieldValue": f'{result.LastName if result.LastName else results2.PetitionerContactLastName}, {result.FirstName if result.FirstName else results2.PetitionerContactFirstName}'
                    },
                    {
                        "FieldName": "1altclient.SEmp.Company",
                        "FieldValue": result.PetitionerName if result.PetitionerName else results2.PetitionerName
                    },
                    {
                        "FieldName": "2altclient.SEmp.Company",
                        "FieldValue": result.PetitionerName if result.PetitionerName else results2.PetitionerName
                    },
                    {
                        "FieldName": "USIMM82468.txt11.04",
                        "FieldValue": result.PetitionerName if result.PetitionerName else results2.PetitionerName
                    },
                    {
                        "FieldName": "USIMM82468.chk1.12.0",
                        "FieldValue": 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk1.12.1",
                        "FieldValue": 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk1.12.2",
                        "FieldValue": 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk1.12.3",
                        "FieldValue": 'Yes'
                    }

                ])

            if True:
                # under a condition when H-1B and H-1B1 Data Collection and
                # Filing Fee Exemption Supplement has to populate

                # need to do everything fresh mapping nothing overlapping
                data_dict.extend([
                    {
                        "FieldName": "1contact.SEmp.NAICSComb",
                        "FieldValue": result.p_NaicsCode if result.p_NaicsCode is not None else results2.NAICSCode
                    },
                    {
                        "FieldName": "USIMM82468.chk7.43",
                        "FieldValue": 'Yes' if result.p_HigherEducationInstitution else 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk7.44",
                        "FieldValue": 'Yes' if result.p_NonprofitOrganizationEntity else 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk7.45.0",
                        "FieldValue":  'Yes' if result.p_NonprofitOrganizationEntity else 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk7.45.2",
                        "FieldValue":  'Yes' if result.p_NonprofitGovernmentResearch else 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk7.45.6",
                        "FieldValue": 'Yes' if result.p_PrimarySecondaryEducationInstitution else 'No'
                    },
                    {
                        "FieldName": "USIMM82468.chk7.45.7",
                        "FieldValue": 'Yes' if result.p_NonprofitCurriculumRelatedTraining else 'No'
                    }
                    # {
                    #     "FieldName": "",
                    #     "FieldValue":
                    # },


                ])

            # define category
            project_cat = ''
            if result.ProjectPetitionName:
                word = result.ProjectPetitionName.lower().strip()
                if word.__contains__('h-1b'):
                    if word.__contains__('regular'):
                        project_cat = 'h1-b regular cap'

                    if word.__contains__('master'):
                        project_cat = 'h1-b master cap'

                    if result.PTag1_Val:
                        Ctag1 = result.PTag1_Val.lower().strip()
                        if Ctag1.__contains__('amendment'):
                            if not re.search("extension|ext.|extn.", Ctag1):
                                project_cat = 'h1-b amendment only'
                            else:
                                project_cat = 'h1-b amendment with ext'
                        if Ctag1.__contains__('change of employer'):
                            project_cat = 'h1-b change of employer'
                        if Ctag1.__contains__('change of status'):
                            project_cat = 'h1-b change of status'
                        if re.search("extension|ext.|extn.", Ctag1):
                            project_cat = 'h1-b ext'

            # logics for H-1B and H-1B1 Data Collection
            value = ''
            if project_cat == 'h1-b amendment only':
                value = 'Yes'
            else:
                value = 'No'

            data_dict.append(

                {
                    "FieldName": "USIMM82468.chk7.45.4",
                    "FieldValue": value
                }
            )

            value = ''
            if project_cat == 'h1-b regular cap':
                value = 1
            elif project_cat == 'h1-b master cap':
                value = 2
            elif word.__contains__('h-1b') and re.search("change of employer|Extension of Status|Amendment|change of status", word, re.IGNORECASE):
                value = 4

                # the below applies if s3 1d goes cap exempt
                data_dict.extend([

                    {
                        "FieldName": "USIMM82468.chk7.01",
                        "FieldValue": '1' if result.p_HigherEducationInstitution else ''
                    },
                    {
                        "FieldName": "USIMM82468.chk7.02",
                        "FieldValue": '1' if result.p_NonprofitOrganizationEntity else ''
                    },
                    {
                        "FieldName": "USIMM82468.chk7.03",
                        "FieldValue": '1' if result.p_NonprofitGovernmentResearch else ''
                    },
                    # { default skip this question
                    #     "FieldName": "USIMM82468.chk7.04",
                    #     "FieldValue": '' #skip
                    # },

                    # { default skip this question
                    #     "FieldName": "USIMM82468.chk7.06",
                    #     "FieldValue":
                    # },

                    {
                        "FieldName": "USIMM82468.chk7.08",
                        "FieldValue": '1' if result.p_PetGUAMCNMICapExempt else ''
                    }
                ])

                if project_cat in ('h1-b change of employer', 'h1-b ext', 'h1-b amendment only', 'h1-b amendment with ext'):

                    data_dict.append({
                        "FieldName": "USIMM82468.chk7.05",
                        "FieldValue": '1'
                    })

                if project_cat == 'h1-b change of status':

                    data_dict.append({
                        "FieldName": "USIMM82468.chk7.07",
                        "FieldValue": '1'
                    })

            data_dict.append(
                {
                    "FieldName": "USIMM82468.chk7.46",
                    "FieldValue": value
                }
            )

            value = ''
            if project_cat == 'h1-b regular cap':
                value = 'Yes'
            elif project_cat == 'h1-b master cap':
                value = 'Yes'
            elif project_cat == 'h1-b change of employer':
                value = 'No'
            elif project_cat == 'h1-b ext':
                value = 'No'
            elif project_cat == 'h1-b amendment only':
                value = 'No'
            elif project_cat == 'h1-b amendment with ext':
                value = 'No'
            elif project_cat == 'h1-b change of status':
                value = 'Yes'
            data_dict.append(
                {
                    "FieldName": "USIMM82468.chk1.10.13",
                    "FieldValue": value
                }
            )

            value = ''
            if project_cat == 'h1-b regular cap':
                value = 'No'
            elif project_cat == 'h1-b master cap':
                value = 'No'
            elif project_cat == 'h1-b change of employer':
                value = 'No'
            elif project_cat == 'h1-b ext':
                value = 'Yes'
            elif project_cat == 'h1-b amendment only':
                value = 'Yes'
            elif project_cat == 'h1-b amendment with ext':
                value = 'Yes'
            elif project_cat == 'h1-b change of status':
                value = ''
            data_dict.append(
                {
                    "FieldName": "USIMM82468.chk1.10.19",
                    "FieldValue": value
                }
            )

            if result.JVisaStatusValidFromDate and result.JVisaStatusValidFromDate:
                data_dict.append(

                    {
                        "FieldName": "USIMM82468.txt1.54",
                        "FieldValue": f"{change_date(result.JVisaStatusValidFromDate)} to {change_date(result.JVisaStatusExpirationDate)}"
                    },
                )

            if project_cat == 'h1-b master cap' and ben_high_edu.IsUSDegree:
                data_dict.extend([

                    {
                        "FieldName": "USIMM82468.txt7.01",
                        "FieldValue": iff(ben_high_edu.CollegeUniversityName)
                    },
                    {
                        "FieldName": "USIMM82468.txt7.02",
                        "FieldValue": change_date(ben_high_edu.DegreeReceivedDate) 
                    },
                    {
                        "FieldName": "USIMM82468.txt7.03",
                        "FieldValue": iff(ben_high_edu.DegreeType)
                    },
                    {
                        "FieldName": "USIMM82468.txt7.04",
                        "FieldValue": iff(ben_high_edu.Address1)
                    },
                    {
                        "FieldName": "USIMM82468.txt7.05",
                        "FieldValue": iff(ben_high_edu.AddressUnitNumber)
                    },
                    {
                        "FieldName": "USIMM82468.txt7.06",
                        "FieldValue": iff(ben_high_edu.City)
                    },
                    {
                        "FieldName": "USIMM82468.txt7.07",
                        "FieldValue": iff(ben_high_edu.StateProvince)
                    },
                    {
                        "FieldName": "USIMM82468.txt7.08",
                        "FieldValue": iff(ben_high_edu.PostalZipCode)
                    }
                ])

            if result.ProjectPetitionName:
                if result.PTag1_Val:
                    value = ''

                    if result.ProjectPetitionName.lower().__contains__('h-1b'):
                        if result.PTag1_Val.__contains__('new employment'):
                            value = 1
                        elif re.search('extn|extension|ext.|extn.', result.PTag1_Val, re.IGNORECASE):
                            value = 2
                        elif re.search('amendment with ext', result.PTag1_Val, re.IGNORECASE):
                            value = 3
                        elif re.search('change of employer', result.PTag1_Val, re.IGNORECASE):
                            value = 5
                        elif re.search('amendment', result.PTag1_Val, re.IGNORECASE):
                            if not re.search('extn|ext.|extension', result.PTag1_Val, re.IGNORECASE):
                                value = 6
                        data_dict.append(
                            {
                                "FieldName": "USIMM82468.chk1.03",
                                "FieldValue": value
                            }
                        )

            if result.p_EmployeeCountUS:
                if int(result.p_EmployeeCountUS) <= 25:
                    data_dict.append(

                        {
                            "FieldName": "USIMM82468.chk7.45.10",
                            "FieldValue": 'Yes'
                        }
                    )
                else:
                    data_dict.extend([

                        {
                            "FieldName": "USIMM82468.chk7.41.5",
                            "FieldValue": 'Yes'
                        },
                        {
                            "FieldName": "USIMM82468.chk7.41.6",
                            "FieldValue": 'Yes' if result.p_Over50PercentEEsinH1BL1AL1BStatus else 'No'
                        },
                        {
                            "FieldName": "USIMM82468.chk7.45.10",
                            "FieldValue": 'No'
                        }
                    ])

            # population based on bigger logics

            if ben_high_edu:
                value = ''
                if ben_high_edu.DegreeType:
                    deg_type = ben_high_edu.DegreeType.lower().strip()

                    if deg_type.__contains__('no diploma'):
                        value = 1
                    if deg_type.__contains__('high school'):
                        value = 2
                    if deg_type.__contains__('associate'):
                        value = 5
                    if deg_type.__contains__('bachelor'):
                        value = 6
                    if deg_type.__contains__('master'):
                        value = 7
                    if deg_type.__contains__('professional'):
                        value = 8
                    if deg_type.__contains__('doctorate'):
                        value = 9
                elif ben_high_edu.ProgramLength:
                    if ben_high_edu.ProgramLength < 1:
                        value = 3
                    if ben_high_edu.ProgramLength >= 1:
                        value = 4

                if value in (7, 8, 9):
                    data_dict.extend([
                        {
                            "FieldName": "USIMM82468.chk7.41.4",
                            "FieldValue": 'Yes'
                        },
                        {
                            "FieldName": "USIMM82468.chk7.41.2",
                            "FieldValue": 'Yes'
                        }
                    ])

                else:
                    data_dict.append(
                        {
                            "FieldName": "USIMM82468.chk7.41.4",
                            "FieldValue": 'No'
                        }
                    )

                data_dict.extend([
                    {
                        "FieldName": "USIMM82468.chk7.42",
                        "FieldValue": value
                    },
                    {
                        "FieldName": "1ben.Educ1.Major",
                        "FieldValue": iff(ben_high_edu.FieldOfStudy)
                    }
                ])

                if ben_high_edu.AddressUnitType:
                    word = ben_high_edu.AddressUnitType.lower().strip()
                    value = ''
                    if word[0] == 'a':
                        value = 1
                    elif word[0] == 's':
                        value = 2
                    elif word[0] == 'f':
                        value = 3

                    data_dict.extend([
                        {
                            "FieldName": "USIMM82468.chk7.47",
                            "FieldValue": value
                        },
                    ])

            if ben_cur_emp:

                if ben_cur_emp.SalaryAmount and ben_cur_emp.SalaryPer:
                    data_dict.extend([
                        {
                            "FieldName": "",
                            "FieldValue": f'{iff(ben_cur_emp.SalaryAmount)} per {iff(ben_cur_emp.SalaryPer)}'
                        },
                    ])

                if ben_cur_emp.CurrentAnnualSalary:
                    value = 'Yes' if int(ben_cur_emp.CurrentAnnualSalary) >= 60000 else 'No' if int(
                        ben_cur_emp.CurrentAnnualSalary) < 60000 else ''
                    data_dict.extend([
                        {
                            "FieldName": "USIMM82468.chk7.41.3",
                            "FieldValue": value
                        },
                        {
                            "FieldName": "USIMM82468.chk7.41.2",
                            "FieldValue": 'Yes'
                        },]
                    )

            # print(data_dict)
            # quit()

            params = {
                "HostFormOnQuik": True,
                "FormFields": data_dict,
                "QuikFormID": "82468",
                "PrintEditablePDF": True
            }

            # return False
            data_json = json.dumps(params)

            response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)

            # response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/html', headers=headersAPI, data=data_json)

            api_response = response.json()

            # print(api_response)
            # quit()

            pdf_base64 = api_response['ResultData']['PDF']
            with open('Form I-129.pdf', 'wb') as pdf:
                pdf.write(base64.b64decode(pdf_base64))


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
                    "FieldValue": ('Form I-129 - '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)+', '+str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_middlename if result.b_middlename is not None else iff(results2.BeneficiaryMiddleName))).strip()
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

            response = requests.post(
                'https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)

            api_response = response.json()

            # print(api_response)
            # print(quit())

            pdf_base64 = api_response['ResultData']['PDF']
            # print()
            with open('Form G-28_for_I-129.pdf', 'wb') as pdf:
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

    shutil.move(op.join(parent_dir, 'Form G-28_for_I-129.pdf'),
                op.join(target_dir, 'Form G-28_for_I-129.pdf'))
    
    shutil.move(op.join(parent_dir, 'Form I-129.pdf'),
                op.join(target_dir, 'Form I-129.pdf'))


    print("Getting supporting docs from sharepoint..")
    get_files(
        site_url=f"https://immilytics.sharepoint.com/sites/{data_dict['beneficiary_xref']}-{data_dict['last_name']}{data_dict['first_name']}",
        sp_folder=f"Shared Documents/Document Library/Project Specific Supporting Docs/{data_dict['project_xref']}",
        dwd_dir = support_doc_dir)
    
    # wait to download file 
    time.sleep(10)

    pdfs.append(op.join(target_dir, 'Form G-28_for_I-129.pdf'))
    pdfs.append(op.join(target_dir, 'Form I-129.pdf'))
   

    if op.exists(op.join(support_doc_dir, 'ETA 9089.pdf')):
        pdfs.append(op.join(support_doc_dir, 'ETA 9089.pdf'))
    

    pdfs.append(op.join(support_doc_dir, 'I-129 Supporting Docs Final Packet.pdf'))

    os.chdir(parent_dir)

    indiv_finals_dir = op.join(target_dir,"indiv_finals_dir")
    
    if not op.exists(indiv_finals_dir):
        os.mkdir(indiv_finals_dir)
    qpdf_merger(pdfs, indiv_finals_dir, formtype)
    time.sleep(5)

    # removing individual files
    os.remove(op.join(target_dir, 'Form G-28_for_I-129.pdf'))
    os.remove(op.join(target_dir, 'Form I-129.pdf'))

    # qpdf_merger(pdfs, target_dir, formtype)


