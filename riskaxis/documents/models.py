from django.db import models
from riskaxis.core.models import TimeStampedModel
class PolicyProcedure(TimeStampedModel):
    code=models.CharField(max_length=40,unique=True); title=models.CharField(max_length=220); document_type=models.CharField(max_length=40,default="policy"); owner=models.ForeignKey("accounts.User",on_delete=models.PROTECT); business_unit=models.ForeignKey("organization.BusinessUnit",null=True,blank=True,on_delete=models.SET_NULL); status=models.CharField(max_length=40,default="draft"); effective_date=models.DateField(null=True,blank=True); review_date=models.DateField(null=True,blank=True); file=models.FileField(upload_to="documents/",blank=True); summary=models.TextField(blank=True)
    def __str__(self): return f"{self.code} — {self.title}"
class PolicyRiskCoverage(TimeStampedModel):
    policy=models.ForeignKey(PolicyProcedure,related_name="risk_coverages",on_delete=models.CASCADE); risk=models.ForeignKey("risks.Risk",related_name="policy_coverages",on_delete=models.CASCADE); coverage_type=models.CharField(max_length=40); coverage_strength=models.CharField(max_length=40,default="not_assessed"); notes=models.TextField(blank=True)
