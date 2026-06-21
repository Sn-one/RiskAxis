# RiskAxis TRD
# Technical Requirements Document — Objective-Centered ERM Graph Platform

## 1. Technical Overview

RiskAxis is a Django-based objective-centered Enterprise Risk Management platform. It uses a modular monolith architecture with a relational data model that supports graph-style relationships between objectives, risks, policies, procedures, controls, KRIs, incidents, treatment actions, assurance activities, and business units.

The MVP will use PostgreSQL as the system of record. Graph relationships will be stored in explicit relationship tables. This allows the application to render graph views while keeping the MVP technically manageable. A graph database such as Neo4j can be considered later if advanced graph analytics becomes necessary.

## 2. Technical Goals

The system must be:

- Objective-centered.
- Secure.
- Role-based.
- Auditable.
- Modular.
- Extendable.
- Graph-aware.
- Standards-aligned.
- Easy to deploy.
- Practical for internal business users.

## 3. Architecture Recommendation

Use a **Django modular monolith** for the MVP.

### Rationale

- Django supports rapid development and clean, pragmatic design.
- Django includes authentication, sessions, users, groups, and permissions.
- Django migrations support controlled schema evolution.
- PostgreSQL supports relational integrity, JSON fields, recursive queries, and indexes.
- A modular monolith is easier to maintain than microservices at MVP stage.
- Relationship tables can support graph visualization without requiring a separate graph database.

## 4. Recommended Stack

## 4.1 Backend

- Python.
- Django.
- Django REST Framework.
- PostgreSQL.
- Celery or Django-Q/RQ later for scheduled tasks.
- Redis later for background jobs and caching.

## 4.2 Frontend

Recommended MVP:

- Django templates.
- HTMX for dynamic partial updates.
- Alpine.js for lightweight client-side behavior.
- Tailwind CSS for styling.
- Chart.js or ECharts for dashboards.
- Cytoscape.js, React Flow, D3.js, or Vis.js for graph visualization.

Alternative future:

- React frontend consuming Django REST Framework APIs.

## 4.3 Infrastructure

- Linux server or containerized deployment.
- Gunicorn.
- Nginx.
- PostgreSQL.
- Object/file storage for attachments.
- Environment variables for configuration.
- CI/CD pipeline.
- Automated backups.

## 5. Proposed Django Apps

| App | Purpose |
|---|---|
| accounts | Custom user model, roles, profile, permissions |
| organization | Business units, departments, teams |
| objectives | Strategy pillars, objectives, objective hierarchy, KPIs |
| risk_universe | Risk taxonomy, categories, themes |
| risks | Risk register, risk statements, risk status |
| graph | Relationship models and graph API |
| documents | Policies, procedures, standards, file metadata |
| controls | Controls library and control-risk links |
| assessments | Inherent, residual, target assessments, scoring |
| appetite | Risk appetite thresholds and breaches |
| treatments | Treatment strategies and actions |
| indicators | KRIs, KPIs, values, thresholds |
| incidents | Incidents, events, realized risks |
| reviews | Objective, risk, control, and document reviews |
| assurance | Assurance activities, findings, recommendations |
| dashboards | Aggregated views and metrics |
| reports | Exports and report generation |
| notifications | In-app and email notifications |
| auditlog | Audit trail |
| core | Shared utilities, base models, services |

## 6. High-Level Data Architecture

RiskAxis should use these key entities:

- User.
- Role / Group.
- BusinessUnit.
- StrategyPillar.
- Objective.
- ObjectiveRelationship.
- RiskUniverseCategory.
- Risk.
- RiskObjectiveLink.
- RiskRelationship.
- PolicyProcedure.
- PolicyRiskCoverage.
- Control.
- ControlRiskLink.
- RiskAssessment.
- RiskAppetite.
- TreatmentAction.
- Indicator.
- IndicatorValue.
- Incident.
- Review.
- AssuranceActivity.
- Attachment.
- Comment.
- Notification.
- AuditLog.

## 7. Relationship Model

The relationship model is central to RiskAxis.

## 7.1 Objective Relationships

Objectives can cascade.

```text
Strategic Objective
  → Departmental Objective
    → Operational Objective
      → Process Objective
```

Store this in `ObjectiveRelationship`.

## 7.2 Risk-Objective Relationships

A risk can affect an objective directly or indirectly.

Store this in `RiskObjectiveLink`.

Relationship types:

- Direct threat.
- Indirect threat.
- Dependency.
- Opportunity.
- Emerging concern.

## 7.3 Risk-Risk Relationships

Risks can influence each other.

Store this in `RiskRelationship`.

Relationship types:

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

## 7.4 Policy-Risk Relationships

Policies and procedures provide coverage.

Store this in `PolicyRiskCoverage`.

Coverage types:

- Preventive.
- Detective.
- Corrective.
- Directive.
- Governance.
- Compliance.

Coverage strength:

- Strong.
- Partial.
- Weak.
- Not assessed.
- No coverage.

## 7.5 Control-Risk Relationships

Controls mitigate risks.

Store this in `ControlRiskLink`.

