from django.contrib import admin
from jad.models import *

class PConfigInline(admin.TabularInline):
    model = PConfig

class ContentSwitchInline(admin.TabularInline):
    model = ContentSwitch

class TargetInline(admin.TabularInline):
    model = Target

class EndpointInline(admin.TabularInline):
    model = Endpoint

class ProxyAdmin(admin.ModelAdmin):
    inlines = [
        PConfigInline,
    ]

class PConfigAdmin(admin.ModelAdmin):
    inlines = [
        ContentSwitchInline,
    ]

class ContentSwitchAdmin(admin.ModelAdmin):
    inlines = [
        TargetInline,
    ]

class TargetAdmin(admin.ModelAdmin):
    inlines = [
        EndpointInline,
    ]

admin.site.register(Proxy, ProxyAdmin)
admin.site.register(PConfig, PConfigAdmin)
admin.site.register(ContentSwitch, ContentSwitchAdmin )
admin.site.register(Target, TargetAdmin)
admin.site.register(Endpoint)
