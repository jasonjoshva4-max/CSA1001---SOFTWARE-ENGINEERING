# EXP-7: Task Management System using MoSCoW and Kano Model in Jira

**Course:** CSA1001 – Software Engineering | **Experiment No.:** 7  
**System Under Study:** Task Management System (TMS) / Jira Software

## 1. AIM
To analyze, classify, and prioritize functional and non-functional requirements of a **Task Management System (TMS)** using the **MoSCoW Method** and **Kano Model**, and configure these prioritized items in **Jira Software**.

## 2. OBJECTIVES
- Understand the dual-framework approach: MoSCoW (Importance/Urgency) and Kano Model (Customer Satisfaction).
- Categorize TMS requirements using both MoSCoW and Kano frameworks.
- Configure Jira custom fields, JQL filters, and dashboards to visually track requirement priorities.

## 3. THEORY & CONCEPTUAL FRAMEWORK
- **MoSCoW:** Must Have (Critical), Should Have (Important), Could Have (Desirable), Won't Have (Out of scope).
- **Kano Model:** Basic Needs (Must-Be), Performance Needs (Linear), Excitement Needs (Attractive), Indifferent, Reverse.

## 4. REQUIREMENTS CLASSIFICATION (MoSCoW & KANO)
| Req ID | Requirement Description | MoSCoW | Kano Model | Justification |
|---|---|---|---|---|
| **FR-01** | Create, edit, and delete tasks | Must Have | Basic | Baseline core requirement. |
| **FR-02** | User authentication & roles | Must Have | Basic | Mandatory security. |
| **FR-03** | Task status tracking (To Do, In Progress, Done) | Must Have | Basic | Mandatory workflow. |
| **FR-04** | Assign task to team members | Must Have | Performance | Speed/clarity impacts satisfaction. |
| **FR-05** | Set task due dates & priorities | Must Have | Performance | Critical sorting feature. |
| **FR-06** | Comments & file attachments | Should Have | Performance | Enhances collaboration. |
| **FR-07** | Automated email due date notifications | Should Have | Performance | Reduces missed deadlines. |
| **FR-08** | Kanban & List view toggle | Should Have | Performance | Improves viewing flexibility. |
| **FR-09** | AI-driven task duration estimation | Could Have | Attractive | Innovative delight feature. |
| **FR-10** | Smart task dependencies (Gantt chart) | Could Have | Attractive | PM delight feature. |
| **FR-11** | Voice-to-task creation via mobile | Could Have | Attractive | Mobile delight. |
| **FR-12** | Dark mode theme toggle | Could Have | Attractive | Visual comfort delight. |
| **FR-13** | Integration with VR/AR workspace | Won't Have | Indifferent | Niche; out of scope. |
| **FR-14** | Gamified points system for tasks | Won't Have | Reverse | Disliked by enterprise users. |

## 5. JIRA IMPLEMENTATION STEPS
1. **Custom Field:** Create `Kano Category` (Select List: Basic, Performance, Attractive, Indifferent).
2. **MoSCoW Mapping:** Map native Priority (Highest -> Must Have, High -> Should Have, Medium -> Could Have, Low -> Won't Have).
3. **JQL Filters:** Create filters `project = "TMS" AND priority = Highest` and `project = "TMS" AND "Kano Category" = "Attractive"`.
4. **Dashboard:** Add 2D Filter Statistics gadget (Priority vs Kano Category).

## 6. CONCLUSION
Combining MoSCoW and Kano prevents building products that lack essential features or contain empty excitement features.
