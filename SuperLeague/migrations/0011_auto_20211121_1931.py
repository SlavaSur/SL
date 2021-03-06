# Generated by Django 3.2.9 on 2021-11-21 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLeague', '0010_auto_20211121_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='club_name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='tour_one',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SuperLeague.club', to_field='club_name'),
        ),
    ]
