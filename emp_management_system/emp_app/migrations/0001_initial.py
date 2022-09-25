# Generated by Django 3.2.5 on 2022-09-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('salary', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('phone', models.IntegerField(default=0)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.department')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emp_app.role')),
            ],
        ),
    ]