from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Update


# Unregister Groups
admin.site.unregister(Group)

# Mix Profile into User
class ProfileInline(admin.StackedInline):
    model = Profile

# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Display username fields on admin page
    fields = ["username"]
    inlines = [ProfileInline]

# Unregister initial User
admin.site.unregister(User)

# Re-register User
admin.site.register(User, UserAdmin)

# admin.site.register(Profile)

admin.site.register(Update)