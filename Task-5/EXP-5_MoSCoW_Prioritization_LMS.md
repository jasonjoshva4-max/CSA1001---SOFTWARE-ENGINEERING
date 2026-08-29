# EXP-5: MoSCoW Prioritization for a Library Management System

**Course:** CSA1001 – Software Engineering  
**Experiment No.:** 5  
**Experiment Title:** Requirements Prioritization using MoSCoW Method  
**System Under Study:** Library Management System (LMS)

---

## 1. AIM

To identify and prioritize the functional and non-functional requirements of a Library Management System (LMS) using the **MoSCoW prioritization technique**, and to understand how requirements are classified based on their importance and urgency.

---

## 2. OBJECTIVE

- To understand the MoSCoW method of requirements prioritization.
- To list the requirements of a Library Management System.
- To classify each requirement into one of four MoSCoW categories.
- To justify the priority assigned to each requirement.

---

## 3. THEORY

### 3.1 What is MoSCoW Prioritization?

**MoSCoW** is a requirements prioritization technique widely used in software engineering and agile project management. The acronym stands for:

| Letter | Category      | Meaning                                                                 |
|--------|---------------|-------------------------------------------------------------------------|
| **M**  | Must Have     | Non-negotiable requirements; the project fails without them.            |
| **S**  | Should Have   | Important but not vital; can be delivered in a later phase if needed.   |
| **C**  | Could Have    | Desirable but not necessary; included only if time/resources allow.     |
| **W**  | Won't Have    | Explicitly excluded from the current release scope.                     |

> **Note:** The lowercase letters `o` in MoSCoW are fillers and carry no meaning.

### 3.2 Why Use MoSCoW?

- **Clarity of Scope:** Prevents scope creep by explicitly defining what will and won't be built.
- **Stakeholder Alignment:** Ensures all parties agree on priorities before development begins.
- **Agile Compatibility:** Works seamlessly with sprint-based delivery.
- **Risk Reduction:** Critical features are delivered first, reducing project failure risk.
- **Resource Management:** Helps allocate limited time, budget, and effort optimally.

### 3.3 Steps to Apply MoSCoW Prioritization

1. **Gather requirements** from stakeholders through interviews, surveys, or workshops.
2. **List all requirements** — both functional and non-functional.
3. **Conduct a prioritization session** with stakeholders.
4. **Assign each requirement** to one of the four MoSCoW categories.
5. **Validate and review** the categorization with stakeholders.
6. **Document** the final prioritized requirements list.

---

## 4. SYSTEM OVERVIEW: Library Management System (LMS)

A **Library Management System (LMS)** is a software application designed to automate and manage the day-to-day operations of a library. It serves multiple user roles:

- **Students / Members** – Search books, borrow/return books, pay fines.
- **Librarians** – Manage book catalog, issue/return books, manage members.
- **Administrators** – Manage staff accounts, generate reports, configure the system.

### Key Operations:
- Book cataloging and inventory management
- Member registration and authentication
- Book issuing and return tracking
- Fine calculation and payment
- Reservation and hold management
- Report generation

---

## 5. REQUIREMENTS GATHERING

### 5.1 Functional Requirements (FR)

| ID    | Requirement Description                                              |
|-------|----------------------------------------------------------------------|
| FR-01 | User (Member) registration and login                                 |
| FR-02 | Librarian login and authentication                                   |
| FR-03 | Administrator login and role-based access control                    |
| FR-04 | Search books by title, author, genre, or ISBN                        |
| FR-05 | Add, update, and delete book records                                 |
| FR-06 | Issue (check out) a book to a member                                 |
| FR-07 | Return a book and update inventory                                   |
| FR-08 | Calculate and track overdue fines                                    |
| FR-09 | Accept fine payments (cash or online)                                |
| FR-10 | Reserve a book that is currently checked out                         |
| FR-11 | Send email/SMS notification for due dates and reservations           |
| FR-12 | Generate reports (issued books, overdue, popular, fines)             |
| FR-13 | Manage multiple copies of the same book                              |
| FR-14 | Categorize books by genre, department, or subject                    |
| FR-15 | View borrowing history for a member                                  |
| FR-16 | Renew a book online                                                  |
| FR-17 | Manage inter-library loan requests                                   |
| FR-18 | Integration with external e-book platform                            |
| FR-19 | QR code / barcode scanning for book issue and return                 |
| FR-20 | Multilingual interface support                                       |
| FR-21 | Mobile app version of the system                                     |
| FR-22 | Reading recommendation engine (AI-based)                             |

### 5.2 Non-Functional Requirements (NFR)

