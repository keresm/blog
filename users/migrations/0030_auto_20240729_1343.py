# Generated by Django 3.2.13 on 2024-07-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_auto_20240613_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_publicity_level',
            field=models.CharField(choices=[('private', 'Параноик'), ('normal', 'Обычный'), ('public', 'Публичный')], default='normal', max_length=16),
        ),
        migrations.RunSQL(
            "update users set profile_publicity_level = 'public' where is_profile_public = true;"
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_profile_public',
        ),
    ]
