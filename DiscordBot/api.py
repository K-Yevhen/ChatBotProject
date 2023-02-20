import requests

DISCORD_API = "https://discord.com/api"

def handle_api_response(resp):
    body = resp.json()
    if resp.status_code != 200:
        raise Exception(f"invalid status code{resp.status_code}: {body}")
    elif "errors" in body:
        raise Exception(f"{body}")
    return body

class DiscordAPI(object):
    def __init__(self, token):
        self._token = token

        def run(self, path, method, body=None):
            url = f"{DISCORD_API}{path}"
            headers = {
                "Authorization": "Bot {self._token}",
            }
            if method == "GET":
                resp = requests.get(url, headers=headers)
                return handle_api_response(resp)
            elif method == "PUT":
                resp = requests.put(url, headers=headers, body=body)
                return handle_api_response(resp)
            elif method == "POST":
                resp = requests.post(url, headers=headers, body=body)
                return handle_api_response(resp)
            else:
                raise Exception("unsupported HTTP method {method}")

if __name__ == "__main__":
    with open(".token") as token_file:
        token = token_file.read()[:-1]
        d = DISCORD_API("foo")
        v = d.run("/user/@me", "GET")
        print(v)