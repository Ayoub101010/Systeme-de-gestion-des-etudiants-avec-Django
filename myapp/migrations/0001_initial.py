# Generated by Django 5.0 on 2024-01-02 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.PositiveIntegerField()),
                ('Prenom', models.CharField(max_length=50)),
                ('Nom', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('Moyenne', models.FloatField()),
            ],
        ),
    ]
