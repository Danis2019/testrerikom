# Generated by Django 4.0.4 on 2022-05-18 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_remove_message_pub_date_message_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_text',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='condition',
        ),
        migrations.AddField(
            model_name='message',
            name='user_id',
            field=models.IntegerField(default=123),
        ),
    ]
