import requests
from typing import Optional


def web_request(url: str, headers: Optional[dict] = {}, body: Optional[dict] = {}, form_data: Optional[dict] = {}, cookies: Optional[dict] = {}, method: Optional[str] = "GET") -> dict:
    """
    Makes a web request and returns status code, response headers, cookies, and the content
    Params:
    - url: https://example.com/path?args=123
    - headers: {"X-Email": "testing@example.com"}
        - By default, uses a common browser user-agent and sets Referer and Origin to the url's domain
    - cookies: {"sessionid": "abcd1234"}
    - body: {"hello": "world"}
    - form_data: {"hello": "world"}
    - method: ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    """
    if method not in ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]:
        return {"error": f"Invalid method {method}"}
    if not url or not url.startswith("http"):
        return {"error": "URL must start with http or https"}
    if not headers:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Accept": "*/*",
            "Referer": url,
            "Connection": "keep-alive",
            "Origin": url.split("/")[0] + "//" + url.split("/")[2],
        }
    if not body:
        body = {}
    if not form_data:
        form_data = {}
    if not cookies:
        cookies = {}
    call_method = {
        "GET": requests.get,
        "POST": requests.post,
        "PUT": requests.put,
        "PATCH": requests.patch,
        "DELETE": requests.delete,
        "OPTIONS": requests.options,
    }
    selected_method = call_method[method]
    response = None
    try:
        response = selected_method(
            url,
            headers=headers,
            json=body,
            data=body,
            cookies=cookies,
        )
    except Exception as e:
        return {"error": str(e)}

    return {
        "status_code": response.status_code,
        "headers": {k: v for k, v in response.headers.items()},
        "content": response.content.decode("utf-8"),
    }
