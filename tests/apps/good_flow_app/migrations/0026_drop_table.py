# Generated by Django 3.1 on 2019-09-22 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('good_flow_app', '0025_drop_index_with_condition'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestTable',
        ),
    ]