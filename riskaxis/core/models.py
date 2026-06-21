import uuid
from django.conf import settings
from django.db import models

class TimeStampedModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="created_%(class)ss", on_delete=models.SET_NULL)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, related_name="updated_%(class)ss", on_delete=models.SET_NULL)
    is_active = models.BooleanField(default=True)
    class Meta:
        abstract = True
        ordering = ["-updated_at"]

class NamedModel(TimeStampedModel):
    name = models.CharField(max_length=180)
    code = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True)
    class Meta(TimeStampedModel.Meta):
        abstract = True
        ordering = ["name"]
    def __str__(self):
        return f"{self.code} — {self.name}"
