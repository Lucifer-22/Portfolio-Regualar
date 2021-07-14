from django.contrib import admin
from .models import (Information,
                    Education,
                    Experience,
                    Skillset,
                    Message,
                    Project,
                    User,
                    FewWords)
# Register your models here.

admin.site.register(User)
admin.site.register(FewWords)
admin.site.register(Information)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skillset)
admin.site.register(Message)
admin.site.register(Project)


