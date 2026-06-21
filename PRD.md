# RiskAxis PRD
# Objective-Centered ERM Graph Platform — Django

## 1. Product Name

**RiskAxis**

## 2. Product Definition

RiskAxis is an objective-centered Enterprise Risk Management platform that helps organizations identify, assess, connect, treat, monitor, and report risks that may affect the achievement of strategic, departmental, operational, project, compliance, and process objectives.

Unlike a traditional risk register, RiskAxis starts from objectives. It asks:

> What can stop, delay, reduce, distort, or improve the achievement of this objective?

The platform links objectives, risks, policies, procedures, controls, KRIs, KPIs, incidents, treatment actions, reviews, assurance activities, and business units into a connected ERM model. It supports direct, indirect, precursor, cascading, departmental, dependency, and systemic risk relationships using a graph-style relationship layer.

## 3. Product Vision

To create a practical, standards-aligned, objective-centered ERM application that turns risk management into a living map of how uncertainty affects business performance.

RiskAxis should allow management to see:

- Which objectives are exposed to risk.
- Which risks directly or indirectly threaten objectives.
- Which risks are connected to other risks.
- Which policies and procedures cover each risk.
- Which controls are relied on.
- Which controls are weak or missing.
- Which risks are outside appetite.
- Which treatment actions are overdue.
- Which KRIs are warning of deteriorating exposure.
- Which objectives lack sufficient risk, control, policy, or monitoring coverage.

## 4. Business Problem

Many ERM systems begin with a risk register. This creates a flat list of risks without showing why each risk matters, what objective it affects, whether the risk is a root cause or consequence, whether controls are mapped properly, or whether policies and procedures actually cover the risk.

Common problems include:

- Objectives are not linked to risks.
- Risks are captured as isolated records.
- Policies and procedures are stored as documents but not mapped to the risks they cover.
- Controls are listed but not clearly linked to objectives, risks, or policies.
- Departments manage risks independently without seeing dependencies.
- Risk reports focus on ratings, not objective achievement.
- Management cannot see cascading risk pathways.
- Assurance teams cannot easily see coverage gaps.
- KRIs are disconnected from objectives and risk appetite.
- Risk registers become compliance documents rather than decision tools.

## 5. Product Philosophy

RiskAxis is built around the following ERM chain:

```text
Strategy
  → Objectives
    → Processes / Activities
      → Risks and Uncertainties
        → Risk Relationships
          → Policies / Procedures
            → Controls
              → Assessments
                → Appetite Comparison
                  → Treatment Actions
                    → KRIs / KPIs / Incidents
                      → Reviews
                        → Assurance
                          → Reporting and Decisions
```

The system should always preserve this logic:

```text
Objective: What are we trying to achieve?
Risk: What could affect achievement?
Related Risk: What causes, amplifies, triggers, or results from this risk?
Policy/Procedure: What guidance exists?
Control: What activity reduces the risk?
Assessment: How severe is the exposure?
Appetite: Is the exposure acceptable?
Treatment: What must be done?
KRI/KPI: How do we monitor change?
Incident: Has it already happened?
Review: Is the assessment still valid?
Assurance: Has the control or process been independently checked?
Dashboard: What decision should management make?
```

## 6. Product Objectives

RiskAxis must:

1. Start ERM from objectives, not risks.
2. Support strategic, departmental, operational, project, compliance, and process objectives.
3. Link risks directly and indirectly to objectives.
4. Support a risk universe taxonomy.
5. Support an official risk register.
6. Support graph-style risk relationships.
7. Map policies and procedures to the risks they cover.
8. Map controls to risks, objectives, policies, and procedures.
9. Assess inherent, residual, and target risk.
10. Compare residual risk to appetite.
11. Track treatment decisions and actions.
12. Track KRIs and KPIs.
13. Track incidents and loss events.
14. Support periodic risk reviews.
15. Support assurance mapping.
16. Generate dashboards focused on objectives, exposure, coverage, and action.
17. Preserve audit history for key ERM decisions.

