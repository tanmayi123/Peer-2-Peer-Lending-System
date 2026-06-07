# Peer-to-Peer Lending Analytics System

A full-stack data analytics and data engineering project built around a peer-to-peer lending platform connecting University student borrowers with alumni investors. The project covers the entire data pipeline from database design and synthetic data generation through to a deployed interactive dashboard and published Tableau visualizations. This project is only a simulation of P2P Lending system.

Live Dashboard: [Streamlit App](https://your-app.streamlit.app)

Tableau: [P2P Lending Platform Overview](https://public.tableau.com/app/profile/tanmayi.shurpali/viz/P2P-Lending-System/P2PLendingSystem-PlatformOverview)

<img width="1509" height="821" alt="p2p2" src="https://github.com/user-attachments/assets/9d2aa288-427c-4625-931c-9954b521f33a" />

<img width="1512" height="821" alt="p2p1" src="https://github.com/user-attachments/assets/af0980dc-6000-42e0-8819-e8d21326287d" />



---

## Project Background

Traditional funding routes for student entrepreneurs involve banks, research grants, and scholarship programs. These processes are slow, rigid, and loaded with eligibility barriers. The idea behind this platform is to cut out the middleman entirely and connect students with startup ideas directly to alumni investors who want to fund them.

The analytics layer built on top of this platform surfaces insights across the full loan lifecycle, from application and approval through funding, repayment, and dispute resolution. The goal was to build something that looks and functions like a real production analytics system, not just a class project.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Database | PostgreSQL hosted on Supabase |
| Data Generation | Python, Faker |
| Data Transformation | SQL Views, SQLAlchemy, psycopg2 |
| Dashboard | Streamlit, Plotly |
| Business Intelligence | Tableau Public |
| Deployment | Streamlit Cloud |
| Version Control | Git, GitHub |

---

## Database Design

The relational schema was designed in MySQL and migrated to PostgreSQL on Supabase for cloud hosting. It consists of 18 normalized tables covering the full domain of a peer-to-peer lending platform.

**Core Tables**

- User, Borrower, Lender
- Loan_Application, Loan_Status, Loan_History
- Repayment_Plan, Transaction_Record
- Collateral, Dispute, Audit_Log
- Notification, Feedback, Rating, Referral
- Startup_Idea, Applies_for, Funds

**Key Design Decisions**

- Borrowers and Lenders inherit from a base User table using shared primary keys, enforcing referential integrity across all three user types
- One loan can have multiple lenders but only one borrower, reflecting real P2P lending structures
- Audit logs and loan history tables provide full traceability of every state change on the platform
- Dispute management is tied directly to individual loans, allowing transactions to be paused during resolution

---

## Data Pipeline

### Synthetic Data Generation

Real user data was never used. All data was generated programmatically using Python's Faker library, which is the standard approach for building realistic synthetic datasets for portfolio and development projects.

The data generation script (`faker_seed.py`) connects directly to the Supabase PostgreSQL instance and inserts data across all 18 tables in the correct dependency order to satisfy foreign key constraints.

**Dataset Scale**

- 300 users (150 borrowers, 150 lenders)
- 300 loan applications
- 300 disputes, notifications, feedback records, ratings, transactions, collateral entries
- 150 startup ideas (one per borrower)
- 100 referrals

Data was inserted in two phases. The first phase used hand-crafted SQL INSERT statements with obviously fake identifiers (emails ending in @xyz.com, phone numbers starting with 000) to establish the base dataset. The second phase used Faker to scale up to the full dataset size.

### Environment and Credentials

Database credentials are managed via a `.env` file locally using `python-dotenv`, and via Streamlit Cloud's secrets manager in the deployed environment. The `.env` file is excluded from version control via `.gitignore`.

---

## Analytics Layer

Six SQL views were created in Supabase to serve as the analytics layer between the raw tables and the dashboard. These views compute derived metrics that would be expensive to recalculate on every query.

**vw_loan_summary**
Joins loan applications with borrower, lender, status, approval, fund, and repayment data into a single flat view. Used as the primary reporting layer for loan-level analysis.

**vw_borrower_risk**
Computes per-borrower risk metrics including loan-to-value ratio, collateral coverage percentage, rejection rate, dispute count, and average rating. Uses NULLIF to handle division-by-zero edge cases safely.

**vw_lender_performance**
Aggregates lender activity including total capital deployed, fund status breakdown (completed, pending, cancelled, partial), average interest rate, and average borrower rating of each lender.

**vw_repayment_health**
Calculates repayment progress per loan including total paid, outstanding balance, repayment completion percentage, and payment health classification (On Track, Due Soon, Overdue) using CURRENT_DATE comparisons.

**vw_platform_overview**
Monthly aggregation of loan volume, approval rates, rejection rates, and dispute counts. Uses DATE_TRUNC to bucket by month and computes approval rate as a percentage using NULLIF-safe division.

**vw_startup_funding**
Joins startup ideas with borrower loan data to show total funding received per startup, approval rates, collateral coverage, and dispute frequency per idea.

---

## Streamlit Dashboard

The dashboard connects live to the Supabase database via psycopg2 on every page load. There is no caching layer or static data involved. All charts and tables reflect the current state of the database.

### Pages

**Home**
Project overview explaining the platform concept, tech stack breakdown, and a summary of what each analytics page covers.

**Platform Overview**
Monthly loan volume bar chart, approval rate trend line, application status donut chart, and a combined loans vs disputes chart. KPI cards show total loans, total volume, average approval rate, average interest rate, and total disputes.

**Borrower Risk Analysis**
Top borrowers by average loan amount, loan-to-value ratio distribution, rejection rate vs dispute count scatter plot colored by borrower rating, and collateral coverage distribution. Full sortable data table included.

**Lender Performance**
Top lenders by total capital deployed, fund status donut chart, rating vs total amount lent scatter plot, and lender rating distribution histogram. Full sortable data table included.

**Repayment Health**
Repayment status breakdown, payment health bar chart (On Track, Due Soon, Overdue), repayment completion distribution, and outstanding balance vs loan amount scatter colored by payment health. Filterable table by payment health status.

### Design

The dashboard uses a custom CSS theme with DM Serif Display for headings and DM Sans for body text.
Each chart includes an insight callout below it explaining what the data shows in plain language.

---

## Tableau Dashboard

A Tableau Public dashboard was built using CSV exports of the six SQL views. The dashboard covers platform-level analytics with four sheets composed into a single interactive view.

**Loan Volume with Month-over-Month Growth**
Dual axis chart combining a bar chart of monthly loan volume with a line showing month-over-month percentage change. A dashed reference line at zero separates growth months from decline months. Uses a LOOKUP table calculation to compute MoM growth.

**Approval Rate vs Platform Average**
Bar chart where each bar is colored based on whether that month's approval rate is above or below the platform average. The platform average is computed using a FIXED LOD expression and rendered as a constant reference line. Above-average months are colored green and below-average months are colored coral.

**Cumulative Loan Volume**
Area chart using a RUNNING_SUM table calculation to show cumulative platform growth from launch. A secondary line shows actual monthly volume, and a linear trend line from the Analytics pane shows the overall directional trend.

**Loan Count vs Average Interest Rate**
Dual axis chart showing total loans as bars colored by whether the average interest rate that month is above or below the platform average (computed via FIXED LOD), with the interest rate itself as a secondary line. Reveals whether high-volume months correlate with more or less competitive interest rates.

---

## Project Structure

```
Peer-2-Peer-Lending-System/
│
├── app.py                  # Streamlit dashboard
├── faker_seed.py           # Synthetic data generation script
├── export_to_csv.py        # Exports SQL views to CSV for Tableau
├── requirements.txt        # Python dependencies
├── .env                    # Local environment variables (not committed)
├── .gitignore
│
├── tableau_data/           # CSV exports for Tableau Public
│   ├── vw_platform_overview.csv
│   ├── vw_borrower_risk.csv
│   ├── vw_lender_performance.csv
│   ├── vw_repayment_health.csv
│   ├── vw_loan_summary.csv
│   └── vw_startup_funding.csv
│
└── DMA_SQL_SCRIPT.sql      # Original MySQL schema
```

---

## Setup and Running Locally

**Prerequisites**
- Python 3.9 or higher
- A Supabase account with the schema and data loaded
- pip

**Installation**

```bash
git clone https://github.com/tanmayi123/Peer-2-Peer-Lending-System.git
cd Peer-2-Peer-Lending-System
pip install -r requirements.txt
```

**Environment Setup**

Create a `.env` file in the root directory:

```
DB_URL=postgresql://postgres.YOUR_PROJECT_REF:YOUR_PASSWORD@aws-0-us-east-1.pooler.supabase.com:6543/postgres
```

**Run the dashboard**

```bash
streamlit run app.py
```

**Regenerate synthetic data**

```bash
python faker_seed.py
```

**Export CSVs for Tableau**

```bash
python export_to_csv.py
```

---

## Requirements

```
streamlit
pandas
plotly
psycopg2-binary
python-dotenv
faker
sqlalchemy
```

---

## Key Analytical Concepts Used

- Loan-to-value ratio as a borrower risk signal
- Collateral coverage percentage to measure loan security
- Month-over-month growth using LOOKUP table calculations in Tableau
- FIXED LOD expressions to compute platform-wide averages independent of view filters
- RUNNING_SUM to show cumulative platform growth over time
- Repayment health classification using date arithmetic against CURRENT_DATE
- Rejection rate as a proxy for borrower creditworthiness on the platform

---
