# Generated by Django 3.2.9 on 2021-11-21 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLeague', '0005_remove_tournament_table_club_ptr'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tournament_table',
        ),
    ]
