from django.contrib import admin
from .models import Pump
from OPDB.models import *
from imagekit.admin import AdminThumbnail

# Register your models here.

class PumpAdmin(admin.ModelAdmin):
    list_display=('pump_name','pump_type','pump_status','pump_users','pump_depth','rcp','pump_visited')

class Pumpcaretaker(admin.ModelAdmin):
    list_display=('fname','sname','contact','pump')
    
class CCadmin(admin.ModelAdmin):
    list_display=('communityname','Targetamount','ContributedAmount','dateReceived')
    
class CAdmin(admin.ModelAdmin):
        list_display=('committee_name','memberFname','memberSname','memberContact','memberTitle')
        
        



admin.site.register(Pump,PumpAdmin)
admin.site.register(PumpCareTaker,Pumpcaretaker)
admin.site.register(CommunityContribution,CCadmin)
admin.site.register(CommitteMember,CAdmin)
admin.site.register(PumpCommitte)
admin.site.register(Photo)
