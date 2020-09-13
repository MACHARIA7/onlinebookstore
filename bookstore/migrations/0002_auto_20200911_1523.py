# Generated by Django 3.1.1 on 2020-09-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='authors', to='bookstore.Author'),
        ),
    ]