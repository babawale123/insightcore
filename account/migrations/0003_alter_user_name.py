# Generated by Django 4.2.4 on 2024-12-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_user_groups_remove_user_is_superuser_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
    ]
