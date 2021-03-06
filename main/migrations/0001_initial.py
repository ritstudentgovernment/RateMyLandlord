# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 17:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activation_key', models.CharField(max_length=40)),
                ('key_expires', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Complex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LandlordReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('responsive', models.PositiveSmallIntegerField()),
                ('communication', models.PositiveSmallIntegerField()),
                ('recommend', models.PositiveSmallIntegerField()),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Landlord')),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=2)),
                ('zip_code', models.CharField(max_length=5)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('furnished', models.BooleanField()),
                ('rooms', models.PositiveSmallIntegerField()),
                ('complx', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Complex')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('lease_start', models.DateTimeField()),
                ('lease_end', models.DateTimeField()),
                ('price', models.PositiveIntegerField()),
                ('utilities', models.PositiveIntegerField()),
                ('accessible', models.BooleanField()),
                ('clean', models.BooleanField()),
                ('laundry', models.BooleanField()),
                ('landlord', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Landlord')),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Property')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Account')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('domain', models.CharField(max_length=20)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('properties', models.ManyToManyField(to='main.Property')),
            ],
        ),
        migrations.CreateModel(
            name='TagCounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0)),
                ('prop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Property')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='landlord',
            name='properties',
            field=models.ManyToManyField(to='main.Property'),
        ),
        migrations.AddField(
            model_name='complex',
            name='landlord',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Landlord'),
        ),
        migrations.AddField(
            model_name='account',
            name='residence',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Property'),
        ),
        migrations.AddField(
            model_name='account',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.School'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