| ID     | Requirement Description                                              |
|--------|----------------------------------------------------------------------|
| NFR-01 | The system shall be available 99.5% of the time (high availability) |
| NFR-02 | Page load time shall not exceed 3 seconds under normal load          |
| NFR-03 | User data shall be encrypted using AES-256 or equivalent             |
| NFR-04 | The system shall support at least 500 concurrent users               |
| NFR-05 | The system shall have an intuitive, easy-to-use interface            |
| NFR-06 | The system shall comply with data privacy regulations (e.g., GDPR)   |
| NFR-07 | The system shall be maintainable and modularly designed              |
| NFR-08 | The system shall support database backup and recovery                |
| NFR-09 | The system shall be scalable to support multiple library branches    |
| NFR-10 | The system shall run on standard web browsers without plugins        |

---

## 6. MoSCoW PRIORITIZATION TABLE

### 6.1 Functional Requirements

| ID    | Requirement                               | Priority        | Justification                                                             |
|-------|-------------------------------------------|-----------------|---------------------------------------------------------------------------|
| FR-01 | Member registration and login             | **Must Have**   | Core identity management; system cannot function without it.              |
| FR-02 | Librarian login and authentication        | **Must Have**   | Primary operator; essential for all library operations.                   |
| FR-03 | Admin login with role-based access        | **Must Have**   | Security and access control are fundamental requirements.                 |
| FR-04 | Search books (title, author, ISBN, genre) | **Must Have**   | Primary feature for members; a library is unusable without search.        |
| FR-05 | Add, update, delete book records          | **Must Have**   | Core cataloging function; necessary to manage the collection.             |
| FR-06 | Issue (check out) a book                  | **Must Have**   | Core library operation; the entire purpose of an LMS.                     |
| FR-07 | Return a book and update inventory        | **Must Have**   | Complements issuing; inventory integrity depends on this.                 |
| FR-08 | Calculate and track overdue fines         | **Must Have**   | Essential for enforcing return policies and financial accountability.      |
| FR-09 | Accept fine payments                      | **Should Have** | Important but manual (cash) payment can be handled offline initially.     |
| FR-10 | Reserve / place a hold on a book          | **Should Have** | Valuable for members but not required for basic operations.               |
| FR-11 | Email/SMS notifications for due dates     | **Should Have** | Greatly improves UX and reduces overdue returns; not core logic.          |
| FR-12 | Generate reports                          | **Should Have** | Important for management but not part of day-to-day operations.           |
| FR-13 | Manage multiple copies of same book       | **Must Have**   | Libraries routinely hold multiple copies; needed from day one.            |
| FR-14 | Categorize books by genre/department      | **Should Have** | Improves discoverability but not critical for core operations.            |
| FR-15 | View member borrowing history             | **Should Have** | Useful for members and librarians; aids in dispute resolution.            |
| FR-16 | Online book renewal                       | **Could Have**  | Convenient but members can renew at the desk as a workaround.             |
| FR-17 | Inter-library loan management             | **Could Have**  | Useful for large networks; not needed for basic single-library setup.     |
| FR-18 | Integration with e-book platform          | **Could Have**  | Adds value but complex; not a core library management function.           |
| FR-19 | QR code / barcode scanning                | **Could Have**  | Speeds up operations but manual entry is a viable alternative.            |
| FR-20 | Multilingual interface support            | **Won't Have**  | Out of scope; targeted at a single-language institution this release.     |
| FR-21 | Mobile app version                        | **Won't Have**  | Web-responsive interface is sufficient; native app is a future phase.     |
| FR-22 | AI-based reading recommendations          | **Won't Have**  | Future enhancement; not justified for current scope/budget.               |

---

### 6.2 Non-Functional Requirements

| ID     | Requirement                                   | Priority        | Justification                                                              |
|--------|-----------------------------------------------|-----------------|----------------------------------------------------------------------------|
| NFR-01 | 99.5% system availability                     | **Must Have**   | Library operations are continuous; downtime is unacceptable.               |
| NFR-02 | Page load time <= 3 seconds                   | **Must Have**   | Poor performance directly impacts usability and adoption.                  |
| NFR-03 | AES-256 data encryption                       | **Must Have**   | Member personal data and financial records must be protected.              |
| NFR-04 | Support 500+ concurrent users                 | **Should Have** | Important for larger institutions; can be scaled post-launch.              |
| NFR-05 | Intuitive, easy-to-use interface              | **Must Have**   | System serves non-technical users; UX is vital for adoption.              |
| NFR-06 | Data privacy compliance (GDPR/similar)        | **Should Have** | Legally important; exact requirements depend on region/institution.        |
| NFR-07 | Modular and maintainable codebase             | **Should Have** | Ensures long-term health and ease of future updates.                       |
| NFR-08 | Database backup and recovery                  | **Must Have**   | Data loss is catastrophic; backups are non-negotiable.                     |
| NFR-09 | Scalability for multiple branches             | **Could Have**  | Single-branch deployment initially; multi-branch is a future need.         |
| NFR-10 | Cross-browser compatibility (no plugins)      | **Must Have**   | Must be accessible on all standard devices without barriers.               |

