import os,json,shutil,glob,requests,base64
import os.path as op,re,time

def generate_131(ProjectID,formtype,other_objects):

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
    target_dir = other_objects['target_dir']
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

            ben_gender = ''
            if result.ben_gender.lower().strip() == 'male':
                ben_gender = '1'
            elif result.ben_gender.lower().strip() == 'female':
                ben_gender = '2'

            data_dict = [
                {
                    "FieldName": "1ben.H.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(current_res_address.Address1)
                },
                {
                    "FieldName": "1lawyer.G28Attached",
                    "FieldValue": 1
                },
                {
                    "FieldName": "1lawyer.LicNum",
                    "FieldValue": iff(result.l_BarNumber)
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
                    "FieldName": "1ben.H.Country",
                    "FieldValue": iff(current_res_address.Country)
                },
                {
                    "FieldName": "1ben.AlienRegNumComb",
                    "FieldValue": iff(result.AlienNumber1)
                },
                {
                    "FieldName": "1ben.BP.Country",
                    "FieldValue": iff(result.BirthCountry)
                },
                {
                    "FieldName": "1ben.Citizenship",
                    "FieldValue": result.CitizenshipCountry if result.CitizenshipCountry is not None else results2.BeneficiaryCountryofCitizenship
                },
                {
                    "FieldName": "1ben.CurrentStatus",
                    "FieldValue": iff(most_recent_entry_rec.I94StatusType)
                },
                {
                    "FieldName": "1ben.DOB",
                    "FieldValue": result.BirthDate.strftime('%m/%d/%Y') if result.BirthDate is not None else results2.BeneficiaryDateofBirth.strftime('%m/%d/%Y')
                },
                {
                    "FieldName": "1ben.SSNComb",
                    "FieldValue": clean_num(result.SSNNumber)
                },

                {
                    "FieldName": "1ben.O.Phone",
                    "FieldValue": iff(result.ben_WorkPhone)
                },
                {
                    "FieldName": "1ben.Gender",
                    "FieldValue": iff(ben_gender)
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
                    "FieldName": "1lawfirm.O.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": result.l_address1 if result.l_address1 else results2.AttorneyAgentAddress1
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
                    "FieldName": "1lawyer.O.Email",
                    "FieldValue": result.l_email if result.l_email is not None else results2.AttorneyAgentEmail
                },
                {
                    "FieldName": "1ben.H.Attn",
                    "FieldValue": f'{iff(result.b_firstname)}, {iff(result.b_lastname)}'
                },
                {
                    "FieldName": "USIMM82537.txt1.52",
                    "FieldValue": change_date(most_recent_entry_rec.TentativeDepartureDate)
                },
                {
                    "FieldName": "USIMM82537.txt1.56",
                    "FieldValue": str(most_recent_entry_rec.trip_length) if most_recent_entry_rec.TentativeArrivalDate and most_recent_entry_rec.TentativeDepartureDate else ''
                },
                {
                    "FieldName": "USIMM82537.chk1.10",
                    "FieldValue": 'Yes' if result.IsInRemovalProceeding else 'No'
                },
                {
                    "FieldName": "USIMM82537.txt1.81",
                    "FieldValue": iff(result.RemovalProceedingJurisdiction)
                },
                {  # p3 4a
                    "FieldName": "USIMM82537.chk1.09",
                    "FieldValue": 'Yes' if (result.RefugeeTravelDocumentIssueDate or result.ReEntryPermitIssueDate) else 'No'
                },
                {
                    "FieldName": "USIMM82537.txt1.82",
                    "FieldValue": change_date(result.RefugeeTravelDocumentIssueDate) if result.RefugeeTravelDocumentIssueDate else change_date(result.ReEntryPermitIssueDate)
                },
                {
                    "FieldName": "USIMM82537.txt1.86",
                    "FieldValue": 'See Attached.' if (result.RefugeeTravelDocumentIssueDate or result.ReEntryPermitIssueDate) else ''
                },

                {
                    "FieldName": "USIMM82537.chk1.21",
                    "FieldValue": '1'
                },
                {
                    "FieldName": "1lawyer.O.PhoneExt",
                    "FieldValue": result.l_PhoneNumberExt if result.l_PhoneNumberExt else results2.AttorneyAgentPhoneNumber
                },

                {
                    "FieldName": "User.D937.PurposeOfTrip.multiline.1",
                    "FieldValue": iff(most_recent_entry_rec.TravelPurpose)
                },
                {
                    "FieldName": "User.D937.CountriesIntendToVisit.multiline.1",
                    "FieldValue": 'France , Germany ; Spain ' #', '.join(result.VisitingCountries.split(';')) if result.VisitingCountries else ''
                },
               
                {
                    "FieldName": "USIMM82537.chk1.26",
                    "FieldValue": '2'
                },
                # {
                #     "FieldName": "",
                #     "FieldValue":
                # },


            ]

            # population based on bigger logics
            p2_1a = ''
            p2_1b = ''
            p2_1c = ''
            if result.PTag3_Val:
                value = ''
                PTag3_Val = result.PTag3_Val.lower().strip()

                # p2 1a
                if re.search("reentry|re-entry",PTag3_Val):
                    value = 1
                    p2_1a = 'checked'
                # p2 1b
                elif re.search("refugee ead",PTag3_Val):
                    value = 2
                    p2_1b = 'checked'
                    # if p2 1b is checked the beloe segments will be populated in p6

                # p2 1c
                elif False:
                    p2_1c = 'checked'

                # p2 1d
                elif (re.search("advance parole",PTag3_Val)) and (US_keyword.fullmatch(current_res_address.Country)):
                    value = 4

                # p2 1e
                elif (re.search("advance parole",PTag3_Val)) and not (US_keyword.fullmatch(current_res_address.Country)):
                    value = 5

                data_dict.append(
                    {
                        "FieldName": "USIMM82537.chk1.07",
                        "FieldValue": value
                    })

            if (p2_1b == 'checked') or (p2_1c == 'checked') :
                # if True:
                data_dict.extend([
                    {
                        "FieldName": "USIMM82537.txt1.19",
                        "FieldValue": iff(result.RefugeeOrAsyleeCountry)
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.0",
                        "FieldValue": 'Yes' if result.PlanningToTravelToRefugeeOrAsyleeCountry else 'No'
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.3",
                        "FieldValue": 'Yes' if result.ReturnedToRefugeeOrAsyleeCountry else 'No'
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.6",
                        "FieldValue": 'Yes' if result.AppliedOrRenewedPassportOrEntryPermitToRefugeeOrAsyleeCountry else 'No'
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.10",
                        "FieldValue": 'Yes' if result.AppliedOrReceivedBenefitsFromRefugeeOrAsyleeCountry else 'No'
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.11",
                        "FieldValue": 'Yes' if result.AppliedOrRenewedPassportOrEntryPermitToRefugeeOrAsyleeCountry else 'No'
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.12",
                        "FieldValue": 'Yes' if result.AcquiredNewNationality else 'No'
                    },
                    {
                        "FieldName": "USIMM82537.chk1.25.13",
                        "FieldValue": 'Yes' if result.BeenGrantedAsyleeOrRefugeeStatus else 'No'
                    }])

            if (result.TotalTimeAbroadSincePermanentUSResidence) and (p2_1a=="checked"):
                value = ''
                if result.TotalTimeAbroadSincePermanentUSResidence == 'less than 6 months':
                    value = 1

                elif result.TotalTimeAbroadSincePermanentUSResidence == '6 months to 1 year':
                    value = 2

                elif result.TotalTimeAbroadSincePermanentUSResidence == '1 to 2 years':
                    value = 3

                elif result.TotalTimeAbroadSincePermanentUSResidence == '2 to 3 years':
                    value = 4

                elif result.TotalTimeAbroadSincePermanentUSResidence == '3 to 4 years':
                    value = 5

                elif result.TotalTimeAbroadSincePermanentUSResidence == 'more than 4 years':
                    value = 6

                data_dict.extend([
                    {
                        "FieldName": "USIMM82537.chk1.23",
                        "FieldValue": value
                    },
                     {
                    "FieldName": "USIMM82537.chk1.24",
                    "FieldValue": 'Yes' if result.FiledFederalIncomeTaxReturn else 'No'
                },])

            # print(data_dict)
            # quit()

            params = {
                "HostFormOnQuik": True,
                "FormFields": data_dict,
                "QuikFormID": "82537",
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
            with open('Form I-131.pdf', 'wb') as pdf:
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
                "FieldValue": ('Form I-131 - '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)+', '+str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_middlename if result.b_middlename is not None else iff(results2.BeneficiaryMiddleName))).strip()
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
                "FieldName": "1ben.MName",
                "FieldValue": iff(result.b_middlename)
            },
            {
                "FieldName": "1ben.SEmp.Company",
                "FieldValue": '' #result.PetitionerName if result.PetitionerName is not None else results2.PetitionerName
            },
            {
                "FieldName": "1ben.SignTitle",
                "FieldValue": '' #result.JobTitle if result.JobTitle is not None else results2.JobTitle
            },
            {
                "FieldName": "1ben.M.Phone",
                "FieldValue": iff(result.ben_WorkPhone) #result.PhoneNumber if result.PhoneNumber is not None else results2.PetitionerPhone
            },
            {
                "FieldName": "1ben.M.Mobile",
                "FieldValue": iff(result.b_Mobile)
            },
            {
                "FieldName": "1ben.M.Email",
                "FieldValue": iff(result.ben_WorkEmail)
            },
            {
                "FieldName": "1ben.M.Addr123",
                "FieldCalcOverride": True,
                "FieldValue": result.Address1 if result.Address1 is not None else results2.PetitionerAddress1
            },
            {
                "FieldName": "1ben.M.Addr4",
                "FieldValue": mailing_address.Address1 if mailing_address.Address1 is not None else results2.BeneficiaryAddress1
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
                "FieldName": "1ben.M.Zip",
                "FieldValue": mailing_address.PostalZipCode if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.M.Country",
                "FieldValue": iff(mailing_address.Country)
            },
            {
                "FieldName": "User.D937.AttorneyEligiblePracticeLawIn",
                "FieldValue": "1"
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
                "FieldValue": 1
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

            api_response = response.json()

            # print(api_response)
            # print(quit())

            pdf_base64 = api_response['ResultData']['PDF']
            # print()
            with open('Form G-28_for_I-131.pdf', 'wb') as pdf:
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

    shutil.move(op.join(parent_dir, 'Form G-28_for_I-131.pdf'),
                op.join(target_dir, 'Form G-28_for_I-131.pdf'))
    
    shutil.move(op.join(parent_dir, 'Form I-131.pdf'),
                op.join(target_dir, 'Form I-131.pdf'))


    print("Getting supporting docs from sharepoint..")
    get_files(
        site_url=f"https://immilytics.sharepoint.com/sites/{data_dict['beneficiary_xref']}-{data_dict['last_name']}{data_dict['first_name']}",
        sp_folder=f"Shared Documents/Document Library/Project Specific Supporting Docs/{data_dict['project_xref']}",
        dwd_dir = support_doc_dir)
    
    # wait to download file 
    time.sleep(10)

    pdfs.append(op.join(target_dir, 'Form G-28_for_I-131.pdf'))
    pdfs.append(op.join(target_dir, 'Form I-131.pdf'))
   

    if op.exists(op.join(support_doc_dir, 'ETA 9089.pdf')):
        pdfs.append(op.join(support_doc_dir, 'ETA 9089.pdf'))
    

    pdfs.append(op.join(support_doc_dir, 'I-131 Supporting Docs Final Packet.pdf'))

    os.chdir(parent_dir)

    indiv_finals_dir = op.join(target_dir,"indiv_finals_dir")
    
    if not op.exists(indiv_finals_dir):
        os.mkdir(indiv_finals_dir)
    qpdf_merger(pdfs, indiv_finals_dir, formtype)
    time.sleep(5)

    # removing individual files
    os.remove(op.join(target_dir, 'Form G-28_for_I-131.pdf'))
    os.remove(op.join(target_dir, 'Form I-131.pdf'))

    # qpdf_merger(pdfs, target_dir, formtype)

