# Generated by Django 4.2.1 on 2023-05-29 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_userdetails_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_lab_head', models.BooleanField(default=False)),
                ('is_patient', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='userDetails',
        ),
    ]
