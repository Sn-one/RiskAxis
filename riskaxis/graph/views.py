from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from riskaxis.controls.models import ControlRiskLink
from riskaxis.documents.models import PolicyRiskCoverage
from riskaxis.objectives.models import Objective, ObjectiveRelationship
from riskaxis.risks.models import Risk, RiskObjectiveLink, RiskRelationship


def _node(node_id, label, node_type, **metadata):
    return {"id": node_id, "label": label, "type": node_type, "metadata": metadata}


def _edge(source, target, label, edge_type, **metadata):
    return {"source": source, "target": target, "label": label, "type": edge_type, "metadata": metadata}


@login_required
def erm_graph(request):
    """Return the objective-centered ERM graph as nodes and edges."""
    nodes = {}
    edges = []

    objectives = Objective.objects.select_related("business_unit", "owner", "strategy_pillar").filter(is_active=True)
    risks = Risk.objects.select_related("category", "primary_business_unit", "owner").filter(is_active=True)

    for objective in objectives:
        nodes[f"objective:{objective.pk}"] = _node(
            f"objective:{objective.pk}",
            objective.title,
            "objective",
            code=objective.objective_code,
            status=objective.status,
            business_unit=str(objective.business_unit),
        )

    for risk in risks:
        nodes[f"risk:{risk.pk}"] = _node(
            f"risk:{risk.pk}",
            risk.title,
            "risk",
            code=risk.risk_code,
            status=risk.status,
            approval_status=risk.approval_status,
            category=str(risk.category),
        )

    for link in ObjectiveRelationship.objects.select_related("parent_objective", "child_objective").filter(is_active=True):
        edges.append(_edge(
            f"objective:{link.parent_objective_id}",
            f"objective:{link.child_objective_id}",
            link.relationship_type,
            "objective_relationship",
            rationale=link.rationale,
        ))

    for link in RiskObjectiveLink.objects.select_related("risk", "objective").filter(is_active=True):
        edges.append(_edge(
            f"risk:{link.risk_id}",
            f"objective:{link.objective_id}",
            link.relationship_type,
            "risk_objective_link",
            strength=link.strength,
            is_primary=link.is_primary,
            impact_path=link.impact_path,
        ))

    for link in RiskRelationship.objects.select_related("source_risk", "target_risk").filter(is_active=True):
        edges.append(_edge(
            f"risk:{link.source_risk_id}",
            f"risk:{link.target_risk_id}",
            link.relationship_type,
            "risk_relationship",
            strength=link.strength,
            rationale=link.rationale,
        ))

    for link in PolicyRiskCoverage.objects.select_related("policy", "risk").filter(is_active=True, policy__is_active=True):
        policy_id = f"policy:{link.policy_id}"
        nodes.setdefault(policy_id, _node(policy_id, link.policy.title, "policy", code=link.policy.code, status=link.policy.status))
        edges.append(_edge(policy_id, f"risk:{link.risk_id}", link.coverage_type, "policy_risk_coverage", coverage_strength=link.coverage_strength))

    for link in ControlRiskLink.objects.select_related("control", "risk").filter(is_active=True, control__is_active=True):
        control_id = f"control:{link.control_id}"
        nodes.setdefault(control_id, _node(control_id, link.control.name, "control", code=link.control.control_code, design_effectiveness=link.control.design_effectiveness, operating_effectiveness=link.control.operating_effectiveness))
        edges.append(_edge(control_id, f"risk:{link.risk_id}", link.mitigation_effect, "control_risk_link", reliance_level=link.reliance_level))

    return JsonResponse({"nodes": list(nodes.values()), "edges": edges})
