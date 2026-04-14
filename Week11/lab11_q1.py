# ============================================================
#  WEEK 11 LAB — Q1: SERVER LOG ANALYZER
#  COMP2152 — Yigit Alkoc
# ============================================================

class LogAnalyzer:
    def __init__(self):
        self.logs = []

    def add_log(self, status_code, endpoint):
        self.logs.append({"code": status_code, "path": endpoint})

    def count_errors(self):
        return sum(1 for log in self.logs if log["code"] >= 400)

    def get_endpoints(self):
        return list(set(log["path"] for log in self.logs))

    def print_summary(self):
        print(f"Total Logs: {len(self.logs)}")
        print(f"Error Count: {self.count_errors()}")
        print("Unique Endpoints:", ", ".join(self.get_endpoints()))

if __name__ == "__main__":
    analyzer = LogAnalyzer()
    analyzer.add_log(200, "/home")
    analyzer.add_log(404, "/admin")
    analyzer.add_log(500, "/api/data")
    analyzer.add_log(200, "/home")
    
    print("--- Log Summary ---")
    analyzer.print_summary()