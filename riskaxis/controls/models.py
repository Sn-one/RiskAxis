from django.db import models
from riskaxis.core.models import TimeStampedModel
class Control(TimeStampedModel):
    control_code=models.CharField(max_length=40,unique=True); name=models.CharField(max_length=220); description=models.TextField(); owner=models.ForeignKey("accounts.User",on_delete=models.PROTECT); business_unit=models.ForeignKey("organization.BusinessUnit",on_delete=models.PROTECT); control_type=models.CharField(max_length=40,default="preventive"); frequency=models.CharField(max_length=40,default="ongoing"); design_effectiveness=models.CharField(max_length=40,default="not_assessed"); operating_effectiveness=models.CharField(max_length=40,default="not_assessed")
    policies=models.ManyToManyField("documents.PolicyProcedure",blank=True,related_name="controls")
    objectives=models.ManyToManyField("objectives.Objective",blank=True,related_name="controls")
    def __str__(self): return f"{self.control_code} — {self.name}"
class ControlRiskLink(TimeStampedModel):
    control=models.ForeignKey(Control,related_name="risk_links",on_delete=models.CASCADE); risk=models.ForeignKey("risks.Risk",related_name="control_links",on_delete=models.CASCADE); mitigation_effect=models.CharField(max_length=40); reliance_level=models.CharField(max_length=40,default="medium"); notes=models.TextField(blank=True)
