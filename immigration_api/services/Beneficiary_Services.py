from flask import make_response
from services.schemaServices import Database
from services.schemaServices.dbQuery import DBQueryForBeneficiary


class Beneficiary_Services:

    def __init__(self):
        self.DB = Database()
        if not self.DB.DB_Conn:
            return make_response({"Error": "Database is not available!"}, 404)

    def getBeneficiaryImmigrationTimeLine(self, bid):
        try:
            h1b = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_H1B, (bid,))
            runp = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_RECENT_UNDERLYING_NIV_PETITION, (bid,))
            rpa = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_RECENT_PERM_APPLICATION, (bid,))
            ri140p = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_RECENT_I140_PETITION, (bid,))
            ri130p = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_RECENT_I130_PETITION, (bid,))
            raosa = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_RECENT_AOS_APPLICATION, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"h1b": h1b, "runp": runp, "rpa": rpa, "ri140p": ri140p,
                                  "ri130p": ri130p, "raosa": raosa}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryQuickAssessmentForm(self, bid):
        try:
            ben_details = self.DB.queryOne(DBQueryForBeneficiary().QA_BEN_DETAILS, (bid,))
            niv = self.DB.queryOne(DBQueryForBeneficiary().QA_NIV, (bid,))
            niv_ead = self.DB.queryOne(DBQueryForBeneficiary().QA_NIV_EAD, (bid,))
            aos_ead = self.DB.queryOne(DBQueryForBeneficiary().QA_AOS_EAD, (bid,))
            advanced_parol = self.DB.queryOne(DBQueryForBeneficiary().QA_ADVANCE_PAROL, (bid,))
            re_entry_permit = self.DB.queryOne(DBQueryForBeneficiary().QA_RE_ENTRY_PERMIT, (bid,))
            green_card = self.DB.queryOne(DBQueryForBeneficiary().QA_GREEN_CARD, (bid,))
            immigration = self.DB.queryOne(DBQueryForBeneficiary().QA_IMMIGRATION, (bid,))
            i797 = self.DB.queryOne(DBQueryForBeneficiary().QA_FORM_I_797, (bid,))
            i129s = self.DB.queryOne(DBQueryForBeneficiary().QA_FORM_I_129S, (bid,))
            us_entry = self.DB.queryOne(DBQueryForBeneficiary().QA_US_ENTRY, ())
            visa = self.DB.queryOne(DBQueryForBeneficiary().QA_VISA, (bid,))
            pr_data = self.DB.queryOne(DBQueryForBeneficiary().QA_PR_DATA, (bid,))
            other1 = self.DB.queryOne(DBQueryForBeneficiary().QA_OTHER_1, (bid, bid))
            other2 = self.DB.queryOne(DBQueryForBeneficiary().QA_OTHER_2, (bid,))
            self.DB.DB_Conn.close()
            table_data = [niv, niv_ead, aos_ead, advanced_parol, re_entry_permit, green_card]
            return make_response({"table": table_data, "immigration": immigration, "i797": i797,
                                  "i129s": i129s, "us_entry": us_entry,
                                  "visa": visa, "pr_data": pr_data, "other1": other1, "other2": other2,
                                  "beneficiary_details": ben_details}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryImmigrationStatusKeyDates(self, bid):
        try:
            immigration = self.DB.queryOne(DBQueryForBeneficiary().ISK_IMMIGRATION_INFO, (bid,))
            i797 = self.DB.queryOne(DBQueryForBeneficiary().ISK_I_797_INFO, (bid,))
            i129s = self.DB.queryOne(DBQueryForBeneficiary().ISK_I_129S_INFO, (bid,))
            us_entry = self.DB.queryOne(DBQueryForBeneficiary().ISK_US_ENTRY_INFO, ())
            visa = self.DB.queryOne(DBQueryForBeneficiary().ISK_VISA_INFO, (bid,))
            pr_data = self.DB.queryOne(DBQueryForBeneficiary().ISK_PR_INFO, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"immigration_status": immigration, "i797": i797, "i129s": i129s,
                                  "us_entry": us_entry, "visa": visa, "pr_data": pr_data}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryProjects(self, bid):
        try:
            h1b = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_H1B, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"h1b": h1b}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryWorkAuthorizationInfo(self, bid):
        try:
            immi = self.DB.queryOne(DBQueryForBeneficiary().WAI_IMMIGRATION, (bid,))
            i797 = self.DB.queryOne(DBQueryForBeneficiary().WAI_I797, (bid,))
            aos = self.DB.queryOne(DBQueryForBeneficiary().WAI_AOS_EAD, (bid,))
            niv = self.DB.queryOne(DBQueryForBeneficiary().WAI_NIV_EAD, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"immigration": immi, "i797": i797,
                                  "aos_ead": aos, "niv_ead": niv}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryPRProcessInfo(self, bid):
        try:
            pr_process = self.DB.queryOne(DBQueryForBeneficiary().PR_PROCESS, (bid,))
            perm_project = self.DB.queryOne(DBQueryForBeneficiary().PR_PERM_Project, (bid,))
            pr_i140 = self.DB.queryOne(DBQueryForBeneficiary().PR_I140, (bid,))
            pr_i485 = self.DB.queryOne(DBQueryForBeneficiary().PR_I485, (bid,))
            pr_i130 = self.DB.queryOne(DBQueryForBeneficiary().PR_I130, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"pr_process": pr_process, "perm_project": perm_project,
                                  "i140": pr_i140, "i485": pr_i485, "i130": pr_i130}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryPriorityInfo(self, bid):
        try:
            aos_status = self.DB.queryOne(DBQueryForBeneficiary().PRIO_AOS_FILING_STATUS, (bid,))
            aos_current = self.DB.queryOne(DBQueryForBeneficiary().PRIO_AOS_FILING_ELIGIBILITY_CURRENT, (bid, bid))
            aos_upcoming = self.DB.queryOne(DBQueryForBeneficiary().PRIO_AOS_FILING_ELIGIBILITY_UPCOMING, (bid, bid))
            priority_table = self.DB.queryAll(DBQueryForBeneficiary().PRIORITY_INFO_TABLE, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"aos_filing_status": aos_status, "aos_filing_eligibility_current": aos_current,
                                  "aos_filing_eligibility_upcoming": aos_upcoming,
                                  "priority_info_table": priority_table}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryEmploymentInfo(self, bid):
        try:
            tab1 = self.DB.queryOne(DBQueryForBeneficiary().EMP_INFO_TAB1, (bid,))
            tab2 = self.DB.queryOne(DBQueryForBeneficiary().EMP_INFO_TAB2, (bid,))
            tab3 = self.DB.queryOne(DBQueryForBeneficiary().EMP_INFO_TAB3, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"emp_info_tab1": tab1, "emp_info_tab2": tab2,
                                  "emp_info_tab3": tab3}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryPassportTravel(self, bid):
        try:
            recent_travel = self.DB.queryOne(DBQueryForBeneficiary().PT_MOST_RECENT_TRAVEL, (bid,))
            passport = self.DB.queryOne(DBQueryForBeneficiary().PT_PASSPORT, (bid,))
            visa = self.DB.queryOne(DBQueryForBeneficiary().PT_VISA, (bid,))
            travel_doc = self.DB.queryOne(DBQueryForBeneficiary().PT_TRAVEL_DOCUMENT, (bid,))
            upcoming_travel = self.DB.queryOne(DBQueryForBeneficiary().PT_UPCOMING_TRAVEL, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"most_recent_travel": recent_travel, "passport": passport, "visa": visa,
                                  "travel_document": travel_doc, "upcoming_travel": upcoming_travel}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryPersonalInfo(self, bid):
        try:
            birth = self.DB.queryOne(DBQueryForBeneficiary().PI_BIRTH_INFO, (bid,))
            citizenship = self.DB.queryOne(DBQueryForBeneficiary().PI_CITIZENSHIP, (bid,))
            marital_status = self.DB.queryOne(DBQueryForBeneficiary().PI_MARITAL_STATUS, (bid, bid,))
            contact = self.DB.queryOne(DBQueryForBeneficiary().PI_CONTACT_INFO, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"birth_info": birth, "citizenship": citizenship,
                                  "marital_status": marital_status, "contact_info": contact}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

    def getBeneficiaryDMSWorkspaceLink(self, bid):
        try:
            h1b = self.DB.queryAll(DBQueryForBeneficiary().IMMI_TIMELINE_H1B, (bid,))
            self.DB.DB_Conn.close()
            return make_response({"h1b": h1b}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)
        
    def getBenificiaryBySearch(self, ben_name, dob, project_id, pet_id):
        try:
            if ben_name and dob and project_id and pet_id:
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_FULL, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%",dob, project_id, pet_id,))
            elif ben_name and not dob and not project_id and not pet_id:
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%",))
            elif ben_name or (dob and project_id):
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME_BDATE_PRJID, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%",dob, project_id,))
            elif ben_name or (dob and pet_id):
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME_BDATE_PETID, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%",dob, pet_id,))
            elif ben_name or (project_id and pet_id):
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME_PRJID_PETID, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%",project_id, pet_id,))
            elif ben_name or dob:
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME_BDATE, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%",dob,))
            elif ben_name or project_id:
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME_PRJID, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%", project_id,))
            elif ben_name or pet_id:
                ben_list = self.DB.queryAll(DBQueryForBeneficiary().BEN_SEARCH_BY_NAME_PetID, (f"{ben_name}%",f"{ben_name}%",f"{ben_name}%", pet_id,))

            return make_response({"ben_list": ben_list}, 200)
        except Exception as e:
            print(e)
            self.DB.DB_Conn.close()
            return make_response({"Error": "Bad Request"}, 400)

