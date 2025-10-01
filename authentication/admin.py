from django.contrib import admin
from.models import Countries,Departments, Cities, Users
# Register your models here.
#admin.site.register(Countries)
#admin.site.register(Departments)
#admin.site.register(Cities)
#admin.site.register(Users)

@admin.register(Countries)
class CountrysAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev','get_status')

    def get_status(self, obj):
        return "Activate" if obj.status else "Inactive"
    get_status.short_description = 'Status' #Table label