# Generated by Django 4.2.5 on 2023-09-21 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dz_karmaapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='foto',
            field=models.ImageField(blank=True, default='uploads/default.jpg', upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='client',
            name='tel',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
