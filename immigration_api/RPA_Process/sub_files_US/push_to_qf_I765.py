import base64
import glob
import json
import os
import os.path as op
import shutil
from pathlib import Path

import requests


def generate_765(CaseID, formtype, other_objects):
    mailing_address = other_objects['mailing_address']
    current_res_address = other_objects['current_res_address']
    last_perm_address_abroad = other_objects['last_perm_address_abroad']
    perm_foreign_address = other_objects['perm_foreign_address']
    mail_addr_vs_phys_addr = other_objects['mail_addr_vs_phys_addr']
    ben_cur_emp = other_objects['ben_cur_emp']
    bit_ans = other_objects['bit_ans']
    iff = other_objects['iff']
    most_recent_entry_rec = other_objects['most_recent_entry_rec']
    most_recent_notice = other_objects['most_recent_notice']
    resp_dic = other_objects['resp_dic']
    prim_ben = other_objects['prim_ben']
    ben_high_edu = other_objects['ben_high_edu']

    conn = other_objects['conn']
    cursor = conn.cursor()
    headersAPI = other_objects['headersAPI']
    qpdf_merger = other_objects['qpdf_merger']
    parent_dir = other_objects['parent_dir']
    change_date = other_objects['change_date']
    AptSteFlr = other_objects['AptSteFlr']
    iff = other_objects['iff']
    return_high_salary = other_objects['return_high_salary']

    result = other_objects['result']
    results2 = other_objects['results2']

    if result:
        dependents = cursor.execute(
            '''select *,DATEDIFF(YY,BirthDate,GETDATE()) as Age from [dbo].[Beneficiary] where PrimaryBeneficiaryID = '{}' and not (LOWER(BirthCountry) Like '%america%' or LOWER(BirthCountry) Like '%u.s.a%' or LOWER(BirthCountry) Like '%usa%' ) and not (LOWER(CitizenshipCountry) Like '%america%' or LOWER(CitizenshipCountry) Like '%u.s.a%' or LOWER(CitizenshipCountry) Like '%usa%' ) and ((LOWER(RelationType) in('husband','spouse','wife'))  or (lower(RelationType) in('child','son','daughter','biological son','biological daughter','biological child') and ((DATEDIFF(YY,BirthDate,GETDATE()))<21))) '''.format(
                result.BeneficiaryID)).fetchall()

        ben_family = cursor.execute(
            f'''select * from BeneficiaryFamily where PrimaryBeneficiaryID = '{result.BeneficiaryID}' ''').fetchall()
        cursor.close()
        ben_father_mname = ''
        ben_father_fname = ''
        ben_father_lname = ''
        ben_mot_fname = ''
        ben_mot_lname = ''
        ben_mot_mname = ''
        for member in ben_family:
            if member.Relation.lower().__contains__('father'):
                ben_father_fname = member.FirstName
                ben_father_lname = member.LastName
                ben_father_mname = member.MiddleName

            if member.Relation.lower().__contains__('mother'):
                ben_mot_fname = member.FirstName
                ben_mot_lname = member.LastName
                ben_mot_mname = member.MiddleName

        If_I765_previously_filed = ''
        if (result.ProjectFiledDate or result.EADType or result.CurrentOtherEADExpirationDate or result.EADApExpirationDate or result.EADAPType) not in ('', None):
            If_I765_previously_filed = 'Yes'
        else:
            If_I765_previously_filed = 'No'

        if result.ben_gender.lower().strip() == 'male':
            ben_gender = 1
        elif result.ben_gender.lower().strip() == 'female':
            ben_gender = 2

        mar_stat = result.ben_mari_stat[0].lower()
        if mar_stat == 's':
            mar_stat = 1
        elif mar_stat == 'm':
            mar_stat = 2
        elif mar_stat == 'd':
            mar_stat = 3
        elif mar_stat == 'w':
            mar_stat = 4
        else:
            mar_stat = ''

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

        for dependent, person in zip(dependents, persons):
            person['FirstName'] = dependent.FirstName
            person['LastName'] = dependent.LastName
            person['MiddleName'] = dependent.MiddleName
            person['DateOfBirth'] = dependent.BirthDate
            person['BirthCountry'] = dependent.BirthCountry
            person['Relation'] = dependent.RelationType

        extension_vs_changeofstatus = ''
        if result.PTag1_Val:
            word = result.PTag1_Val.lower().strip()
            if word.__contains__('initial'):
                extension_vs_changeofstatus = 1
            elif word.__contains__('renew'):
                extension_vs_changeofstatus = 3
            else:
                extension_vs_changeofstatus = 2

        if str(result.ProjectPriorityCategory) in ["EB2", "EB-2", "Employment-Based 2nd", "Employment Based 2nd",
                                                   "203(b)(2)"]:
            result_priority_category_chkbox_val = 4
        if str(result.ProjectPriorityCategory) in ["EB3", "EB-3", "Employment-Based 3rd", "Employment Based 3rd",
                                                   "203(b)(3)(A)(ii)"]:
            result_priority_category_chkbox_val = 5

        part_4_checkbox_text = perm_foreign_address.AddressUnitType if str(
            mailing_address.Country).lower() in ('usa', 'u.s.a', 'america', 'united states of america') else ''

        ren_ext = ['renewal', 'ren.', 'ren', 'initial', 'init.', 'init', 'extension', 'ext', 'extn.', 'extn']

        form_765_code = ''
        if result.PTag1_Val and result.PTag3_Val:
            if (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "asylee ead"):
                form_765_code = "a 5"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "aos ead"):
                form_765_code = "c 9"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "asylum ead"):
                form_765_code = "c 8"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (
                    result.PTag3_Val.lower().strip() == "b-1 ead (domestic servant of niv)"):
                form_765_code = "c 17 i"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (
                    result.PTag3_Val.lower().strip() == "b-1 ead (domestic servant of usc)"):
                form_765_code = "c 17 ii"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (
                    result.PTag3_Val.lower().strip() == "b-1 ead (emp of foreign airline)"):
                form_765_code = "c 17 iii"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (
                    result.PTag3_Val.lower().strip() == "compelling circumstances"):
                form_765_code = "c 3 6"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "daca ead"):
                form_765_code = "c 3 3"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "e-1 ead"):
                form_765_code = "a 1 7"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "e-2 ead"):
                form_765_code = "a 1 7"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "e-3 ead"):
                form_765_code = "a 1 7"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "f-1 cpt"):
                form_765_code = "N/A"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "f-1 pre-opt"):
                form_765_code = "c 3 A"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "f-1 opt"):
                form_765_code = "c 3 B"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (
                    result.PTag3_Val.lower().strip() == "f-1 opt - not stem eligible"):
                form_765_code = "N/A"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "f-1 stem ead"):
                form_765_code = "c 3 C"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (
                    result.PTag3_Val.lower().strip() == "f-1 student - not work authorized"):
                form_765_code = "N/A"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "h-4 ead"):
                form_765_code = "c 2 6"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "j-2 ead"):
                form_765_code = "c 5"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "k-1 ead"):
                form_765_code = "a 6"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "k-2 ead"):
                form_765_code = "a 6"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "k-3 ead"):
                form_765_code = "a 9"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "k-4 ead"):
                form_765_code = "a 9"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "l-2 ead"):
                form_765_code = "a 1 8"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "other ead"):
                form_765_code = "N/A"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "refugee ead"):
                form_765_code = "a 3"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "paroled refugee ead"):
                form_765_code = "a 4"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "tps ead"):
                form_765_code = "a 1 2"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "u-1 ead"):
                form_765_code = "a 1 9"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "u-2 ead"):
                form_765_code = "a 2 0"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "u-3 ead"):
                form_765_code = "a 2 0"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "u-4 ead"):
                form_765_code = "a 2 0"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "u-5 ead"):
                form_765_code = "a 2 0"

            elif (result.PTag1_Val.lower().strip() in ren_ext) and (result.PTag3_Val.lower().strip() == "withholding of deportation ead"):
                form_765_code = "a 1 0"

        form_765_code = 'c 2 6'

        p2q31a = ''
        if form_765_code == 'c 3 5':
            p2q31a = most_recent_notice.ReceiptNumber if most_recent_notice.ReceiptNumber else ''
        elif form_765_code == 'c 3 6':
            p2q31a = prim_ben.ReceiptNumber if prim_ben.ReceiptNumber else ''

        data_dict = [
            {
                "FieldName": "1lawyer.ELISNumComb",
                "FieldValue": iff(result.l_USCISNumber)
            },
            {
                "FieldName": "USIMM82541.txt1.51.4.0",
                "FieldValue": form_765_code.split()[0] if len(form_765_code) > 0 else ''
            },
            {
                "FieldName": "USIMM82541.txt1.51.4.1",
                "FieldValue": form_765_code.split()[1] if len(form_765_code) > 1 else ''
            },
            {
                "FieldName": "USIMM82541.txt1.51.4.2",
                "FieldValue": form_765_code.split()[2] if len(form_765_code) > 2 else ''
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
                "FieldName": "USIMM82541.chk1.04.2",
                "FieldValue": 'Yes' if result.SSNNumber else 'No'
            },
            {
                "FieldName": "USIMM82541.chk1.01.1",
                "FieldValue": 'Yes' if not result.SSNNumber else 'No'
            },
            {
                "FieldName": "USIMM82541.chk1.01.2",
                "FieldValue": 'Yes' if not result.SSNNumber else ''
            },
            {
                "FieldName": "USIMM82541.txt1.61.3",
                "FieldValue": iff(most_recent_entry_rec.TravelDocumentNumber)
            },
            {
                "FieldName": "1ben.I94.ArrivalCityState",
                "FieldValue": most_recent_entry_rec.EntryCity + ', ' + most_recent_entry_rec.EntryState if (
                            most_recent_entry_rec.EntryCity and most_recent_entry_rec.EntryState) else ''
            },
            {
                "FieldName": "1ben.SEVIS",
                "FieldValue": iff(result.SevisNumber1)
            },
            {
                "FieldName": "USIMM82541.chk1.04.1",
                "FieldValue": iff(If_I765_previously_filed)
            },
            {
                "FieldName": "1ben.TD.ID",
                "FieldValue": iff(most_recent_entry_rec.TravelDocumentNumber)
            },
            {
                "FieldName": "1lawyer.ExtendsPrepApp",
                "FieldValue": '1'
            },
            {
                "FieldName": "USIMM82541.chk1.05",
                "FieldValue": iff(extension_vs_changeofstatus)
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
                "FieldName": "USIMM82541.txt1.57.1.1",
                "FieldValue": p2q31a
            },
            {
                "FieldName": "USIMM82541.txt3.178",
                "FieldValue": current_res_address.Country if str(current_res_address.Country).lower().strip() not in (
                'usa', 'u.s.a', 'america', 'united states of america') else last_perm_address_abroad.Country
            },
            {
                "FieldName": "1ben.SameAddr",
                "FieldValue": 'Yes' if mail_addr_vs_phys_addr else 'No'
            },
            {
                "FieldName": "1ben.H.Addr123",
                "FieldCalcOverride": True,
                "FieldValue": current_res_address.Address1 if current_res_address.Address1 and not mail_addr_vs_phys_addr else ''
            },
            {
                "FieldName": "1ben.H.AddrUnitType",
                "FieldValue": AptSteFlr(
                    current_res_address.AddressUnitType) if current_res_address.AddressUnitType and not mail_addr_vs_phys_addr else ''
            },
            {
                "FieldName": "1ben.H.Addr4",
                "FieldValue": current_res_address.AddressUnitNumber if current_res_address.AddressUnitNumber and not mail_addr_vs_phys_addr else ''
            },
            {
                "FieldName": "1ben.H.City",
                "FieldValue": current_res_address.City if current_res_address.City and not mail_addr_vs_phys_addr else ''
            },
            {
                "FieldName": "1ben.H.State",
                "FieldValue": current_res_address.StateProvince if current_res_address.StateProvince and not mail_addr_vs_phys_addr else ''
            },
            {
                "FieldName": "1ben.H.Zip",
                "FieldValue": current_res_address.PostalZipCode if current_res_address.PostalZipCode and not mail_addr_vs_phys_addr else ''
            },
            {
                "FieldName": "1ben.Gender",
                "FieldValue": iff(ben_gender)
            },
            {
                "FieldName": "1ben.Married",
                "FieldValue": iff(mar_stat)
            },
            {
                "FieldName": "1ben.F.Addr123",
                "FieldCalcOverride": True,
                "FieldValue": perm_foreign_address.Address1 if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.F.AddrUnitType",
                "FieldValue": AptSteFlr(part_4_checkbox_text)
            },
            {
                "FieldName": "1ben.F.Addr4",  # p43b blankbx
                "FieldValue": perm_foreign_address.AddressUnitNumber if str(
                    mailing_address.Country).lower().strip() in ('usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.F.City",  # p43c blankbx
                "FieldValue": perm_foreign_address.City if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.F.County",  # p43d blankbx
                "FieldValue": perm_foreign_address.StateProvince if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.F.ForeignRoute",  # p43e blankbx
                "FieldValue": perm_foreign_address.PostalZipCode if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.F.Country",  # p43f blankbx
                "FieldValue": perm_foreign_address.Country if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "USIMM82541.txt1.01",
                "FieldValue": iff(results2.WorkLocationAddress1)
            },
            {
                "FieldName": "USIMM82541.txt1.02",
                "FieldValue": iff(results2.WorkLocationAddress2)
            },
            {
                "FieldName": "USIMM82541.txt1.03",
                "FieldValue": iff(results2.WorkLocationCity)
            },
            {
                "FieldName": "USIMM82541.txt1.04",
                "FieldValue": iff(results2.WorkLocationState)
            },
            {
                "FieldName": "USIMM82541.txt1.05",
                "FieldValue": iff(results2.WorkLocationZipCode)
            },
            {
                "FieldName": "1spou.FName",
                "FieldValue": iff(p1['FirstName'])
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
                "FieldName": "USIMM82541.txt3.83",
                "FieldValue": iff(results2.OfferedWageType)
            },
            {
                "FieldName": "USIMM82541.txt3.79",
                "FieldValue": results2.OfferedWageFrom if float(results2.OfferedWageFrom.replace(',', '')) >= float(
                    ben_cur_emp.CurrentAnnualSalary.replace(',', '')) else ben_cur_emp.CurrentAnnualSalary
            },
            {
                "FieldName": "USIMM82541.txt3.74",
                "FieldValue": iff(results2.JobTitle)
            },
            {
                "FieldName": "USIMM82541.txt3.78.0",
                "FieldValue": iff(results2.SOCCODE.split('-')[0].strip())
            },
            {
                "FieldName": "USIMM82541.txt3.78.1",
                "FieldValue": iff(results2.SOCCODE.split('-')[1].strip())
            },
            {
                "FieldName": "USIMM82541.txt3.68.0",
                "FieldValue": change_date(results2.PERMFilingDate)
            },
            {
                "FieldName": "USIMM82541.txt3.68.1",
                "FieldValue": change_date(results2.PERMValidTo)
            },
            {
                "FieldName": "USIMM82541.txt3.38",
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
                "FieldValue": result.MiddleName if result.MiddleName is not None else results2.PetitionerContactMiddleInitial
            },
            {
                "FieldName": "1contact.SEmp.Company",
                "FieldValue": result.PetitionerName if result.PetitionerName is not None else (
                            str(results2.PetitionerContactLastName) + ', ' + str(
                        results2.PetitionerContactFirstName) + ' ' + str(
                        results2.PetitionerContactMiddleInitial)).strip()
            },
            {
                "FieldName": "1contact.EO.Attn",
                "FieldValue": (str(result.FirstName if result.FirstName is not None else results2.PetitionerContactFirstName) + ' ' + str(
                        result.LastName if result.LastName is not None else results2.PetitionerContactLastName)).strip()
            },
            {
                "FieldName": "txtCalcEO.Addr1",
                "FieldValue": result.Address1 if result.Address1 is not None else results2.PetitionerContactAddress1
            },
            {
                "FieldName": "USIMM82541.chk3.11.6",
                "FieldValue": 'No'
            },
            {
                "FieldName": "USIMM82541.chk3.11.0",
                "FieldValue": 'No'
            },
            {  # part4 2a
                "FieldName": "USIMM82541.chk3.07",
                "FieldValue": '2'
            },
            {  # part4 6a
                "FieldName": "USIMM82541.chk3.10",
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
                "FieldName": "USIMM82541.chk3.27.0",
                "FieldValue": 'No' if p1['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk3.26.0",
                "FieldValue": 'Yes' if p1['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.54.1.0",
                "FieldValue": '1'
            },
            {
                "FieldName": "USIMM82541.chk3.26.1",
                "FieldValue": 'Yes' if p2['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk3.27.1",
                "FieldValue": 'No' if p2['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.26.0.0",
                "FieldValue": 'Yes' if p3['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.27.0.0",
                "FieldValue": 'No' if p3['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.54.1.2",
                "FieldValue": '1'
            },
            {
                "FieldName": "USIMM82541.chk2.26.0.1",
                "FieldValue": 'Yes' if p4['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.27.0.1",
                "FieldValue": 'No' if p4['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.26.1.0",
                "FieldValue": 'Yes' if p5['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.27.1.0",
                "FieldValue": 'No' if p5['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.26.1.1",
                "FieldValue": 'Yes' if p6['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.27.1.1",
                "FieldValue": 'No' if p6['FirstName'] else ''
            },
            {
                "FieldName": "USIMM82541.chk2.54.0",
                "FieldValue": '1'
            },
            {
                "FieldName": "User.D1272.NontechnicalDescriptionOfJob.multiline.1",
                "FieldValue": "See attached Certified ETA Form 9089"
            },
            {
                "FieldName": "1contact.EO.City",
                "FieldValue": result.City if result.City is not None else results2.PetitionerContactCity
            },
            {
                "FieldName": "USIMM82541.chk3.22",
                "FieldValue": '1'
            },
            {
                "FieldName": "USIMM82541.chk3.24",
                "FieldValue": 'Yes'
            },
            {
                "FieldName": "USIMM82541.chk3.23.0",
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
                "FieldValue": result.FederalEmployerId.replace('-',
                                                               '') if result.FederalEmployerId is not None else str(
                    results2.FEIN).replace('-', '')
            },
            {
                "FieldName": "USIMM82541.chk1.04",
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
                "FieldValue": result.b_middlename if result.b_middlename is not None else results2.BeneficiaryMiddleName
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
                "FieldName": "1ben.M.Attn",
                "FieldValue": (str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName) + ' ' + str(
                        result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)).strip()
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
                "FieldValue": mailing_address.StateProvince if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.M.County",
                "FieldValue": mailing_address.StateProvince if str(mailing_address.Country).lower().strip() not in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.M.Zip",
                "FieldValue": mailing_address.PostalZipCode if str(mailing_address.Country).lower().strip() in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
            },
            {
                "FieldName": "1ben.M.ForeignRoute",
                "FieldValue": mailing_address.PostalZipCode if str(mailing_address.Country).lower().strip() not in (
                'usa', 'u.s.a', 'america', 'united states of america') else ''
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
                "FieldValue": result.SSNNumber if result.SSNNumber else 'N/A'
            },
            {
                "FieldName": "1ben.I94.ArrivalDate",
                "FieldValue": most_recent_entry_rec.EntryDate.strftime(
                    '%m/%d/%Y') if most_recent_entry_rec.EntryDate is not None else ''
            },
            {
                "FieldName": "1ben.I94.IDComb",
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
                "FieldName": "1ben.GOV.ID",
                "FieldValue": iff(result.PassportNumber)
            },
            {
                "FieldName": "1ben.GOV.IDCountry",
                "FieldValue": iff(result.pp_IssuingCountry)
            },
            {
                "FieldName": "1ben.GOV.IDExpire",
                "FieldValue": change_date(most_recent_entry_rec.ValidTo)
            },
            {
                "FieldName": "USIMM82541.txt3.19.1",
                "FieldValue": (str(result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName) + ' ' + str(
                        result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName)).strip()
            },
            {
                "FieldName": "USIMM82541.txt3.19.0",
                "FieldValue": mailing_address.Address1 if mailing_address.Address1 is not None else results2.BeneficiaryAddress1
            },
            {
                "FieldName": "USIMM82541.txt3.24.0",
                "FieldValue": mailing_address.AddressUnitNumber if mailing_address.AddressUnitNumber is not None else results2.BeneficiaryAddress2
            },
            {
                "FieldName": "USIMM82541.chk3.09",
                "FieldValue": AptSteFlr(mailing_address.AddressUnitType)
            },
            {
                "FieldName": "USIMM82541.txt3.29.0",
                "FieldValue": mailing_address.City if mailing_address.City is not None else results2.BeneficiaryAddressCity
            },
            {
                "FieldName": "USIMM82541.txt3.29.2",
                "FieldValue": mailing_address.StateProvince if mailing_address.StateProvince is not None else results2.BeneficiaryAddressState
            },
            {
                "FieldName": "USIMM82541.txt3.29.3",
                "FieldValue": mailing_address.PostalZipCode if mailing_address.PostalZipCode is not None else results2.BeneficiaryAddressZipCode
            },
            {
                "FieldName": "USIMM82541.txt3.34",
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
                "FieldName": "User.D1272.1contact.SEmp.NumEmployeesUS",
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
                "FieldValue": iff(result.p_NaicsCode)
            },
            {
                "FieldName": "USIMM82541.txt3.01.1",
                "FieldValue": (str(iff(result.l_firstname)) + ' ' + str(iff(result.l_lastname))).strip()
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
                "FieldName": "USIMM82541.txt3.525",
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
            {
                "FieldName": "USIMM82541.chk1.22",
                "FieldValue": 1
            },
            {
                "FieldName": "1ben.CurrentStatus",
                "FieldValue": iff(most_recent_entry_rec.I94StatusType)
            },
            {
                "FieldName": "User.F82541.J1ExchangeVisitor",
                "FieldValue": 'Yes' if ((str(most_recent_entry_rec.I94StatusType.lower() in ('j1', 'j2'))) or (
                            result.HasPreviouslyHeldJVisaStatus == 1)) else 'No'
            },
            {
                "FieldName": "USIMM82541.chk1.26",
                "FieldValue": 1
            },
            {
                "FieldName": "1lawyer.FullName",
                "FieldValue": f'{result.l_lastname}, {iff(result.l_firstname)}'
            },
            {
                "FieldName": "USIMM82541.chk1.23",
                "FieldValue": 1
            },
            {
                "FieldName": "1ben.NonImmigExpiry",
                "FieldValue": change_date(most_recent_entry_rec.I94ExpirationDate)
            }
        ]

        if form_765_code == 'c 3 C':
            if ben_high_edu:
                data_dict.extend([
                    {
                        "FieldName": "USIMM82541.txt1.51.9.0",
                        "FieldValue": iff(ben_high_edu.DegreeType)
                    },
                    {
                        "FieldName": "USIMM82541.txt1.51.9.1",
                        "FieldValue": result.p_EmployerEVerifyName if result.p_EmployerEVerifyName else iff(
                            ben_cur_emp.EmployerEVerifyName) if ben_cur_emp else ''
                    },
                    {
                        "FieldName": "USIMM82541.txt1.51.11",
                        "FieldValue": result.p_EmployerEVerifyNumber if result.p_EmployerEVerifyNumber else ben_cur_emp.EmployerEVerifyNumber if ben_cur_emp.EmployerEVerifyNumber else ''
                    }
                ])

        if form_765_code == 'c 2 6':
            if prim_ben:
                # p2 29
                data_dict.append(
                    {
                        "FieldName": "USIMM82541.txt1.51.15.0.0",
                        "FieldValue": iff(prim_ben.ReceiptNumber)
                    })

        if form_765_code == 'c 8':
            data_dict.extend([
                {
                    "FieldName": "USIMM82541.chk1.8765",
                    "FieldValue": resp_dic.get('7', '')
                },
                {
                    "FieldName": "USIMM82541.chk1.8756",
                    "FieldValue": 'Yes' if most_recent_entry_rec.IsInspectedAdmitted else 'No'
                },

                {
                    "FieldName": "USIMM82541.txt1.57.1.0",
                    "FieldValue": change_date(
                        result.AsylumReportedDateToDHS) if result.AsylumReportedDateToDHS else 'No'
                }
            ])

            if not most_recent_entry_rec.IsInspectedAdmitted:
                data_dict.append({
                    "FieldName": "USIMM82541.chk1.87",
                    "FieldValue": 'Yes' if result.AsylumReportedToDHS else 'No'
                })

            if result.AsylumReportedToDHS:
                data_dict.extend([
                    {
                        "FieldName": "USIMM82541.txt1.57.2",
                        "FieldValue": iff(result.AsylumReportedDHSLocation)
                    },
                    {
                        "FieldName": "USIMM82541.txt1.57.3",
                        "FieldValue": iff(result.AsylumPersecutionCountry)
                    },
                    {
                        "FieldName": "User.D1272.ExplanationEnteringUSIllegaly.multiline.1",
                        "FieldValue": iff(resp_dic.get('87', ''))
                    }
                ])

        if form_765_code in ('c 3 5', 'c 3 6'):
            data_dict.extend([
                {
                    "FieldName": "USIMM82541.chk3.43.165.0",
                    "FieldValue": iff(resp_dic.get('7', ''))
                }
            ])

        params = {
            "HostFormOnQuik": True,
            "FormFields": data_dict,
            "QuikFormID": "82541",
            "PrintEditablePDF": True
        }

        data_json = json.dumps(params)
        response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf',
                                 headers=headersAPI, data=data_json)
        api_response = response.json()
        pdf_base64 = api_response['ResultData']['PDF']
        with open('Form I-765.pdf', 'wb') as pdf:
            pdf.write(base64.b64decode(pdf_base64))

        data_dict2 = [
            {
                "FieldName": "1ben.AlienRegNumComb",
                "FieldValue": result.AlienNumber1 if result.AlienNumber1 is not None else results2.BeneficiaryAlienNumber
            },
            {
                "FieldName": "1lawyer.ELISNumComb",
                "FieldValue": iff(result.l_USCISNumber)
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
                "FieldValue": result.l_middlename if result.l_middlename is not None else results2.AttorneyAgentMiddleInitial
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
                "FieldValue": ('Form I-140 - ' + str(
                    result.b_lastname if result.b_lastname is not None else results2.BeneficiaryLastName) + ', ' + str(
                    result.b_firstname if result.b_firstname is not None else results2.BeneficiaryFirstName) + ' ' + str(
                    result.b_middlename if result.b_middlename is not None else results2.BeneficiaryMiddleName)).strip()
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
        response = requests.post('https://websvcs.quikforms.com/rest/quikformsengine/qfe/execute/pdf',
                                 headers=headersAPI, data=data_json)
        api_response = response.json()
        pdf_base64 = api_response['ResultData']['PDF']
        with open('Form G-28_for_I-765.pdf', 'wb') as pdf:
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
        pdf_merge_sequence(data_dict, formtype, result, results2, most_recent_entry_rec, most_recent_notice, parent_dir,
                           iff, change_date, qpdf_merger)

    else:
        print('No Matching record in db to Process..')


def pdf_merge_sequence(data_dict, formtype, result, results2, most_recent_entry_rec, most_recent_notice, parent_dir,
                       iff, change_date, qpdf_merger):
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

    support_doc_dir = op.join(target_dir, 'Supporting Docs')
    project_level_dir = op.dirname(target_dir)

    if not op.exists(support_doc_dir):
        Path(support_doc_dir).mkdir(parents=True, exist_ok=True)

    if op.exists(support_doc_dir):
        pdfs = []
        sequence = ["Masters Degree", "Masters Transcripts", "Bachelors Degree", "Bachelors Transcripts",
                    "EVL", "Additional Supporting Docs", "Misc. Docs", "Passport", "I-94", "Pay Stub",
                    "PR Sponsorship Letter"]

        sequence_multiple = [
            "Additional Supporting Docs", "Misc. Docs", "Pay Stubs"]
        pdf_files = glob.glob(op.join(support_doc_dir, "*.pdf"))

        shutil.move(op.join(parent_dir, 'Form G-28_for_I-765.pdf'),
                    op.join(target_dir, 'Form G-28_for_I-765.pdf'))
        shutil.move(op.join(parent_dir, 'Form I-765.pdf'),
                    op.join(target_dir, 'Form I-765.pdf'))

        pdfs.append(op.join(target_dir, 'Form G-28_for_I-765.pdf'))
        pdfs.append(op.join(target_dir, 'Form I-765.pdf'))
        pdfs.append(op.join(support_doc_dir, 'ETA 9089.pdf'))

        for seq in sequence:
            for pdf_f in glob.glob(seq + "*"):
                pdfs.append(op.join(support_doc_dir, pdf_f))

        latest_annual_report = 0
        latest_annual_report_file = ''
        for pdf_f in glob.glob(op.join(project_level_dir, "*.pdf")):
            if "Annual Report" in pdf_f:
                file_name_annual = op.splitext(op.basename(pdf_f))
                file_name_split = (str(file_name_annual[0]).strip()).split(' ')
                if int(file_name_split[-1]) > latest_annual_report:
                    latest_annual_report = int(file_name_split[-1])
                    latest_annual_report_file = pdf_f
            elif "Tax Docs" in pdf_f:
                pdfs.append(op.join(project_level_dir, pdf_f))

        if latest_annual_report_file:
            pdfs.append(op.join(project_level_dir, latest_annual_report_file))

        os.chdir(parent_dir)
        qpdf_merger(pdfs, target_dir, formtype)

    else:
        print(f'Appropriate folder structure\n{support_doc_dir}\nnot found')
