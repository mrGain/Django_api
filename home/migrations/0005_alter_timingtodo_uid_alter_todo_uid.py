# Generated by Django 4.0.3 on 2022-04-09 01:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_todo_user_alter_timingtodo_uid_alter_todo_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timingtodo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6d564238-c780-4ed2-aa25-59ab770ef843'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='todo',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('6d564238-c780-4ed2-aa25-59ab770ef843'), editable=False, primary_key=True, serialize=False),
        ),
    ]
