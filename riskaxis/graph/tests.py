from django.test import TestCase, override_settings
from django.urls import reverse

from riskaxis.accounts.models import User
from riskaxis.objectives.models import Objective
from riskaxis.organization.models import BusinessUnit
from riskaxis.risk_universe.models import RiskUniverseCategory
from riskaxis.risks.models import Risk, RiskObjectiveLink


@override_settings(SECURE_SSL_REDIRECT=False)
class ErmGraphTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="erm@example.com", password="testpass123")
        self.unit = BusinessUnit.objects.create(name="Enterprise", code="ENT")
        self.category = RiskUniverseCategory.objects.create(name="Operational", code="OPS")
        self.objective = Objective.objects.create(
            objective_code="OBJ-1",
            title="Improve resilience",
            description="Improve operational resilience.",
            objective_type=Objective.ObjectiveType.STRATEGIC,
            business_unit=self.unit,
            owner=self.user,
        )
        self.risk = Risk.objects.create(
            risk_code="RSK-1",
            title="Supplier outage",
            risk_statement="A supplier outage could disrupt operations.",
            category=self.category,
            primary_business_unit=self.unit,
            owner=self.user,
        )
        RiskObjectiveLink.objects.create(risk=self.risk, objective=self.objective, relationship_type="direct_threat")

    def test_graph_endpoint_requires_login(self):
        response = self.client.get(reverse("graph:erm"))
        self.assertEqual(response.status_code, 302)

    def test_graph_endpoint_returns_nodes_and_edges(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("graph:erm"))
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(len(payload["nodes"]), 2)
        self.assertEqual(len(payload["edges"]), 1)
        self.assertEqual(payload["edges"][0]["type"], "risk_objective_link")
