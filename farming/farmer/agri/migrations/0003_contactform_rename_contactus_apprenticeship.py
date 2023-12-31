# Generated by Django 4.2.4 on 2023-09-12 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agri', '0002_rename_contactform_contactus_delete_apprenticeship'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
        migrations.RenameModel(
            old_name='ContactUs',
            new_name='ApprenticeShip',
        ),
    ]
