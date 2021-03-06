# Generated by Django 3.2.9 on 2021-11-21 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLeague', '0003_rename_clab_name_club_club_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament_table',
            fields=[
                ('club_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='SuperLeague.club')),
                ('position', models.AutoField(primary_key=True, serialize=False)),
                ('game', models.IntegerField(default=0, max_length=3)),
                ('goal_difference', models.IntegerField(default=0, max_length=3)),
                ('point', models.IntegerField(default=0, max_length=3)),
            ],
            bases=('SuperLeague.club',),
        ),
    ]
