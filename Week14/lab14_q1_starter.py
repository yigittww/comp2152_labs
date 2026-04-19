# ============================================================
#  WEEK 14 LAB — Q1: API EXPLORER
#  COMP2152 — [Yigit Alkoc]
# ============================================================

import urllib.request
import json

def make_request(url):
    # grab the data from the url and return status, headers, etc.
    try:
        with urllib.request.urlopen(url) as res:
            content = res.read().decode('utf-8')
            return {
                "status": res.status,
                "headers": dict(res.headers),
                "body": content
            }
    except Exception as err:
        # rip, something broke
        return {"status": 0, "headers": {}, "body": "", "error": str(err)}

def parse_json(body):
    # turn the string into a python dict
    try:
        return json.loads(body)
    except (ValueError, TypeError):
        # probably not json lol
        return None

def check_api_info(response):
    # look for basic info leaks in headers
    alerts = []
    hdrs = response.get("headers", {})

    # server version check
    if "Server" in hdrs:
        alerts.append(f"Server version exposed: {hdrs['Server']}")
    
    # tech check
    if "X-Powered-By" in hdrs:
        alerts.append(f"Technology exposed: {hdrs['X-Powered-By']}")
    
    # cors check - why is it always * if hdrs.get("Access-Control-Allow-Origin") == "*":
        alerts.append("CORS: open to all origins")
        
    return alerts

# --- Main stuff ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q1: API EXPLORER")
    print("=" * 60)

    target = "http://httpbin.org/headers"
    print(f"\n--- Hitting {target} ---")

    resp = make_request(target)

    if resp and resp.get("status"):
        print(f"  Status: {resp['status']}")

        print("\n--- Response Headers ---")
        for k, v in resp["headers"].items():
            print(f"  {k:<16}: {v}")

        print("\n--- Parsed JSON Body ---")
        parsed_data = parse_json(resp["body"])
        
        if parsed_data:
            for k, v in parsed_data.items():
                print(f"  {k}: {v}")
        else:
            print("  (not JSON or parse failed)")

        print("\n--- Security Findings ---")
        issues = check_api_info(resp)
        
        if issues:
            for issue in issues:
                print(f"  {issue}")
        else:
            print("  (all good, no issues found)")
    else:
        err_msg = resp.get("error", "unknown") if resp else "make_request returned None"
        print(f"  Error: {err_msg}")

    print("\n" + "=" * 60)
