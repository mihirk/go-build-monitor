from django.contrib import admin

from models import Configuration, BuildsToMonitor


class ConfigurationAdmin(admin.ModelAdmin):
    fields = ('pipeline_url', 'username', 'password',)
    list_display = ("pipeline_url", "username",)


admin.site.register(Configuration, ConfigurationAdmin)
admin.site.register(BuildsToMonitor)