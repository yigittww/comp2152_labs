# ============================================================
#  WEEK 10 LAB — Q3: SECURITY AUDIT LOG + UNIT TESTS
#  COMP2152 — Yigit Alkoc (101558073)
# ============================================================

import sqlite3
import unittest

DB_NAME = "audit.db"

def seed_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS audit_log")
    cursor.execute("""CREATE TABLE audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        user TEXT,
        action TEXT,
        severity TEXT,
        details TEXT
    )""")
    sample_data = [
        ("2026-03-16 08:00:00", "admin", "LOGIN", "LOW", "Successful login"),
        ("2026-03-16 08:05:00", "root", "FAILED_LOGIN", "HIGH", "Failed SSH attempt"),
        ("2026-03-16 08:10:00", "admin", "FILE_ACCESS", "LOW", "Read config"),
        ("2026-03-16 08:15:00", "root", "FAILED_LOGIN", "HIGH", "Failed SSH attempt"),
        ("2026-03-16 08:20:00", "guest", "FILE_MODIFY", "MEDIUM", "Modified upload"),
        ("2026-03-16 08:25:00", "admin", "PERMISSION_CHANGE", "HIGH", "Changed shadow"),
        ("2026-03-16 08:30:00", "guest", "LOGOUT", "LOW", "Session ended"),
        ("2026-03-16 08:35:00", "backup", "FILE_ACCESS", "LOW", "Read backup"),
        ("2026-03-16 08:40:00", "guest", "FILE_MODIFY", "MEDIUM", "Modified json"),
        ("2026-03-16 08:45:00", "admin", "LOGOUT", "LOW", "Session ended"),
    ]
    cursor.executemany("INSERT INTO audit_log (timestamp, user, action, severity, details) VALUES (?, ?, ?, ?, ?)", sample_data)
    conn.commit()
    conn.close()

def get_events_by_severity(severity):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM audit_log WHERE severity = ?", (severity,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_recent_events(limit):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM audit_log ORDER BY timestamp DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return rows

def count_by_severity():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT severity, COUNT(*) FROM audit_log GROUP BY severity ORDER BY COUNT(*) DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def safe_query(query):
    conn = sqlite3.connect(DB_NAME)
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

class TestAuditLog(unittest.TestCase):
    def setUp(self): seed_database()
    def test_high_severity(self): self.assertEqual(len(get_events_by_severity("HIGH")), 3)
    def test_recent_events(self): self.assertEqual(len(get_recent_events(5)), 5)
    def test_count(self): self.assertIn(("HIGH", 3), count_by_severity())
    def test_safe_bad_query(self): self.assertEqual(safe_query("SELECT * FROM fake_table"), [])

if __name__ == "__main__":
    seed_database()
    unittest.main(verbosity=2, exit=False)