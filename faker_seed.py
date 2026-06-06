import random
from faker import Faker
from sqlalchemy import create_engine, text

fake = Faker()

from dotenv import load_dotenv
import os

load_dotenv()
DB_URL = os.getenv("DB_URL")

# ─────────────────────────────────────────────────────────────────────

engine = create_engine(DB_URL)

STARTUP_IDEAS = [
    "AI-driven supply chain optimization platform",
    "Peer-to-peer renewable energy trading app",
    "Blockchain-based voting system for student councils",
    "AR-powered interior design tool for renters",
    "On-demand mental health coaching for athletes",
    "Micro-lending platform for international students",
    "Smart waste management system for universities",
    "AI-based plagiarism detection for research papers",
    "Decentralized freelance marketplace for creatives",
    "Carbon credit trading platform for small businesses",
    "Personalized sleep optimization app using wearables",
    "Community-owned grocery delivery cooperative",
    "Real-time sign language translation using computer vision",
    "Gamified financial literacy platform for teens",
    "AI tutor for competitive exam preparation",
    "Hyperlocal news aggregator for college campuses",
    "Sustainable travel booking platform",
    "Student-run venture capital fund platform",
    "Remote lab access platform for science students",
    "Digital marketplace for open-source software tools",
    "AI-powered accessibility tool for visually impaired",
    "Peer-to-peer textbook exchange platform",
    "Smart parking solution for urban campuses",
    "On-demand legal aid platform for gig workers",
    "Crowdsourced urban infrastructure reporting app",
    "AI nutritionist for student dining halls",
    "Decentralized identity verification for students",
    "Subscription platform for indie music artists",
    "Mental health journaling app with AI insights",
    "Green commute rewards platform for universities",
]

COLLATERAL_TYPES = ["Laptop", "Car", "Property", "Jewelry", "Equipment",
                    "Stocks", "Real Estate", "Vehicle", "Bonds", "Art"]

LOAN_STATUSES = ["Approved", "Pending", "Rejected", "Under Review", "Disbursed", "Closed"]
APPROVAL_STATUSES = ["Approved", "Rejected", "Pending", "Under Review"]
FUND_STATUSES = ["Funded", "Pending", "Completed", "Partial", "Cancelled"]
DISPUTE_REASONS = [
    "Incorrect interest rate applied", "Payment not recorded",
    "Collateral value disputed", "Loan terms misrepresented",
    "Late payment fee incorrect", "Unauthorized loan modification",
    "Missing repayment record", "Interest calculation error",
    "Collateral not returned", "Loan disbursement delayed",
]
DISPUTE_STATUSES = ["Resolved", "Pending", "Under Review"]
AUDIT_CHANGES = [
    "Loan application submitted", "Loan amount updated",
    "Interest rate modified", "Collateral added",
    "Repayment plan changed", "Loan status updated",
    "Dispute raised", "Loan disbursed",
    "Repayment received", "Loan closed",
]
NOTIFICATION_MESSAGES = [
    "Your loan application has been received.",
    "Your loan has been approved.",
    "Repayment reminder: payment due in 7 days.",
    "Your collateral has been verified.",
    "Your repayment plan has been updated.",
    "Loan disbursement completed.",
    "A dispute has been raised on your loan.",
    "Your loan repayment has been recorded.",
    "Your loan account is now closed.",
    "New lender matched for your loan request.",
]

