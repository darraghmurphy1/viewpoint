# Generated by Django 4.1.3 on 2022-11-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_alter_comment_approved_alter_post_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=1),
        ),
    ]