import responses
import json

@responses.activate
def mockRequestsGet(url: str, data: json, statusCode: int):
    responses.add(
        responses.GET,
        url,
        json=data,
        status=statusCode
    )