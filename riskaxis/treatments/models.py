from django.db import models
from riskaxis.core.models import TimeStampedModel
class TreatmentAction(TimeStampedModel):
    risk=models.ForeignKey("risks.Risk",related_name="treatment_actions",on_delete=models.CASCADE); title=models.CharField(max_length=220); description=models.TextField(); owner=models.ForeignKey("accounts.User",on_delete=models.PROTECT); due_date=models.DateField(); status=models.CharField(max_length=40,default="not_started"); progress_percent=models.PositiveSmallIntegerField(default=0); evidence=models.FileField(upload_to="treatment_evidence/",blank=True)
    def __str__(self): return self.title
