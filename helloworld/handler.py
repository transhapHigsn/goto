#178.128.40.109
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    body = json.dumps(req)
    nex = json.loads(body)

    try:
        par = json.loads(req)
    except Exception as e:
        par = e

    return json.dumps({
        "body": body,
        "nex": nex,
        "request": req,
        "par": par,
    })
