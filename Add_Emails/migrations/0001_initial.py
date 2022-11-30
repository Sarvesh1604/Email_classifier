# Generated by Django 3.2.7 on 2021-09-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload_Emails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='')),
                ('email', models.FileField(upload_to='Email_Uploads')),
                ('remarks', models.TextField(default='')),
            ],
        ),
    ]