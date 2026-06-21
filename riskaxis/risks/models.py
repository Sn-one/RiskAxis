from django.conf import settings
from django.db import models
from riskaxis.core.models import TimeStampedModel
class Risk(TimeStampedModel):
    risk_code=models.CharField(max_length=40, unique=True); title=models.CharField(max_length=220); risk_statement=models.TextField(); cause=models.TextField(blank=True); event=models.TextField(blank=True); consequence=models.TextField(blank=True)
    category=models.ForeignKey("risk_universe.RiskUniverseCategory",on_delete=models.PROTECT); primary_business_unit=models.ForeignKey("organization.BusinessUnit",on_delete=models.PROTECT); owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.PROTECT)
    risk_type=models.CharField(max_length=30,default="threat"); status=models.CharField(max_length=40,default="open"); approval_status=models.CharField(max_length=40,default="draft"); confidentiality=models.CharField(max_length=40,default="normal"); treatment_strategy=models.CharField(max_length=40,default="reduce")
    next_review_date=models.DateField(null=True,blank=True); last_review_date=models.DateField(null=True,blank=True); approved_by=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,related_name="approved_risks",on_delete=models.SET_NULL); approved_at=models.DateTimeField(null=True,blank=True); closed_at=models.DateTimeField(null=True,blank=True); closure_reason=models.TextField(blank=True)
    class Meta: indexes=[models.Index(fields=["risk_code"]),models.Index(fields=["status"]),models.Index(fields=["approval_status"])]
    def __str__(self): return f"{self.risk_code} — {self.title}"
class RiskObjectiveLink(TimeStampedModel):
    risk=models.ForeignKey(Risk, related_name="objective_links", on_delete=models.CASCADE); objective=models.ForeignKey("objectives.Objective", related_name="risk_links", on_delete=models.CASCADE); relationship_type=models.CharField(max_length=40); impact_path=models.TextField(blank=True); strength=models.CharField(max_length=20,default="medium"); is_primary=models.BooleanField(default=False); notes=models.TextField(blank=True)
    class Meta: constraints=[models.UniqueConstraint(fields=["risk","objective","relationship_type"], name="unique_risk_objective_link")]
class RiskRelationship(TimeStampedModel):
    source_risk=models.ForeignKey(Risk, related_name="outgoing_relationships", on_delete=models.CASCADE); target_risk=models.ForeignKey(Risk, related_name="incoming_relationships", on_delete=models.CASCADE); relationship_type=models.CharField(max_length=50); strength=models.CharField(max_length=20,default="medium"); rationale=models.TextField()
