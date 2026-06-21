from django.db import models
from riskaxis.core.models import TimeStampedModel
class Incident(TimeStampedModel):
    incident_code=models.CharField(max_length=40,unique=True); title=models.CharField(max_length=220); description=models.TextField(); occurred_on=models.DateField(); discovered_on=models.DateField(null=True,blank=True); business_unit=models.ForeignKey("organization.BusinessUnit",on_delete=models.PROTECT); risk=models.ForeignKey("risks.Risk",null=True,blank=True,related_name="incidents",on_delete=models.SET_NULL); objective=models.ForeignKey("objectives.Objective",null=True,blank=True,related_name="incidents",on_delete=models.SET_NULL); severity=models.CharField(max_length=40,default="medium"); status=models.CharField(max_length=40,default="open"); root_cause=models.TextField(blank=True); corrective_action=models.TextField(blank=True)
    def __str__(self): return self.incident_code
