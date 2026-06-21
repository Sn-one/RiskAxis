from django.db import models
from riskaxis.core.models import TimeStampedModel
class Review(TimeStampedModel):
    title=models.CharField(max_length=220); review_type=models.CharField(max_length=40); reviewer=models.ForeignKey("accounts.User",on_delete=models.PROTECT); objective=models.ForeignKey("objectives.Objective",null=True,blank=True,on_delete=models.CASCADE); risk=models.ForeignKey("risks.Risk",null=True,blank=True,on_delete=models.CASCADE); control=models.ForeignKey("controls.Control",null=True,blank=True,on_delete=models.CASCADE); due_date=models.DateField(); completed_at=models.DateTimeField(null=True,blank=True); outcome=models.CharField(max_length=40,default="pending"); notes=models.TextField(blank=True)
    def __str__(self): return self.title
