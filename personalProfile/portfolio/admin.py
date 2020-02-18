from django.contrib import admin
from .models import Experience, Education, Cert, Activity, Project, Skill, Award, Image

# imports the models into the admin page so that they can be modified later on
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Cert)
admin.site.register(Activity)
admin.site.register(Project)
admin.site.register(Skill)
admin.site.register(Award)
admin.site.register(Image)

