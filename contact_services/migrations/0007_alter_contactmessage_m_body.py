# Generated by Django 3.2 on 2022-03-23 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_services', '0006_auto_20220323_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='m_body',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Body: '),
        ),
    ]
