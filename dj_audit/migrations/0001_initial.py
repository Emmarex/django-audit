# Generated by Django 3.2.8 on 2021-10-18 21:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField(null=True, verbose_name='IP Address')),
                ('content_type', models.CharField(max_length=200, verbose_name='Content Type')),
                ('query_string', models.TextField(verbose_name='Query String')),
                ('http_method', models.CharField(max_length=20, verbose_name='HTTP Method')),
                ('http_referer', models.CharField(max_length=500, verbose_name='HTTP Method')),
                ('path_info', models.CharField(max_length=255, verbose_name='Path')),
                ('request_data', models.TextField(null=True)),
                ('response_status_code', models.IntegerField(null=True)),
                ('response_reason_phrase', models.TextField()),
                ('attempt_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-attempt_time'],
            },
        ),
    ]
