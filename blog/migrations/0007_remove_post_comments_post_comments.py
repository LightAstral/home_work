# Generated by Django 4.2.4 on 2023-09-24 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_comments_post_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, null=True, related_name='post_comments', to='blog.comment', verbose_name='Коментарі'),
        ),
    ]
