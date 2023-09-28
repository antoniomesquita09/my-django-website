# Generated by Django 4.2.4 on 2023-09-28 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MeuApp', '0004_alter_ride_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='passenger',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='rides_as_passenger', to='MeuApp.profile'),
            preserve_default=False,
        ),
    ]
