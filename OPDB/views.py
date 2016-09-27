from django.shortcuts import render
import json

from .models import Pump

# Create your views here.


def index(request):
    #This is osiligi langing page, displays a summary of pumps worked on
    pumps= Pump.objects.count()
    
    tas=[['Londo, London', 51.507474,-0.179562],['Palace of Westminster, London', 51.499633,-0.124755]]
    tags= json.dumps(tas)
   

    
    
    
    
    
    report= pumps
    working_pumps= Pump.objects.filter(pump_status='Green')
    working_pumpdt=0
    pc=0
    for working_pump in working_pumps:
        pc=pc+1
        users=working_pump.pump_users
        working_pumpdt=working_pumpdt+ int(users)
        
    nonworking_pumps= Pump.objects.filter(pump_status='Amber')
    nonworking_pumpdt=0
    nwp=0
    for nonworking_pump in nonworking_pumps:
        nwp=nwp+1
        users=nonworking_pump.pump_users
        nonworking_pumpdt=nonworking_pumpdt+ int(users)
        
    stopped_pumps= Pump.objects.filter(pump_status='Red')
    sp=0
    stopped_pumpdt=0
    for stopped_pump in stopped_pumps:
        users=stopped_pump.pump_users
        stopped_pumpdt=stopped_pumpdt+ int(users)
        sp=sp+1


    
    
    
    
    context = {
               'report':report ,
               'users':working_pumpdt,
               'StoppedWorking':nonworking_pumpdt,
               'Stopped':stopped_pumpdt,
               'pc':pc,
               'nwp':nwp,
               'sp':sp,
               'plist':tags
               
               
               }
    return render(request, 'OPDB/index.html', context)
    