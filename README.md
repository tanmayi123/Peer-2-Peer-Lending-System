# Peer-2-Peer-Lending-System

Introduction


The traditional way of funding for a college student aspiring to venture into the world of start-ups with creative ideas and technology that can potentially bring a change to the society, include, going to banks to acquire bank loans or getting a funding via research and scholarship programs. However, this process is cumbersome, involves a lot of time and eligibility constraints. The aim of this project is to eliminate the middleman (bank) and create a platform for Northeastern Students by connecting students to alumni investors through a Peer-2-Peer lending system which would enable students to acquire loans for their entrepreneurial ventures with the help of strong alumni networks.


The aim is to create a platform that is decentralized and has a secure environment for loan transactions and is beneficial for both borrowers and lenders. This platform would provide flexible financing options for students, and alumni will also benefit from earning good returns as the middleman (bank) is obsolete in this picture.


Objective

The main objective of the P2P platform for northeastern students is to:


1.Help students (borrowers) to bring forward their start up ideas and get funding from alumni investors
2.Help Alumni (lenders) invest in and fund student start-ups, negotiate loan payment terms and gain back returns on their investments

Theory for P2P Lending Platform


The P2P lending platform offers a secure environment for loan transactions in exchange for startup ideas. The idea is to create a database that includes profiles created by users. User profiles include both - profiles of borrowers and lenders. A borrower can choose the startup category while creating their profile and can add their ideas in their profile. A borrower user profile will also contain their personal details like name, age, phone number, email address, LinkedIn profile link, user_id etc. A lender profile will contain their personal details like name, age, LinkedIn profile link, work email address, borrower_id etc. The borrower can search for lenders to whom they want to request a loan from. Upon placing a request, the lender will be able to view the borrower profile and can connect with them over email/phone for discussions. The lenders can also view different user profiles of the borrowers and can actively connect with them to invest in their ideas. Similarly, borrowers can view alumni profiles to place loan requests. The database structure will also include loan applications, where the borrower can input the loan that they require. It also includes collateral, loan repayment plan, interest rate, credit history, business description, financial projections, and other terms and conditions of the loan. The business process starts when the borrowers submit their loan application. Once the loan is approved, the repayment plan is created in the user profile, where the borrower will update the lender after each repayment period. The database will also include an audit log, which would help in tracking each transaction, and will be helpful in maintaining transparency. A single borrower can apply for multiple loans, and a single investor can also lend multiple loans. The database structure will also contain a dispute section, where users (both borrowers and lenders) can raise disputes on a loan application if needed, where no further repayments or investment activities can happen until the dispute is settled. Users (both investors and borrowers) can view the loan history each have to better assess the risk of investing and chances of getting a fund. The database system would also have a real time notification system that gets triggered to send out notification when a certain change occurs, such as approval of loan or a missed repayment. The system would also support a feedback system for borrowers and lenders and a rating system for both. The system would also include a referral program, where every user (borrower) can be referred by other users (borrowers and lenders). This system would not only help the students by giving them a head start but would also help the investors gain a benefit by eliminating the intermediaries.

Requirements
1.A borrower (student) can establish one start up idea in their profile at one time, however, the idea can fall into any category (tech, health, finance, fashion etc.)
2.A borrower (student) can request zero to many loans.
3.A lender (investor/alumni) can invest in zero to many ideas.
4.One loan can have only one borrower (to prevent shared ownership on the loan)
5.One loan can have multiple investors
6.One borrower can have different repayment schedules (as one borrower may have multiple investors)
7.One loan must have only one repayment schedule
8.A borrower can have multiple transaction records
9.A transaction record is linked to only one loan application
10.One loan application can have multiple transaction records
11.A loan request can have zero or many collateral
12.A loan application can have different status (approved, pending, dispersed). This loan status may change over time
13.A dispute may be tied to one loan
14.A user (both borrower and lender) can have multiple loan histories tied to them
15.A user (both borrower and lender) can receive multiple notifications
16.One loan application is tied to multiple audit logs
17.One user is tied to multiple audit logs
18.One user (both borrower and lender) can have multiple ratings and feedback
19.A user can have multiple referrals
