# Generated by Django 4.1.7 on 2023-03-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.AddField(
            model_name='image',
            name='image_filename',
            field=models.CharField(default='error_image', max_length=200, verbose_name='Image Filename'),
        ),
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.URLField(default='https://www.lifewire.com/thmb/5Y8ggTdQiyLdq9us-IMpsACJP-s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/alert-icon-5807a14f5f9b5805c2aa679c.PNG', verbose_name='Image URL'),
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail_filename',
            field=models.CharField(default='error_thumbnail', max_length=200, verbose_name='Thumbnail Filename'),
        ),
        migrations.AddField(
            model_name='image',
            name='thumbnail_url',
            field=models.URLField(default='https://www.lifewire.com/thmb/5Y8ggTdQiyLdq9us-IMpsACJP-s=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/alert-icon-5807a14f5f9b5805c2aa679c.PNG', verbose_name='Thumbnail URL'),
        ),
    ]
