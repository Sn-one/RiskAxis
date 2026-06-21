# RiskAxis UI/UX Design Brief
# Objective-Centered ERM Graph Platform

## 1. Product Experience Goal

RiskAxis should feel like a professional ERM command center. It should help users start from objectives, identify what can affect achievement, map related risks, connect policies and controls, monitor actions and indicators, and report exposure clearly to management.

The application must not feel like a spreadsheet converted to a website. It must feel like a structured ERM system where every screen answers:

> What objective is at risk, why, how serious is it, what covers it, what is missing, and what decision is needed?

## 2. Design Principles

## 2.1 Objectives First

Every risk must be shown in relation to objectives. Users should be encouraged to begin with the objective and then identify risks.

## 2.2 Show Relationships

The UI must reveal connections:

- Objective to risk.
- Risk to risk.
- Risk to policy.
- Risk to control.
- Risk to KRI.
- Risk to action.
- Risk to incident.
- Risk to assurance.

## 2.3 Reduce ERM Complexity

ERM can become abstract. The interface must guide users through practical questions and avoid overwhelming them.

## 2.4 Make Gaps Visible

The app should clearly show missing links:

- Objectives without risks.
- Risks without objectives.
- Risks without controls.
- Risks without policy coverage.
- Risks without KRIs.
- Risks outside appetite.
- High risks without treatment.
- Controls without assurance.

## 2.5 Management-Ready

Dashboards must be clean enough for management discussions without manual formatting.

## 3. Visual Identity

## 3.1 Name

**RiskAxis**

## 3.2 Meaning

RiskAxis represents the central axis connecting objectives, risks, controls, policies, actions, KRIs, incidents, departments, and assurance.

## 3.3 Tone

- Professional.
- Clear.
- Strategic.
- Calm.
- Intelligent.
- Enterprise-grade.

## 3.4 Suggested Tagline

```text
Connect objectives, risks, controls, and assurance.
```

Alternative:

```text
ERM built around what matters: objectives.
```

## 4. Navigation Structure

Recommended left sidebar:

1. Dashboard
2. Objectives
3. Risk Universe
4. Risk Register
5. Risk Graph
6. Policies & Procedures
7. Controls
8. KRIs & KPIs
9. Treatment Actions
10. Incidents
11. Reviews
12. Assurance
13. Reports
14. Notifications
15. Administration

## 5. Role-Based Home Pages

## 5.1 Executive Viewer

Landing page:

- Strategic objectives at risk.
- Top enterprise risks.
- Risk appetite breaches.
- Critical risk pathways.
- Overdue executive actions.
- Major coverage gaps.
- KRI breaches.

## 5.2 ERM Manager

Landing page:

- ERM coverage score.
- Objectives without risk assessment.
- Risks pending approval.
- Risks outside appetite.
- Risks without policies.
- Risks without controls.
- Overdue reviews.
- Overdue actions.
- Graph clusters.

## 5.3 Objective Owner

Landing page:

- My objectives.
- Objective status.
- Risks affecting my objectives.
- Direct and indirect risks.
- Actions linked to my objectives.
- KRIs and KPIs.
- Coverage gaps.

## 5.4 Risk Owner

Landing page:

- My risks.
- Reviews due.
- Linked objectives.
- Risk relationships.
- Treatment actions.
- KRI breaches.
- Controls requiring update.

## 5.5 Risk Champion

Landing page:

- Department objectives.
- Department risks.
- Draft risks.
- Risks requiring updates.
- Policy/control mapping gaps.

## 6. Key Screens

## 6.1 Objective Detail Page

This is one of the most important screens.

### Header

- Objective title.
- Objective status.
- Owner.
- Business unit.
- Priority.
- Target date.
- Overall ERM coverage score.

### Top Cards

- Linked risks.
- High/critical risks.
- Risks outside appetite.
- Overdue actions.
- Breached KRIs.
- Policy coverage score.
- Control coverage score.
- Assurance confidence.

### Tabs

1. Overview.
2. Linked Risks.
3. Risk Graph.
4. Policies & Procedures.
5. Controls.
6. KRIs & KPIs.
7. Treatment Actions.
8. Incidents.
9. Reviews.
10. Assurance.
11. History.

### Primary Actions

- Add Risk.
- Link Existing Risk.
- Add KRI/KPI.
- Add Review.
- View Graph.
- Export Profile.

## 6.2 Risk Detail Page

### Header

- Risk ID.
- Risk title.
- Residual rating.
- Appetite status.
- Owner.
- Business unit.
- Approval status.

### Risk Summary Panel

Show:

- Risk statement.
- Cause.
- Event.
- Consequence.
- Linked objectives.
- Direct/indirect impact.
- Related risks.
- Risk universe category.

### Tabs

1. Overview.
2. Objectives.
3. Assessment.
4. Related Risks.
5. Policies & Procedures.
6. Controls.
7. Treatment Actions.
8. KRIs.
9. Incidents.
10. Reviews.
11. Assurance.
12. Attachments.
13. Comments.
14. History.

## 6.3 Risk Graph Page

The graph page should allow users to explore relationships.

### Graph Controls

- Search node.
- Filter by node type.
- Filter by relationship type.
- Depth selector: 1, 2, 3 hops.
- Show only high/critical risks.
- Show only gaps.
- Show upstream.
- Show downstream.
- Export image or data later.

### Node Visuals

Node types should be visually distinct:

- Objective: circle or rounded rectangle.
- Risk: diamond or alert node.
- Policy/Procedure: document node.
- Control: shield node.
- KRI/KPI: gauge node.
- Incident: warning node.
- Action: task node.
- Assurance: checkmark node.
- Business unit: building node.

