# Generated by Django 4.0 on 2021-12-18 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_services', '0003_contactmessage_m_sender_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmessage',
            name='m_sender_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]