from django.conf import settings
from django.db import models
from riskaxis.core.models import NamedModel, TimeStampedModel

class BusinessUnit(NamedModel):
    parent = models.ForeignKey("self", null=True, blank=True, related_name="children", on_delete=models.PROTECT)

class UserBusinessUnit(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="business_units", on_delete=models.CASCADE)
    business_unit = models.ForeignKey(BusinessUnit, related_name="members", on_delete=models.CASCADE)
    role_in_unit = models.CharField(max_length=120, blank=True)
    is_primary = models.BooleanField(default=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=["user", "business_unit"], name="unique_user_business_unit")]
    def __str__(self): return f"{self.user} @ {self.business_unit}"
