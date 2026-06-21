from django.contrib import admin
from . import models

for name in dir(models):
    obj = getattr(models, name)
    if getattr(obj, "_meta", None) and getattr(obj._meta, "app_label", None) == "risks":
        try:
            admin.site.register(obj)
        except admin.sites.AlreadyRegistered:
            pass
