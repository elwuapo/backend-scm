# Generated by Django 3.2.9 on 2022-04-29 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=99, null=True)),
                ('employees', models.ManyToManyField(blank=True, to='api.Account')),
            ],
        ),
        migrations.CreateModel(
            name='WorkDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(blank=True, choices=[('monday', 'monday'), ('tuesday', 'tuesday'), ('wednesday', 'wednesday'), ('thursday', 'thursday'), ('friday', 'friday'), ('saturday', 'saturday'), ('sunday', 'sunday')], max_length=20, null=True)),
                ('check_in_time', models.TimeField()),
                ('departure_time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='workinghours',
            name='working_hours',
        ),
        migrations.DeleteModel(
            name='WorkingDay',
        ),
        migrations.AddField(
            model_name='workinghours',
            name='workday',
            field=models.ManyToManyField(blank=True, to='api.WorkDay'),
        ),
    ]