def generate_data():
    # ID offsets — start after existing 100 rows
    USER_START       = 101
    BORROWER_START   = 101
    LENDER_START     = 151
    LOAN_START       = 101
    AUDIT_START      = 101
    HISTORY_START    = 101
    PLAN_START       = 101
    DISPUTE_START    = 101
    NOTIF_START      = 101
    FEEDBACK_START   = 101
    RATING_START     = 101
    REFERRAL_START   = 51
    TXN_START        = 101
    COLLATERAL_START = 101
    STATUS_START     = 101
    IDEA_START       = 51
    APPLIES_START    = 101
    FUNDS_START      = 101

    N_BORROWERS = 100   # new borrowers (IDs 101-200)
    N_LENDERS   = 100   # new lenders   (IDs 201-300, users 151-250)
    N_LOANS     = 200   # new loans

    users, borrowers, lenders = [], [], []
    used_emails = set()

    # ── Users + Borrowers (101-200) ──────────────────────────────────
    for i in range(N_BORROWERS):
        uid = USER_START + i
        name = fake.name()
        first = name.split()[0].lower()
        last  = name.split()[-1].lower()
        email = f"{first}.{last}{uid}@xyz.com"
        while email in used_emails:
            email = f"{first}.{last}{uid}{random.randint(1,99)}@xyz.com"
        used_emails.add(email)
        phone = f"000-200-{str(uid).zfill(4)}"
        linkedin = f"http://xyz.com/{first}-{last}"
        inv = round(random.uniform(10000, 100000), 2)
        users.append((uid, name, email, linkedin, phone, inv))
        borrowers.append((uid, name, email, linkedin, phone, inv))

    # ── Users + Lenders (201-300 users, 151-250 lender IDs) ─────────
    for i in range(N_LENDERS):
        uid = USER_START + N_BORROWERS + i      # 201-300
        lid = LENDER_START + i                   # 151-250
        name = fake.name()
        first = name.split()[0].lower()
        last  = name.split()[-1].lower()
        email = f"{first}.{last}{uid}@xyz.com"
        while email in used_emails:
            email = f"{first}.{last}{uid}{random.randint(1,99)}@xyz.com"
        used_emails.add(email)
        phone = f"000-300-{str(uid).zfill(4)}"
        linkedin = f"http://xyz.com/{first}-{last}"
        inv = round(random.uniform(10000, 100000), 2)
        users.append((uid, name, email, linkedin, phone, inv))
        lenders.append((lid, name, email, linkedin, phone, inv))

    # ── Supporting tables ─────────────────────────────────────────────
    audit_logs, loan_histories, repayment_plans = [], [], []
    for i in range(N_LOANS):
        aid = AUDIT_START + i
        audit_logs.append((aid,
            fake.date_time_between(start_date="-2y", end_date="now"),
            random.choice(AUDIT_CHANGES)))
        loan_histories.append((HISTORY_START + i,
            fake.date_between(start_date="-2y", end_date="today")))
        repayment_plans.append((PLAN_START + i,
            round(random.uniform(300, 1500), 2),
            fake.date_between(start_date="today", end_date="+2y")))

    # ── Loan Applications ─────────────────────────────────────────────
    borrower_ids = list(range(USER_START, USER_START + N_BORROWERS))         # 101-200
    lender_ids   = list(range(LENDER_START, LENDER_START + N_LENDERS))       # 151-250
    loans = []
    for i in range(N_LOANS):
        loans.append((
            LOAN_START + i,
            random.choice(borrower_ids),
            random.choice(lender_ids),
            AUDIT_START + i,
            HISTORY_START + i,
            PLAN_START + i,
            round(random.uniform(3.5, 10.0), 2),
            round(random.uniform(2000, 50000), 2),
            round(random.uniform(5000, 80000), 2),
        ))

    # ── Disputes ──────────────────────────────────────────────────────
    disputes = []
    for i in range(N_LOANS):
        disputes.append((
            DISPUTE_START + i,
            random.choice(DISPUTE_REASONS),
            random.choice(DISPUTE_STATUSES),
            LOAN_START + i,
        ))

    # ── Notifications ─────────────────────────────────────────────────
    all_user_ids = list(range(USER_START, USER_START + N_BORROWERS + N_LENDERS))
    notifications = []
    for i in range(N_LOANS):
        notifications.append((
            NOTIF_START + i,
            random.choice(all_user_ids),
            fake.date_between(start_date="-2y", end_date="today"),
            random.choice(NOTIFICATION_MESSAGES),
        ))

    # ── Feedback ──────────────────────────────────────────────────────
    feedback = []
    for i in range(N_LOANS):
        feedback.append((
            FEEDBACK_START + i,
            random.choice(all_user_ids),
            random.randint(1, 5),
            fake.date_between(start_date="-2y", end_date="today"),
            fake.sentence(nb_words=10),
        ))

    # ── Ratings ───────────────────────────────────────────────────────
    ratings = []
    for i in range(N_LOANS):
        ratings.append((
            RATING_START + i,
            random.choice(all_user_ids),
            random.randint(1, 5),
            fake.date_between(start_date="-2y", end_date="today"),
        ))

    # ── Referrals ─────────────────────────────────────────────────────
    referrals = []
    for i in range(50):
        uid = random.choice(all_user_ids)
        referred_by = random.choice(all_user_ids)
        while referred_by == uid:
            referred_by = random.choice(all_user_ids)
        referrals.append((REFERRAL_START + i, uid, referred_by))

    # ── Transactions ──────────────────────────────────────────────────
    transactions = []
    for i in range(N_LOANS):
        transactions.append((
            TXN_START + i,
            fake.date_between(start_date="-2y", end_date="today"),
            round(random.uniform(300, 2000), 2),
            LOAN_START + i,
        ))

    # ── Collateral ────────────────────────────────────────────────────
    collaterals = []
    for i in range(N_LOANS):
        collaterals.append((
            COLLATERAL_START + i,
            random.choice(COLLATERAL_TYPES),
            round(random.uniform(2000, 50000), 2),
            LOAN_START + i,
        ))

    # ── Loan Status ───────────────────────────────────────────────────
    loan_statuses = []
    for i in range(N_LOANS):
        loan_statuses.append((
            STATUS_START + i,
            random.choice(LOAN_STATUSES),
            LOAN_START + i,
        ))

    # ── Startup Ideas ─────────────────────────────────────────────────
    startup_ideas = []
    for i in range(N_BORROWERS):
        startup_ideas.append((
            IDEA_START + i,
            USER_START + i,
            random.choice(STARTUP_IDEAS),
        ))

    # ── Applies For ───────────────────────────────────────────────────
    applies_for = []
    seen_applies = set()
    for loan in loans:
        loan_id    = loan[0]
        borrower_id = loan[1]
        key = (borrower_id, loan_id)
        if key not in seen_applies:
            seen_applies.add(key)
            applies_for.append((
                borrower_id,
                loan_id,
                random.choice(APPROVAL_STATUSES),
                fake.date_between(start_date="-2y", end_date="today"),
            ))

    # ── Funds ─────────────────────────────────────────────────────────
    funds = []
    seen_funds = set()
    for loan in loans:
        loan_id   = loan[0]
        lender_id = loan[2]
        key = (lender_id, loan_id)
        if key not in seen_funds:
            seen_funds.add(key)
            funds.append((
                lender_id,
                loan_id,
                random.choice(FUND_STATUSES),
                fake.date_between(start_date="-2y", end_date="today"),
            ))

    return (users, borrowers, lenders, audit_logs, loan_histories,
            repayment_plans, loans, disputes, notifications, feedback,
            ratings, referrals, transactions, collaterals, loan_statuses,
            startup_ideas, applies_for, funds)