---

## 7. SUMMARY OF MoSCoW CLASSIFICATION

### 7.1 Requirement Count by Category

| Category      | Functional | Non-Functional | Total  |
|---------------|------------|----------------|--------|
| Must Have     | 9          | 6              | **15** |
| Should Have   | 7          | 3              | **10** |
| Could Have    | 4          | 1              | **5**  |
| Won't Have    | 3          | 0              | **3**  |
| **Total**     | **23**     | **10**         | **33** |

### 7.2 Visual Distribution

```
Must Have   [===============================] 45%  (15/33)
Should Have [===================          ] 30%  (10/33)
Could Have  [==========                   ] 15%  ( 5/33)
Won't Have  [=====                        ] 10%  ( 3/33)
```

---

## 8. RELEASE PLANNING (Based on MoSCoW)

| Phase   | Sprint   | Requirements Targeted                                                                        |
|---------|----------|----------------------------------------------------------------------------------------------|
| Phase 1 | Sprint 1 | All **Must Have**: FR-01 to FR-08, FR-13, NFR-01, NFR-02, NFR-03, NFR-05, NFR-08, NFR-10   |
| Phase 2 | Sprint 2 | All **Should Have**: FR-09, FR-10, FR-11, FR-12, FR-14, FR-15, NFR-04, NFR-06, NFR-07      |
| Phase 3 | Sprint 3 | **Could Have** (capacity-based): FR-16, FR-17, FR-18, FR-19, NFR-09                        |
| Future  | Backlog  | **Won't Have** (future releases): FR-20 (multilingual), FR-21 (mobile app), FR-22 (AI)     |

---

## 9. ADVANTAGES OF MoSCoW METHOD

1. **Simplicity:** Easy to understand and apply, even for non-technical stakeholders.
2. **Stakeholder Communication:** Creates a shared language between developers and clients.
3. **Flexibility:** Can be applied to any project size or methodology (Agile, Waterfall, etc.).
4. **Focus on Value:** Ensures the highest-value features are delivered first.
5. **Avoids Gold-Plating:** Prevents teams from building unnecessary features.
6. **Scope Management:** "Won't Have" explicitly manages expectations and prevents scope creep.

---

## 10. LIMITATIONS OF MoSCoW METHOD

1. **Subjectivity:** Priority assignment can be subjective without proper stakeholder consensus.
2. **No Ranking Within Categories:** "Must Haves" are not ranked against each other.
3. **Changing Priorities:** Priorities can shift across sprints, requiring re-evaluation.
4. **Over-classification:** Teams may place too many items in "Must Have," defeating the purpose.
5. **No Effort Estimation:** MoSCoW does not consider the cost or effort of implementing features.

---

## 11. CONCLUSION

In this experiment, the **MoSCoW Prioritization** technique was applied to the **Library Management System (LMS)**. A total of **33 requirements** (23 functional + 10 non-functional) were gathered, analyzed, and classified into the four MoSCoW categories.

Key findings:
- **15 requirements (45%)** are critical for the initial release (**Must Have**), including core operations like login, book search, issue/return, fine tracking, data encryption, and system availability.
- **10 requirements (30%)** add significant value and should be delivered soon after (**Should Have**), such as notifications, reports, online payments, and scalability.
- **5 requirements (15%)** are desirable enhancements (**Could Have**) like barcode scanning and online renewals.
- **3 requirements (10%)** are intentionally excluded from this release (**Won't Have**), including a mobile app, multilingual support, and AI-based recommendations.

This structured approach ensures that the development team delivers a functional, valuable system within time and budget constraints, while maintaining clear expectations with all stakeholders.

---

## 12. REFERENCES

1. Clegg, D., & Barker, R. (1994). *CASE Method Fast-Track: A RAD Approach.* Addison-Wesley.
2. Sommerville, I. (2016). *Software Engineering* (10th ed.). Pearson.
3. Pressman, R. S. (2014). *Software Engineering: A Practitioner's Approach* (8th ed.). McGraw-Hill.
4. DSDM Consortium. (2014). *MoSCoW Prioritization.* https://www.dsdm.org

---
*End of EXP-5*
