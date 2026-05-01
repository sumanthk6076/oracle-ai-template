# Data Documentation

## Source
All data in this repository is **100% synthetic**.
No real customer, vendor, employee, or financial data is used anywhere.

## Fictional Company
**GlobalManufacturing Corp** — a fictional multinational manufacturer
used across all 13 repos in this portfolio.

| Org ID    | Region                       |
|-----------|------------------------------|
| CORP_US   | United States operations     |
| CORP_EMEA | Europe, Middle East, Africa  |
| CORP_APAC | Asia Pacific                 |

## Data Volume
Default: **500 records** per run.
Change by setting `FIXTURE_COUNT=1000` in your `.env` file.

## Regenerating Data
To reset all data and start fresh:
```bash
python generate_fixtures.py
```
This drops and recreates all tables with new synthetic data.
Safe to run multiple times.

## Schema — ap_invoices

| Column       | Type           | Example Value        | Notes                          |
|--------------|----------------|----------------------|--------------------------------|
| invoice_id   | VARCHAR2(20)   | AP-2025-00001        | Primary key, sequential        |
| vendor_name  | VARCHAR2(100)  | Acme Industrial      | One of 12 fictional suppliers  |
| invoice_date | DATE           | 15-JAN-2025          | Within last 120 days           |
| due_date     | DATE           | 15-FEB-2025          | invoice_date + 30/45/60 days   |
| amount_usd   | NUMBER(12,2)   | 45250.00             | Random $500 - $85,000          |
| status       | VARCHAR2(20)   | UNPAID               | UNPAID / PAID / ON HOLD        |
| hold_reason  | VARCHAR2(50)   | PRICE_VARIANCE       | Null for most invoices         |
| org_id       | VARCHAR2(20)   | CORP_US              | One of 3 org IDs               |
| po_number    | VARCHAR2(20)   | PO-48291             | Random 5-digit PO number       |

## Hold Reasons
| Hold Reason     | Meaning                                    |
|-----------------|--------------------------------------------|
| PRICE_VARIANCE  | Invoice amount differs from PO amount      |
| PO_MISMATCH     | Invoice references a non-existent PO       |
| MISSING_RECEIPT | No goods receipt recorded against this PO  |

## Why Synthetic Data
Oracle ERP consulting engagements involve confidential
client financial data. This portfolio uses Faker-generated
data to demonstrate identical technical patterns without
exposing any real information. The data structures, volumes,
and business scenarios are representative of real Oracle
AP implementations.