## 7. Target Users

## 7.1 System Administrator

Configures users, roles, permissions, business units, scoring scales, categories, statuses, and application settings.

## 7.2 ERM Manager

Owns the ERM framework, reviews submitted risks, monitors objective risk exposure, manages the risk universe, oversees risk appetite, and prepares management reporting.

## 7.3 Strategy / Performance Manager

Defines strategic and departmental objectives, links KPIs, monitors objective status, and reviews how risks affect performance.

## 7.4 Risk Champion

Supports business units in identifying risks, mapping procedures, linking controls, updating risks, and maintaining departmental risk views.

## 7.5 Objective Owner

Accountable for achievement of an objective. Reviews risks, KRIs, actions, and control coverage linked to the objective.

## 7.6 Risk Owner

Accountable for a specific risk. Maintains risk assessment, controls, treatment plans, KRIs, and reviews.

## 7.7 Control Owner

Responsible for operating or maintaining a control linked to one or more risks.

## 7.8 Action Owner

Responsible for completing a treatment action.

## 7.9 Executive Viewer

Views strategic objectives at risk, top enterprise exposures, risk pathways, residual risk outside appetite, and overdue management actions.

## 7.10 Auditor / Assurance Reviewer

Reviews risk-control-policy-assurance relationships, control coverage, audit trails, evidence, and assurance gaps.

## 8. Scope

## 8.1 MVP Scope

The MVP should include:

- Authentication and user management.
- Role-based access control.
- Business units.
- Objective management.
- Objective hierarchy.
- Risk universe.
- Risk register.
- Risk-objective links.
- Risk-to-risk relationship mapping.
- Policy and procedure library.
- Policy/procedure-to-risk coverage mapping.
- Controls library.
- Control-to-risk mapping.
- Inherent and residual risk assessment.
- Risk appetite thresholds.
- Treatment actions.
- Basic KRIs.
- Periodic risk reviews.
- Objective-centered dashboards.
- Basic graph view.
- Reports and CSV export.
- Audit trail.
- Notifications for assignments and overdue items.

## 8.2 Out of Scope for MVP

The MVP will not include:

- Advanced AI risk recommendations.
- Automated KRI ingestion from external systems.
- Full audit management module.
- Full compliance obligation engine.
- Complex workflow designer.
- Multi-tenant SaaS billing.
- Advanced graph algorithms.
- Native mobile app.
- Automated policy text analysis.
- Board pack generation in PowerPoint.
- Advanced Monte Carlo or quantitative risk modeling.

These can be later releases.

## 9. Product Modules

## 9.1 Strategy & Objectives

The Objectives module is the foundation of RiskAxis.

### Functional Requirements

The system must allow users to create and manage objectives with:

- Objective ID.
- Objective title.
- Objective description.
- Objective type.
- Strategy pillar.
- Business unit.
- Owner.
- Parent objective.
- Linked child objectives.
- Priority.
- Start date.
- Target date.
- Status.
- KPI or success measure.
- Target value.
- Current performance.
- Risk appetite reference.
- Linked risks.
- Linked policies/procedures.
- Linked controls.
- Linked KRIs.
- Review frequency.

### Objective Types

- Strategic objective.
- Departmental objective.
- Operational objective.
- Project objective.
- Compliance objective.
- Process objective.

### Objective Statuses

- Draft.
- Active.
- On Track.
- At Risk.
- Off Track.
- Achieved.
- Closed.
- Archived.

### Acceptance Criteria

- A risk can be linked to one or more objectives.
- An objective can be linked to many risks.
- Objectives can cascade from strategic to departmental and operational levels.
- Objective dashboards show direct and indirect risks.
- Objective owners can see their risks, actions, KRIs, and coverage gaps.

## 9.2 Risk Universe

The Risk Universe is the structured taxonomy of possible risk areas across the organization.

### Functional Requirements

The system must support:

