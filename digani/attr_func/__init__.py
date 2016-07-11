# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-07-07 14:29:27
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-11 16:59:40


from telephone import *
from identifier import *
from date import *
from email import *
from text import *
from junk import *
from city import *
from state import *
from person import *


# attribute names

ATTRIBUTE_NAMES_JUNK = 'junk'
ATTRIBUTE_NAMES_TELEPHONE = 'telephone'
ATTRIBUTE_NAMES_DATE = 'date'
ATTRIBUTE_NAMES_EMAIL = 'email'
ATTRIBUTE_NAMES_LOCATION = 'location'
ATTRIBUTE_NAMES_ZIP ='zip'  # dict
ATTRIBUTE_NAMES_PERSON = 'name'
ATTRIBUTE_NAMES_TEXT = 'text'
ATTRIBUTE_NAMES_AGE ='age'
ATTRIBUTE_NAMES_WEBSITE ='website'
ATTRIBUTE_NAMES_IDENTIFIER ='identifier' # 6- more
ATTRIBUTE_NAMES_HAIR ='hair' #
ATTRIBUTE_NAMES_EYE ='eye' #
ATTRIBUTE_NAMES_BREAST ='breast' #
ATTRIBUTE_NAMES_ETHNICITY ='ethnicity' # nationality


def dummy(attr_vals):
    return False

ATTRIBUTE_NAMES = {
    ATTRIBUTE_NAMES_TELEPHONE: attr_func_telephone,
    ATTRIBUTE_NAMES_IDENTIFIER: attr_func_identifier,
    ATTRIBUTE_NAMES_DATE: attr_func_date,
    ATTRIBUTE_NAMES_ZIP: dummy,
    ATTRIBUTE_NAMES_AGE: dummy,
    ATTRIBUTE_NAMES_EMAIL: attr_func_email,
    ATTRIBUTE_NAMES_WEBSITE: dummy,
    ATTRIBUTE_NAMES_LOCATION: attr_func_city,   # attr_func_location
    ATTRIBUTE_NAMES_PERSON: attr_func_person,
    ATTRIBUTE_NAMES_HAIR: dummy,
    ATTRIBUTE_NAMES_EYE: dummy,
    ATTRIBUTE_NAMES_BREAST: dummy,
    ATTRIBUTE_NAMES_ETHNICITY: dummy,
    ATTRIBUTE_NAMES_JUNK: attr_func_junk,
    ATTRIBUTE_NAMES_TEXT: lambda _: True
}

ATTRIBUTE_NAMES_IN_ORDER = [
    ATTRIBUTE_NAMES_TELEPHONE,
    ATTRIBUTE_NAMES_IDENTIFIER,
    ATTRIBUTE_NAMES_DATE,
    ATTRIBUTE_NAMES_ZIP,
    ATTRIBUTE_NAMES_AGE,
    ATTRIBUTE_NAMES_EMAIL,
    ATTRIBUTE_NAMES_WEBSITE,
    ATTRIBUTE_NAMES_HAIR,
    ATTRIBUTE_NAMES_EYE,
    ATTRIBUTE_NAMES_BREAST,
    ATTRIBUTE_NAMES_ETHNICITY,
    ATTRIBUTE_NAMES_LOCATION,
    ATTRIBUTE_NAMES_PERSON,
    ATTRIBUTE_NAMES_JUNK,
    ATTRIBUTE_NAMES_TEXT
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