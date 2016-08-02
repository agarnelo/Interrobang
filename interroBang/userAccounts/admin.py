from django.contrib import admin

# Register your models here.

from .models import User

#What we will see in the admin page for each user (need to add more)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ["username", "id"]
    class Meta:
        model = User
admin.site.register(User, UserModelAdmin)