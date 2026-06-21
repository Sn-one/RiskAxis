from django.conf import settings
from django.db import models
from riskaxis.core.models import NamedModel, TimeStampedModel

class StrategyPillar(NamedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL)

class Objective(TimeStampedModel):
    class ObjectiveType(models.TextChoices):
        STRATEGIC="strategic","Strategic"; DEPARTMENTAL="departmental","Departmental"; OPERATIONAL="operational","Operational"; PROJECT="project","Project"; COMPLIANCE="compliance","Compliance"; PROCESS="process","Process"
    class Priority(models.TextChoices): LOW="low","Low"; MEDIUM="medium","Medium"; HIGH="high","High"; CRITICAL="critical","Critical"
    class Status(models.TextChoices): DRAFT="draft","Draft"; ACTIVE="active","Active"; ON_TRACK="on_track","On track"; AT_RISK="at_risk","At risk"; OFF_TRACK="off_track","Off track"; ACHIEVED="achieved","Achieved"; CLOSED="closed","Closed"
    objective_code=models.CharField(max_length=40, unique=True); title=models.CharField(max_length=220); description=models.TextField()
    objective_type=models.CharField(max_length=30, choices=ObjectiveType.choices); strategy_pillar=models.ForeignKey(StrategyPillar,null=True,blank=True,on_delete=models.SET_NULL)
    business_unit=models.ForeignKey("organization.BusinessUnit", on_delete=models.PROTECT); owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    priority=models.CharField(max_length=20, choices=Priority.choices, default=Priority.MEDIUM); status=models.CharField(max_length=30, choices=Status.choices, default=Status.DRAFT)
    start_date=models.DateField(null=True,blank=True); target_date=models.DateField(null=True,blank=True); review_frequency=models.CharField(max_length=30, default="quarterly")
    next_review_date=models.DateField(null=True,blank=True); success_measure=models.TextField(blank=True); target_value=models.CharField(max_length=120,blank=True); current_value=models.CharField(max_length=120,blank=True); appetite_notes=models.TextField(blank=True)
    class Meta: indexes=[models.Index(fields=["objective_code"]),models.Index(fields=["status"]),models.Index(fields=["target_date"])]
    def __str__(self): return f"{self.objective_code} — {self.title}"

class ObjectiveRelationship(TimeStampedModel):
    parent_objective=models.ForeignKey(Objective, related_name="child_links", on_delete=models.CASCADE); child_objective=models.ForeignKey(Objective, related_name="parent_links", on_delete=models.CASCADE)
    relationship_type=models.CharField(max_length=40, default="cascades_to"); rationale=models.TextField(blank=True)
    class Meta: constraints=[models.UniqueConstraint(fields=["parent_objective","child_objective","relationship_type"], name="unique_objective_relationship")]
