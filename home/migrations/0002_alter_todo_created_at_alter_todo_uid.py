# Generated by Django 4.0.3 on 2022-04-08 02:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1db3b0bc-6229-425c-b835-e5a883a26931'), editable=False, primary_key=True, serialize=False),
        ),
    ]
