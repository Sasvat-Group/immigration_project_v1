from flask import make_response
from RPA_Process.master import RPA_Quick_Form_Automation


class Services:

    def runRPAQuickFormAutomation(self):
        result = RPA_Quick_Form_Automation()
        if not result:
            return make_response({"Error": "RPA Process got failed"}, 422)
        return make_response({"target_dir": result[1], "file_list": result[2]}, 200)
