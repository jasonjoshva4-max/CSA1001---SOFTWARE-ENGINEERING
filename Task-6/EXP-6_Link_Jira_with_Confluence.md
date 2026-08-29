# EXP-6: Integration of Jira and Confluence for Agile Software Project Management

**Course:** CSA1001 – Software Engineering  
**Experiment No.:** 6  
**Experiment Title:** Linking Jira with Confluence for Requirements Traceability and Documentation  
**System Under Study:** Atlassian Ecosystem (Jira Software & Confluence Cloud/Data Center)

---

## 1. AIM

To integrate **Jira Software** and **Confluence** to establish seamless traceability between project documentation (requirements, specs, meeting notes) and issue tracking (epics, user stories, tasks, bugs).

---

## 2. OBJECTIVES

- Understand the roles of Jira (issue tracking) and Confluence (knowledge management).
- Learn how to establish and verify Application Links between Jira and Confluence.
- Create Jira issues directly from Confluence requirements documentation.
- Embed dynamic Jira reports, filters, and roadmaps into Confluence pages.
- Link relevant Confluence pages inside Jira issues for two-way traceability.

---

## 3. THEORY & KEY CONCEPTS

### 3.1 Overview of Jira and Confluence

| Tool | Primary Purpose | Key Units |
|---|---|---|
| **Jira Software** | Project management, issue tracking, sprint planning, backlog management | Epics, Stories, Tasks, Bugs, Sprints, Roadmaps |
| **Confluence** | Knowledge base, technical documentation, meeting notes, project vision | Spaces, Pages, Templates, Macros |

### 3.2 Benefits of Integrating Jira and Confluence

1. **Two-Way Traceability:** Connect high-level requirements in Confluence to specific technical tasks in Jira.
2. **Single Source of Truth:** Developers write code based on linked specifications; product managers track progress without leaving documentation.
3. **Contextual Awareness:** Developers can view relevant requirements directly within Jira tickets.
4. **Real-time Status Updates:** Confluence displays live Jira issue status (To Do, In Progress, Done) automatically.
5. **Reduced Context Switching:** Teams create Jira tickets from Confluence text with a single click.

---

## 4. PREREQUISITES

- An active **Atlassian Account** (Cloud or Data Center edition).
- Admin or User access to a **Jira Software** project (e.g., `LMS-Project`).
- Admin or User access to a **Confluence** space (e.g., `LMS-Documentation`).

---

## 5. STEP-BY-STEP PROCEDURE

### Step 1: Connect Jira and Confluence (Application Links)

*(Note: For Atlassian Cloud, products under the same organization are auto-linked. For Server/Data Center, follow these steps.)*

1. Log in to **Jira** as an Administrator.
2. Navigate to **Settings (Gear Icon) > System > Application Links**.
3. Enter your **Confluence URL** (e.g., `https://your-org.atlassian.net/wiki`).
4. Click **Create new link** and approve reciprocal access when prompted in Confluence.
5. Verify that status shows **Connected**.

---

### Step 2: Create a Requirements Document in Confluence

1. Open your Confluence Space (`LMS Space`).
2. Click **Create (+)** and select the **Product Requirements** template (or a blank page).
3. Title the page: `Library Management System - Software Requirements Specification (SRS)`.
4. Create a requirements table with columns:
   - `Req ID` | `User Story / Feature` | `Priority` | `Jira Ticket` | `Status`

---

### Step 3: Create Jira Issues Directly from Confluence Text

1. Highlight any requirement text in your Confluence page (e.g., *"System must calculate overdue fines automatically"*).
2. A small context menu will appear above the highlighted text.
3. Click the **Create Jira Issue** icon (Jira logo).
4. Select:
   - **Project:** Library Management System (`LMS`)
   - **Issue Type:** Story / Task
   - **Summary:** Auto-filled from highlighted text
5. Click **Create**.
6. **Result:** Confluence automatically inserts a dynamic **Jira Smart Link** in place of or next to the text.

---

### Step 4: Embed Jira Issues and Filters into Confluence Pages (Jira Macro)

1. While editing a Confluence page, type `/jira` or click **+ (Insert) > Jira**.
2. In the modal dialog, search for issues using **JQL (Jira Query Language)** or simple search:
   - Example JQL: `project = "LMS" AND status = "In Progress"`
3. Select display options:
   - **Single Issue:** Shows detailed card or inline badge with live status.
   - **Table:** Displays a dynamic list of matching Jira tickets.
4. Click **Insert**.
5. Save the page. The table now auto-updates whenever Jira issue statuses change.

---

### Step 5: Link Confluence Pages Inside Jira Tickets

1. Open any Jira issue (e.g., `LMS-12: Implement Fine Calculation Logic`).
2. Look at the **Linked Confluence pages** field (in the right sidebar or issue details panel).
3. Click **+ Add Confluence page**.
4. Paste the URL of the Confluence SRS page or search for `Library Management System SRS`.
5. Select the page and click **Link**.
6. **Result:** The ticket now displays a direct link to the specification page, allowing developers to quickly view requirement context.

---

### Step 6: Embed Jira Sprint Reports and Roadmaps in Confluence

1. Open your Confluence Project Homepage.
2. Type `/jira roadmap` or `/jira chart` while editing.
3. Choose **Jira Roadmap** macro:
   - Select Project `LMS`.
   - Embeds an interactive Gantt-style timeline of Epics directly into Confluence.
4. Choose **Jira Chart** macro:
   - Select **Pie Chart** or **Created vs Resolved**.
   - Set Filter to `project = LMS`.
5. Save the page. Executive stakeholders can now view live project progress directly from Confluence.

---

## 6. VERIFICATION AND TESTING

To ensure the integration is successful, perform the following verification checks:

| Test Case | Procedure | Expected Result | Pass / Fail |
|---|---|---|---|
| **TC-01: Smart Link Resolution** | Paste a Jira issue URL in Confluence | Displays inline badge with live status (`In Progress`, `Done`) | **PASS** |
| **TC-02: Issue Creation from Text** | Highlight text in Confluence -> Create Issue | Issue created in Jira and linked in Confluence | **PASS** |
| **TC-03: Two-Way Link Check** | Open Jira issue linked in TC-02 | "Linked Confluence Pages" section shows SRS page | **PASS** |
| **TC-04: Dynamic JQL Macro** | Change status of `LMS-01` in Jira | Confluence table updates status automatically on refresh | **PASS** |
| **TC-05: Embedded Roadmap** | View Confluence project overview page | Live Jira Roadmap widget renders correctly | **PASS** |

---

## 7. ADVANTAGES OF JIRA-CONFLUENCE INTEGRATION

- **Traceability matrix automation:** Eliminates manual updating of Excel traceability matrices.
- **Improved developer efficiency:** Developers don't need to search through documents to find task details.
- **Real-time executive reporting:** Management can monitor delivery status on Confluence dashboards.
- **Enhanced collaboration:** Product Owners, Developers, and QA engineers share complete context.

---

## 8. CONCLUSION

In this experiment, **Jira Software and Confluence were successfully integrated**. We demonstrated how to link specifications with technical tasks, embed dynamic Jira gadgets into Confluence pages, and establish two-way traceability. This integration significantly improves Agile project management, documentation consistency, and team productivity.

---

## 9. REFERENCES

1. Atlassian Documentation. *Use Jira and Confluence together.* https://support.atlassian.com
2. Rubin, K. S. (2012). *Essential Scrum: A Practical Guide to the Most Popular Agile Process.* Addison-Wesley.
3. Pressman, R. S. (2014). *Software Engineering: A Practitioner's Approach.* McGraw-Hill.

---
*End of EXP-6*
