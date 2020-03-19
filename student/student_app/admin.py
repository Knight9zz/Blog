from django.contrib import admin
from .models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq'
    ,'phone', 'status', 'create_time')

    list_filter = ('sex', 'status', 'create_time')

    search_fields = ('name', 'profession')

    fieldsets = (
        ('这里是学员信息',{
            'fields':(
                'name',
                ('sex', 'profession'),
                ('email', 'qq', 'phone'),
                'status',
            )
        }),
    )

admin.site.register(Student,StudentAdmin)