- Risk universe categories.
- Parent and child categories.
- Risk themes.
- Category owners.
- Category descriptions.
- Appetite guidance by category.
- Active/inactive categories.
- Mapping of risks to universe categories.

### Example Categories

- Strategic risk.
- Operational risk.
- Financial risk.
- Compliance risk.
- Legal risk.
- HSSE risk.
- Technology risk.
- Cyber risk.
- People risk.
- Supply chain risk.
- Market risk.
- Reputational risk.
- Fraud risk.
- Project risk.
- Third-party risk.

### Acceptance Criteria

- Every risk must belong to a risk universe category.
- ERM Manager can identify categories with no mapped risks.
- Dashboards show risk distribution by universe category.
- Risk universe can be filtered by business unit, objective, and residual rating.

## 9.3 Risk Register

The Risk Register is the official list of identified risks.

### Functional Requirements

Each risk must include:

- Risk ID.
- Risk title.
- Risk statement.
- Cause.
- Event.
- Consequence.
- Risk universe category.
- Primary business unit.
- Risk owner.
- Risk type.
- Status.
- Approval status.
- Inherent likelihood.
- Inherent impact.
- Inherent score.
- Inherent rating.
- Existing controls.
- Control effectiveness.
- Residual likelihood.
- Residual impact.
- Residual score.
- Residual rating.
- Target rating.
- Appetite status.
- Treatment strategy.
- Linked objectives.
- Linked risks.
- Linked policies/procedures.
- Linked controls.
- Linked KRIs.
- Linked incidents.
- Review date.
- Attachments.
- Comments.

### Risk Statement Format

Risk statements should follow this format:

```text
There is a risk that [event] caused by [cause], resulting in [consequence], which may affect [objective].
```

### Acceptance Criteria

- A risk cannot be approved without at least one linked objective.
- A risk cannot be approved without inherent and residual assessment.
- A high or critical residual risk must have treatment actions or formal acceptance.
- A risk can have multiple linked objectives.
- A risk can have multiple related risks.
- Approved risks appear in the official register.
- Draft risks remain outside the official register until approved.

## 9.4 Risk Graph

The Risk Graph module shows relationships across objectives, risks, policies, procedures, controls, KRIs, incidents, actions, and business units.

### Node Types

- Objective.
- Risk.
- Risk universe category.
- Business unit.
- Policy.
- Procedure.
- Control.
- KRI.
- KPI.
- Incident.
- Treatment action.
- Assurance activity.

### Relationship Types

Risk-to-objective:

- Direct threat.
- Indirect threat.
- Dependency.
- Opportunity.
- Emerging concern.

Risk-to-risk:

- Causes.
- Contributes to.
- Triggers.
- Precursor to.
- Consequence of.
- Amplifies.
- Mitigates.
- Shares control with.
- Same root cause as.
- Cascades to.
- Departmental dependency.

Policy/procedure-to-risk:

- Covers.
- Partially covers.
- Does not cover.
- Requires control.
- Provides guidance.

Control-to-risk:

- Prevents.
- Detects.
- Corrects.
- Reduces likelihood.
- Reduces impact.
- Reduces both.

### Acceptance Criteria

- Users can view a graph from an objective, risk, control, policy, or business unit.
- Users can filter graph by node type and relationship type.
- Users can open a node detail page from the graph.
- Graph relationships are stored as structured records, not just visual elements.
- MVP graph can be relationally stored and rendered in the UI.

## 9.5 Policies & Procedures

Policies and procedures are coverage objects. They must be mapped to the risks and controls they are intended to address.

### Functional Requirements

The system must capture:

- Document ID.
- Title.
- Document type.
- Owner.
- Business unit.
- Version.
- Effective date.
- Review date.
- Status.
- File attachment or document link.
- Linked objectives.
- Linked risks.
- Linked controls.
- Coverage type.
- Coverage strength.
- Coverage gap notes.

### Document Types

- Policy.
- Procedure.
- Standard.
- Guideline.
- Manual.
- Framework.
- Checklist.

### Coverage Strength