Mitigation effects:

- Reduces likelihood.
- Reduces impact.
- Reduces both.
- Detects occurrence.
- Corrects after occurrence.

## 8. Graph Storage Strategy

## 8.1 MVP Approach

Use PostgreSQL tables for all relationships.

Advantages:

- Simple deployment.
- Strong data integrity.
- Easy integration with Django ORM.
- Sufficient for MVP graph visualization.
- Avoids premature complexity.

## 8.2 Future Graph Database Option

Introduce Neo4j or another graph database only if the app requires:

- Multi-hop risk pathway analytics.
- Centrality analysis.
- Community detection.
- Systemic risk clustering.
- Advanced dependency path scoring.
- Large-scale relationship exploration.

## 9. Core Services

## 9.1 Objective Risk Coverage Service

Calculates whether an objective has adequate ERM coverage.

Inputs:

- Linked risks.
- Risk assessments.
- Policy coverage.
- Control coverage.
- KRI/KPI coverage.
- Treatment actions.
- Reviews.
- Assurance activities.

Outputs:

- Risk coverage score.
- Policy coverage score.
- Control coverage score.
- Monitoring coverage score.
- Assurance confidence.

## 9.2 Risk Scoring Service

Calculates:

- Inherent score.
- Residual score.
- Target score.
- Rating.
- Appetite status.

Default formula:

```text
Risk Score = Likelihood × Impact
```

## 9.3 Appetite Service

Determines whether a residual risk is:

- Within appetite.
- At appetite limit.
- Outside appetite.
- Formally accepted.

## 9.4 Graph Service

Provides graph data to the UI.

Functions:

- Get graph for objective.
- Get graph for risk.
- Get graph for business unit.
- Get graph for policy.
- Get upstream risks.
- Get downstream risks.
- Get risk pathway.
- Get uncovered nodes.

## 9.5 Notification Service

Creates notifications for:

- Risk assigned.
- Objective assigned.
- Action assigned.
- Risk submitted.
- Risk approved.
- Review due.
- Action due.
- Action overdue.
- KRI breached.
- Risk outside appetite.

## 9.6 Audit Service

Logs important actions:

- Objective creation/update.
- Risk creation/update.
- Risk approval.
- Risk rating change.
- Owner change.
- Relationship creation/deletion.
- Policy coverage change.
- Control effectiveness change.
- Appetite breach acceptance.
- Export generation.

## 10. Workflow State Machines

## 10.1 Objective Status

- Draft.
- Active.
- On Track.
- At Risk.
- Off Track.
- Achieved.
- Closed.
- Archived.

## 10.2 Risk Approval Status

- Draft.
- Submitted.
- Revision Required.
- Approved.
- Rejected.
- Closed.
- Archived.

## 10.3 Risk Operational Status

- Open.
- Under Review.
- Treatment In Progress.
- Accepted.
- Escalated.
- Closed.
- Archived.

## 10.4 Treatment Action Status

- Not Started.
- In Progress.
- Blocked.
- Completed.
- Overdue.
- Cancelled.

## 10.5 Policy/Procedure Status

- Draft.
- Active.
- Under Review.
- Expired.
- Superseded.
- Archived.

## 10.6 Control Status

- Active.
- Inactive.
- Under Review.
- Ineffective.
- Retired.

## 11. Permissions Model

## 11.1 Roles

- Admin.
- ERM Manager.
- Strategy Manager.
- Objective Owner.
- Risk Champion.
- Risk Owner.
- Control Owner.
- Action Owner.
- Executive Viewer.
- Auditor.

## 11.2 Access Principles

- Admin can configure system and manage users.
- ERM Manager can access all ERM records.
- Strategy Manager can manage objectives and performance links.
- Objective Owner can manage objectives assigned to them.
- Risk Owner can manage assigned risks.
- Risk Champion can support risks in assigned business units.
- Control Owner can manage assigned controls.
- Action Owner can update assigned actions.
- Executive Viewer can view approved executive dashboards.
- Auditor can view assigned assurance and audit records.

## 11.3 Object-Level Access

Object-level access is required for:

- Objectives.
- Risks.
- Controls.
- Actions.
- Documents.
- Incidents.
- Assurance records.

Rules should consider:

- User role.
- Business unit assignment.
- Ownership.
- Approval status.
- Confidentiality level.
- Executive-only classification.

## 12. API Requirements

## 12.1 Example API Endpoints

```text
GET    /api/objectives/
POST   /api/objectives/
GET    /api/objectives/{id}/
PATCH  /api/objectives/{id}/
GET    /api/objectives/{id}/risks/
GET    /api/objectives/{id}/graph/
GET    /api/objectives/{id}/coverage/

GET    /api/risks/
POST   /api/risks/
GET    /api/risks/{id}/
PATCH  /api/risks/{id}/
POST   /api/risks/{id}/submit/
POST   /api/risks/{id}/approve/
GET    /api/risks/{id}/graph/
GET    /api/risks/{id}/pathways/

POST   /api/relationships/risk-objective/
POST   /api/relationships/risk-risk/
POST   /api/relationships/policy-risk/
POST   /api/relationships/control-risk/

GET    /api/dashboard/executive/
GET    /api/dashboard/erm/
GET    /api/dashboard/department/{id}/

GET    /api/reports/objective-risk-profile/
GET    /api/reports/risk-register/
GET    /api/reports/policy-coverage/
```

