# Generated by Django 4.0.3 on 2022-03-27 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_urllog_origin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='urlredirect',
            options={'ordering': ['-created_at'], 'verbose_name': 'URL Redirect', 'verbose_name_plural': "URL's Redirect"},
        ),
    ]
