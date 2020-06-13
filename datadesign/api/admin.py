from django.contrib import admin
from api.models import User, Agent, Event, Group, GroupUser

# Register your models here.
class UserModelAdmin(admin.ModelAdmin):
    def users(self, obj):
        list_display = ('name', 'last_login', 'email')


class AgentModelAdmin(admin.ModelAdmin):
    pass


class EventModelAdmin(admin.ModelAdmin):
    pass


class GroupModelAdmin(admin.ModelAdmin):
    pass


class GrupoUserModelAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserModelAdmin)
admin.site.register(Agent, AgentModelAdmin)
admin.site.register(Event, EventModelAdmin)
admin.site.register(Group, GroupModelAdmin)
admin.site.register(GroupUser, GrupoUserModelAdmin)