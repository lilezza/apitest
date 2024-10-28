from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name' , 'last_name' , 'age' , 'published_date')
    fieldsets = (
        (None , {
            'fields' : ('first_name' , 'last_name' , 'age' , 'published_date')
        }),
    )

admin.site.register(User,UserAdmin)
