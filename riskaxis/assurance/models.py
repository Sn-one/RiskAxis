from django.db import models
from riskaxis.core.models import TimeStampedModel
class AssuranceActivity(TimeStampedModel):
    title=models.CharField(max_length=220); activity_type=models.CharField(max_length=60,default="control_testing"); owner=models.ForeignKey("accounts.User",on_delete=models.PROTECT); start_date=models.DateField(null=True,blank=True); end_date=models.DateField(null=True,blank=True); status=models.CharField(max_length=40,default="planned"); scope=models.TextField(blank=True); conclusion=models.TextField(blank=True); risks=models.ManyToManyField("risks.Risk",blank=True,related_name="assurance_activities"); controls=models.ManyToManyField("controls.Control",blank=True,related_name="assurance_activities")
    def __str__(self): return self.title
