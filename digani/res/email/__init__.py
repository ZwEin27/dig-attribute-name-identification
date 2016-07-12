# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-12 12:43:44
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-12 19:39:45

import os
from email_extractor import EE

res_email_extractor = EE()

class ResourceEmail():

    res_names_path = os.path.join(os.path.dirname(__file__), 'names.json')

    def match(self, token):
        if 0 == len(res_email_extractor.extract_email(token)):
            return False
        return True

res_email_obj = ResourceEmail()