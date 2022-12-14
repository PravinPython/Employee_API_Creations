# Generated by Django 2.2.9 on 2022-02-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=30, unique=True)),
                ('role', models.CharField(default='Guest', max_length=30)),
                ('phone_num', models.BigIntegerField(unique=True)),
                ('joiningDate', models.DateField()),
                ('address', models.CharField(default='Y', max_length=255)),
            ],
            options={
                'db_table': 'EMPLOYEE_MASTER',
                'ordering': ['role'],
            },
        ),
    ]
