# Generated by Django 3.2.9 on 2021-11-21 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SuperLeague', '0009_auto_20211121_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_home', models.IntegerField(default=0)),
                ('goal_away', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='club',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Tournament_table',
        ),
        migrations.AddField(
            model_name='tour_one',
            name='home',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SuperLeague.club'),
        ),
    ]
