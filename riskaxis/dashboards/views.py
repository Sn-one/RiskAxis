from django.contrib.auth.decorators import login_required
from django.db.models import Count, Max
from django.shortcuts import render
from riskaxis.objectives.models import Objective
from riskaxis.risks.models import Risk
from riskaxis.controls.models import Control
from riskaxis.treatments.models import TreatmentAction
from riskaxis.incidents.models import Incident

@login_required
def dashboard(request):
    context = {
        "objective_count": Objective.objects.count(),
        "risk_count": Risk.objects.count(),
        "control_count": Control.objects.count(),
        "incident_count": Incident.objects.count(),
        "open_actions": TreatmentAction.objects.exclude(status__in=["done", "closed", "completed"]).count(),
        "objectives_by_status": list(Objective.objects.values("status").annotate(count=Count("id")).order_by("status")),
        "risks_by_status": list(Risk.objects.values("status").annotate(count=Count("id")).order_by("status")),
        "recent_risks": Risk.objects.select_related("category", "owner")[:8],
        "recent_objectives": Objective.objects.select_related("business_unit", "owner")[:8],
        "last_updated": max(filter(None, [Objective.objects.aggregate(v=Max("updated_at"))["v"], Risk.objects.aggregate(v=Max("updated_at"))["v"]]), default=None),
    }
    return render(request, "riskaxis/dashboard.html", context)
