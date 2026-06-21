from django.db import models
from riskaxis.core.models import TimeStampedModel
class RiskAssessment(TimeStampedModel):
    risk=models.ForeignKey("risks.Risk",related_name="assessments",on_delete=models.CASCADE); assessment_type=models.CharField(max_length=30,default="residual"); likelihood=models.PositiveSmallIntegerField(default=1); impact=models.PositiveSmallIntegerField(default=1); score=models.PositiveSmallIntegerField(default=1); rating=models.CharField(max_length=30,default="low"); rationale=models.TextField(blank=True); assessed_on=models.DateField(auto_now_add=True)
    def save(self,*args,**kwargs): self.score=self.likelihood*self.impact; super().save(*args,**kwargs)
