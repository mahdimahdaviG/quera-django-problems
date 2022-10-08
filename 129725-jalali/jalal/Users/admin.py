from Users.models import Birthday, CustomUser
from django.contrib import admin

#from django_jalali.admin.filters import JDateFieldListFilter
#import django_jalali.admin as jadmin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'gender', 'national_code', 'birthday_date')
    ordering = ['ceremony_datetime']
    search_fields = ['username', 'full_name']

    def first_name(self, obj):
        return obj.full_name.split()[0]

    def last_name(self, obj):
        return obj.full_name.split()[1]


        


admin.site.register(Birthday)


