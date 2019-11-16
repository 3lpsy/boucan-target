from flask import request as current_request
from functools import wraps
import requests


def proxyable(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # httpoxy
        headers = dict(current_request.headers).copy()
        if headers.get("Proxy", None):
            proxy = current_request.headers.get("Proxy")
            proxies = {"http": proxy, "https": proxy}
            del headers["Proxy"]
            if current_request.method.upper() in ["PUT", "PATCH", "POST", "DELETE"]:
                command = getattr(requests, current_request.method.lower(), "get")
                return command(
                    current_request.url,
                    data=dict(current_request.form),
                    proxies=proxies,
                    headers=headers,
                ).content
            elif current_request.method.upper() == "GET":
                command = requests.get
                return command(
                    current_request.url, proxies=proxies, headers=headers
                ).content
        return f(*args, **kwargs)

    return decorated_function
