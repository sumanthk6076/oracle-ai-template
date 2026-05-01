"""
GlobalManufacturing Corp — Synthetic Data Generator
====================================================
Run this once to populate Oracle 23ai with test data.

Usage:
    python generate_fixtures.py

Environment variables (from .env):
    FIXTURE_COUNT   — number of records to generate (default: 500)
    ORG_IDS         — comma-separated org IDs (default: CORP_US,CORP_EMEA,CORP_APAC)
"""

import os
import random
import sys
from datetime import datetime, timedelta
from db_connect import get_connection
from dotenv import load_dotenv
from faker import Faker

sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

load_dotenv()

fake = Faker()

# ── CONFIGURATION ──
ORG_IDS = os.getenv("ORG_IDS", "CORP_US,CORP_EMEA,CORP_APAC").split(",")
RECORD_COUNT = int(os.getenv("FIXTURE_COUNT", "500"))
TODAY = datetime.today()

# ── REFERENCE DATA ──
SUPPLIERS = [
    "Acme Industrial Supplies",
    "Global Tech Parts",
    "Western Manufacturing Co",
    "Pacific Logistics Ltd",
    "Delta Components Inc",
    "Summit Raw Materials",
    "Apex Freight Services",
    "Horizon Packaging Corp",
    "Vertex Electronics",
    "CoreTech Solutions",
    "Meridian Systems",
    "Atlas Industrial Group",
]

# None appears 3x to make most invoices clean (no hold)
HOLD_REASONS = [
    None,
    None,
    None,
    "PRICE_VARIANCE",
    "PO_MISMATCH",
    "MISSING_RECEIPT",
]

PAYMENT_TERMS = [30, 45, 60]


# ── TABLE SETUP ──
def create_table(conn):
    """Drop and recreate the ap_invoices table."""
    with conn.cursor() as cur:
        # Drop if exists — ignore error if it doesn't
        cur.execute("""
            BEGIN
                EXECUTE IMMEDIATE 'DROP TABLE ap_invoices PURGE';
            EXCEPTION WHEN OTHERS THEN NULL;
            END;
        """)

        cur.execute("""
            CREATE TABLE ap_invoices (
                invoice_id      VARCHAR2(20)    PRIMARY KEY,
                vendor_name     VARCHAR2(100)   NOT NULL,
                invoice_date    DATE            NOT NULL,
                due_date        DATE            NOT NULL,
                amount_usd      NUMBER(12,2)    NOT NULL,
                status          VARCHAR2(20)    NOT NULL,
                hold_reason     VARCHAR2(50),
                org_id          VARCHAR2(20)    NOT NULL,
                po_number       VARCHAR2(20)    NOT NULL,
                created_by      VARCHAR2(50)    DEFAULT 'GENERATE_FIXTURES'
            )
        """)
        conn.commit()
        print("✅ Table ap_invoices created")


# ── DATA GENERATION ──
def build_rows(count):
    """Build a list of invoice tuples ready for Oracle insert."""
    rows = []
    for i in range(count):
        inv_date = TODAY - timedelta(days=random.randint(1, 120))
        due_date = inv_date + timedelta(days=random.choice(PAYMENT_TERMS))
        hold = random.choice(HOLD_REASONS)
        status = (
            "ON HOLD" if hold else random.choice(["UNPAID", "UNPAID", "UNPAID", "PAID"])
        )
        rows.append(
            (
                f"AP-{TODAY.year}-{i + 1:05d}",  # invoice_id
                random.choice(SUPPLIERS),  # vendor_name
                inv_date,  # invoice_date
                due_date,  # due_date
                round(random.uniform(500, 85000), 2),  # amount_usd
                status,  # status
                hold,  # hold_reason (can be None)
                random.choice(ORG_IDS),  # org_id
                f"PO-{random.randint(10000, 99999)}",  # po_number
            )
        )
    return rows


# ── INSERT DATA ──
def insert_rows(conn, rows):
    """Bulk insert rows into Oracle using executemany."""
    with conn.cursor() as cur:
        cur.executemany(
            """
            INSERT INTO ap_invoices (
                invoice_id, vendor_name, invoice_date, due_date,
                amount_usd, status, hold_reason, org_id, po_number
            ) VALUES (
                :1, :2, :3, :4, :5, :6, :7, :8, :9
            )
        """,
            rows,
        )
        conn.commit()
    print(f"✅ {len(rows)} rows inserted into ap_invoices")


# ── VERIFICATION ──
def verify(conn):
    """Print a summary to confirm data landed correctly."""
    with conn.cursor() as cur:
        # Total count
        cur.execute("SELECT COUNT(*) FROM ap_invoices")
        total = cur.fetchone()[0]
        print(f"\n📊 Verification — {total} total records")

        # Breakdown by org
        print("\nBy organisation:")
        cur.execute("""
            SELECT org_id,
                   COUNT(*) AS count,
                   ROUND(SUM(amount_usd), 2) AS total_usd
            FROM ap_invoices
            GROUP BY org_id
            ORDER BY org_id
        """)
        for row in cur.fetchall():
            print(f"   {row[0]}: {row[1]} invoices — ${row[2]:,.2f}")

        # Breakdown by status
        print("\nBy status:")
        cur.execute("""
            SELECT status, COUNT(*) AS count
            FROM ap_invoices
            GROUP BY status
            ORDER BY status
        """)
        for row in cur.fetchall():
            print(f"   {row[0]}: {row[1]}")

        # Holds breakdown
        print("\nHolds by reason:")
        cur.execute("""
            SELECT hold_reason, COUNT(*) AS count,
                   ROUND(SUM(amount_usd), 2) AS total_usd
            FROM ap_invoices
            WHERE hold_reason IS NOT NULL
            GROUP BY hold_reason
            ORDER BY count DESC
        """)
        for row in cur.fetchall():
            print(f"   {row[0]}: {row[1]} invoices — ${row[2]:,.2f}")


# ── MAIN ──
if __name__ == "__main__":
    print(f"Generating {RECORD_COUNT} synthetic AP invoices")
    print("Company: GlobalManufacturing Corp")
    print(f"Orgs: {', '.join(ORG_IDS)}\n")

    conn = get_connection()
    create_table(conn)
    rows = build_rows(RECORD_COUNT)
    insert_rows(conn, rows)
    verify(conn)
    conn.close()

    print("\n✅ Done. Run main.py to start the pipeline.")
