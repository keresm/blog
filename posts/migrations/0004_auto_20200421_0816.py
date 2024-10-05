# Generated by Django 3.0.4 on 2020-04-21 08:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20200421_0749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postview',
            old_name='first_viewed_at',
            new_name='first_view_at',
        ),
        migrations.RenameField(
            model_name='postview',
            old_name='last_viewed_at',
            new_name='last_view_at',
        ),
        migrations.AddField(
            model_name='postview',
            name='registered_view_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postview',
            name='unread_comments',
            field=models.IntegerField(default=0),
        ),
    ]
