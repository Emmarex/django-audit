# Generated by Django 3.2.8 on 2022-05-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_audit', '0004_alter_auditlog_response_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='user_agent',
            field=models.TextField(),
        ),
    ]
