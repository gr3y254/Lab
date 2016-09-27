# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommitteMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('memberFname', models.CharField(max_length=50)),
                ('memberSname', models.CharField(max_length=50)),
                ('memberContact', models.CharField(max_length=20)),
                ('memberTitle', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='CommunityContribution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Targetamount', models.IntegerField(default=b'5000')),
                ('ContributedAmount', models.IntegerField(default=b'0')),
                ('dateReceived', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=b'Pumps')),
            ],
        ),
        migrations.CreateModel(
            name='Pump',
            fields=[
                ('rcp', models.CharField(default=b'Emmanuel', max_length=7, choices=[(b'Eastern', b'Emmanuel'), (b'Central', b'David'), (b'Western', b'Victor')])),
                ('lon', models.FloatField(default=b'0.0')),
                ('lat', models.FloatField(default=b'0.0')),
                ('pump_name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('pump_type', models.CharField(max_length=50)),
                ('pump_depth', models.IntegerField(default=b'0')),
                ('pump_users', models.IntegerField(default=b'0')),
                ('pump_status', models.CharField(max_length=7, choices=[(b'Green', b'Working'), (b'Amber', b'Stopped working '), (b'Red', b'Not Working,More Resources needed')])),
                ('pump_visited', models.DateField(verbose_name=b'Date Visited')),
            ],
        ),
        migrations.CreateModel(
            name='PumpCareTaker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('contact', models.CharField(max_length=20)),
                ('pump', models.ForeignKey(to='OPDB.Pump')),
            ],
        ),
        migrations.CreateModel(
            name='PumpCommitte',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('committeName', models.CharField(max_length=50)),
                ('pumpname', models.OneToOneField(to='OPDB.Pump')),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='pump',
            field=models.ForeignKey(to='OPDB.Pump'),
        ),
        migrations.AddField(
            model_name='communitycontribution',
            name='communityname',
            field=models.ForeignKey(to='OPDB.PumpCommitte'),
        ),
        migrations.AddField(
            model_name='committemember',
            name='committee_name',
            field=models.ForeignKey(to='OPDB.PumpCommitte'),
        ),
    ]
