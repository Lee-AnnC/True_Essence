# Generated by Django 3.1.5 on 2021-02-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20210227_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(default='gardening', max_length=255),
        ),
    ]
