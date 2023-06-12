# Generated by Django 4.1.7 on 2023-03-21 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donormodel',
            name='phonenumber',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='medmodel',
            name='image',
            field=models.ImageField(blank=True, default='images/default.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='ngomodel',
            name='phonenumber',
            field=models.IntegerField(),
        ),
    ]