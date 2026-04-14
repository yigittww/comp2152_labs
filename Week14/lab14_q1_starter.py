import urllib.request
import json

def make_request(url):
    response = urllib.request.urlopen(url)
    body = response.read().decode()
    status = response.status
    headers = dict(response.headers)

    return {
        "status": status,
        "headers": headers,
        "body": body
    }

def parse_json(body):
    try:
        return json.loads(body)
    except:
        return {}

def check_api_info(response):
    headers = response["headers"]

    print("\n--- Security Checks ---")

    # Server info leak
    if "Server" in headers:
        print(f"[!] Server exposed: {headers['Server']}")

    # Technology leak
    if "X-Powered-By" in headers:
        print(f"[!] Technology exposed: {headers['X-Powered-By']}")

    # CORS issue
    if headers.get("Access-Control-Allow-Origin") == "*":
        print("[!] CORS is wide open (*)")

# Test
url = "http://example.com"
res = make_request(url)

print("Status:", res["status"])
print("Headers:", res["headers"])

data = parse_json(res["body"])
print("JSON:", data)

check_api_info(res)