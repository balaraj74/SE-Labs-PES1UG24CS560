# Lab 2: Agile Backlog Creation & Sprint Simulation in Jira

**Course:** Software Engineering Laboratory (UE24CS342AA3)  
**Student Name:** Balaraj R  
**SRN:** PES1UG24CS560  
**Assigned Problem Statement:** PS #48 — Incident Escalation & On-Call Rotation Engine  
**Project Key:** `IES`  

---

## 1. Objective
Transform the functional requirements identified in Lab 1 (Incident Escalation & On-Call Rotation Engine) into structured Agile Epics and User Stories, estimate them using Planning Poker (Fibonacci scale), prioritize the product backlog, simulate two one-week sprints in Jira, and evaluate team progress and velocity using Jira's Active Sprint Board and Burndown Chart.

---

## 2. Deliverables Summary
* **Full Lab Report (PDF):** [`LAB2_SE_PES1UG24CS560_Report.pdf`](./LAB2_SE_PES1UG24CS560_Report.pdf)
* **Editable Report (DOCX):** [`LAB2_SE_PES1UG24CS560_Report.docx`](./LAB2_SE_PES1UG24CS560_Report.docx)
* **Screenshots:**
  1. Product Backlog with Story Points & Priorities: [`screenshots/jira_backlog.png`](./screenshots/jira_backlog.png)
  2. Sprint 1 Active Board: [`screenshots/sprint1_board.png`](./screenshots/sprint1_board.png)
  3. Sprint 2 Active Board: [`screenshots/sprint2_board.png`](./screenshots/sprint2_board.png)
  4. Sprint 2 Burndown Chart: [`screenshots/burndown_chart.png`](./screenshots/burndown_chart.png)

---

## 3. Epics & User Stories Breakdown

| Issue Key | Epic Association | User Story Summary | Priority | Estimate | Sprint |
|---|---|---|---|---|---|
| **IES-1** | Epic 1: Alert Ingestion (FR-001) | Ingest Webhook Alert Payloads & Trigger Schedule Lookup | High | 5 pts | Sprint 1 |
| **IES-2** | Epic 2: Rotation Schedule (FR-002) | Primary & Secondary Schedule Configuration Interface | High | 8 pts | Sprint 1 |
| **IES-3** | Epic 3: Acknowledgement (FR-003) | Engineer Fast-Acknowledgement UI with Timestamp Capture | High | 3 pts | Sprint 1 |
| **IES-4** | Epic 3: Acknowledgement (FR-003) | Incident State Machine Transition to Acknowledged | Medium | 3 pts | Sprint 1 |
| **IES-5** | Epic 1: Alert Ingestion (FR-001) | Automated 5-Minute Timeout & Secondary Tier Trigger | High | 3 pts | Sprint 2 |
| **IES-6** | Epic 4: Escalation Tiers (FR-004) | Multi-Channel Notification Dispatcher (SMS, Voice, Webhook) | High | 5 pts | Sprint 2 |
| **IES-7** | Epic 5: Post-Mortem (FR-005) | Structured Incident Post-Mortem Authoring & Action Items | Medium | 5 pts | Sprint 2 |
| **IES-8** | Epic 4: Escalation Tiers (NFR-002) | Immutable Audit Log Generation for Escalation Events | Medium | 3 pts | Sprint 2 |

---

## 4. Sprint Execution & Telemetry
* **Sprint 1 Velocity:** 19 Story Points completed (4 issues)
* **Sprint 2 Velocity:** 16 Story Points completed (4 issues)
* **Total Story Points Delivered:** 35 Story Points across 2 Sprints

### Burndown Analysis & Reflection
* **Estimations vs Actual Effort:** Story points followed the Fibonacci scale (3, 5, 8) evaluating technical uncertainty, state dependencies, and third-party integrations (telephony/audit logging) rather than simple hours.
* **Backlog Prioritization:** Sprint 1 established core routing and ingestion foundations without which multi-tier escalation could not trigger. Sprint 2 delivered automated failovers and compliance audits.
* **Sprint Progress:** Telemetry reflected a stepped burndown curve tracking predictable incremental completion across daily standups, avoiding end-of-sprint crunches.
