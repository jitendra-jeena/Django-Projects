from django.contrib import admin
from .models import Job
from .models import Project
from .models import Skill
from .models import Certificates

admin.site.register(Job)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Certificates)
# Register your models here.

