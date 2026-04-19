# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — [Yigit Alkoc]
# ============================================================

import urllib.request

# the must-have security headers
REQUIRED_HEADERS = {
    "Content-Type":              "Defines the content format",
    "X-Frame-Options":           "Vulnerable to clickjacking",
    "X-Content-Type-Options":    "Vulnerable to MIME sniffing",
    "Strict-Transport-Security": "No HTTPS enforcement",
    "Content-Security-Policy":   "No XSS protection policy",
    "X-XSS-Protection":          "No XSS filter",
}

def check_headers(url):
    # hits the url and checks if it has the required security headers
    try:
        with urllib.request.urlopen(url) as res:
            hdrs = dict(res.headers)
            scan_results = []
            
            for h_name in REQUIRED_HEADERS:
                if h_name in hdrs:
                    scan_results.append({
                        "header": h_name, 
                        "present": True, 
                        "value": hdrs[h_name]
                    })
                else:
                    scan_results.append({
                        "header": h_name, 
                        "present": False, 
                        "value": "MISSING"
                    })
            return scan_results
    except Exception:
        # failed to connect or read
        return []

def generate_report(url, results):
    # prints out the findings nicely
    print(f"URL: {url}")
    missing_count = 0
    
    for item in results:
        hdr = item["header"]
        val = item["value"]
        
        if item["present"]:
            print(f"  ✓ {hdr}: {val}")
        else:
            print(f"  ✗ {hdr}: MISSING — {REQUIRED_HEADERS[hdr]}")
            missing_count += 1
            
    print(f"\n  Missing {missing_count} out of {len(results)} security headers!")

# --- Main stuff ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    targets = [
        "http://httpbin.org",
        "https://www.google.com",
    ]

    for target in targets:
        print(f"\n--- Checking {target} ---")
        findings = check_headers(target)
        
        if findings:
            generate_report(target, findings)
        else:
            print("  (could not connect or something broke)")

    print("\n" + "=" * 60)
