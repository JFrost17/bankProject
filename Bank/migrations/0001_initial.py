# Generated by Django 3.1.7 on 2021-04-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depositAmount', models.DecimalField(decimal_places=2, max_digits=65)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Withdrawl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('withdrawlAmount', models.DecimalField(decimal_places=2, max_digits=65)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]