### Edge Labels

Edges must be labeled:

- Threatens.
- Supports.
- Covers.
- Mitigates.
- Causes.
- Triggers.
- Amplifies.
- Monitors.
- Reviews.

## 6.4 Create Objective Flow

Use a guided form:

### Step 1: Objective Basics

- Title.
- Description.
- Type.
- Strategy pillar.
- Business unit.
- Owner.
- Parent objective.

### Step 2: Performance

- KPI.
- Target.
- Current value.
- Target date.
- Review frequency.

### Step 3: Appetite

- Appetite level.
- Tolerance notes.
- Escalation rule.

### Step 4: Initial Risk Prompt

Ask:

```text
What could prevent this objective from being achieved?
What could delay it?
What could reduce its value?
What dependencies could fail?
What external changes could affect it?
What opportunities could be missed?
```

Users may add initial risks immediately or skip.

## 6.5 Create Risk Flow

Use a guided wizard.

### Step 1: Link Objective

- Select objective.
- Define link type: direct, indirect, dependency, opportunity, emerging.
- Explain how the risk affects the objective.

### Step 2: Risk Statement

- Cause.
- Event.
- Consequence.
- Auto-generated statement preview.

### Step 3: Categorize

- Risk universe category.
- Business unit.
- Risk owner.
- Risk type.

### Step 4: Related Risks

- Add precursor risk.
- Add triggering risk.
- Add cascading risk.
- Add departmental dependency.
- Add same root cause relationship.

### Step 5: Policies and Procedures

- Link existing policy/procedure.
- Mark coverage strength.
- Record coverage gap if missing.

### Step 6: Controls

- Link existing controls.
- Add new control.
- Set control effectiveness.

### Step 7: Assessment

- Inherent likelihood and impact.
- Residual likelihood and impact.
- Rationale.
- Appetite comparison.

### Step 8: Treatment

- Treatment strategy.
- Action owner.
- Due date.
- Priority.

### Step 9: Review and Submit

- Summary.
- Missing coverage warnings.
- Submit for approval.

## 6.6 Policy / Procedure Detail Page

### Header

- Document title.
- Type.
- Owner.
- Status.
- Version.
- Review date.

### Tabs

1. Overview.
2. Covered Risks.
3. Supported Objectives.
4. Linked Controls.
5. Coverage Gaps.
6. Review History.
7. Attachments.

## 6.7 Control Detail Page

### Header

- Control title.
- Control owner.
- Type.
- Frequency.
- Effectiveness.
- Status.

### Tabs

1. Overview.
2. Linked Risks.
3. Linked Policies/Procedures.
4. Evidence.
5. Testing / Assurance.
6. History.

## 7. Dashboard Design

## 7.1 Executive Dashboard

Top section:

- Strategic objectives at risk.
- Critical residual risks.
- Appetite breaches.
- Overdue executive actions.
- Breached KRIs.
- Assurance confidence.

Middle section:

- Objective risk profile.
- Top 10 enterprise risks.
- Risk heatmap.
- Critical risk pathways.

Bottom section:

- Policy/control gaps.
- Actions requiring executive attention.
- Emerging risks.

## 7.2 ERM Dashboard

Top cards:

- Total active objectives.
- Objectives with risk assessment.
- Active risks.
- High/critical risks.
- Risks outside appetite.
- Overdue reviews.
- Overdue actions.
- Coverage gaps.

Main panels:

- Objectives without linked risks.
- Risks without policy coverage.
- Risks without controls.
- Risks without KRIs.
- Ineffective controls.
- Graph cluster summary.
- Pending approvals.

## 7.3 Department Dashboard

Show:

- Department objectives.
- Linked risks.
- Risks from other departments affecting this department.
- Department risks affecting other departments.
- Open actions.
- Overdue actions.
- Coverage gaps.
- KRI breaches.

## 8. Data Table Design

Tables should support:

- Search.
- Filters.
- Saved views.
- Column visibility.
- Export.
- Bulk actions where authorized.
- Status badges.
- Rating badges.
- Appetite badges.
- Coverage badges.

## 9. Color Semantics

Risk ratings:

- Low: green.
- Medium: amber.
- High: orange.
- Critical: red.

Coverage:

- Strong: green.
- Partial: amber.
- Weak: orange.
- Missing: red.
- Not assessed: gray.

Status:

- Draft: gray.
- Active: blue.
- Approved: green.
- Under review: purple.
- Overdue: red.
- Closed: gray.

## 10. Empty States

## 10.1 Objective Without Risks

```text
No risks have been linked to this objective yet.
Start by identifying what could prevent, delay, reduce, or distort achievement.

[Add Risk] [Link Existing Risk]
```

## 10.2 Risk Without Policy Coverage

```text
No policy or procedure coverage has been mapped for this risk.
This may indicate a governance gap.

[Link Policy/Procedure] [Record Gap]
```

## 10.3 Risk Without Controls

```text
No controls are currently linked to this risk.
Add a control or mark the risk as requiring treatment.

[Add Control] [Create Treatment Action]
```

## 11. UX Acceptance Criteria

- Users can create an objective and link risks within one guided flow.
- Users can see all risks affecting an objective from the objective page.
- Users can distinguish direct and indirect risks.
- Users can map a policy/procedure to a risk.
- Users can identify missing policy or control coverage.
- Users can view a graph for any objective or risk.
- ERM Manager can see risks outside appetite immediately.
- Executive Viewer can understand top objective exposures without entering detailed records.
- High-risk gaps are visible without manual analysis.
