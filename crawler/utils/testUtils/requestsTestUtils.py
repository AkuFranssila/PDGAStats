import json


def mock_requests_get(url: str, data: json, mock_request: any):
    """
    Mocks requests Get with url and json data
    """
    text_content = data.get('content')
    if not text_content:
        text_content = data.get('data')
    mock_request.get(url, text=text_content)
