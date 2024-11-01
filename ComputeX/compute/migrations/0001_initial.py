# Generated by Django 5.1.2 on 2024-10-31 16:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='accounts.request')),
            ],
        ),
    ]
