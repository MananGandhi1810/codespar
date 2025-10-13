import requests
from typing import Optional


def web_request(url: str, headers: Optional[dict] = {}, body: Optional[dict] = {}, form_data: Optional[dict] = {}, method: Optional[str] = "GET") -> dict:
    """
    Makes a web request and returns status code, response headers, cookies, and the content
    Params:
    - url: https://example.com/path?args=123
    - headers: {"X-Email": "testing@example.com"}
    - body: {"hello": "world"}
    - form_data: {"hello": "world"}
    - method: ["GET", "POST", "PUT", "PATCH", "DELETE"]
    """
    if method not in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        return {"error": f"Invalid method {method}"}
    if not url or not url.startswith("http"):
        return {"error": "URL must start with http or https"}
    if not headers:
        headers = {}
    if not body:
        body = {}
    if not form_data:
        form_data = {}
    function_calls = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
        "PATCH": requests.patch,
        "DELETE": requests.delete,
    }
    function_call = function_calls[method]
    response = None
    try:
        response = function_call(
            url,
            headers=headers,
            json=body,
            data=body,
        )
    except Exception as e:
        return {"error": str(e)}

    print(response.status_code, response.headers, response.content.decode("utf-8"))

    return {
        "status_code": response.status_code,
        "headers": {k: v for k, v in response.headers.items()},
        "content": response.content.decode("utf-8"),
    }
