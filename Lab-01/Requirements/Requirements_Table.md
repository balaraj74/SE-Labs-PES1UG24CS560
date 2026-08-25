# Lab 1 — Requirements Engineering & UML Use-Case Modelling

## Problem Statement #48 — Incident Escalation & On-Call Rotation Engine

| Req ID | Type | Description | Priority | Acceptance Criteria | Rationale |
|---|---|---|---|---|---|
| FR-001 | Functional | The system shall ingest incident alerts, identify the active on-call engineer from the rotation schedule, and escalate to the secondary engineer if the alert is unacknowledged within 5 minutes. | High | Pass: Escalation is triggered after 5 minutes without acknowledgement. Fail: An unacknowledged incident is not escalated. | Ensures critical incidents receive timely attention. |
| FR-002 | Functional | The system shall allow authorized users to create and update on-call rotation schedules, including primary and secondary engineers. | High | Pass: A valid schedule containing primary and secondary engineers is saved successfully. Fail: An invalid or incomplete schedule is saved. | Ensures incidents are routed to the correct engineers. |
| FR-003 | Functional | The system shall allow an on-call engineer to acknowledge an assigned incident and record the acknowledgement time. | High | Pass: The incident status changes to Acknowledged and an acknowledgement timestamp is recorded. Fail: The incident remains unacknowledged after acknowledgement. | Prevents unnecessary escalation after an engineer accepts responsibility. |
| FR-004 | Functional | The system shall escalate an unacknowledged incident through configured escalation tiers using available notification channels such as SMS, phone, or email. | High | Pass: The next configured escalation target is contacted when the escalation timeout expires. Fail: Escalation stops without contacting the next target. | Provides fault tolerance when the primary engineer does not respond. |
| FR-005 | Functional | The system shall allow the Incident Commander to create and record a post-mortem for a resolved incident. | Medium | Pass: A post-mortem containing the required incident details is saved against the resolved incident. Fail: An incomplete post-mortem is saved. | Enables analysis and learning from previous incidents. |
| NFR-001 | Nonfunctional | Alert dispatch via webhook, SMS, and email shall initiate within 3 seconds of alert ingestion. | High | Pass: Benchmarking confirms notification initiation within 3 seconds under the specified test load. Fail: Notification initiation exceeds 3 seconds. | Ensures rapid incident response. |
| NFR-002 | Nonfunctional | The system shall maintain an auditable record of incident alerts, acknowledgements, escalations, and status changes. | High | Pass: Every tested incident action produces a timestamped audit record. Fail: Any tested action has no corresponding audit record. | Supports accountability and incident investigation. |

## Source

Problem Statement #48 — Incident Escalation & On-Call Rotation Engine.
https://docs.google.com/spreadsheets/d/1xrdZuFybfh2ps43HP1Q7S8YadIET5wizgwYDmTwg5SY/edit?usp=sharing
