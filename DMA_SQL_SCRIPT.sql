SET SQL_SAFE_UPDATES = 0;

CREATE TABLE User (
    User_ID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    LinkedinID VARCHAR(255),
    PhoneNo VARCHAR(15) NOT NULL,
    Investment_Amt DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Lender (
    Lender_ID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    LinkedinID VARCHAR(255),
    PhoneNo VARCHAR(15) NOT NULL,
    Investment_Amt DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Lender_ID) REFERENCES User(User_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Borrower (
    Borrower_ID INT PRIMARY KEY NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE,
    LinkedinID VARCHAR(255),
    PhoneNo VARCHAR(15) NOT NULL,
    Investment_Amt DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Borrower_ID) REFERENCES User(User_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Audit_Log (
    Audit_ID INT PRIMARY KEY NOT NULL,
    Timestamp DATETIME,
    Changes TEXT
);

CREATE TABLE Loan_History (
    History_ID INT PRIMARY KEY NOT NULL,
    Date_of_Record DATE NOT NULL
);

CREATE TABLE Repayment_Plan (
    Plan_ID INT PRIMARY KEY NOT NULL,
    Installment_Amt DECIMAL(10, 2) NOT NULL,
    Next_Payment_DT DATE NOT NULL
);

CREATE TABLE Loan_Application (
    Loan_ID INT PRIMARY KEY NOT NULL,
    Borrower_ID INT NOT NULL,
    Lender_ID INT NOT NULL,
    Audit_ID INT,
    History_ID INT,
    Plan_ID INT,
    Interest_Rate DECIMAL(5, 2) NOT NULL,
    Collateral_Val DECIMAL(10, 2),
    Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (Borrower_ID) REFERENCES Borrower(Borrower_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Lender_ID) REFERENCES Lender(Lender_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Audit_ID) REFERENCES Audit_Log(Audit_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (History_ID) REFERENCES Loan_History(History_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Dispute (
    Dispute_ID INT PRIMARY KEY NOT NULL,
    Reason TEXT NOT NULL,
    Status VARCHAR(50),
    Loan_ID INT NOT NULL,
    FOREIGN KEY (Loan_ID) REFERENCES Loan_Application(Loan_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Notification (
    Notification_ID INT PRIMARY KEY NOT NULL,
    User_ID INT NOT NULL,
    Date DATE NOT NULL,
    Message TEXT NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Feedback (
    Feedback_ID INT PRIMARY KEY NOT NULL,
    User_ID INT NOT NULL,
    Comment TEXT,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Referral (
    Referral_ID INT PRIMARY KEY NOT NULL,
    User_ID INT NOT NULL,
    Referred_by INT NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Transaction_Record (
    Transaction_ID INT PRIMARY KEY NOT NULL,
    Payment_DT DATE NOT NULL,
    Amt DECIMAL(10, 2) NOT NULL,
    Loan_ID INT NOT NULL,
    FOREIGN KEY (Loan_ID) REFERENCES Loan_Application(Loan_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Collateral (
    Collateral_ID INT PRIMARY KEY NOT NULL,
    Type VARCHAR(255) NOT NULL,
    Value DECIMAL(10, 2) NOT NULL,
    Loan_ID INT,
    FOREIGN KEY (Loan_ID) REFERENCES Loan_Application(Loan_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Loan_Status (
    Status_ID INT PRIMARY KEY NOT NULL,
    Status VARCHAR(50) NOT NULL,
    Loan_ID INT,
    FOREIGN KEY (Loan_ID) REFERENCES Loan_Application(Loan_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Rating (
    Rating_ID INT PRIMARY KEY NOT NULL,
    User_ID INT NOT NULL,
    Date DATE NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Startup_Idea (
    Startup_ID INT PRIMARY KEY NOT NULL,
    Borrower_ID INT NOT NULL,
    Idea TEXT NOT NULL,
    FOREIGN KEY (Borrower_ID) REFERENCES Borrower(Borrower_ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Applies_for (
    Borrower_ID INT NOT NULL,
    Loan_ID INT NOT NULL,
    Approval_Status VARCHAR(50),
    Approval_Date DATE NOT NULL,
    PRIMARY KEY (Borrower_ID, Loan_ID),
    FOREIGN KEY (Borrower_ID) REFERENCES Borrower(Borrower_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Loan_ID) REFERENCES Loan_Application(Loan_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE Funds (
    Lender_ID INT NOT NULL,
    Loan_ID INT NOT NULL,
    Fund_Status VARCHAR(50),
    Fund_Date DATE NOT NULL,
    PRIMARY KEY (Lender_ID, Loan_ID),
    FOREIGN KEY (Lender_ID) REFERENCES Lender(Lender_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Loan_ID) REFERENCES Loan_Application(Loan_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

INSERT INTO User (User_ID, Name, Email, LinkedinID, PhoneNo, Investment_Amt) VALUES
(1, 'Tiffany Wilson', 'luishogan@perkins.info', 'http://hurley-hester.net/', '+11092541995', 55127.50),
(2, 'Justin Thomas', 'sherylspencer@welch-huynh.org', 'http://jarvis-moore.com/', '+11429836089', 67151.08),
(3, 'James Parsons', 'mgolden@hotmail.com', 'http://valenzuela-garcia.com/', '+13204571900', 96748.39),
(4, 'Gabriel Williams', 'youngrodney@gmail.com', 'http://jones-jacobs.org/', '+18503034453', 90714.04),
(5, 'Tammy Miller', 'vdorsey@hotmail.com', 'http://choi.org/', '+16869663938', 61845.37),
(6, 'Mark Bryant', 'jodimoore@yahoo.com', 'http://kim-harper.com/', '+18539013310', 86006.71),
(7, 'Julie Nichols', 'matthewjones@garcia.com', 'http://mcgee.org/', '+13274701908', 43296.42),
(8, 'Brad Mays', 'theresajenkins@williams.info', 'http://powell-miller.net/', '+17639319118', 32675.18),
(9, 'Michael Moore', 'sperez@yahoo.com', 'http://wade-baker.com/', '+13146067243', 19873.73),
(10, 'Christopher Vega', 'rgordon@cook.com', 'http://davidson.net/', '+15369030240', 67381.90),
(11, 'Sarah Watkins', 'rburton@gmail.com', 'http://long.com/', '+12093882735', 92593.20),
(12, 'David Fuller', 'howellnicholas@hotmail.com', 'http://diaz-king.org/', '+12645194778', 14537.54),
(13, 'Jessica Bryant', 'vfitzgerald@gmail.com', 'http://jackson.info/', '+14055090543', 45342.09),
(14, 'Daniel James', 'peterscynthia@gmail.com', 'http://richardson-harris.com/', '+12439978785', 38712.82),
(15, 'Nancy Walker', 'edwardscourtney@gmail.com', 'http://gray-barnett.org/', '+11896894579', 90493.02),
(16, 'Steven Gregory', 'gonzalesjessica@hotmail.com', 'http://brown.com/', '+11913554452', 67280.62),
(17, 'Andrew Miller', 'martinsharon@yahoo.com', 'http://morales.biz/', '+18496309256', 45372.50),
(18, 'Christine Patterson', 'joanwatson@gmail.com', 'http://bryant-powers.net/', '+13932143605', 80547.86),
(19, 'Scott Thomas', 'fishercharles@bell.net', 'http://bennett-holloway.biz/', '+16765872590', 18638.75),
(20, 'Larry Schmidt', 'robinsonanthony@hotmail.com', 'http://williams-meyer.com/', '+17889290557', 53796.90),
(21, 'Robert Murphy', 'smorales@yahoo.com', 'http://morgan-graham.org/', '+17624876533', 72680.57),
(22, 'Ronald Long', 'jsmith@hotmail.com', 'http://garcia.org/', '+19478546595', 93014.32),
(23, 'Kimberly Garcia', 'lewisjamie@hotmail.com', 'http://nelson.org/', '+18368144374', 40195.56),
(24, 'Heather Johnson', 'stanleyrichard@yahoo.com', 'http://powell.org/', '+12103854643', 28076.90),
(25, 'Brandon Jones', 'vmcdonald@gmail.com', 'http://turner-fox.biz/', '+18791584674', 90286.44),
(26, 'Dennis Hernandez', 'jramos@gmail.com', 'http://robinson-patterson.com/', '+19067594381', 49382.62),
(27, 'Maria Miller', 'waltersjudy@gmail.com', 'http://mitchell.biz/', '+14102076459', 18794.30),
(28, 'Eric Fisher', 'dorisjohnson@gmail.com', 'http://butler-anderson.biz/', '+14595370257', 58647.23),
(29, 'Brenda Hernandez', 'bcole@gmail.com', 'http://murphy.com/', '+14803802753', 71903.15),
(30, 'Gary Adams', 'scottross@hotmail.com', 'http://russell.biz/', '+13272407620', 67282.51);

INSERT INTO Borrower (Borrower_ID, Name, Email, LinkedinID, PhoneNo, Investment_Amt) VALUES
(1, 'Tiffany Wilson', 'luishogan@perkins.info', 'http://hurley-hester.net/', '+11092541995', 55127.50),
(2, 'Justin Thomas', 'sherylspencer@welch-huynh.org', 'http://jarvis-moore.com/', '+11429836089', 67151.08),
(3, 'James Parsons', 'mgolden@hotmail.com', 'http://valenzuela-garcia.com/', '+13204571900', 96748.39),
(4, 'Gabriel Williams', 'youngrodney@gmail.com', 'http://jones-jacobs.org/', '+18503034453', 90714.04),
(5, 'Tammy Miller', 'vdorsey@hotmail.com', 'http://choi.org/', '+16869663938', 61845.37),
(6, 'Mark Bryant', 'jodimoore@yahoo.com', 'http://kim-harper.com/', '+18539013310', 86006.71),
(7, 'Julie Nichols', 'matthewjones@garcia.com', 'http://mcgee.org/', '+13274701908', 43296.42),
(8, 'Brad Mays', 'theresajenkins@williams.info', 'http://powell-miller.net/', '+17639319118', 32675.18),
(9, 'Michael Moore', 'sperez@yahoo.com', 'http://wade-baker.com/', '+13146067243', 19873.73),
(10, 'Christopher Vega', 'rgordon@cook.com', 'http://davidson.net/', '+15369030240', 67381.90),
(11, 'Sarah Watkins', 'rburton@gmail.com', 'http://long.com/', '+12093882735', 92593.20),
(12, 'David Fuller', 'howellnicholas@hotmail.com', 'http://diaz-king.org/', '+12645194778', 14537.54),
(13, 'Jessica Bryant', 'vfitzgerald@gmail.com', 'http://jackson.info/', '+14055090543', 45342.09),
(14, 'Daniel James', 'peterscynthia@gmail.com', 'http://richardson-harris.com/', '+12439978785', 38712.82),
(15, 'Nancy Walker', 'edwardscourtney@gmail.com', 'http://gray-barnett.org/', '+11896894579', 90493.02);

select * from lender; 
select * from borrower;
select * from loan_application;

INSERT INTO Audit_Log (Audit_ID, Timestamp, Changes) VALUES
(1, '2024-08-27 19:38:47', 'Loan application submitted by borrower.'),
(2, '2024-02-16 19:38:47', 'Lender approved the loan application.'),
(3, '2024-03-06 19:38:47', 'Borrower updated loan collateral details.'),
(4, '2024-05-03 19:38:47', 'Interest rate adjusted for loan application.'),
(5, '2024-06-04 19:38:47', 'Repayment plan updated by borrower.'),
(6, '2023-12-19 19:38:47', 'Lender added additional funds to loan.'),
(7, '2024-01-20 19:38:47', 'Dispute raised regarding loan terms.'),
(8, '2024-09-15 19:38:47', 'Loan application marked as reviewed.'),
(9, '2024-10-30 19:38:47', 'Borrower payment recorded in transaction history.'),
(10, '2024-07-05 19:38:47', 'Loan status updated to Active.'),
(11, '2024-06-14 19:38:47', 'Notification sent to borrower about upcoming payment.'),
(12, '2024-03-15 19:38:47', 'Loan closed after successful repayment.'),
(13, '2024-04-18 19:38:47', 'System audit log entry for interest adjustment.'),
(14, '2024-02-24 19:38:47', 'Referral recorded in user profile.'),
(15, '2023-11-26 19:38:47', 'Loan application rejected by lender.');

INSERT INTO Loan_History (History_ID, Date_of_Record) VALUES
(1, '2024-06-28'),
(2, '2023-06-18'),
(3, '2023-05-25'),
(4, '2023-11-18'),
(5, '2024-01-28'),
(6, '2023-12-07'),
(7, '2023-04-16'),
(8, '2024-05-05'),
(9, '2023-10-14'),
(10, '2023-08-23'),
(11, '2024-03-12'),
(12, '2024-09-29'),
(13, '2024-07-19'),
(14, '2023-09-03'),
(15, '2023-07-11');


INSERT INTO Repayment_Plan (Plan_ID, Installment_Amt, Next_Payment_DT) VALUES
(1, 1529.75, '2024-08-03'),
(2, 580.00, '2023-12-03'),
(3, 794.53, '2023-11-18'),
(4, 804.89, '2024-05-15'),
(5, 638.40, '2024-06-13'),
(6, 1262.90, '2024-01-31'),
(7, 1932.25, '2024-07-15'),
(8, 1795.55, '2024-06-18'),
(9, 1200.75, '2024-01-20'),
(10, 1403.90, '2024-06-05'),
(11, 630.00, '2024-04-11'),
(12, 1357.80, '2024-11-10'),
(13, 1700.15, '2024-09-08'),
(14, 1558.40, '2024-02-03');


INSERT INTO Loan_Application (Loan_ID, Borrower_ID, Lender_ID, Audit_ID, History_ID, Plan_ID, Interest_Rate, Collateral_Val, Amount) VALUES
(1, 1, 16, 1, 1, 1, 7.61, 34528.71, 60701.45),
(2, 2, 17, 2, 2, 2, 9.68, 16946.73, 92285.36),
(3, 3, 16, 3, 3, 3, 3.87, 11338.20, 33938.17),
(4, 4, 19, 4, 4, 4, 4.78, 25135.92, 89432.30),
(5, 5, 20, 5, 5, 5, 6.94, 10999.54, 10835.40),
(6, 6,  16, 6, 6, 6, 2.89, 21387.67, 67730.12),
(7, 7, 22, 7, 7, 7, 8.32, 38844.85, 25015.54),
(8, 8, 22, 8, 8, 8, 5.75, 13674.10, 78324.96),
(9, 9, 24, 9, 9, 9, 6.13, 47202.93, 67856.45),
(10, 10, 25, 10, 10, 10, 7.41, 15498.43, 95102.36),
(11, 10, 26, 11, 11, 11, 9.22, 26358.11, 70392.15),
(12, 12, 22, 12, 12, 12, 4.50, 21235.20, 31754.67),
(13, 13, 30, 13, 13, 13, 5.35, 40123.90, 49685.20),
(14, 14, 29, 14, 14, 14, 3.47, 18121.72, 21954.88),
(15, 14, 30, 15, 15, 15, 6.82, 32479.13, 82531.75);

select * from loan_application;

INSERT INTO Dispute (Dispute_ID, Reason, Status, Loan_ID) VALUES
(1, 'Incorrect loan terms applied', 'Resolved', 1),
(2, 'Payment not recorded correctly', 'Closed', 2),
(3, 'Interest rate discrepancy', 'Under Review', 3),
(4, 'Collateral incorrectly valued', 'Closed', 4),
(5, 'Unauthorized loan status change', 'Closed', 5),
(6, 'Late payment penalty dispute', 'Pending', 6),
(7, 'Loan amount calculation error', 'Under Review', 7),
(8, 'Repayment schedule miscalculated', 'Resolved', 8),
(9, 'Notification error on missed payment', 'Pending', 9),
(10, 'Unexpected fees applied', 'Resolved', 10);


INSERT INTO Notification (Notification_ID, User_ID, Date, Message) VALUES
(1, 21, '2024-02-15', 'Loan application approved.'),
(2, 17, '2023-11-23', 'New repayment schedule available.'),
(3, 11, '2024-09-30', 'Your loan status has been updated.'),
(4, 18, '2024-01-03', 'Upcoming payment due soon.'),
(5, 4, '2024-05-18', 'Payment successfully received.'),
(6, 13, '2023-10-11', 'Document verification completed.'),
(7, 2, '2024-07-21', 'Reminder: Payment due in 3 days.'),
(8, 16, '2024-04-04', 'Notification on updated interest rate.'),
(9, 7, '2023-12-27', 'Dispute status has been resolved.'),
(10, 26, '2024-06-30', 'Your feedback has been recorded.'),
(11, 15, '2024-08-19', 'New message from lender.'),
(12, 9, '2024-03-25', 'Repayment missed - please contact support.'),
(13, 30, '2023-09-14', 'Collateral information updated.'),
(14, 10, '2024-02-08', 'Loan application requires additional info.'),
(15, 5, '2023-11-01', 'Transaction history available for download.');

INSERT INTO Feedback (Feedback_ID, User_ID, Comment) VALUES
(1, 19, 'Great platform for peer-to-peer lending.'),
(2, 2, 'Easy to use and very informative.'),
(3, 28, 'Found the loan approval process seamless.'),
(4, 20, 'Interest rates could be more competitive.'),
(5, 2, 'Appreciate the transparency in transactions.'),
(6, 15, 'Support team was very helpful.'),
(7, 9, 'Quick response to disputes.'),
(8, 22, 'Could use more flexible repayment options.'),
(9, 5, 'Loan process was a bit lengthy but worth it.'),
(10, 12, 'Highly recommend for new borrowers.'),
(11, 16, 'Platform offers excellent guidance on loans.'),
(12, 6, 'Interest rates are fair and competitive.'),
(13, 3, 'Enjoyed the user-friendly interface.'),
(14, 25, 'Platform should add more notification features.'),
(15, 11, 'Support team solved my issue promptly.'),
(16, 27, 'Collateral process could be simplified.'),
(17, 7, 'Found helpful resources for managing loans.'),
(18, 30, 'Transparent fee structure is a plus.'),
(19, 14, 'Would like more personalized loan options.'),
(20, 17, 'User experience is top-notch.'),
(21, 10, 'Loan amount options fit my needs well.'),
(22, 13, 'Repayment process was smooth and easy to track.'),
(23, 18, 'Found answers to questions in the FAQ section.'),
(24, 8, 'Good for both borrowers and lenders.'),
(25, 23, 'System alerts help keep me on track.'),
(26, 4, 'Easy account setup and verification.'),
(27, 21, 'Loan status updates are very useful.'),
(28, 29, 'Clear communication from lenders.'),
(29, 1, 'Reliable platform for financial support.'),
(30, 26, 'Could benefit from more customization options.');


INSERT INTO Referral (Referral_ID, User_ID, Referred_by) VALUES
(1, 1, 27),
(2, 2, 30),
(3, 3, 27),
(4, 4, 16),
(5, 5, 29),
(6, 6, 21),
(7, 7, 22),
(8, 8, 19),
(9, 9, 18),
(10, 10, 24),
(11, 11, 20),
(12, 12, 25),
(13, 13, 28),
(14, 14, 23),
(15, 15, 26);

INSERT INTO Transaction_Record (Transaction_ID, Payment_DT, Amt, Loan_ID) VALUES
(1, '2023-11-09', 2485.92, 1),
(2, '2024-04-24', 4629.82, 2),
(3, '2024-08-12', 4091.88, 3),
(4, '2024-02-16', 1608.54, 4),
(5, '2023-12-07', 1013.55, 5),
(6, '2023-10-23', 3725.60, 6),
(7, '2024-01-15', 1540.73, 7),
(8, '2024-05-29', 2112.99, 8),
(9, '2023-11-19', 1327.44, 9),
(10, '2024-03-10', 2958.68, 10),
(11, '2023-12-28', 3874.90, 11),
(12, '2024-06-14', 975.65, 12),
(13, '2024-07-21', 2514.30, 13),
(14, '2023-09-05', 3289.42, 14),
(15, '2024-02-26', 1984.50, 15);

INSERT INTO Collateral (Collateral_ID, Type, Value, Loan_ID) VALUES
(1, 'Real Estate', 46763.66, 1),
(2, 'Vehicle', 29751.60, 2),
(3, 'Equipment', 30144.87, 3),
(4, 'Inventory', 41822.99, 4),
(5, 'Accounts Receivable', 14454.38, 5),
(6, 'Cash Deposit', 18250.45, 6),
(7, 'Stocks', 25110.73, 7),
(8, 'Bonds', 19530.21, 8),
(9, 'Gold', 32984.54, 9),
(10, 'Machinery', 28475.15, 10),
(11, 'Intellectual Property', 45982.67, 11),
(12, 'Artwork', 22840.79, 12),
(13, 'Jewelry', 18790.33, 13),
(14, 'Insurance Policy', 37204.56, 14),
(15, 'Farm Land', 26983.40, 15);

INSERT INTO Loan_Status (Status_ID, Status, Loan_ID) VALUES
(1, 'Approved', 1),
(2, 'Pending', 2),
(3, 'Active', 3),
(4, 'Closed', 4),
(5, 'In Review', 5),
(6, 'Defaulted', 6),
(7, 'Under Investigation', 7),
(8, 'Settled', 8),
(9, 'Suspended', 9),
(10, 'Partially Paid', 10),
(11, 'Fully Paid', 11),
(12, 'Refinanced', 12),
(13, 'Overdue', 13),
(14, 'Payment Deferred', 14),
(15, 'Written Off', 15);

ALTER TABLE Rating
ADD Rating_Number INT NOT NULL,
ADD Comment TEXT;

INSERT INTO Rating (Rating_ID, User_ID, Date, Rating_Number, Comment) VALUES
(1, 1, '2024-04-12', 5, 'The platform made loan processing simple and effective.'),
(2, 2, '2024-04-05', 1, 'Interest rates are fair, but some features could improve.'),
(3, 3, '2024-03-26', 5, 'The system is efficient for tracking loan progress.'),
(4, 4, '2024-11-03', 1, 'Loan approval was surprisingly fast and easy.'),
(5, 5, '2024-04-03', 5, 'Repayment process was clear and organized.'),
(6, 6, '2024-06-01', 2, 'Support was quick to respond to my queries.'),
(7, 7, '2023-12-19', 5, 'Reliable notifications helped me stay on schedule.'),
(8, 8, '2023-09-29', 4, 'Great experience with a straightforward process.'),
(9, 9, '2023-10-25', 3, 'Useful platform for managing peer-to-peer loans.'),
(10, 10, '2024-03-08', 5, 'Appreciate the platform''s transparency on fees.'),
(11, 11, '2024-05-13', 4, 'Navigating the platform was intuitive and helpful.'),
(12, 12, '2024-02-27', 5, 'Solid platform with helpful loan status updates.'),
(13, 13, '2024-09-05', 4, 'Clear documentation for the entire loan journey.'),
(14, 14, '2023-11-15', 5, 'Good overall experience with transparent terms.'),
(15, 15, '2024-01-17', 5, 'Smooth loan disbursement process and good guidance.'),
(16, 16, '2023-10-07', 5, 'Good platform for exploring lending options.'),
(17, 17, '2024-02-01', 4, 'System is user-friendly with responsive updates.'),
(18, 18, '2023-11-14', 5, 'Platform provided good loan tracking capabilities.'),
(19, 19, '2024-09-27', 3, 'Overall pleased with the flexibility in payments.'),
(20, 20, '2024-07-15', 5, 'App interface was easy to use and informative.'),
(21, 21, '2024-04-19', 4, 'Timely reminders for payments are appreciated.'),
(22, 22, '2023-12-06', 5, 'Loan terms were clear and easy to follow.'),
(23, 23, '2024-01-20', 4, 'Notifications about loan progress were useful.'),
(24, 24, '2024-06-30', 3, 'The platform could add more repayment options.'),
(25, 25, '2024-05-01', 5, 'Impressed with the quick loan disbursal.'),
(26, 26, '2024-08-10', 4, 'Good transparency on loan details and requirements.'),
(27, 27, '2023-10-31', 5, 'Helpful for both borrowers and lenders alike.'),
(28, 28, '2024-03-12', 3, 'Received useful guidance throughout the process.'),
(29, 29, '2024-04-24', 5, 'Trustworthy platform for peer-to-peer lending.'),
(30, 30, '2024-05-26', 4, 'Platform is reliable for personal financial needs.');

INSERT INTO Startup_Idea (Startup_ID, Borrower_ID, Idea) VALUES
(1, 1, 'Develop an AI-driven personal finance assistant.'),
(2, 2, 'Create a platform for eco-friendly product rentals.'),
(3, 3, 'Launch a sustainable packaging solutions startup.'),
(4, 4, 'Build a mobile app for mental health tracking.'),
(5, 5, 'Establish a virtual reality education platform.'),
(6, 6, 'Introduce a smart home energy management system.'),
(7, 7, 'Create an online marketplace for handmade goods.'),
(8, 8, 'Build a blockchain-based property rental platform.'),
(9, 9, 'Start a subscription box for wellness products.'),
(10, 10, 'Develop an AI-powered recruitment platform.'),
(11, 11, 'Create a platform for remote workspaces.'),
(12, 12, 'Build an app for local farm produce deliveries.'),
(13, 13, 'Establish a digital art and NFT marketplace.'),
(14, 14, 'Launch a personalized travel itinerary planner.'),
(15, 15, 'Start an online platform for tutoring services.');

delete from startup_idea where startup_id = 17;


INSERT INTO Startup_Idea (Startup_ID, Borrower_ID, Idea) VALUES
(18, 3, 'Data Privacy for cybersecurity in Public Campsuses'),
(19, 4, 'AI driven solar power in northeastern univeristy'),
(20, 6, 'Tree Plantation drive at Northeastern University');
INSERT INTO Startup_Idea (Startup_ID, Borrower_ID, Idea) VALUES
(17, 1, 'Virtual Assistant for students');



INSERT INTO Applies_for (Borrower_ID, Loan_ID, Approval_Status, Approval_Date) VALUES
(1, 1, 'Rejected', '2024-03-07'),
(2, 2, 'Approved', '2024-01-01'),
(3, 3, 'Approved', '2024-02-12'),
(4, 4, 'Under Review', '2024-05-20'),
(5, 5, 'Rejected', '2023-11-25'),
(6, 6, 'Pending', '2023-10-18'),
(7, 7, 'Approved', '2024-06-15'),
(8, 8, 'Under Review', '2023-12-09'),
(9, 9, 'Approved', '2024-08-03'),
(10, 10, 'Rejected', '2024-04-10'),
(11, 11, 'Pending', '2024-02-21'),
(12, 12, 'Approved', '2024-07-29'),
(13, 13, 'Approved', '2023-09-17'),
(14, 14, 'Under Review', '2024-06-04'),
(15, 15, 'Rejected', '2023-11-01');

INSERT INTO Funds (Lender_ID, Loan_ID, Fund_Status, Fund_Date) VALUES
(16, 1, 'Funded', '2024-03-01'),
(17, 2, 'Pending', '2024-01-17'),
(18, 3, 'Completed', '2024-06-07'),
(19, 4, 'Partial', '2023-12-23'),
(20, 5, 'Pending', '2024-03-08'),
(21, 6, 'Cancelled', '2023-11-04'),
(22, 7, 'Funded', '2024-08-19'),
(23, 8, 'Completed', '2024-04-29'),
(24, 9, 'Partial', '2023-09-15'),
(25, 10, 'Pending', '2024-02-10'),
(26, 11, 'Funded', '2023-10-31'),
(27, 12, 'Completed', '2024-05-05'),
(28, 13, 'Cancelled', '2024-07-26'),
(29, 14, 'Funded', '2023-11-12'),
(30, 15, 'Completed', '2024-06-14');

#
# 1. List of Start up idea that a borrower has submitted
select b.borrower_id as 'Borrower Id', b.name as 'Borrower Name',s.idea as 'Startup Idea' from borrower b, startup_idea s
where b.borrower_id = s.borrower_id;

# 2. Using group by function to List the Start up idea that a borrower has submitted
select b.borrower_id as 'Borrower Id', b.name as 'Borrower Name',GROUP_CONCAT(s.idea SEPARATOR ', ') AS 'Startup Ideas'
from borrower b, startup_idea s
where b.borrower_id = s.borrower_id
group by b.borrower_id;

# 3. STARTUP IDEA THE LENDER FUNDS FOR
SELECT l.LENDER_ID, l.NAME AS 'LENDER NAME', l.INVESTMENT_AMT, idea as 'IDEA' FROM
LENDER L, LOAN_APPLICATION LA, STARTUP_IDEA S 
WHERE 
LA.BORROWER_ID= S.BORROWER_ID AND
L.LENDER_ID= LA.LENDER_ID;

select * from audit_log;

# 4. what changes has been made by the borrower to the loan application
SELECT 
    B.Name AS 'Borrower Name', 
    A.Timestamp, 
    A.Changes 
FROM 
    Borrower B
INNER JOIN 
    Loan_Application LA ON B.Borrower_ID = LA.Borrower_ID
INNER JOIN 
    Audit_Log A ON A.Audit_ID = LA.Audit_ID;

# 5. LIST OF BORROWERS WHOSE LOAN HAS BEEN APPROVED BY THE LENDER

SELECT B.NAME AS 'BORROWER NAME', L.NAME AS 'LENDER NAME', LS.STATUS AS 'LOAN STATUS'
FROM BORROWER B,LENDER L, LOAN_APPLICATION LA, LOAN_STATUS LS
WHERE
LA.LOAN_ID=LS.LOAN_ID AND
LA.BORROWER_ID= B.BORROWER_ID AND
LA.LENDER_ID= L.LENDER_ID AND
LS.STATUS IN ('Approved');

# 6. BORROWERS WITH HIGHEST LOAN AMOUNT

SELECT B.Name AS 'Borrower Name', LA.Amount AS 'Loan Amount'
FROM Borrower B
JOIN Loan_Application LA ON B.Borrower_ID = LA.Borrower_ID
WHERE LA.Amount = (SELECT MAX(Amount) FROM Loan_Application);

#BORROWERS WHO HAVE MORE THAN 1 LOAN
SELECT 
    B.Borrower_ID, 
    B.Name AS 'Borrower Name',
    LA.Loan_Count AS 'Application Submitted'
FROM 
    Borrower B
JOIN 
    (SELECT Borrower_ID, COUNT(Loan_ID) AS Loan_Count
     FROM Loan_Application
     GROUP BY Borrower_ID
     HAVING COUNT(Loan_ID) > 1) AS LA ON B.Borrower_ID = LA.Borrower_ID;
     
     # 7. List Borrowers and Their Loan Amount if It’s Above the Average Loan Amount
     SELECT B.Name AS 'Borrower Name', LA.Amount AS 'Loan Amount'
FROM Borrower B
JOIN Loan_Application LA ON B.Borrower_ID = LA.Borrower_ID
WHERE LA.Amount > (SELECT AVG(Amount) FROM Loan_Application);

#  8. Using co-related query we find the Average Rating per Lender and List Lenders with Above-Average Ratings
SELECT 
    L.Lender_ID, 
    L.Name AS 'Lender Name', 
    AVG(R.Rating_Number) AS 'Average Rating'
FROM 
    Lender L
JOIN 
    Rating R ON L.Lender_ID = R.User_ID
GROUP BY 
    L.Lender_ID, L.Name
HAVING 
    AVG(R.Rating_Number) > (SELECT AVG(Rating_Number) FROM Rating);
    
    # 9. Find Borrowers with Disputes Resolved
    SELECT 
    B.Borrower_ID, 
    B.Name AS 'Borrower Name', D.STATUS
FROM 
    Borrower B
JOIN 
    Loan_Application LA ON B.Borrower_ID = LA.Borrower_ID
JOIN 
    Dispute D ON LA.Loan_ID = D.Loan_ID
WHERE 
    EXISTS (
        SELECT 1 
        FROM Dispute 
        WHERE Dispute.Loan_ID = D.Loan_ID 
        AND Dispute.Status = 'Resolved' 
    );

# 10. Find Borrowers Who Have Never Received a Notification
SELECT 
    B.Borrower_ID, 
    B.Name AS 'Borrower Name'
FROM 
    Borrower B
WHERE 
    B.Borrower_ID NOT IN (SELECT User_ID FROM Notification);



