from django.conf import settings
from django.db import models
from riskaxis.core.models import NamedModel
class RiskUniverseCategory(NamedModel):
    parent=models.ForeignKey("self",null=True,blank=True,related_name="children",on_delete=models.PROTECT)
    owner=models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET_NULL)
    default_appetite_level=models.CharField(max_length=40,blank=True)
