from django.db import models
from django.contrib import admin

# Create your models here.



class Pump(models.Model):
    regions_rcp_chices=(
                        ('Eastern','Emmanuel'),
                        ('Central','David'),
                        ('Western','Victor'))
    rcp=models.CharField(max_length=7,choices=regions_rcp_chices,default='Emmanuel')
    
    lat= models.FloatField(default='0.0N')
    lon = models.FloatField(default='0.0E')
    
    pump_name =  models.CharField(max_length=50,primary_key=True)
    pump_type =  models.CharField(max_length=50)
    pump_depth=  models.IntegerField(default='0')
    pump_users = models.IntegerField(default='0')
    
    pump_status_options = (
    ('Green', 'Working'),
    ('Amber', 'Stopped working '),
    ('Red', 'Not Working,More Resources needed'))
    
    pump_status = models.CharField(max_length=7,choices= pump_status_options)
    
    
    pump_visited = models.DateField('Date Visited')
    
    def __str__(self):
        return self.pump_name
    
    
class Photo(models.Model):
    pump = models.ForeignKey(Pump)
    photo_name=models.CharField(max_length=50,default='ImageName')
    photo_decription=models.TextField(default='Briefly decribe what is in the photo')
    photo= models.ImageField(upload_to='media')

    def __str__(self):
        return self.photo_name
    


class PumpCareTaker(models.Model):
    pump= models.ForeignKey(Pump)
    fname=models.CharField(max_length=50)
    sname=models.CharField(max_length=50)
    contact=models.CharField(max_length=20)
    
    def __str__(self):
        return self.fname
    
class PumpCommitte(models.Model):
    committeName=models.CharField(max_length=50)
    pumpname=models.OneToOneField(Pump)
    
    def __str__(self):
        return self.committeName
    
class CommitteMember(models.Model):
    committee_name=models.ForeignKey(PumpCommitte)
    memberFname=models.CharField(max_length=50)
    memberSname=models.CharField(max_length=50)
    memberContact=models.CharField(max_length=20)
    memberTitle=models.CharField(max_length=40)
    
    def __str__(self):
        return self.memberFname
    
    class Admin(admin.ModelAdmin):
        list_display=('committee_name','memberFname','memberSname','memberContact','memberTitle')
    
class CommunityContribution(models.Model):
    communityname=models.ForeignKey(PumpCommitte)
    Targetamount=models.IntegerField(default='5000')
    ContributedAmount=models.IntegerField(default='0')
    dateReceived=models.DateField()
    
    
    