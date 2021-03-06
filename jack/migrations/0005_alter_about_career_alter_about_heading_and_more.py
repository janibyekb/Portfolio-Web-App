# Generated by Django 4.0.4 on 2022-06-03 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jack', '0004_alter_home_greetings_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='about',
            name='heading',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='home',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=40),
        ),
    ]
