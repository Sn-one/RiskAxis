# APPFLOW.md
# RiskAxis Application Flow

## 1. Purpose

This document describes the user and system flows for RiskAxis, an objective-centered ERM graph platform.

The core application flow is:

```text
Define objectives
  → Identify risks
    → Link risks to objectives
      → Link risks to other risks
        → Map policies and procedures
          → Map controls
            → Assess risk
              → Compare to appetite
                → Treat risk
                  → Monitor with KRIs/KPIs
                    → Review
                      → Assure
                        → Report
```

## 2. Main Entry Flow

```text
User opens RiskAxis
  ↓
Login
  ↓
Authentication check
  ↓
Role and permission check
  ↓
Redirect to role-based dashboard
```

## 3. Role-Based Landing Flow

## 3.1 Executive Viewer

```text
Login
  → Executive Dashboard
  → Strategic Objectives at Risk
  → Top Enterprise Risks
  → Appetite Breaches
  → Critical Risk Pathways
  → Management Actions
```

## 3.2 ERM Manager

```text
Login
  → ERM Dashboard
  → Pending Risk Approvals
  → Objectives Without Risk Assessment
  → Risks Outside Appetite
  → Coverage Gaps
  → Overdue Reviews
  → Reports
```

## 3.3 Objective Owner

```text
Login
  → My Objectives
  → Objective Detail
  → Linked Risks
  → KRIs/KPIs
  → Treatment Actions
  → Reviews
```

## 3.4 Risk Owner

```text
Login
  → My Risks
  → Risk Detail
  → Risk Assessment
  → Related Risks
  → Controls
  → Treatment Actions
  → Reviews
```

## 3.5 Risk Champion

```text
Login
  → Department Dashboard
  → Department Objectives
  → Department Risks
  → Draft Risks
  → Coverage Gaps
```

## 4. Objective Creation Flow

```text
User clicks Create Objective
  ↓
Enter objective title and description
  ↓
Select objective type
  ↓
Select strategy pillar
  ↓
Assign business unit
  ↓
Assign objective owner
  ↓
Link parent objective if applicable
  ↓
Define KPI or success measure
  ↓
Define target date and review frequency
  ↓
Set appetite guidance
  ↓
Save objective
  ↓
Prompt user to identify risks
```

## 5. Objective-to-Risk Identification Flow

```text
Open objective
  ↓
Click Add Risk
  ↓
System asks guided questions:
    - What could prevent achievement?
    - What could delay achievement?
    - What could reduce value?
    - What dependency could fail?
    - What external event could affect this?
    - What opportunity could be missed?
  ↓
User creates risk statement
  ↓
Risk is linked to objective
  ↓
User defines relationship type
  ↓
Risk enters draft state
```

## 6. Risk Creation Flow

```text
Create or open draft risk
  ↓
Link to objective
  ↓
Define link type:
    - Direct threat
    - Indirect threat
    - Dependency
    - Opportunity
    - Emerging concern
  ↓
Enter cause, event, consequence
  ↓
Select risk universe category
  ↓
Assign business unit and risk owner
  ↓
Add related risks
  ↓
Map policies/procedures
  ↓
Map controls
  ↓
Perform inherent assessment
  ↓
Perform residual assessment
  ↓
Compare to appetite
  ↓
Add treatment actions if needed
  ↓
Submit for ERM review
```

## 7. Risk Approval Flow

```text
Draft Risk
  ↓
Submitted for Review
  ↓
ERM Manager reviews:
    - Objective linkage
    - Risk statement
    - Category
    - Assessment
    - Policies/procedures
    - Controls
    - Appetite status
    - Treatment plan
  ↓
Decision:
  ├── Approve → Official Risk Register
  ├── Request Revision → Returned to owner/champion
  └── Reject → Rejected archive
```

## 8. Risk-to-Risk Relationship Flow

```text
Open Risk Detail
  ↓
Go to Related Risks tab
  ↓
Click Add Relationship
  ↓
Select related risk
  ↓
Select relationship type:
    - Causes
    - Triggers
    - Precursor to
    - Consequence of
    - Amplifies
    - Cascades to
    - Same root cause as
    - Departmental dependency
  ↓
Add rationale
  ↓
Save relationship
  ↓
Graph updates
```

