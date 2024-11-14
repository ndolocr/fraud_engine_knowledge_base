from django.shortcuts import render
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view

from KnowledgeBase.models import Rule
from KnowledgeBase.models import Request

# Create your views here.

@api_view(['GET'])
def getAllRules(request):
    if request.method == "GET":
        try:
            rules = Rule.objects.all()
            rules_list = list(rules.values())

            return JsonResponse(
                {
                    "responseObject": {
                        "code": 1,
                        'data': rules_list
                    },
                    "statusCode": "00",
                    "successful": True,
                    "statusMessage": "Success"                        
                }
            )
        except ObjectDoesNotExist as o:
            message = f"Rule Objects do not exist in the databse --> {o}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        except Exception as e:
            message = f"Error occured while accessing Rules from the databse --> {e}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        else:
            message = f"Wrong request type. This is a 'GET' Request! "
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )

@api_view(['GET'])
def getRuleByNamespace(request, namespace):
    if request.method == "GET":
        try:
            rules = Rule.objects.filter(ruleNamespace = namespace)
            rules_list = list(rules.values())

            return JsonResponse(
                {
                    "responseObject": {
                        "code": 1,
                        'data': rules_list
                    },
                    "statusCode": "00",
                    "successful": True,
                    "statusMessage": "Success"                        
                }
            )
        except ObjectDoesNotExist as o:
            message = f"Rule Objects do not exist in the databse --> {o}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        except Exception as e:
            message = f"Error occured while accessing Rules from the databse --> {e}"
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )
        else:
            message = f"Wrong request type. This is a 'GET' Request! "
            return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        'data': message
                    },
                    "statusCode": "99",
                    "successful": False,
                    "statusMessage": "Fail"                        
                }
            )

@api_view(["POST"])
def save_request(request):
    score = request.data.get("score", "")
    decision = request.data.get("decision", "")
    cr_account = request.data.get("cr_account", "")
    dr_account = request.data.get("dr_account", "")    
    name_space = request.data.get("name_space", "")
    response_status = request.data.get("response_status", "")
    request_payload = request.data.get("request_payload", "")
    transaction_time = request.data.get("transaction_time", "")
    response_message = request.data.get("response_message", "")
    response_payload = request.data.get("response_payload", "")

    try:
        queryset = Request.objects.create(
            score = score,
            decision = decision,
            cr_account = cr_account,
            dr_account = dr_account,
            name_space = name_space,
            response_status = response_status,
            request_payload = request_payload,
            transaction_time = transaction_time,
            response_message = response_message,
            response_payload = response_payload,
        )
    except Exception as e:
        return JsonResponse(
                {
                    "responseObject": {
                        "code": -1,
                        "data": f"Error Saving Data --> {str(e)}"
                    },
                    "statusCode": "00",
                    "successful": True,
                    "statusMessage": "Success"                        
                }
            )

    return JsonResponse(
        {
            "responseObject": {
                "code": 1,
                'data': f"record Successfully Saved!"
            },
            "statusCode": "00",
            "successful": True,
            "statusMessage": "Success"                        
        }
    )