# Generated by Django 2.2.2 on 2019-06-10 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Enter Suitable Title', max_length=100)),
                ('text', models.TextField(default='Write your post here...', max_length=256)),
            ],
        ),
    ]
