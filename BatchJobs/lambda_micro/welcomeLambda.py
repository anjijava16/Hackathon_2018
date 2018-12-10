import json
import sys
from callHiveProcess import *;
from callDynamoDbProcess import *;
from callAthenaProcess import *;

from io import StringIO


def validation(event, context):
    print("event Info ===> ", event);
    print("context Info ===> ", context);


def processJobBasedOnInput():
    pass


def lambda_handler(event, context):
    # get code from payload
    print("================================================")
    print("==============Calling Validation Logic Start  Here ==================")
    validation(event, context);
    print("================================================")
    print("==============End Calling Validation Logic Start  Here ==================")

    validation(event, context)
    code = event['output']
    print("Code Here ,===>", code);
    if code == 'hive':
        hiveProcess();

    return True