- Strong.
- Partial.
- Weak.
- Not assessed.
- No coverage.

### Acceptance Criteria

- A risk detail page shows policies and procedures covering the risk.
- A policy page shows all risks it covers.
- Dashboard identifies critical risks without policy/procedure coverage.
- Dashboard identifies expired policies linked to active risks.
- Users can record coverage gaps.

## 9.6 Controls Library

Controls are specific activities or mechanisms that reduce risk.

### Functional Requirements

The system must capture:

- Control ID.
- Control title.
- Control description.
- Control owner.
- Control type.
- Control nature.
- Frequency.
- Linked risks.
- Linked policies/procedures.
- Linked objectives.
- Design effectiveness.
- Operating effectiveness.
- Evidence.
- Last tested date.
- Next test date.
- Status.

### Control Types

- Preventive.
- Detective.
- Corrective.
- Directive.

### Control Nature

- Manual.
- Automated.
- Semi-automated.
- System-enforced.

### Acceptance Criteria

- A control can mitigate multiple risks.
- A risk can have multiple controls.
- Controls can be linked to policies and procedures.
- Ineffective controls appear on dashboards.
- Risks relying only on weak controls are flagged.

## 9.7 Risk Assessment

### Functional Requirements

The system must support:

- Inherent risk assessment.
- Residual risk assessment.
- Target risk assessment.
- Assessment rationale.
- Assessment history.
- Current assessment flag.
- Configurable likelihood scale.
- Configurable impact scale.
- Configurable rating thresholds.
- Risk appetite comparison.

### Default Formula

```text
Risk Score = Likelihood × Impact
```

### Acceptance Criteria

- Score is automatically calculated.
- Rating is automatically derived.
- Appetite status is automatically shown.
- Historical assessments are preserved.
- Residual rating can be compared against objective or category appetite.

## 9.8 Risk Appetite

Risk appetite defines acceptable exposure by objective, category, or enterprise level.

### Functional Requirements

The system must support:

- Enterprise appetite.
- Objective-level appetite.
- Category-level appetite.
- Business-unit appetite.
- Appetite rating threshold.
- Appetite breach flag.
- Acceptance approval for risks outside appetite.

### Acceptance Criteria

- Risks outside appetite are clearly flagged.
- A risk outside appetite requires treatment or formal acceptance.
- Dashboards show objectives with residual risk outside appetite.

## 9.9 Treatment Actions

### Functional Requirements

The system must support:

- Treatment strategy.
- Action title.
- Action description.
- Linked risk.
- Linked objective.
- Owner.
- Due date.
- Priority.
- Status.
- Progress.
- Evidence.
- Completion notes.
- Validation.

### Treatment Strategies

- Avoid.
- Reduce.
- Transfer.
- Accept.
- Monitor.
- Pursue opportunity.

### Acceptance Criteria

- High and critical risks require treatment or formal acceptance.
- Overdue actions appear on dashboards.
- Completed actions require evidence or completion notes.
- Action status history is retained.

## 9.10 KRIs and KPIs

KRIs monitor risk exposure. KPIs monitor objective performance. Both should be connectable to objectives and risks.

### Functional Requirements

The system must support:

- KRI/KPI name.
- Type: KRI or KPI.
- Owner.
- Unit of measure.
- Data source.
- Reporting frequency.
- Current value.
- Target value.
- Warning threshold.
- Breach threshold.
- Direction.
- Status.
- Linked objectives.
- Linked risks.
- Historical values.

### Acceptance Criteria

- Breached KRIs appear on dashboards.
- KPIs can show objectives at risk.
- KRI trends are visible.
- KRIs can be linked to risk appetite.

## 9.11 Incidents and Events

Incidents show realized risks or control failures.

### Functional Requirements

The system must support:

- Incident ID.
- Incident title.
- Date occurred.
- Date reported.
- Business unit.
- Description.
- Linked risk.
- Linked objective.
- Root cause.
- Impact.
- Loss amount if applicable.
- Status.
- Corrective actions.
- Attachments.

