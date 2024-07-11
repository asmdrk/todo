# Generated by Django 5.0.6 on 2024-07-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('xp', models.PositiveIntegerField()),
                ('is_sub', models.BooleanField(default=False)),
                ('subskills', models.ManyToManyField(blank=True, to='skills.skill')),
            ],
        ),
    ]
