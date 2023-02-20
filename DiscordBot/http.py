import requests

DISCORD_API = "https://discord.com/api"

def handle_api_response(resp):
    body = resp.json()
    if r.status_code != 200 or "errors" in body:
        raise Exception(f"invalid status code{r.status_code} : {body}")
    return body

class DiscordAPI(object):
    def __init__(self, token):
        self._token = token

        def run(self, path, method, body):
            url = f"{DISCORD_API}{path}"
            headers = {
                "Authorization": "Bot {self._token}",
            }
            if method == "GET":
                resp = requests.get(path, headers=headers)
                return handle_api_response(resp)
            elif method == "PUT":
                resp = requests.put(path, headers=headers, body=body)
                return handle_api_response(resp)
            elif method == "POST":
                resp = requests.post(path, headers=headers, body=body)
                return handle_api_response(resp)
            else:
                raise Exception("unsupported HTTP method {method}")

if __name__ == "__main__":
    d = DISCORD_API("foo")
    v = d.run("/user/@me", "GET")
    print(v)