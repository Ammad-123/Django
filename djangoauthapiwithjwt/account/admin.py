from django.contrib import admin
from account.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    # The fields to be used in displaying the User Model
    list_display = ('id','email','name','tc','is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('User Credentials',{'fields':('email','password')}),
        ('Personal Info', {'fields':('name','tc')}),
        ('Permissions',{'fields':('is_admin',)}),
    )


    add_fieldsets= (
            (None, {
                'classes':('wide',),
                'fields':('email','name','tc','password1','password2'),
            }),
        
    )
    search_fields = ('email',),
    ordering = ('email'),
    filter_horizontal = ()


# register the new UserModelAdmin
admin.site.register(User,UserModelAdmin)