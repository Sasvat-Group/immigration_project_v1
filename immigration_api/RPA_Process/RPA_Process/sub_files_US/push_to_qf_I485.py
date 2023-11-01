import os
import os.path as op
import json
import shutil
import glob
import requests
import base64
import re
import time


def generate_485(ProjectID, formtype, other_objects):

    mailing_address = other_objects['mailing_address']
    current_res_address = other_objects['current_res_address']
    last_perm_address_abroad = other_objects['last_perm_address_abroad']
    perm_foreign_address = other_objects['perm_foreign_address']
    mail_addr_vs_phys_addr = other_objects['mail_addr_vs_phys_addr']
    marriage_history = other_objects['marriage_history']
    ben_high_edu = other_objects['ben_high_edu']
    ben_all_edu = other_objects['ben_all_edu']
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
    clean_price = other_objects['clean_price']
    US_keyword = other_objects['US_keyword']
    results2 = other_objects['results2']
    clean_num = other_objects['clean_num']


    # for sharepoint activities
    get_files = other_objects['get_files']
    download_files = other_objects['download_files']
    upload_to_sharepoint = other_objects['upload_to_sharepoint']
   

    if result:

        ben_father_mname = ''
        ben_father_fname = ''
        ben_father_lname = ''
        ben_mot_fname = ''
        ben_mot_lname = ''
        ben_mot_mname = ''
        father_data = ''
        mother_data = ''

        for member in ben_family:
            if member.Relation.lower().__contains__('father'):
                ben_father_fname = member.FirstName
                ben_father_lname = member.LastName
                ben_father_mname = member.MiddleName

            if member.Relation.lower().__contains__('mother'):
                ben_mot_fname = member.FirstName
                ben_mot_lname = member.LastName
                ben_mot_mname = member.MiddleName

        # new cond only for children no other conds
        dependents = cursor.execute('''select * from [dbo].[Beneficiary] where PrimaryBeneficiaryID = '{}'  and ( lower(RelationType) in('child','son','daughter','biological son','biological daughter','biological child'))
            '''.format(result.BeneficiaryID)).fetchall()

        result_priority_category_chkbox_val = ''
        if str(result.ProjectPriorityCategory) in ["EB2", "EB-2", "Employment-Based 2nd", "Employment Based 2nd", "203(b)(2)"]:
            result_priority_category_chkbox_val = 4
        if str(result.ProjectPriorityCategory) in ["EB3", "EB-3", "Employment-Based 3rd", "Employment Based 3rd", "203(b)(3)(A)(ii)"]:
            result_priority_category_chkbox_val = 5

        # print(str(result.ProjectPriorityCategory), result_priority_category_chkbox_val)
        # quit()

        part_4_checkbox_text = perm_foreign_address.AddressUnitType if str(
            mailing_address.Country).lower() in ('usa', 'u.s.a', 'america', 'united states of america') else ''

        result_l_address1_chkbox_val = ''
        if result.l_addressunittype and len(result.l_addressunittype) > 0:
            if str(result.l_addressunittype).lower()[0] == 'a':
                result_l_address1_chkbox_val = 1
            elif str(result.l_addressunittype).lower()[0] == 's':
                result_l_address1_chkbox_val = 2
            elif str(result.l_addressunittype).lower()[0] == 'f':
                result_l_address1_chkbox_val = 3

        isspouseinmilitary = ''
        if result.IsSpouseCurrentMemberOfUSArmedForcesOrCoastGuard == True:
            isspouseinmilitary = 'Yes'
        elif result.IsSpouseCurrentMemberOfUSArmedForcesOrCoastGuard == False:
            isspouseinmilitary = 'No'
        else:
            isspouseinmilitary = '1'

        ben_gender = ''
        if result.ben_gender.lower().strip() == 'male':
            ben_gender = '1'
        elif result.ben_gender.lower().strip() == 'female':
            ben_gender = '2'

        ethnicity = ''
        if result.Ethnicity:
            word = result.Ethnicity.lower().strip()
            if word.__contains__('hispanic'):
                ethnicity = '1'
            else:
                ethnicity = '2'

        eye_color = ''
        if result.EyeColor:
            word = result.EyeColor.lower()
            if word.__contains__('black'):
                eye_color = 6
            elif word.__contains__('blue'):
                eye_color = 2
            elif word.__contains__('brown'):
                eye_color = 1
            elif word.__contains__('gray'):
                eye_color = 5
            elif word.__contains__('green'):
                eye_color = 3
            elif word.__contains__('hazel'):
                eye_color = 4
            elif word.__contains__('marron'):
                eye_color = 7
            elif word.__contains__(''):
                eye_color = 8
            else:
                eye_color = 0

        hair_color = ''
        if result.HairColor:
            word = result.HairColor.lower()
            if re.search('bald|no hair', word):
                hair_color = 8
            elif word.__contains__('black'):
                hair_color = 1
            elif word.__contains__('blond'):
                hair_color = 3
            elif word.__contains__('brown'):
                hair_color = 2
            elif re.search('gr[ea]y', word):
                hair_color = 4
            elif word.__contains__('red'):
                hair_color = 6
            elif word.__contains__('sandy'):
                hair_color = 7
            elif word.__contains__('white'):
                hair_color = 5
            else:
                hair_color = 0

        ben_mari_stat = ''
        if result.ben_mari_stat:
            word = result.ben_mari_stat.lower().strip()
            if word.__contains__('single'):
                ben_mari_stat = 1
            elif word.__contains__('married'):
                ben_mari_stat = 2
            elif word.__contains__('Divorced'):
                ben_mari_stat = 3
            elif word.__contains__('widow'):
                ben_mari_stat = 4
            elif word.__contains__('annul'):
                ben_mari_stat = 5
            elif word.__contains__('Legally Separated'):
                ben_mari_stat = 6
            else:
                ben_mari_stat = ''

        inspect_value = '1' if most_recent_entry_rec.IsInspectedAdmitted else '2' if most_recent_entry_rec.IsInspectedParoled else '3' if (
            most_recent_entry_rec.IsInspectedAdmitted or most_recent_entry_rec.IsInspectedParoled) == False else '0'

        if clean_price(resp_dic.get("92", "")):
            prc = clean_price(resp_dic.get("92", ""))
            if prc <= 27000:
                annual_household_income = 1
            elif prc <= 52000:
                annual_household_income = 2
            elif prc <= 85000:
                annual_household_income = 3
            elif prc <= 141000:
                annual_household_income = 4
            else:
                annual_household_income = 5

        if clean_price(resp_dic.get("94", "")):
            prc = clean_price(resp_dic.get("94", ""))
            if prc <= 18400:
                annual_household_asset = 1
            elif prc <= 136000:
                annual_household_asset = 2
            elif prc <= 321400:
                annual_household_asset = 3
            elif prc <= 707100:
                annual_household_asset = 4
            else:
                annual_household_asset = 5

        if clean_price(resp_dic.get("95", "")):
            prc = clean_price(resp_dic.get("95", ""))
            if prc == 0:
                annual_household_liability = 1
            elif prc <= 10100:
                annual_household_liability = 2
            elif prc <= 57700:
                annual_household_liability = 3
            elif prc <= 186800:
                annual_household_liability = 4
            else:
                annual_household_liability = 5

        data_dict = [

            {
                "FieldName": "1ben.NonImmigExchangeVisitor",
                "FieldValue": bit_ans(resp_dic.get("11", ""))
            },
            {
                "FieldName": "1ben.BeenWeaponsDealer",
                "FieldValue": bit_ans(resp_dic.get("11", ""))
            },
            {
                "FieldName": "1ben.RelatedWithOrg",
                "FieldValue": 'Yes' if len(org_membership) >= 1 else 'No'
            },
            {
                "FieldName": "1ben.UsedWeapon",
                "FieldValue": bit_ans(resp_dic.get("8", ""))
            },
            {
                "FieldName": "1ben.ServedUSMilitary",
                "FieldValue": bit_ans(resp_dic.get("16", ""))
            },
            {
                "FieldName": "1ben.CommunistPartyRelated",
                "FieldValue": bit_ans(resp_dic.get("53", ""))
            },
            {
                "FieldName": "1ben.NaziGovtArmyRelated",
                "FieldValue": bit_ans(resp_dic.get("54", ""))
            },
            {
                "FieldName": "USIMM82483.chk2.44",
                "FieldValue": '1'
            },
            {
                "FieldName": "1ben.WorkedPrison",
                "FieldValue": bit_ans(resp_dic.get("17", ""))
            },
            {
                "FieldName": "1ben.MarriedTimes",
                "FieldValue": len(marriage_history)
            },
            {
                "FieldName": "1ben.Hispanic",
                "FieldValue": (ethnicity)
            },
            {
                "FieldName": "1ben.EyeColor",
                "FieldValue": (eye_color)
            },
            {
                "FieldName": "1ben.HairColor",
                "FieldValue": (hair_color)
            },
            {
                "FieldName": "1ben.Married",
                "FieldValue": iff(ben_mari_stat)
            },

            {
                "FieldName": "1ben.RaceWhite",
                "FieldValue": '1' if str(result.Race).lower().__contains__('white') else ''
            },
            {
                "FieldName": "1ben.RaceAsian",
                "FieldValue": '1' if str(result.Race).lower().__contains__('asian') else ''
            },
            {
                "FieldName": "1ben.RaceBlack",
                "FieldValue": '1' if re.search('black|africa', str(result.Race).lower()) else ''
            },
            {
                "FieldName": "1ben.RaceIndian",
                "FieldValue": '1' if re.search('india|alaska', str(result.Race).lower()) else ''
            },
            {
                "FieldName": "1ben.RacePacIslander",
                "FieldValue": '1' if re.search('pacific|hawai', str(result.Race).lower()) else ''
            },
            {
                "FieldName": "1ben.HeightFeet",
                "FieldValue": iff(result.HeightFeet)
            },
            {
                "FieldName": "1ben.HeightInch",
                "FieldValue": iff(result.HeightInches)
            },
            {
                "FieldName": "1ben.Weight",
                "FieldValue": iff(result.WeightLbs)
            },

            {
                "FieldName": "1lawyer.G28Attached",
                "FieldValue": 1
            },
            {
                "FieldName": "1ben.PermResImmCategory",
                # if str(result.UnderlyingImmigrantClassification).__contains__('140') else ''
                "FieldValue": '6'
            },
            {
                "FieldName": "1ben.LivingChildren",
                "FieldValue": len(dependents)
            },
            {
                "FieldName": "USIMM82483.txt1.09.200",
                "FieldValue": iff(result.b_USCISNumber)
            },
            {
                "FieldName": "1lawyer.ELISNumComb",
                "FieldValue": clean_num(result.l_USCISNumber)
            },
            {
                "FieldName": "1lawyer.LicNum",
                "FieldValue": iff(result.l_BarNumber)
            },
            {
                "FieldName": "1ben.AlienRegNumComb",
                "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
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
                "FieldName": "1ben.DOB",
                "FieldValue": result.BirthDate.strftime('%m/%d/%Y') if result.BirthDate is not None else results2.BeneficiaryDateofBirth.strftime('%m/%d/%Y')
            },
            {
                "FieldName": "1ben.Gender",
                "FieldValue": iff(ben_gender)
            },
            {
                "FieldName": "1ben.BP.City",
                "FieldValue": iff(result.BirthCity)
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
                "FieldName": "1ben.I94.ArrivalCity",
                "FieldValue": iff(most_recent_entry_rec.EntryCity)
            },
            {
                "FieldName": "1ben.I94.ArrivalState",
                "FieldValue": iff(most_recent_entry_rec.EntryState)
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
                "FieldName": "1ben.M.State",
                "FieldValue": mailing_address.StateProvince if str(mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
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
                "FieldName": "1ben.SSNComb",
                "FieldValue": clean_num(result.SSNNumber)
            },
            {
                "FieldName": "1ben.GOV.ID",
                "FieldValue": iff(result.PassportNumber)
            },
            {
                "FieldName": "1ben.GOV.IDExpire",
                "FieldValue": change_date(most_recent_entry_rec.ValidTo)
            },
            {
                "FieldName": "1ben.GOV.IDCountry",
                "FieldValue": iff(result.pp_IssuingCountry)
            },
            {
                "FieldName": "1ben.I94.ArrivalDate",
                "FieldValue": change_date(most_recent_entry_rec.EntryDate)
            },
            {
                "FieldName": "1ben.NonImmigExpiry",
                "FieldValue": most_recent_entry_rec.I94ExpirationDate.strftime('%m/%d/%Y') if str(most_recent_entry_rec.I94StatusType).lower() not in ('j1', 'j2', 'f1', 'f2') else 'N/A'
            },
            {
                "FieldName": "1ben.I94.IDStatus",
                "FieldValue": iff(most_recent_entry_rec.I94StatusType)
            },
            {
                "FieldName": "1ben.CurrentStatus",
                "FieldValue": iff(most_recent_entry_rec.I94StatusType)
            },

            {
                "FieldName": "1ben.AppVisaAbroad",
                "FieldValue": bit_ans(result.IsImmigrantVisaApplicant)
            },
            {
                "FieldName": "1spou.CurrMilitary",
                "FieldValue": iff(isspouseinmilitary)
            },
            {
                "FieldName": "1ben.H.Addr123",
                "FieldCalcOverride": True,
                "FieldValue": iff(current_res_address.Address1)
            },
            {
                "FieldName": "1ben.H.AddrUnitType",
                "FieldValue":  AptSteFlr(current_res_address.AddressUnitType)
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
                "FieldValue": iff(current_res_address.PostalZipCode) if US_keyword.search(current_res_address.Country) else ''
            },
            {
                "FieldName": "1ben.H.ForeignRoute",
                "FieldValue": iff(current_res_address.PostalZipCode) if not US_keyword.search(current_res_address.Country) else ''
            },
            {
                "FieldName": "1ben.H.Country",
                "FieldValue": iff(current_res_address.Country)
            },
            {
                "FieldName": "1ben.H.County",
                "FieldValue": iff(current_res_address.County)
            },
            {
                "FieldName": "1ben.ResidedFrom",
                "FieldValue": change_date(current_res_address.AddressFromDate)
            },


            {
                "FieldName": "1father.LName",
                "FieldValue": iff(ben_father_lname)
            },
            {
                "FieldName": "1father.FName",
                "FieldValue": iff(ben_father_fname)
            },
            {
                "FieldName": "1mother.LName",
                "FieldValue": iff(ben_mot_lname)
            },
            {
                "FieldName": "1mother.FName",
                "FieldValue": iff(ben_mot_fname)
            },


            {
                "FieldName": "1ben.BeenArrested",
                "FieldValue": bit_ans(resp_dic.get("7", ""))
            },
            {
                "FieldName": "1ben.SentencedToProgram",
                "FieldValue": bit_ans(resp_dic.get("28", ""))
            },
            {
                "FieldName": "1ben.InvolvedInTorture",
                "FieldValue": bit_ans(resp_dic.get("1", ""))
            },
            {
                "FieldName": "1ben.InvolvedInKilling",
                "FieldValue": bit_ans(resp_dic.get("14", ""))
            },
            {
                "FieldName": "1ben.InvolvedInSevereInjury",
                "FieldValue": bit_ans(resp_dic.get("13", ""))
            },
            {
                "FieldName": "1ben.CommittedRape",
                "FieldValue": bit_ans(resp_dic.get("5", ""))
            },
            {
                "FieldName": "1ben.DenyingReligiousBeliefs",
                "FieldValue": bit_ans(resp_dic.get("15", ""))
            },
            {
                "FieldName": "1ben.UsedMinorForHostilities",
                "FieldValue": bit_ans(resp_dic.get("56", ""))
            },
            {
                "FieldName": "1lawyer.FullName",
                "FieldValue": f'{result.l_lastname}, {iff(result.l_firstname)}'
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
                "FieldName": "1ben.H.Email",
                "FieldValue": iff(result.ben_WorkEmail)
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
                "FieldValue": AptSteFlr(result_l_address1_chkbox_val)
            },
            {
                "FieldName": "1lawfirm.O.Addr123",
                "FieldValue": result.l_address1 if result.l_address1 is not None else results2.AttorneyAgentAddress1
            },
            {
                "FieldName": "1lawfirm.O.Addr4",
                "FieldValue": result.l_addressunitnumber if result.l_addressunitnumber is not None else results2.AttorneyAgentAddress1
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
                "FieldName": "1ben.AlienRegNumComb",
                "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
            },
            {
                "FieldName": "1ben.DeniedEntry",
                "FieldValue": bit_ans(resp_dic.get("18", ""))
            },
            {
                "FieldName": "1ben.DeniedVisa",
                "FieldValue": bit_ans(resp_dic.get("19", ""))
            },
            {
                "FieldName": "1ben.WorkedWithoutAuth",
                "FieldValue": bit_ans(resp_dic.get("20", ""))
            },
            {
                "FieldName": "1ben.ViolatedTerms",
                "FieldValue": bit_ans(resp_dic.get("10", ""))
            },
            {
                "FieldName": "1ben.PendingProceedings",
                "FieldValue": bit_ans(result.IsInRemovalProceeding)
            },
            {
                "FieldName": "1ben.OrderedToBeDeported",
                "FieldValue": bit_ans(resp_dic.get("21", ""))
            },
            {
                "FieldName": "1ben.DeportedReinstated",
                "FieldValue": bit_ans(resp_dic.get("22", ""))
            },
            {
                "FieldName": "1ben.PermResidentRescind",
                "FieldValue": bit_ans(resp_dic.get("23", ""))
            },
            {
                "FieldName": "1ben.GrantedVoluntaryDeparture",
                "FieldValue": bit_ans(resp_dic.get("24", ""))
            },
            {
                "FieldName": "1ben.DeportReliefApplied",
                "FieldValue": bit_ans(resp_dic.get("25", ""))
            },

            # not done yet cos to know where to pick value
            {
                "FieldName": "1ben.NonImmigExchangeVisitor",
                "FieldValue": bit_ans(result.HasPreviouslyHeldJVisaStatus)
            },
            {
                "FieldName": "1ben.CompliedResidencyReqt",
                "FieldValue": bit_ans(result.JVisaHomeStayRequirementComplied) if result.HasPreviouslyHeldJVisaStatus else ''
            },
            {
                "FieldName": "1ben.GrantedWaiver",
                "FieldValue": bit_ans(result.JVisaHomeStayRequirementWaiverReceived) if result.HasPreviouslyHeldJVisaStatus else ''
            },
            {
                "FieldName": "1ben.NotArrested",
                "FieldValue": bit_ans(resp_dic.get("26", ""))
            },
            {
                "FieldName": "1ben.PledGuilty",
                "FieldValue": bit_ans(resp_dic.get("27", ""))
            },
            {
                "FieldName": "1ben.SentencedToProgram",
                "FieldValue": bit_ans(resp_dic.get("28", ""))
            },
            {
                "FieldName": "1ben.BeenDefendant",
                "FieldValue": bit_ans(resp_dic.get("29", ""))
            },
            {
                "FieldName": "1ben.BeenDrugDealer",
                "FieldValue": bit_ans(resp_dic.get("30", ""))
            },
            {
                "FieldName": "1ben.Convicted5YearsPlus",
                "FieldValue": bit_ans(resp_dic.get("31", ""))
            },
            {
                "FieldName": "1ben.TraffickedDrugs",
                "FieldValue": bit_ans(resp_dic.get("32", ""))
            },
            {
                "FieldName": "1ben.AidedTraffickedDrugs",
                "FieldValue": bit_ans(resp_dic.get("42", ""))
            },
            # p8 34 doubt
            # {
            #     "FieldName": "1ben.RcvdDrugMoney",
            #     "FieldValue":bit_ans(result.)
            # },
            {
                "FieldName": "1ben.BeenProstitute",
                "FieldValue": bit_ans(resp_dic.get("34", ""))
            },
            {
                "FieldName": "1ben.ImportProstitutes",
                "FieldValue": bit_ans(resp_dic.get("35", ""))
            },
            {
                "FieldName": "1ben.ProstitutionProceeds",
                "FieldValue": bit_ans(resp_dic.get("36", ""))
            },
            {
                "FieldName": "1ben.BeenIllegalGambler",
                "FieldValue": bit_ans(resp_dic.get("37", ""))
            },
            {
                "FieldName": "1ben.ExercisedImmunity",
                "FieldValue": bit_ans(resp_dic.get("38", ""))
            },
            {
                "FieldName": "1ben.ReligiousFreedomViolation",
                "FieldValue": bit_ans(resp_dic.get("39", ""))
            },
            {
                "FieldName": "1ben.CommercialSex",
                "FieldValue": bit_ans(resp_dic.get("40", ""))
            },
            {
                "FieldName": "1ben.TraffickedSlavery",
                "FieldValue": bit_ans(resp_dic.get("41", ""))
            },
            {
                "FieldName": "1ben.AidedSexTrafficking",
                "FieldValue": bit_ans(resp_dic.get("33", ""))
            },
            # doubt p8 44
            # {
            #     "FieldName": "1ben.RcvdTraffickingMoney",
            #     "FieldValue":bit_ans(result.)
            # },
            {
                "FieldName": "1ben.MoneyLaundering",
                "FieldValue": bit_ans(resp_dic.get("43", ""))
            },
            {
                "FieldName": "1ben.EngagedInEspionage",
                "FieldValue": bit_ans(resp_dic.get("44", ""))
            },
            {
                "FieldName": "1ben.ProhibitExportingGoods",
                "FieldValue": bit_ans(resp_dic.get("45", ""))
            },
            {
                "FieldName": "1ben.OverthrowGovt",
                "FieldValue": bit_ans(resp_dic.get("46", ""))
            },
            {
                "FieldName": "1ben.EndangerUS",
                "FieldValue": bit_ans(resp_dic.get("47", ""))
            },
            {
                "FieldName": "1ben.UnlawfulActivity",
                "FieldValue": bit_ans(resp_dic.get("48", ""))
            },
            {
                "FieldName": "1ben.ForeignPolicyConsequences",
                "FieldValue": bit_ans(resp_dic.get("49", ""))
            },
            {
                "FieldName": "1ben.EngagedInTerrorism",
                "FieldValue": bit_ans(resp_dic.get("50", ""))
            },
            {
                "FieldName": "1ben.ParticipatedViolentCrime",
                "FieldValue": bit_ans(resp_dic.get("50", ""))
            },
            {
                "FieldName": "1ben.RecruitedViolentCriminals",
                "FieldValue": bit_ans(resp_dic.get("50", ""))
            },
            {
                "FieldName": "1ben.FinancedViolentCrime",
                "FieldValue": bit_ans(resp_dic.get("50", ""))
            },
            {
                "FieldName": "1ben.VisaNum",
                "FieldValue": iff(result.NonimmigrantVisaNumber)
            },
            {
                "FieldName": "1ben.LastArrivedInspected",
                "FieldValue": iff(inspect_value)
            },
            {
                "FieldName": "1ben.LastArrivedInspectedOther",
                "FieldValue": 'Some other reason here' if inspect_value == 0 else ''
            },
            {
                "FieldName": "USIMM82483.txt1.13",
                "FieldValue":  most_recent_entry_rec.InspectedAdmittedAs if most_recent_entry_rec.InspectedAdmittedAs and (inspect_value == '1') else ''
            },
            {
                "FieldName": "USIMM82483.txt1.18.0",
                "FieldValue": most_recent_entry_rec.IsInspectedParoledAs if most_recent_entry_rec.IsInspectedParoledAs and (inspect_value == '2') else ''
            },
            {
                "FieldName": "1ben.FinancedEntityViolentCrime",
                "FieldValue": bit_ans(resp_dic.get("50", ""))
            },
            {
                "FieldName": "1ben.CombatTraining",
                "FieldValue": bit_ans(resp_dic.get("12", ""))
            },
            {
                "FieldName": "1ben.IntendViolentCrime",
                "FieldValue": 'No'
            },
            {
                "FieldName": "1ben.ImmFamEngagedInTerrorism",
                "FieldValue": bit_ans(resp_dic.get("51", ""))
            },
            {
                "FieldName": "1ben.ImmFamParticipatedViolentCrime",
                "FieldValue": bit_ans(resp_dic.get("51", ""))
            },
            {
                "FieldName": "1ben.ImmFamRecruitedViolentCriminals",
                "FieldValue": bit_ans(resp_dic.get("51", ""))
            },
            {
                "FieldName": "1ben.ImmFamFinancedViolentCrime",
                "FieldValue": bit_ans(resp_dic.get("51", ""))
            },
            {
                "FieldName": "1ben.ImmFamFinancedEntityViolentCrime",
                "FieldValue": bit_ans(resp_dic.get("51", ""))
            },
            {
                "FieldName": "1ben.ImmFamCombatTraining",
                "FieldValue": bit_ans(resp_dic.get("52", ""))
            },
            # no provision or id given to map input
            # {
            #     "FieldName": "",
            #     "FieldValue":bit_ans(resp_dic.get("11",""))
            # },

            # from p8 53 to 57 id mismatch


            {
                "FieldName": "1ben.RecruitedMinorsToFight",
                "FieldValue": bit_ans(resp_dic.get("55", ""))
            },
            {
                "FieldName": "1ben.PublicAssistance",
                "FieldValue": bit_ans(resp_dic.get("57", ""))
            },
            {
                "FieldName": "1ben.FailedToAttendProceeding",
                "FieldValue": bit_ans(resp_dic.get("58", ""))
            },
            {
                "FieldName": "1ben.ReasonableCauseProceeding",
                "FieldValue": 'Yes' if bit_ans(resp_dic.get("58", "")) == 'Yes' else ''
            },
            {
                "FieldName": "1ben.SubmittedFraudDoc",
                "FieldValue": bit_ans(resp_dic.get("59", ""))
            },
            {
                "FieldName": "1ben.GivenFalseInfo",
                "FieldValue": bit_ans(resp_dic.get("59", ""))
            },
            {
                "FieldName": "1ben.LiedOnVisaApp",
                "FieldValue": bit_ans(resp_dic.get("60", ""))
            },
            {
                "FieldName": "1ben.BeenStowaway",
                "FieldValue": bit_ans(resp_dic.get("61", ""))
            },
            {
                "FieldName": "1ben.BeenSmuggler",
                "FieldValue": bit_ans(resp_dic.get("88", ""))
            },
            {
                "FieldName": "1ben.CivilPenalty274C",
                "FieldValue": bit_ans(resp_dic.get("62", ""))
            },
            {
                "FieldName": "1ben.BeenDeported",
                "FieldValue": bit_ans(resp_dic.get("63", ""))
            },
            {
                "FieldName": "1ben.EnteredUSWithoutInspection",
                "FieldValue": bit_ans(resp_dic.get("64", ""))
            },
            {
                "FieldName": "1ben.UnlawfullyPresent180to365Days",
                "FieldValue": bit_ans(resp_dic.get("65", ""))
            },
            {
                "FieldName": "1ben.UnlawfullyPresentOneYearPlus",
                "FieldValue": bit_ans(resp_dic.get("66", ""))
            },
            {
                "FieldName": "1ben.Since1997UnlawfullyPresentOneYear",
                "FieldValue": bit_ans(resp_dic.get("68", ""))
            },
            {
                "FieldName": "1ben.Since1997BeenDeported",
                "FieldValue": bit_ans(resp_dic.get("67", ""))
            },
            {
                "FieldName": "1ben.PracticePolygamy",
                "FieldValue": bit_ans(resp_dic.get("69", ""))
            },
            {
                "FieldName": "1ben.GuardianForInadmissible",
                "FieldValue": bit_ans(resp_dic.get("70", ""))
            },
            {
                "FieldName": "1ben.WithholdChildFromUS",
                "FieldValue": bit_ans(resp_dic.get("71", ""))
            },
            {
                "FieldName": "1ben.VotedInViolation",
                "FieldValue": bit_ans(resp_dic.get("72", ""))
            },
            {
                "FieldName": "1ben.ClaimedNonResident",
                "FieldValue": bit_ans(resp_dic.get("73", ""))
            },
            {
                "FieldName": "1ben.AppliedDischargedMilitary",
                "FieldValue": bit_ans(resp_dic.get("74", ""))
            },
            {
                "FieldName": "1ben.DischargedMilitaryForeignNational",
                "FieldValue": bit_ans(resp_dic.get("75", ""))
            },
            {
                "FieldName": "1ben.USMilitaryAWOL",
                "FieldValue": bit_ans(resp_dic.get("76", ""))
            },
            {
                "FieldName": "1ben.AvoidArmedForces",
                "FieldValue": bit_ans(resp_dic.get("77", ""))
            },
            {
                "FieldName": "1ben.AvoidArmedForcesImmigStatus",
                "FieldValue": bit_ans(resp_dic.get("78", ""))
            },
            {
                "FieldName": "1ben.DisabilityAccommodation",
                "FieldValue": bit_ans(resp_dic.get("79", ""))
            },



            {
                "FieldName": "1ben.RcvdDrugMoney",
                "FieldValue": bit_ans(resp_dic.get("84", ""))
            },
            {
                "FieldName": "1ben.RcvdTraffickingMoney",
                "FieldValue": bit_ans(resp_dic.get("85", ""))
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
                "FieldName": "1lawyer.ExtendsPrepApp",
                "FieldValue": '1'
            },
            {
                "FieldName": "User.D937.AttorneyOrAccreditedRep",
                "FieldValue": '1'
            },
            {
                "FieldName": "USIMM82483.chk1.01.0",
                "FieldValue": 'Yes' if result.SSNNumber else 'No'
            },
            {
                "FieldName": "USIMM82483.chk1.01.1",
                "FieldValue": 'Yes' if not result.SSNNumber else 'No'
            },
            {
                "FieldName": "USIMM82483.chk1.01.2",
                "FieldValue": 'Yes' if not result.SSNNumber else ''
            },
            {
                "FieldName": "1ben.TD.ID",
                "FieldValue": iff(most_recent_entry_rec.TravelDocumentNumber) if not result.PassportNumber else ''
            },
        ]

        if bit_ans(resp_dic.get("79", "")) == 'Yes':

            data_dict.extend([
                {
                    "FieldName": "1ben.Deaf",
                    "FieldValue": bit_ans(resp_dic.get("80", ""))
                },

                {
                    "FieldName": "1ben.Blind",
                    "FieldValue": bit_ans(resp_dic.get("82", ""))
                },


                {
                    "FieldName": "1ben.AnotherDisability",
                    "FieldValue": bit_ans(resp_dic.get("89", ""))
                },
            ])

            if bit_ans(resp_dic.get("80", "")) == 'Yes':
                data_dict.append(
                    {
                        "FieldName": "1ben.DeafDesc",
                        "FieldValue": (resp_dic.get("81", ""))
                    },
                )

            if bit_ans(resp_dic.get("82", "")) == 'Yes':
                data_dict.append(
                    {
                        "FieldName": "1ben.BlindDesc",
                        "FieldValue": (resp_dic.get("83", ""))
                    },
                )

            if bit_ans(resp_dic.get("89", "")) == 'Yes':
                data_dict.append(
                    {
                        "FieldName": "1ben.AnotherDisabilityDesc",
                        "FieldValue": resp_dic.get("90", "")
                    },
                )

        # revisit - put the respective ProjectPetitionID in future
        underlying_pet_data = cursor.execute('''select top 1 * from [Project] 
        where BeneficiaryID = ? and
        ProjectPetitionID = '1'
        order by ProjectOpenDate desc

        ''', (result.BeneficiaryID)).fetchone()

        # revisit - put the respective ProjectPetitionID in future
        prim_underlying_pet_data = cursor.execute('''select top 1 * from [Project] 
        where BeneficiaryID = ? and
        ProjectPetitionID = '1'
        order by ProjectOpenDate desc

        ''', (prim_ben.BeneficiaryID)).fetchone()

        if (result.BeneficiaryType.lower().strip() == 'primary') and underlying_pet_data:
            data_dict.extend([
                {
                    "FieldName": "1ben.RecNumUndPet",
                    "FieldValue": iff(underlying_pet_data.ReceiptNumber)
                },
                {
                    "FieldName": "1ben.PrtyDateUndPet",
                    "FieldValue": change_date(underlying_pet_data.ProjectPriorityDate)
                }
            ])

        elif (result.BeneficiaryType.lower().strip() == 'dependent'):
            if prim_ben:
                data_dict.extend([
                    {
                        "FieldName": "2altclient.LName",
                        "FieldValue": iff(prim_ben.LastName)
                    },
                    {
                        "FieldName": "2altclient.FName",
                        "FieldValue": iff(prim_ben.FirstName)
                    },
                    {
                        "FieldName": "2altclient.MName",
                        "FieldValue": iff(prim_ben.MiddleName)
                    },
                    {
                        "FieldName": "2altclient.AlienRegNumComb",
                        "FieldValue": iff(prim_ben.AlienNumber1)
                    },
                    {
                        "FieldName": "2altclient.DOB",
                        "FieldValue": change_date(prim_ben.BirthDate)
                    },
                    {
                        "FieldName": "2altclient.RecNumUndPet",
                        "FieldValue": iff(prim_underlying_pet_data.ReceiptNumber)
                    },
                    {
                        "FieldName": "2altclient.PrtyDateUndPet",
                        "FieldValue": change_date(prim_underlying_pet_data.ProjectPriorityDate)
                    },
                ])

        if most_recent_entry_rec:
            data_dict.extend([
                {
                    "FieldName": "1ben.I94.ID",
                    "FieldValue": iff(most_recent_entry_rec.I94Number)
                },

                {
                    "FieldName": "1ben.NonImmigExpiry",
                    "FieldValue": change_date(most_recent_entry_rec.I94ExpirationDate) if most_recent_entry_rec.I94ExpirationDate else ''
                },
                {
                    "FieldName": "1ben.I94.IDStatus",
                    "FieldValue": most_recent_entry_rec.I94StatusType if most_recent_entry_rec.I94Number else ''
                },
                {
                    "FieldName": "1ben.CurrentStatus",
                    "FieldValue": iff(most_recent_entry_rec.I94StatusType)
                },
                {
                    "FieldName": "1ben.I94.ExactLName",
                    "FieldValue": iff(most_recent_entry_rec.LastNameOnI94Document)
                },
                {
                    "FieldName": "1ben.I94.ExactFName",
                    "FieldValue": iff(most_recent_entry_rec.FirstNameOnI94Document)
                },
                {
                    "FieldName": "1ben.I94.ExactMName",
                    "FieldValue": iff(most_recent_entry_rec.MiddleNameOnI94Document)
                },
            ])

        if result.IsImmigrantVisaApplicant:
            data_dict.extend([
                {
                    "FieldName": "1ben.E.City",
                    "FieldValue": iff(result.USEmbassyConsulateCity)
                },
                {
                    "FieldName": "1ben.E.Country",
                    "FieldValue": iff(result.USEmbassyConsulateCountry)
                },
                {
                    "FieldName": "1ben.VisaAbroadDecision",
                    "FieldValue": iff(result.ImmigrantVisaApplicationDecision)
                },
                {
                    "FieldName": "1ben.VisaAbroadDate",
                    "FieldValue": change_date(result.ImmigrantVisaApplicationDecisionDate) if result.ImmigrantVisaApplicationDecisionDate else ''
                }
            ])

        if len(l5_res) > 0:
            data_dict.extend([
                {
                    "FieldName": "1ben.PH1.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(l5_res[0].Address1)
                },
                {
                    "FieldName": "1ben.PH1.AddrUnitType",
                    "FieldValue": AptSteFlr(l5_res[0].AddressUnitType)
                },
                {
                    "FieldName": "1ben.PH1.Addr4",
                    "FieldValue": iff(l5_res[0].AddressUnitNumber)
                },
                {
                    "FieldName": "1ben.PH1.City",
                    "FieldValue": iff(l5_res[0].City)
                },
                {
                    "FieldName": "1ben.PH1.State",
                    "FieldValue": iff(l5_res[0].StateProvince)
                },
                {
                    "FieldName": "1ben.PH1.Zip",
                    "FieldValue": iff(l5_res[0].PostalZipCode) if US_keyword.search(l5_res[0].Country) else ''
                },
                {
                    "FieldName": "1ben.PH1.ForeignRoute",
                    "FieldValue": iff(l5_res[0].PostalZipCode) if not US_keyword.search(l5_res[0].Country) else ''
                },
                {
                    "FieldName": "1ben.PH1.Country",
                    "FieldValue": iff(l5_res[0].Country)
                },
                {
                    "FieldName": "1ben.PH1.County",
                    "FieldValue": iff(l5_res[0].County)
                },
                {
                    "FieldName": "1ben.PH1.StartDate",
                    "FieldValue": change_date(l5_res[0].AddressFromDate)
                },
                {
                    "FieldName": "1ben.PH1.EndDate",
                    "FieldValue": change_date(l5_res[0].AddressToDate)
                }

            ])

        for addr in l5_res:
            if not US_keyword.search(addr.Country):
                break
            elif not US_keyword.search(current_res_address.Country):
                break
        else:
            data_dict.extend([
                {
                    "FieldName": "1ben.F.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(last_perm_address_abroad.Address1)
                },
                {
                    "FieldName": "1ben.F.AddrUnitType",
                    "FieldValue": AptSteFlr(last_perm_address_abroad.AddressUnitType)
                },
                {
                    "FieldName": "1ben.F.Addr4",
                    "FieldValue": iff(last_perm_address_abroad.AddressUnitNumber)
                },
                {
                    "FieldName": "1ben.F.City",
                    "FieldValue": iff(last_perm_address_abroad.City)
                },
                {
                    "FieldName": "1ben.F.State",
                    "FieldValue": iff(last_perm_address_abroad.StateProvince)
                },
                {
                    "FieldName": "1ben.F.Zip",
                    "FieldValue": iff(last_perm_address_abroad.PostalZipCode) if US_keyword.search(last_perm_address_abroad.Country) else ''
                },
                {
                    "FieldName": "1ben.F.ForeignRoute",
                    "FieldValue": iff(last_perm_address_abroad.PostalZipCode) if not US_keyword.search(last_perm_address_abroad.Country) else ''
                },
                {
                    "FieldName": "1ben.F.Country",
                    "FieldValue": iff(last_perm_address_abroad.Country)
                },
                {
                    "FieldName": "1ben.F.County",
                    "FieldValue": iff(last_perm_address_abroad.County)
                },
                {
                    "FieldName": "1ben.F.StartDate",
                    "FieldValue": change_date(l5_res[0].AddressFromDate)
                },
                {
                    "FieldName": "1ben.F.EndDate",
                    "FieldValue": change_date(l5_res[0].AddressToDate)
                }
            ])

        if len(l5_emp) > 0:
            data_dict.extend([
                {
                    "FieldName": "1ben.Emp.Company",
                    "FieldValue": iff(l5_emp[0].EmployerName)
                },
                {
                    "FieldName": "1ben.EO.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(l5_emp[0].Address1)
                },
                {
                    "FieldName": "1ben.EO.AddrUnitType",
                    "FieldValue": AptSteFlr(l5_emp[0].AddressUnitType)
                },
                {
                    "FieldName": "1ben.EO.Addr4",
                    "FieldValue": iff(l5_emp[0].AddressUnitNumber)
                },
                {
                    "FieldName": "1ben.EO.City",
                    "FieldValue": iff(l5_emp[0].City)
                },
                {
                    "FieldName": "1ben.EO.State",
                    "FieldValue": iff(l5_emp[0].StateProvince)
                },
                {
                    "FieldName": "1ben.EO.Zip",
                    "FieldValue": iff(l5_emp[0].PostalZipCode) if US_keyword.search(l5_emp[0].Country) else ''
                },
                {
                    "FieldName": "1ben.EO.ForeignRoute",
                    "FieldValue": iff(l5_emp[0].PostalZipCode) if not US_keyword.search(l5_emp[0].Country) else ''
                },
                {
                    "FieldName": "1ben.EO.Country",
                    "FieldValue": iff(l5_emp[0].Country)
                },
                {
                    "FieldName": "1ben.EO.County",
                    "FieldValue": iff(l5_emp[0].County)
                },
                {
                    "FieldName": "1ben.Emp.Title",
                    "FieldValue": iff(l5_emp[0].JobTitle)
                },
                {
                    "FieldName": "1ben.Emp.StartDate",
                    "FieldValue": change_date(l5_emp[0].HireDate)
                },
                {
                    "FieldName": "1ben.Emp.EndDate",
                    "FieldValue": change_date(l5_emp[0].TerminationDate) if l5_emp[0].TerminationDate else 'Present '
                }
            ])

        if len(l5_emp) > 1:
            data_dict.extend([
                {
                    "FieldName": "1ben.PEmp1.Company",
                    "FieldValue": iff(l5_emp[1].EmployerName)
                },
                {
                    "FieldName": "1ben.PEO1.Addr123",
                    "FieldCalcOverride": True,
                    "FieldValue": iff(l5_emp[1].Address1)
                },
                {
                    "FieldName": "1ben.PEO1.AddrUnitType",
                    "FieldValue": AptSteFlr(l5_emp[1].AddressUnitType)
                },
                {
                    "FieldName": "1ben.PEO1.Addr4",
                    "FieldValue": iff(l5_emp[1].AddressUnitNumber)
                },
                {
                    "FieldName": "1ben.PEO1.City",
                    "FieldValue": iff(l5_emp[1].City)
                },
                {
                    "FieldName": "1ben.PEO1.State",
                    "FieldValue": iff(l5_emp[1].StateProvince)
                },
                {
                    "FieldName": "1ben.PEO1.Zip",
                    "FieldValue": iff(l5_emp[1].PostalZipCode) if US_keyword.search(l5_emp[1].Country) else ''
                },
                {
                    "FieldName": "1ben.PEO1.ForeignRoute",
                    "FieldValue": iff(l5_emp[1].PostalZipCode) if not US_keyword.search(l5_emp[1].Country) else ''
                },
                {
                    "FieldName": "1ben.PEO1.Country",
                    "FieldValue": iff(l5_emp[1].Country)
                },
                {
                    "FieldName": "1ben.PEO1.County",
                    "FieldValue": iff(l5_emp[1].County)
                },
                {
                    "FieldName": "1ben.PEmp1.Title",
                    "FieldValue": iff(l5_emp[1].JobTitle)
                },
                {
                    "FieldName": "1ben.PEmp1.StartDate",
                    "FieldValue": change_date(l5_emp[1].HireDate)
                },
                {
                    "FieldName": "1ben.PEmp1.EndDate",
                    "FieldValue": change_date(l5_emp[1].TerminationDate)
                }
            ])

        for i in l5_emp:
            if not US_keyword.search(i.Country):

                ben_all_emp = cursor.execute(
                    f'''
                select *
                
                from [dbo].[BeneficiaryEmployment]
                where
                
                HireDate is not null and 

                BeneficiaryID = '{result.BeneficiaryID}'

                order by HireDate desc''').fetchall()

                for emp in ben_all_emp:
                    if not US_keyword.search(emp.Country):
                        data_dict.extend([
                            {
                                "FieldName": "1ben.PEmp2.Company",
                                "FieldValue": iff(emp.EmployerName)
                            },
                            {
                                "FieldName": "1ben.PEO2.Addr123",
                                "FieldCalcOverride": True,
                                "FieldValue": iff(emp.Address1)
                            },
                            {
                                "FieldName": "1ben.PEO2.AddrUnitType",
                                "FieldValue": AptSteFlr(emp.AddressUnitType)
                            },
                            {
                                "FieldName": "1ben.PEO2.Addr4",
                                "FieldValue": iff(emp.AddressUnitNumber)
                            },
                            {
                                "FieldName": "1ben.PEO2.City",
                                "FieldValue": iff(emp.City)
                            },
                            {
                                "FieldName": "1ben.PEO2.State",
                                "FieldValue": iff(emp.StateProvince)
                            },
                            {
                                "FieldName": "1ben.PEO2.Zip",
                                "FieldValue": iff(emp.PostalZipCode) if US_keyword.search(emp.Country) else ''
                            },
                            {
                                "FieldName": "1ben.PEO2.ForeignRoute",
                                "FieldValue": iff(emp.PostalZipCode) if not US_keyword.search(emp.Country) else ''
                            },
                            {
                                "FieldName": "1ben.PEO2.Country",
                                "FieldValue": iff(emp.Country)
                            },
                            {
                                "FieldName": "1ben.PEO2.County",
                                "FieldValue": iff(emp.County)
                            },
                            {
                                "FieldName": "1ben.PEmp2.Title",
                                "FieldValue": iff(emp.JobTitle)
                            },
                            {
                                "FieldName": "1ben.PEmp2.StartDate",
                                "FieldValue": change_date(emp.HireDate)
                            },
                            {
                                "FieldName": "1ben.PEmp2.EndDate",
                                "FieldValue": change_date(emp.TerminationDate)
                            }
                        ])

                break  # break the outer loop

        if len(parents) > 0:
            data_dict.extend([
                {
                    "FieldName": "1father.LName",
                    "FieldValue": iff(parents[0].LastName)
                },
                {
                    "FieldName": "1father.FName",
                    "FieldValue": iff(parents[0].FirstName)
                },
                {
                    "FieldName": "1father.MName",
                    "FieldValue": iff(parents[0].MiddleName)
                },
                {
                    "FieldName": "1father.DOB",
                    "FieldValue": change_date(parents[0].BirthDate)
                },
                {
                    "FieldName": "1father.Gender",
                    "FieldValue": get_gender(parents[0].Gender)
                },

                {
                    "FieldName": "1father.BP.City",
                    "FieldValue": iff(parents[0].BirthCity)
                },
                {
                    "FieldName": "1father.BP.Country",
                    "FieldValue": iff(parents[0].BirthCountry)
                },
                {
                    "FieldName": "1father.H.City",
                    "FieldValue": iff(parents[0].LivingCity) if parents[0].IsAlive else ''
                },
                {
                    "FieldName": "1father.H.Country",
                    "FieldValue": iff(parents[0].LivingCountry) if parents[0].IsAlive else ''
                }])

        if len(parents) > 1:
            data_dict.extend([
                {
                    "FieldName": "1mother.LName",
                    "FieldValue": iff(parents[1].LastName)
                },
                {
                    "FieldName": "1mother.FName",
                    "FieldValue": iff(parents[1].FirstName)
                },
                {
                    "FieldName": "1mother.MName",
                    "FieldValue": iff(parents[1].MiddleName)
                },
                {
                    "FieldName": "1mother.DOB",
                    "FieldValue": change_date(parents[1].BirthDate)
                },
                {
                    "FieldName": "1mother.Gender",
                    "FieldValue": get_gender(parents[1].Gender)
                },

                {
                    "FieldName": "1mother.BP.City",
                    "FieldValue": iff(parents[1].BirthCity)
                },
                {
                    "FieldName": "1mother.BP.Country",
                    "FieldValue": iff(parents[1].BirthCountry)
                },
                {
                    "FieldName": "1mother.H.City",
                    "FieldValue": iff(parents[1].LivingCity) if parents[1].IsAlive else ''
                },
                {
                    "FieldName": "1mother.H.Country",
                    "FieldValue": iff(parents[1].LivingCountry) if parents[1].IsAlive else ''
                }]

            )

        if len(dependents) > 0:
            data_dict.extend([
                {
                    "FieldName": "1child.LName",
                    "FieldValue": iff(dependents[0].LastName)
                },
                {
                    "FieldName": "1child.FName",
                    "FieldValue": iff(dependents[0].FirstName)
                },
                {
                    "FieldName": "1child.MName",
                    "FieldValue": iff(dependents[0].MiddleName)
                },
                {
                    "FieldName": "1child.AlienRegNumComb",
                    "FieldValue": iff(dependents[0].AlienNumber1)
                },
                {
                    "FieldName": "1child.DOB",
                    "FieldValue": change_date(dependents[0].BirthDate)
                },
                {
                    "FieldName": "1child.BP.Country",
                    "FieldValue": iff(dependents[0].BirthCountry)
                },
            ])

            if not US_keyword.search(dependents[0].CitizenshipCountry) and (calculate_age(dependents[0].BirthDate) < 21):
                value = 'Yes'
            else:
                value = 'No'

            data_dict.append(
                {
                    "FieldName": "1child.IncludeInApp",
                    "FieldValue": value
                },
            )

        if len(dependents) > 1:
            data_dict.extend([
                {
                    "FieldName": "2child.LName",
                    "FieldValue": iff(dependents[1].LastName)
                },
                {
                    "FieldName": "2child.FName",
                    "FieldValue": iff(dependents[1].FirstName)
                },
                {
                    "FieldName": "2child.MName",
                    "FieldValue": iff(dependents[1].MiddleName)
                },
                {
                    "FieldName": "2child.AlienRegNumComb",
                    "FieldValue": iff(dependents[1].AlienNumber1)
                },
                {
                    "FieldName": "2child.DOB",
                    "FieldValue": change_date(dependents[1].BirthDate)
                },
                {
                    "FieldName": "2child.BP.Country",
                    "FieldValue": iff(dependents[1].BirthCountry)
                },

            ])

            if not US_keyword.search(dependents[1].CitizenshipCountry) and (calculate_age(dependents[1].BirthDate) < 21):
                value = 'Yes'
            else:
                value = 'No'

            data_dict.append(
                {
                    "FieldName": "2child.IncludeInApp",
                    "FieldValue": value
                },
            )

        if len(dependents) > 2:
            data_dict.extend([
                {
                    "FieldName": "3child.LName",
                    "FieldValue": iff(dependents[2].LastName)
                },
                {
                    "FieldName": "3child.FName",
                    "FieldValue": iff(dependents[2].FirstName)
                },
                {
                    "FieldName": "3child.MName",
                    "FieldValue": iff(dependents[2].MiddleName)
                },
                {
                    "FieldName": "3child.AlienRegNumComb",
                    "FieldValue": iff(dependents[2].AlienNumber1)
                },
                {
                    "FieldName": "3child.DOB",
                    "FieldValue": change_date(dependents[2].BirthDate)
                },
                {
                    "FieldName": "3child.BP.Country",
                    "FieldValue": iff(dependents[2].BirthCountry)
                }

            ])

            if not US_keyword.search(dependents[2].CitizenshipCountry) and (calculate_age(dependents[2].BirthDate) < 21):
                value = 'Yes'
            else:
                value = 'No'

            data_dict.append(
                {
                    "FieldName": "3child.IncludeInApp",
                    "FieldValue": value
                },
            )

        if len(marriage_history) > 0:
            data_dict.extend([
                {
                    "FieldName": "1spou.LName",
                    "FieldValue": iff(marriage_history[0].SpouseLastName)
                },
                {
                    "FieldName": "1spou.FName",
                    "FieldValue": iff(marriage_history[0].SpouseFirstName)
                },
                {
                    "FieldName": "1spou.MName",
                    "FieldValue": iff(marriage_history[0].SpouseMiddleName)
                },
                {
                    "FieldName": "1spou.AlienRegNumComb",
                    "FieldValue": iff(spouse[0].AlienNumber1)
                },
                {
                    "FieldName": "1spou.DOB",
                    "FieldValue": change_date(marriage_history[0].SpouseBirthDate)
                },
                {
                    "FieldName": "1ben.Marriage.MarryDate",
                    "FieldValue": change_date(marriage_history[0].MarriageDate) if marriage_history[0].MarriageDate else ''
                },
                {
                    "FieldName": "1spou.BP.City",
                    "FieldValue": iff(marriage_history[0].SpouseBirthCity)
                },
                {
                    "FieldName": "1spou.BP.State",
                    "FieldValue": iff(marriage_history[0].SpouseBirthState)
                },
                {
                    "FieldName": "1spou.BP.Country",
                    "FieldValue": iff(marriage_history[0].SpouseBirthCountry)
                },
                {
                    "FieldName": "1ben.Marriage.MarryCity",
                    "FieldValue": iff(marriage_history[0].MarriageCity)
                },
                {
                    "FieldName": "1ben.Marriage.MarryState",
                    "FieldValue": iff(marriage_history[0].MarriageState)
                },
                {
                    "FieldName": "1ben.Marriage.MarryCountry",
                    "FieldValue": iff(marriage_history[0].MarriageCountry)
                },
                {
                    "FieldName": "1ben.IncludeInApp",
                    "FieldValue": 'Yes'
                }
            ])

        if len(marriage_history) > 1:
            data_dict.extend([
                {
                    "FieldName": "1ben.PMarriage1.SpouseLName",
                    "FieldValue": iff(marriage_history[1].SpouseLastName)
                },
                {
                    "FieldName": "1ben.PMarriage1.SpouseFName",
                    "FieldValue": iff(marriage_history[1].SpouseFirstName)
                },
                {
                    "FieldName": "1ben.PMarriage1.SpouseMName",
                    "FieldValue": iff(marriage_history[1].SpouseMiddleName)
                },
                {
                    "FieldName": "1ben.PMarriage1.SpouseDOB",
                    "FieldValue": change_date(marriage_history[1].SpouseBirthDate) if marriage_history[1].SpouseBirthDate else ''
                },
                {
                    "FieldName": "1ben.PMarriage1.MarryDate",
                    "FieldValue": change_date(marriage_history[1].MarriageDate) if marriage_history[1].MarriageDate else ''
                },
                {
                    "FieldName": "1ben.PMarriage1.MarryCity",
                    "FieldValue": iff(marriage_history[1].MarriageCity)
                },
                {
                    "FieldName": "1ben.PMarriage1.MarryState",
                    "FieldValue": iff(marriage_history[1].MarriageState)
                },
                {
                    "FieldName": "1ben.PMarriage1.MarryCountry",
                    "FieldValue": iff(marriage_history[1].MarriageCountry)
                },
                {
                    "FieldName": "1ben.PMarriage1.DivorceDate",
                    "FieldValue": change_date(marriage_history[1].MarriageEndDate) if marriage_history[1].MarriageEndDate else ''
                },
                {
                    "FieldName": "1ben.PMarriage1.DivCity",
                    "FieldValue": iff(marriage_history[1].MarriageEndCity)
                },
                {
                    "FieldName": "1ben.PMarriage1.DivState",
                    "FieldValue": iff(marriage_history[1].MarriageEndState)
                },
                {
                    "FieldName": "1ben.PMarriage1.DivCountry",
                    "FieldValue": iff(marriage_history[1].MarriageEndCountry)
                }
            ])

        if len(org_membership) > 1:
            data_dict.extend([
                {
                    "FieldName": "1ben.RelatedOrg1",
                    "FieldValue": iff(org_membership[0].OrganizationName)
                },
                {
                    "FieldName": "1ben.RelatedOrgCity1",
                    "FieldValue": iff(org_membership[0].City)
                },
                {
                    "FieldName": "1ben.RelatedOrgState1",
                    "FieldValue": iff(org_membership[0].StateProvince)
                },
                {
                    "FieldName": "1ben.RelatedOrgCountry1",
                    "FieldValue": iff(org_membership[0].Country)
                },
                {
                    "FieldName": "1ben.RelatedOrgNature1",
                    "FieldValue": iff(org_membership[0].NatureOfGroup)
                },
                {
                    "FieldName": "1ben.RelatedOrgStartDate1",
                    "FieldValue": change_date(org_membership[0].MembershipStartDate) if org_membership[0].MembershipStartDate else ''
                },
                {
                    "FieldName": "1ben.RelatedOrgEndDate1",
                    "FieldValue": change_date(org_membership[0].MembershipEndDate) if org_membership[0].MembershipEndDate else ''
                }

            ])

        if len(org_membership) > 2:
            data_dict.extend([
                {
                    "FieldName": "1ben.RelatedOrg2",
                    "FieldValue": iff(org_membership[1].OrganizationName)
                },
                {
                    "FieldName": "1ben.RelatedOrgCity2",
                    "FieldValue": iff(org_membership[1].City)
                },
                {
                    "FieldName": "1ben.RelatedOrgState2",
                    "FieldValue": iff(org_membership[1].StateProvince)
                },
                {
                    "FieldName": "1ben.RelatedOrgCountry2",
                    "FieldValue": iff(org_membership[1].Country)
                },
                {
                    "FieldName": "1ben.RelatedOrgNature2",
                    "FieldValue": iff(org_membership[1].NatureOfGroup)
                },
                {
                    "FieldName": "1ben.RelatedOrgStartDate2",
                    "FieldValue": change_date(org_membership[1].MembershipStartDate) if org_membership[1].MembershipStartDate else ''
                },
                {
                    "FieldName": "1ben.RelatedOrgEndDate2",
                    "FieldValue": change_date(org_membership[1].MembershipEndDate) if org_membership[1].MembershipEndDate else ''
                }

            ])

        if len(org_membership) > 3:
            data_dict.extend([
                {
                    "FieldName": "1ben.RelatedOrg3",
                    "FieldValue": iff(org_membership[2].OrganizationName)
                },
                {
                    "FieldName": "1ben.RelatedOrgCity3",
                    "FieldValue": iff(org_membership[2].City)
                },
                {
                    "FieldName": "1ben.RelatedOrgState3",
                    "FieldValue": iff(org_membership[2].StateProvince)
                },
                {
                    "FieldName": "1ben.RelatedOrgCountry3",
                    "FieldValue": iff(org_membership[2].Country)
                },
                {
                    "FieldName": "1ben.RelatedOrgNature3",
                    "FieldValue": iff(org_membership[2].NatureOfGroup)
                },
                {
                    "FieldName": "1ben.RelatedOrgStartDate3",
                    "FieldValue": change_date(org_membership[2].MembershipStartDate) if org_membership[2].MembershipStartDate else ''
                },
                {
                    "FieldName": "1ben.RelatedOrgEndDate3",
                    "FieldValue": change_date(org_membership[2].MembershipEndDate) if org_membership[2].MembershipEndDate else ''
                },
                {
                    "FieldName": "USIMM82483.chk1.01.0",
                    "FieldValue": 'Yes' if result.SSNNumber else 'No'
                },
                {
                    "FieldName": "USIMM82483.chk1.01.1",
                    "FieldValue": 'Yes' if not result.SSNNumber else 'No'
                },
                {
                    "FieldName": "USIMM82483.chk1.01.2",
                    "FieldValue": 'Yes' if not result.SSNNumber else ''
                },
            ])

        if bit_ans(resp_dic.get("57", "")) == 'Yes':

            data_dict.extend([
                {
                    "FieldName": "USIMM82483.txt1.01.0",
                    "FieldValue": resp_dic.get("91", "")
                },
                {
                    "FieldName": "1ben.HouseholdIncome.Range",
                    "FieldValue": annual_household_income
                },
                {
                    "FieldName": "1ben.InvAssets.Range",
                    "FieldValue": annual_household_asset
                },
                {
                    "FieldName": "USIMM82483.chk1.02.2",
                    "FieldValue": annual_household_liability
                },

            ])
            if ben_high_edu:
                value = ''
                if ben_high_edu.DegreeType:
                    deg_type = ben_high_edu.DegreeType.lower().strip()

                    if deg_type.__contains__('no diploma'):
                        value = 1
                    if deg_type.__contains__('high school'):
                        value = 3
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
                    if deg_type.__contains__('through'):
                        value = 0
                    data_dict.append(
                        {
                            "FieldName": "USIMM82483.chk1.02.3",
                            "FieldValue": value
                        },
                    )
                elif ben_high_edu.ProgramLength:
                    if ben_high_edu.ProgramLength >= 1:
                        value = 4
                        data_dict.append(
                            {
                                "FieldName": "USIMM82483.chk1.02.3",
                                "FieldValue": value
                            },
                        )

            if ben_all_edu:
                data_dict.extend([
                    {
                        "FieldName": "USIMM82483.txt1.01.1.0",
                        "FieldValue": iff(ben_all_edu[0].DegreeType) + " " + iff(ben_all_edu[0].FieldOfStudy) if len(ben_all_edu) > 0 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.1",
                        "FieldValue": iff(ben_all_edu[1].DegreeType) + " " + iff(ben_all_edu[1].FieldOfStudy) if len(ben_all_edu) > 1 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.2",
                        "FieldValue": iff(ben_all_edu[2].DegreeType) + " " + iff(ben_all_edu[2].FieldOfStudy) if len(ben_all_edu) > 2 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.3",
                        "FieldValue": iff(ben_all_edu[3].DegreeType) + " " + iff(ben_all_edu[3].FieldOfStudy) if len(ben_all_edu) > 3 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.4",
                        "FieldValue": iff(ben_all_edu[4].DegreeType) + " " + iff(ben_all_edu[4].FieldOfStudy) if len(ben_all_edu) > 4 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.5",
                        "FieldValue": iff(ben_all_edu[5].DegreeType) + " " + iff(ben_all_edu[5].FieldOfStudy) if len(ben_all_edu) > 5 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.6",
                        "FieldValue": iff(ben_all_edu[6].DegreeType) + " " + iff(ben_all_edu[6].FieldOfStudy) if len(ben_all_edu) > 6 else ''
                    },
                    {
                        "FieldName": "USIMM82483.txt1.01.1.7",
                        "FieldValue": iff(ben_all_edu[7].DegreeType) + " " + iff(ben_all_edu[7].FieldOfStudy) if len(ben_all_edu) > 7 else ''
                    }

                    # {
                    #     "FieldName": "",
                    #     "FieldValue":
                    # },
                    # {
                    #     "FieldName": "",
                    #     "FieldValue":
                    # },

                ])

        # last part 14 logics
        if True:
            place1, place2, place3, place4, place5 = '', '', '', '', ''

            # if True:
            if len(l5_res) > 1:
                place1 = 'full'

                data_dict.extend([
                    {
                        "FieldName": "USIMM82483.txt2.25.0.0",
                        "FieldValue": '5'
                    },
                    {
                        "FieldName": "USIMM82483.txt2.25.1.0",
                        "FieldValue": '3'
                    },
                    {
                        "FieldName": "USIMM82483.txt2.25.2.0",
                        "FieldValue": '5'
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.1",
                        "FieldValue": iff(l5_res[1].Address1)
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.2",
                        "FieldValue": f'{iff(l5_res[1].AddressUnitType)} - {iff(l5_res[1].AddressUnitNumber)}, {iff(l5_res[1].City)}, {iff(l5_res[1].StateProvince)}'
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.3",
                        "FieldValue": f'{iff(l5_res[1].Country)} - {iff(l5_res[1].PostalZipCode)}'
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.4",
                        "FieldValue": f'From {change_date(l5_res[1].AddressFromDate)} till {change_date(l5_res[1].AddressToDate)}'
                    }
                ])

            # if True:
            if len(l5_res) > 2:
                place1 = 'full'
                data_dict.extend([
                    # 2nd address set below

                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.6",
                        "FieldValue": iff(l5_res[2].Address1)
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.7",
                        "FieldValue": f'{iff(l5_res[2].AddressUnitType)} - {iff(l5_res[2].AddressUnitNumber)}, {iff(l5_res[2].City)}, {iff(l5_res[2].StateProvince)}'
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.8",
                        "FieldValue": f'{iff(l5_res[2].Country)} - {iff(l5_res[2].PostalZipCode)}'
                    },
                    {
                        "FieldName": "User.D937.AdditionalInfo1.multiline.9",
                        "FieldValue": f'From {change_date(l5_res[2].AddressFromDate)} till {change_date(l5_res[2].AddressToDate)}'
                    }
                ])

            # if True:
            if place1 == 'full':
                if len(l5_emp) > 1:
                    data_dict.extend([

                    ])
            else:
                if len(l5_emp) > 1:
                    data_dict.extend([
                        {
                            "FieldName": "USIMM82483.txt2.25.0.0",
                            "FieldValue": '5'
                        },
                        {
                            "FieldName": "USIMM82483.txt2.25.1.0",
                            "FieldValue": '3'
                        },
                        {
                            "FieldName": "USIMM82483.txt2.25.2.0",
                            "FieldValue": '5'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.1",
                            "FieldValue": iff(l5_emp[1].Address1)
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.2",
                            "FieldValue": f'{iff(l5_emp[1].AddressUnitType)} - {iff(l5_emp[1].AddressUnitNumber)}, {iff(l5_emp[1].City)}, {iff(l5_emp[1].StateProvince)}'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.3",
                            "FieldValue": f'{iff(l5_emp[1].Country)} - {iff(l5_emp[1].PostalZipCode)}'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.4",
                            "FieldValue": f'From {change_date(l5_emp[1].AddressFromDate)} till {change_date(l5_emp[1].AddressToDate)}'
                        }
                    ])
                if len(l5_emp) > 2:
                    data_dict.extend([
                        {
                            "FieldName": "USIMM82483.txt2.25.0.6",
                            "FieldValue": '5'
                        },
                        {
                            "FieldName": "USIMM82483.txt2.25.1.7",
                            "FieldValue": '3'
                        },
                        {
                            "FieldName": "USIMM82483.txt2.25.2.8",
                            "FieldValue": '5'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.6",
                            "FieldValue": iff(l5_emp[2].Address1)
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.7",
                            "FieldValue": f'{iff(l5_emp[2].AddressUnitType)} - {iff(l5_emp[2].AddressUnitNumber)}, {iff(l5_emp[2].City)}, {iff(l5_emp[2].StateProvince)}'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.8",
                            "FieldValue": f'{iff(l5_emp[2].Country)} - {iff(l5_emp[2].PostalZipCode)}'
                        },
                        {
                            "FieldName": "User.D937.AdditionalInfo1.multiline.9",
                            "FieldValue": f'From {change_date(l5_emp[2].AddressFromDate)} till {change_date(l5_emp[2].AddressToDate)}'
                        }
                    ])

        params = {
            "HostFormOnQuik": True,
            "FormFields": data_dict,
            "QuikFormID": "82483",
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
        with open('Form I-485.pdf', 'wb') as pdf:
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
                "FieldCalcOverride": True,

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
                "FieldValue": ('Form I-485 - '+str(result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)+', '+str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName)+' '+str(result.b_middlename if result.b_middlename is not None else iff(results2.BeneficiaryMiddleName))).strip()
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
                "FieldValue": ''  # result.PetitionerName if result.PetitionerName is not None else results2.PetitionerName
            },
            {
                "FieldName": "1ben.SignTitle",
                "FieldValue": ''  # result.JobTitle if result.JobTitle is not None else results2.JobTitle
            },
            {
                "FieldName": "1ben.M.Phone",
                # result.PhoneNumber if result.PhoneNumber is not None else results2.PetitionerPhone
                "FieldValue": iff(result.ben_WorkPhone)
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

        response = requests.post(
            'https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf', headers=headersAPI, data=data_json)

        # response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/html', headers=headersAPI, data=data_json)

        api_response = response.json()

        # print(api_response)
        # print(quit())

        pdf_base64 = api_response['ResultData']['PDF']
        # print()
        with open('Form G-28_for_I-485.pdf', 'wb') as pdf:
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

    shutil.move(op.join(parent_dir, 'Form G-28_for_I-485.pdf'),
                op.join(target_dir, 'Form G-28_for_I-485.pdf'))
    
    shutil.move(op.join(parent_dir, 'Form I-485.pdf'),
                op.join(target_dir, 'Form I-485.pdf'))


    print("Getting supporting docs from sharepoint..")
    get_files(
        site_url=f"https://immilytics.sharepoint.com/sites/{data_dict['beneficiary_xref']}-{data_dict['last_name']}{data_dict['first_name']}",
        sp_folder=f"Shared Documents/Document Library/Project Specific Supporting Docs/{data_dict['project_xref']}",
        dwd_dir = support_doc_dir)
    
    # wait to download file 
    time.sleep(10)

    pdfs.append(op.join(target_dir, 'Form G-28_for_I-485.pdf'))
    pdfs.append(op.join(target_dir, 'Form I-485.pdf'))
   

    if op.exists(op.join(support_doc_dir, 'ETA 9089.pdf')):
        pdfs.append(op.join(support_doc_dir, 'ETA 9089.pdf'))
    

    pdfs.append(op.join(support_doc_dir, 'I-485 Supporting Docs Final Packet.pdf'))

    os.chdir(parent_dir)

    indiv_finals_dir = op.join(target_dir,"indiv_finals_dir")
    
    if not op.exists(indiv_finals_dir):
        os.mkdir(indiv_finals_dir)
    qpdf_merger(pdfs, indiv_finals_dir, formtype)
    time.sleep(5)

    # removing individual files
    os.remove(op.join(target_dir, 'Form G-28_for_I-485.pdf'))
    os.remove(op.join(target_dir, 'Form I-485.pdf'))

    # qpdf_merger(pdfs, target_dir, formtype)

