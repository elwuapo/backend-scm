from django.contrib import admin

from api.models import WorkDay, WorkingHours, Browser, Mark, Account, Business

# Register your models here.
admin.site.register(WorkDay)
admin.site.register(WorkingHours)
admin.site.register(Browser)
admin.site.register(Mark)
admin.site.register(Account)
admin.site.register(Business)