from django.db import models
from riskaxis.core.models import TimeStampedModel
class RiskAppetite(TimeStampedModel):
    name=models.CharField(max_length=180); objective=models.ForeignKey("objectives.Objective",null=True,blank=True,on_delete=models.CASCADE); category=models.ForeignKey("risk_universe.RiskUniverseCategory",null=True,blank=True,on_delete=models.CASCADE); threshold_score=models.PositiveSmallIntegerField(default=9); statement=models.TextField(); escalation_required=models.BooleanField(default=True)
    def __str__(self): return self.name
