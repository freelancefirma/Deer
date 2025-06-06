# Generated by Django 5.2.1 on 2025-06-02 23:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0042_alter_cmsplugin_id_alter_globalpagepermission_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='%(app_label)s_%(class)s', serialize=False, to='cms.cmsplugin')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
            bases=('cms.cmsplugin',),
        ),
    ]
