# Generated by Django 5.0.2 on 2024-03-31 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veggie', '0003_receipe_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipe',
            name='receipe_view_count',
            field=models.IntegerField(default=1),
        ),
    ]
