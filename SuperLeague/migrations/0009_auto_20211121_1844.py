# Generated by Django 3.2.9 on 2021-11-21 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLeague', '0008_tournament_table_club'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament_table',
            name='club',
        ),
        migrations.AddField(
            model_name='tournament_table',
            name='club_ptr',
            field=models.OneToOneField(auto_created=True, default=0, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='SuperLeague.club'),
            preserve_default=False,
        ),
    ]