# Generated by Django 3.1.2 on 2020-10-31 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BetaArgenti', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='authod',
            new_name='author',
        ),
    ]
