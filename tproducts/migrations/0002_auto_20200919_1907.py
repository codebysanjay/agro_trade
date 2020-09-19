# Generated by Django 3.1.1 on 2020-09-19 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tproducts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tproduct',
            name='description',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tproduct',
            name='image_url',
            field=models.ImageField(upload_to='products/'),
        ),
    ]