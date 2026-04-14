# ============================================================
#  WEEK 11 LAB — Q3: VULNERABILITY REPORT
#  COMP2152 — Yigit Alkoc
# ============================================================
from collections import Counter

class Finding:
    def __init__(self, subdomain, title, severity, description):
        self.subdomain = subdomain
        self.title = title
        self.severity = severity.upper()
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.subdomain} — {self.title}"

class Report:
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_by_severity(self, severity):
        return [f for f in self.findings if f.severity == severity.upper()]

    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")
        counts = Counter(f.severity for f in self.findings)
        for sev in ["HIGH", "MEDIUM", "LOW"]:
            print(f"  {sev:<8}: {counts[sev]}")
        print("  " + "-" * 40)
        for f in self.findings:
            print(f"  {f}")

if __name__ == "__main__":
    print("=" * 60)
    report = Report("CyberHunters")
    findings_data = [
        ("ssh.0x10.cloud",  "Default credentials admin:admin",   "HIGH",   "SSH server accepts admin:admin"),
        ("blog.0x10.cloud", "No HTTPS (cleartext)",              "LOW",    "Blog served over HTTP"),
        ("ftp.0x10.cloud",  "Anonymous FTP access",              "HIGH",   "FTP allows anonymous login"),
        ("api.0x10.cloud",  "Server version exposed in headers", "MEDIUM", "API returns Server header"),
        ("cdn.0x10.cloud",  "Missing security headers",          "LOW",    "No X-Frame-Options or CSP headers"),
    ]

    print("\n--- Adding Findings ---")
    for data in findings_data:
        f = Finding(*data)
        report.add_finding(f)
        print(f"  Added: {f}")

    print("\n--- Full Report ---")
    report.summary()

    print("\n--- HIGH Severity Only ---")
    for f in report.get_by_severity("HIGH"):
        print(f"  {f}")
    print("\n" + "=" * 60)