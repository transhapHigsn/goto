178.128.40.109
import json

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    body = json.dumps(req)
    # nex = json.loads(req)

    return body
