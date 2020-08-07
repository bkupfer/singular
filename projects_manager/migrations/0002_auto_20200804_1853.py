# Generated by Django 3.0.7 on 2020-08-04 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects_manager', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer',
            new_name='Client',
        ),
        migrations.RemoveField(
            model_name='project',
            name='customer',
        ),
        migrations.AddField(
            model_name='project',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='projects_manager.Client'),
            preserve_default=False,
        ),
    ]