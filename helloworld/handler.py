#178.128.40.109
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    try:
        par = json.loads(req)
    except Exception as e:
        par = e

    return json.dumps({
        "environment": "dev", 
        "request": req,
        "parsed_request": par,
    })
