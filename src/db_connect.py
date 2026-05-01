"""
Oracle Autonomous 23ai — Connection Helper
All repos use this single module for database connections.
"""

import oracledb
import os
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """
    Returns a connection to Oracle Autonomous 23ai.
    Reads all credentials from environment variables (.env file).
    Uses wallet-based mTLS for secure connection.
    """
    return oracledb.connect(
        user=os.getenv("ORACLE_USER"),
        password=os.getenv("ORACLE_PASSWORD"),
        dsn=os.getenv("ORACLE_DSN"),
        config_dir=os.getenv("ORACLE_WALLET_DIR"),  # 👈 add this
        wallet_location=os.getenv("ORACLE_WALLET_DIR"),
        wallet_password=os.getenv("ORACLE_WALLET_PASSWORD"),
    )


def test_connection():
    """
    Quick sanity check — run to verify Oracle connection is working.
    Usage: python src/db_connect.py
    """
    try:
        conn = get_connection()
        print(f"✅ Connected to Oracle {conn.version}")

        with conn.cursor() as cur:
            cur.execute("SELECT 'Connection verified' AS status FROM dual")
            result = cur.fetchone()
            print(f"   Query test: {result[0]}")

        conn.close()
        print("   Connection closed cleanly.")

    except Exception as e:
        print(f"❌ Connection failed: {e}")
        print("\nCheck:")
        print("  1. ORACLE_WALLET_DIR path is correct and absolute")
        print("  2. ORACLE_DSN matches a name in wallet/tnsnames.ora")
        print("  3. ORACLE_PASSWORD is your ADB admin password")
        print("  4. ADB instance is running (not auto-paused)")


if __name__ == "__main__":
    test_connection()
