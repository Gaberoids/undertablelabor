# Generated by Django 4.0 on 2021-12-18 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_services', '0002_remove_contactmessage_m_id_contactmessage_m_receiver_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='m_sender_email',
            field=models.EmailField(default=False, max_length=254),
        ),
    ]