## 9. Policy and Procedure Coverage Flow

```text
Open Risk Detail
  ↓
Go to Policies & Procedures tab
  ↓
Search existing document
  ↓
Link document to risk
  ↓
Select coverage type
  ↓
Select coverage strength
  ↓
Add gap notes if partial or weak
  ↓
Save coverage
  ↓
Coverage dashboard updates
```

## 10. Control Mapping Flow

```text
Open Risk Detail
  ↓
Go to Controls tab
  ↓
Link existing control or create new control
  ↓
Define mitigation effect:
    - Reduces likelihood
    - Reduces impact
    - Reduces both
    - Detects occurrence
    - Corrects after occurrence
  ↓
Set design effectiveness
  ↓
Set operating effectiveness
  ↓
Attach evidence if available
  ↓
Save control mapping
  ↓
Residual assessment can be updated
```

## 11. Risk Assessment Flow

```text
Open Risk Assessment tab
  ↓
Select inherent likelihood
  ↓
Select inherent impact
  ↓
System calculates inherent score and rating
  ↓
Review linked controls
  ↓
Select residual likelihood
  ↓
Select residual impact
  ↓
System calculates residual score and rating
  ↓
System compares residual rating to appetite
  ↓
If outside appetite:
    - Require treatment action, or
    - Require formal acceptance
  ↓
Save assessment
  ↓
Assessment history updated
```

## 12. Treatment Action Flow

```text
Risk outside appetite or requiring treatment
  ↓
Risk owner creates treatment action
  ↓
Assign action owner
  ↓
Set due date and priority
  ↓
Action owner receives notification
  ↓
Action owner updates progress
  ↓
Evidence or notes added
  ↓
Risk owner validates completion
  ↓
Action closed
```

## 13. KRI/KPI Monitoring Flow

```text
Create KRI or KPI
  ↓
Link to objective and/or risk
  ↓
Set unit of measure
  ↓
Set target, warning threshold, breach threshold
  ↓
Enter current value
  ↓
System evaluates status:
    - Normal
    - Watch
    - Breached
  ↓
If breached, notify risk owner and ERM Manager
  ↓
Dashboard updates
```

## 14. Incident Flow

```text
Incident occurs
  ↓
User records incident
  ↓
Link incident to objective and risk
  ↓
Record root cause and impact
  ↓
Add corrective action
  ↓
System flags risk for review
  ↓
Incident trend informs assessment
```

## 15. Review Flow

```text
Objective/risk/control/policy reaches review window
  ↓
System sends notification
  ↓
Owner performs review
  ↓
Update status, assessment, coverage, or controls
  ↓
Record review outcome
  ↓
Set next review date
  ↓
Review history saved
```

## 16. Assurance Flow

```text
Assurance activity created
  ↓
Link to objective, risk, control, or policy
  ↓
Record assurance provider
  ↓
Record findings and rating
  ↓
Create recommendations or actions
  ↓
Update assurance confidence
  ↓
Dashboard updates
```

## 17. Graph Exploration Flow

```text
User opens Risk Graph
  ↓
Select starting node:
    - Objective
    - Risk
    - Policy
    - Control
    - Business unit
  ↓
Select graph depth
  ↓
Filter node types
  ↓
Filter relationship types
  ↓
System renders graph
  ↓
User clicks node
  ↓
Node side panel opens
  ↓
User navigates to detail page
```

## 18. Reporting Flow

```text
User opens Reports
  ↓
Select report type:
    - Objective risk profile
    - Risk register
    - Policy coverage
    - Control coverage
    - Appetite breach
    - Assurance gap
  ↓
Apply filters
  ↓
Preview report
  ↓
Export CSV
  ↓
Audit log created
```

## 19. Key System Rules

1. An approved risk must be linked to at least one objective.
2. A risk must belong to the risk universe.
3. A risk must have an owner.
4. A risk must have inherent and residual assessment before approval.
5. A risk outside appetite must have treatment or formal acceptance.
6. Critical risks should have policy/procedure coverage or a documented gap.
7. Critical risks should have at least one control or a documented gap.
8. Every risk relationship must have a relationship type.
9. Every coverage link must have a coverage strength.
10. Key changes must create audit records.
