from django.contrib import admin
from django.contrib.auth.models import User
from employees.models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login')
    search_fields = ['username', 'email']
    admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Employees)
admin.site.register(Department)
admin.site.register(Position)