### Acceptance Criteria

- Incidents can be linked to risks.
- Repeated incidents can trigger risk review.
- Incident trends can inform risk assessment.

## 9.12 Reviews

### Functional Requirements

The system must support:

- Objective review.
- Risk review.
- Control review.
- Policy/procedure review.
- Review owner.
- Review date.
- Outcome.
- Notes.
- Next review date.
- Review history.

### Acceptance Criteria

- Overdue reviews appear on dashboards.
- Reviews can update risk ratings or coverage status.
- Review history cannot be deleted by ordinary users.

## 9.13 Assurance Mapping

Assurance mapping shows whether risks and controls have been independently reviewed.

### Functional Requirements

The system must support:

- Assurance activity.
- Assurance provider.
- Assurance type.
- Linked objective.
- Linked risk.
- Linked control.
- Findings.
- Rating.
- Date.
- Recommendations.
- Follow-up action.

### Assurance Types

- Management self-assessment.
- Compliance review.
- Internal audit.
- External audit.
- Control testing.
- Regulatory review.

### Acceptance Criteria

- Critical risks without assurance are flagged.
- Ineffective controls with no assurance are flagged.
- Assurance findings can create treatment actions.

## 9.14 Dashboards and Reports

### Executive Dashboard

Must show:

- Strategic objectives at risk.
- Top enterprise risks.
- Residual risks outside appetite.
- Critical risk pathways.
- Policy/control coverage gaps.
- Overdue executive actions.
- Breached KRIs.
- Emerging risks.

### ERM Dashboard

Must show:

- Objectives without risk assessment.
- Risks without linked objectives.
- Risks without policy coverage.
- Risks without controls.
- Risks outside appetite.
- High risks without treatment.
- Overdue reviews.
- Overdue actions.
- Ineffective controls.
- Risk graph clusters.
- Risk universe coverage.

### Department Dashboard

Must show:

- Department objectives.
- Risks linked to department objectives.
- Risks received from other departments.
- Risks affecting other departments.
- Open treatment actions.
- Overdue reviews.
- Policy gaps.
- Control gaps.

### Reports

MVP reports:

- Objective risk profile.
- Enterprise risk register.
- Risk universe coverage.
- Policy coverage report.
- Control coverage report.
- Treatment action report.
- KRI breach report.
- Risk appetite breach report.
- Assurance gap report.

## 10. Coverage Intelligence

RiskAxis should calculate coverage indicators.

### Objective Coverage

Measures whether an objective has:

- Linked risks.
- Assessed risks.
- Linked controls.
- Linked policies/procedures.
- Linked KRIs/KPIs.
- Treatment plans where needed.
- Up-to-date reviews.
- Assurance coverage.

### Coverage Outputs

- Risk coverage score.
- Policy coverage score.
- Control coverage score.
- Monitoring coverage score.
- Assurance confidence level.

### Example

```text
Objective: Improve station availability
Risk Coverage: 85%
Policy Coverage: 70%
Control Coverage: 65%
Monitoring Coverage: 50%
Assurance Confidence: Medium
```

## 11. MVP Success Metrics

- 100% of active objectives entered.
- 80% of active objectives have linked risks.
- 100% of critical risks linked to at least one objective.
- 100% of critical risks have a risk owner.
- 90% of critical risks mapped to policies/procedures or marked as coverage gap.
- 90% of critical risks mapped to at least one control.
- 100% of risks outside appetite have treatment or formal acceptance.
- Overdue actions visible on dashboard.
- Executive dashboard generated without manual spreadsheet consolidation.
- Risk graph available for objectives and top risks.

## 12. Future Enhancements

- AI-assisted risk identification from objectives.
- AI-assisted policy coverage analysis.
- Graph analytics for systemic risk.
- Automated KRI data ingestion.
- Internal audit module.
- Compliance obligation mapping.
- Board reporting pack.
- Scenario analysis.
- Quantitative risk modeling.
- Multi-entity support.
- Advanced workflow builder.
