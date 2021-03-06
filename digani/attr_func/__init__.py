# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 14:29:27
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-13 12:18:17


from telephone import *
from identifier import *
from date import *
from email import *
from text import *
from junk import *
from person import *
from location import *
from age import *
from zipcode import *
from hair import *
from eye import *
from website import *
from breast import *
from ethnicity import *
from nationality import *


# attribute names

ATTRIBUTE_NAMES_JUNK = 'junk'
ATTRIBUTE_NAMES_TELEPHONE = 'telephone'
ATTRIBUTE_NAMES_DATE = 'date'
ATTRIBUTE_NAMES_EMAIL = 'email'
ATTRIBUTE_NAMES_LOCATION = 'location'
ATTRIBUTE_NAMES_ZIPCODE ='zipcode'  # dict
ATTRIBUTE_NAMES_PERSON = 'name'
ATTRIBUTE_NAMES_TEXT = 'text'
ATTRIBUTE_NAMES_AGE ='age'
ATTRIBUTE_NAMES_WEBSITE ='website'
ATTRIBUTE_NAMES_IDENTIFIER ='identifier' # 6- more
ATTRIBUTE_NAMES_HAIR ='hair' #
ATTRIBUTE_NAMES_EYE ='eye' #
ATTRIBUTE_NAMES_BREAST ='breast' #
ATTRIBUTE_NAMES_ETHNICITY ='ethnicity' # nationality
ATTRIBUTE_NAMES_NATIONALITY ='nationality' # nationality


def dummy(attr_vals):
    return False

ATTRIBUTE_NAMES = {
    ATTRIBUTE_NAMES_TELEPHONE: AttributeFunctionTelephone.match,
    ATTRIBUTE_NAMES_IDENTIFIER: AttributeFunctionIdentifier.match,
    ATTRIBUTE_NAMES_DATE: AttributeFunctionDate.match,
    ATTRIBUTE_NAMES_ZIPCODE: AttributeFunctionZipCode.match,
    ATTRIBUTE_NAMES_AGE: AttributeFunctionAge.match,
    ATTRIBUTE_NAMES_EMAIL: AttributeFunctionEmail.match,
    ATTRIBUTE_NAMES_WEBSITE: AttributeFunctionWebsite.match,
    ATTRIBUTE_NAMES_LOCATION: AttributeFunctionLocation.match,
    ATTRIBUTE_NAMES_PERSON: AttributeFunctionPerson.match,
    ATTRIBUTE_NAMES_HAIR: AttributeFunctionHair.match,
    ATTRIBUTE_NAMES_EYE: AttributeFunctionEye.match,
    ATTRIBUTE_NAMES_BREAST: AttributeFunctionBreast.match,
    ATTRIBUTE_NAMES_ETHNICITY: AttributeFunctionEthnicity.match,
    ATTRIBUTE_NAMES_NATIONALITY: AttributeFunctionNationality.match,
    ATTRIBUTE_NAMES_JUNK: AttributeFunctionJunk.match,
    ATTRIBUTE_NAMES_TEXT: lambda _: True
}

ATTRIBUTE_NAMES_IN_ORDER = [
    ATTRIBUTE_NAMES_TELEPHONE,
    ATTRIBUTE_NAMES_ZIPCODE,
    ATTRIBUTE_NAMES_DATE,
    ATTRIBUTE_NAMES_AGE,
    ATTRIBUTE_NAMES_IDENTIFIER,
    ATTRIBUTE_NAMES_EMAIL,      
    ATTRIBUTE_NAMES_WEBSITE,
    ATTRIBUTE_NAMES_ETHNICITY,
    ATTRIBUTE_NAMES_NATIONALITY,
    ATTRIBUTE_NAMES_HAIR,
    ATTRIBUTE_NAMES_EYE,        
    ATTRIBUTE_NAMES_BREAST,     # todo
    ATTRIBUTE_NAMES_PERSON,
    ATTRIBUTE_NAMES_LOCATION,
    ATTRIBUTE_NAMES_JUNK,
    ATTRIBUTE_NAMES_TEXT        # simple return
]

IGNORED_ATTRIBUTE_NAMES = [
    '_url',
    '_cdr_id'
]



"""
ATTRIBUTE_NAMES_CITY = 'city'
ATTRIBUTE_NAMES_STATE = 'state'
ATTRIBUTE_NAMES_COUNTRY = 'country'

ATTRIBUTE_NAMES_CITY: attr_func_city,
ATTRIBUTE_NAMES_STATE: attr_func_state,
ATTRIBUTE_NAMES_COUNTRY: dummy,

ATTRIBUTE_NAMES_CITY,   # city dict contains colors
ATTRIBUTE_NAMES_STATE,
ATTRIBUTE_NAMES_COUNTRY,

"""