def insert_data():
    (users, borrowers, lenders, audit_logs, loan_histories,
     repayment_plans, loans, disputes, notifications, feedback,
     ratings, referrals, transactions, collaterals, loan_statuses,
     startup_ideas, applies_for, funds) = generate_data()

    with engine.connect() as conn:
        print("Inserting Users...")
        conn.execute(text("""
            INSERT INTO "User" (User_ID, Name, Email, LinkedinID, PhoneNo, Investment_Amt)
            VALUES (:a,:b,:c,:d,:e,:f)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3],e=r[4],f=r[5]) for r in users])

        print("Inserting Borrowers...")
        conn.execute(text("""
            INSERT INTO Borrower (Borrower_ID, Name, Email, LinkedinID, PhoneNo, Investment_Amt)
            VALUES (:a,:b,:c,:d,:e,:f)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3],e=r[4],f=r[5]) for r in borrowers])

        print("Inserting Lenders...")
        conn.execute(text("""
            INSERT INTO Lender (Lender_ID, Name, Email, LinkedinID, PhoneNo, Investment_Amt)
            VALUES (:a,:b,:c,:d,:e,:f)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3],e=r[4],f=r[5]) for r in lenders])

        print("Inserting Audit Logs...")
        conn.execute(text("""
            INSERT INTO Audit_Log (Audit_ID, Timestamp, Changes)
            VALUES (:a,:b,:c)
        """), [dict(a=r[0],b=r[1],c=r[2]) for r in audit_logs])

        print("Inserting Loan Histories...")
        conn.execute(text("""
            INSERT INTO Loan_History (History_ID, Date_of_Record)
            VALUES (:a,:b)
        """), [dict(a=r[0],b=r[1]) for r in loan_histories])

        print("Inserting Repayment Plans...")
        conn.execute(text("""
            INSERT INTO Repayment_Plan (Plan_ID, Installment_Amt, Next_Payment_DT)
            VALUES (:a,:b,:c)
        """), [dict(a=r[0],b=r[1],c=r[2]) for r in repayment_plans])

        print("Inserting Loan Applications...")
        conn.execute(text("""
            INSERT INTO Loan_Application
            (Loan_ID, Borrower_ID, Lender_ID, Audit_ID, History_ID, Plan_ID,
             Interest_Rate, Collateral_Val, Amount)
            VALUES (:a,:b,:c,:d,:e,:f,:g,:h,:i)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3],e=r[4],f=r[5],g=r[6],h=r[7],i=r[8])
               for r in loans])

        print("Inserting Disputes...")
        conn.execute(text("""
            INSERT INTO Dispute (Dispute_ID, Reason, Status, Loan_ID)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in disputes])

        print("Inserting Notifications...")
        conn.execute(text("""
            INSERT INTO Notification (Notification_ID, User_ID, Date, Message)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in notifications])

        print("Inserting Feedback...")
        conn.execute(text("""
            INSERT INTO Feedback (Feedback_ID, User_ID, Rating_Number, Date, Comment)
            VALUES (:a,:b,:c,:d,:e)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3],e=r[4]) for r in feedback])

        print("Inserting Ratings...")
        conn.execute(text("""
            INSERT INTO Rating (Rating_ID, User_ID, Rating_Number, Date)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in ratings])

        print("Inserting Referrals...")
        conn.execute(text("""
            INSERT INTO Referral (Referral_ID, User_ID, Referred_by)
            VALUES (:a,:b,:c)
        """), [dict(a=r[0],b=r[1],c=r[2]) for r in referrals])

        print("Inserting Transactions...")
        conn.execute(text("""
            INSERT INTO Transaction_Record (Transaction_ID, Payment_DT, Amt, Loan_ID)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in transactions])

        print("Inserting Collateral...")
        conn.execute(text("""
            INSERT INTO Collateral (Collateral_ID, Type, Value, Loan_ID)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in collaterals])

        print("Inserting Loan Statuses...")
        conn.execute(text("""
            INSERT INTO Loan_Status (Status_ID, Status, Loan_ID)
            VALUES (:a,:b,:c)
        """), [dict(a=r[0],b=r[1],c=r[2]) for r in loan_statuses])

        print("Inserting Startup Ideas...")
        conn.execute(text("""
            INSERT INTO Startup_Idea (Startup_ID, Borrower_ID, Idea)
            VALUES (:a,:b,:c)
        """), [dict(a=r[0],b=r[1],c=r[2]) for r in startup_ideas])

        print("Inserting Applies For...")
        conn.execute(text("""
            INSERT INTO Applies_for (Borrower_ID, Loan_ID, Approval_Status, Approval_Date)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in applies_for])

        print("Inserting Funds...")
        conn.execute(text("""
            INSERT INTO Funds (Lender_ID, Loan_ID, Fund_Status, Fund_Date)
            VALUES (:a,:b,:c,:d)
        """), [dict(a=r[0],b=r[1],c=r[2],d=r[3]) for r in funds])

        conn.commit()
        print("\n All done! Faker data inserted successfully.")


if __name__ == "__main__":
    insert_data()