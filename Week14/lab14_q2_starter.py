import urllib.request

required_headers = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Strict-Transport-Security"
]

def check_headers(url):
    response = urllib.request.urlopen(url)
    headers = dict(response.headers)

    results = {}

    for header in required_headers:
        results[header] = header in headers

    return results

def generate_report(url, results):
    print(f"\nChecking: {url}")

    for header, present in results.items():
        if present:
            print(f"✓ {header}")
        else:
            print(f"✗ {header} (Missing - security risk)")

# Test
urls = ["http://example.com"]

for url in urls:
    results = check_headers(url)
    generate_report(url, results)