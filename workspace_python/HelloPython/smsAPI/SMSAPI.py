import sys

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


## @brief This sample code demonstrate how to send sms through CoolSMS Rest API PHP
def testingsms(phone,text):
    # set api key, api secret
    api_key = "NCS2BHRMQKWJLZGF"
    api_secret = "QM4KJEJRWMUTZQS0QUST7PUIB85LH63L"
    ## 4 params(to, from, type, text) are mandatory. must be filled
    params = dict()
    params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
    params['to'] = phone # Recipients Number '01000000000,01000000001'
    params['from'] = '01046867852' # Sender number
    params['text'] = text # Message
    cool = Message(api_key, api_secret)
    try:
        response = cool.send(params)
        print("Success Count : %s" % response['success_count'])
        print("Error Count : %s" % response['error_count'])
        print("Group ID : %s" % response['group_id'])
        
        if "error_list" in response:
            print("Error List : %s" % response['error_list'])
    except CoolsmsException as e:
        print("Error Code : %s" % e.code)
        print("Error Message : %s" % e.msg)
    return "Success Count : %s" % response['success_count']