## 13. Security Requirements

## 13.1 Authentication

- Authenticated access required.
- Password reset flow.
- Secure sessions.
- Optional MFA in later release.
- Production HTTPS.
- Secure cookie configuration.

## 13.2 Authorization

- Role-based access control.
- Object-level permissions.
- API permission checks.
- UI permission checks.
- Prevent unauthorized direct object access.

## 13.3 Data Protection

- Store secrets in environment variables.
- Disable debug in production.
- Validate file uploads.
- Restrict file types.
- Protect media access where needed.
- Avoid sensitive data in logs.
- Maintain audit trail.

## 13.4 Secure Development

- Use CSRF protection.
- Validate input server-side.
- Use Django ORM safely.
- Escape template output.
- Follow OWASP access control and logging guidance.
- Monitor failed access attempts.

## 14. Performance Requirements

- Paginate lists.
- Add indexes to common filters.
- Use `select_related` and `prefetch_related`.
- Cache dashboard aggregates if needed.
- Optimize graph queries.
- Limit graph depth in UI.
- Support export jobs asynchronously in later phases.

## 15. Recommended Indexes

- Objective: owner, business_unit, status, objective_type.
- Risk: owner, business_unit, category, status, approval_status, residual_rating.
- RiskObjectiveLink: risk, objective, relationship_type.
- RiskRelationship: source_risk, target_risk, relationship_type.
- PolicyRiskCoverage: policy, risk, coverage_strength.
- ControlRiskLink: control, risk, effectiveness.
- TreatmentAction: owner, status, due_date, risk.
- IndicatorValue: indicator, measurement_date, status.
- AuditLog: actor, event_type, object_type, object_id, created_at.

## 16. Testing Requirements

## 16.1 Unit Tests

- Risk score calculation.
- Rating threshold calculation.
- Appetite breach logic.
- Objective coverage score.
- Policy coverage score.
- Control coverage score.
- Risk relationship validation.
- Workflow state transitions.
- Permission checks.

## 16.2 Integration Tests

- Objective creation to risk mapping.
- Risk creation to approval.
- Policy coverage mapping.
- Control mapping.
- Treatment action workflow.
- KRI breach workflow.
- Review workflow.
- Dashboard aggregation.
- Graph API response.

## 16.3 Security Tests

- Unauthenticated access.
- Unauthorized object access.
- Role escalation.
- Business-unit boundary access.
- CSRF enforcement.
- File upload validation.
- Export authorization.

## 17. Deployment Requirements

## 17.1 Environments

- Local.
- Staging.
- Production.

## 17.2 Environment Variables

- SECRET_KEY.
- DEBUG.
- ALLOWED_HOSTS.
- DATABASE_URL.
- EMAIL settings.
- STORAGE settings.
- CSRF_TRUSTED_ORIGINS.
- SESSION_COOKIE_SECURE.
- CSRF_COOKIE_SECURE.

## 18. Suggested Repository Structure

```text
riskaxis/
  manage.py
  pyproject.toml
  README.md
  .env.example
  config/
    settings/
      base.py
      local.py
      production.py
    urls.py
    wsgi.py
    asgi.py
  apps/
    accounts/
    organization/
    objectives/
    risk_universe/
    risks/
    graph/
    documents/
    controls/
    assessments/
    appetite/
    treatments/
    indicators/
    incidents/
    reviews/
    assurance/
    dashboards/
    reports/
    notifications/
    auditlog/
    core/
  templates/
  static/
  media/
  docs/
    PRD.md
    TRD.md
    UI_UX_DESIGN_BRIEF.md
    APPFLOW.md
    SCHEMA.md
    README.md
    REFERENCES.md
  tests/
```

## 19. Technical Roadmap

## Phase 1: Foundation

- Django project setup.
- Custom user model.
- Roles and permissions.
- Business units.
- Risk universe.
- Objective model.
- Objective hierarchy.

## Phase 2: Core ERM

- Risk register.
- Risk-objective links.
- Risk assessments.
- Approval workflow.
- Risk appetite.
- Basic dashboards.

## Phase 3: Coverage Mapping

- Policies and procedures.
- Controls.
- Policy-risk coverage.
- Control-risk mapping.
- Coverage gap indicators.

## Phase 4: Graph and Monitoring

- Risk-to-risk relationships.
- Graph API.
- Graph visualization.
- KRIs/KPIs.
- Treatment actions.
- Reviews.

## Phase 5: Assurance and Reporting

- Assurance activities.
- Incidents.
- Advanced dashboards.
- Reports and exports.
- Audit hardening.

## Phase 6: Advanced Intelligence

- Graph analytics.
- Automated KRI ingestion.
- AI-assisted risk suggestions.
- AI-assisted policy coverage review.
