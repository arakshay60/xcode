# Generated by Django 4.2.9 on 2024-01-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_alter_submission_code_alter_submission_stderr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='code',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='submission',
            name='stderr',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='submission',
            name='stdout',
            field=models.TextField(default=''),
        ),
    ]
