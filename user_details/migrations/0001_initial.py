# Generated by Django 2.2a1 on 2019-03-12 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FillProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adv_air', models.IntegerField(default=0)),
                ('mains_air', models.IntegerField(default=0)),
                ('state', models.CharField(choices=[('select', 'Select your Home State'), ('andhra pradesh', 'Andhra Pradesh'), ('arrunachal pradesh', 'Arrunachal Pradesh'), ('assam', 'Assam'), ('bihar', 'Bihar'), ('chattisgarh', 'Chattisgarh'), ('goa', 'Goa'), ('gujrat', 'Gujrat'), ('haryana', 'Haryana'), ('himachal pradesh', 'Himachal Pradesh'), ('jammu & kashmir', 'Jammu & Kashmir'), ('jharkhand', 'Jharkhand'), ('karnataka', 'Karnataka'), ('kerala', 'Kerala'), ('madhya pradesh', 'Madhya Pradesh'), ('maharashtra', 'Maharashtra'), ('manipur', 'Manipur'), ('meghalaya', 'Meghalaya'), ('mizoram', 'Mizoram'), ('nagaland', 'Nagaland'), ('odisha', 'Odisha'), ('rajasthan', 'Rajasthan'), ('sikkim', 'Sikkim'), ('tamil nadu', 'Tamil Nadu'), ('telangana', 'Telangana'), ('tripura', 'Tripura'), ('uttarakhand', 'Uttharakhand'), ('uttar pradesh', 'Uttar Pradesh'), ('west bengal', 'West Bengal')], default='select', max_length=100)),
                ('category', models.CharField(choices=[('select category', 'Select your Category'), ('general', 'General'), ('general-pwd', 'General-PwD'), ('obc-ncl', 'OBC-NCL'), ('obc-ncl-pwd', 'OBC-NCL-PWD'), ('sc', 'SC'), ('st', 'ST')], default='select category', max_length=100)),
                ('gender', models.BooleanField(choices=[(True, 'Male'), (False, 'Female')], default=True)),
                ('Logged_in_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FillPrefer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_choices', multiselectfield.db.fields.MultiSelectField(choices=[('c1', 'college1'), ('c2', 'college2'), ('c3', 'college3'), ('c4', 'college4'), ('c5', 'college5')], default='c1', max_length=14)),
                ('college_selected', multiselectfield.db.fields.MultiSelectField(choices=[('c6', 'college6'), ('c7', 'college7'), ('c8', 'college8'), ('c9', 'college9'), ('c10', 'college10')], default='c6', max_length=15)),
                ('Logged_in_user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]