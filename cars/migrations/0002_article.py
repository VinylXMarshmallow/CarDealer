# Generated by Django 4.2.6 on 2023-11-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('content', models.TextField(default='')),
                ('year', models.PositiveSmallIntegerField(default=2023)),
                ('imgThumb', models.ImageField(blank=True, null=True, upload_to='media_img')),
            ],
        ),
    ]
