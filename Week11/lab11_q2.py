# ============================================================
#  WEEK 11 LAB — Q2: PASSWORD STRENGTH CHECKER
#  COMP2152 — Yigit Alkoc
# ============================================================

class PasswordChecker:
    def __init__(self):
        self.common_passwords = {"admin", "password", "123456", "root", "guest", "letmein", "welcome"}
        self.history = []

    def check_common(self, password):
        return password.lower() in self.common_passwords

    def check_strength(self, password):
        return {
            "length": len(password) >= 8,
            "digit": any(c.isdigit() for c in password),
            "special": any(c in "!@#$%^&*" for c in password)
        }

    def evaluate(self, password):
        if self.check_common(password):
            res = "WEAK (common password)"
        else:
            stats = self.check_strength(password)
            score = sum(stats.values())
            levels = {0: "WEAK", 1: "WEAK", 2: "MEDIUM", 3: "STRONG"}
            res = levels.get(score, "WEAK")
                
        self.history.append((password, res))
        return res

if __name__ == "__main__":
    print("=" * 60)
    checker = PasswordChecker()
    test_passwords = ["admin", "hello", "hello123", "MyP@ss99", "p@ssw0rd!", "root"]

    print("\n--- Checking Passwords ---")
    for pw in test_passwords:
        print(f"  {pw:<15} → {checker.evaluate(pw)}")

    print("\n--- Check History ---")
    for pw, res in checker.history:
        print(f"  {pw:<15} : {res}")
    print("\n" + "=" * 60)