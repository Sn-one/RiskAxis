from django.db import models
from riskaxis.core.models import TimeStampedModel
class Indicator(TimeStampedModel):
    code=models.CharField(max_length=40,unique=True); name=models.CharField(max_length=220); indicator_type=models.CharField(max_length=10,default="KRI"); owner=models.ForeignKey("accounts.User",on_delete=models.PROTECT); objective=models.ForeignKey("objectives.Objective",null=True,blank=True,related_name="indicators",on_delete=models.CASCADE); risk=models.ForeignKey("risks.Risk",null=True,blank=True,related_name="indicators",on_delete=models.CASCADE); unit=models.CharField(max_length=40,blank=True); target_value=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True); warning_threshold=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True); breach_threshold=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
    def __str__(self): return f"{self.code} — {self.name}"
class IndicatorValue(TimeStampedModel):
    indicator=models.ForeignKey(Indicator,related_name="values",on_delete=models.CASCADE); value=models.DecimalField(max_digits=12,decimal_places=2); measured_at=models.DateField(); commentary=models.TextField(blank=True)
