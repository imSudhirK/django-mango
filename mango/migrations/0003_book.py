# Generated by Django 5.0 on 2023-12-28 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mango', '0002_rename_decription_contact_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
