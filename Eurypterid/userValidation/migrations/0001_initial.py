# Generated by Django 4.2 on 2023-05-03 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AadharCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('aadhar_no', models.CharField(max_length=14)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='GateCandidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=50)),
                ('parent_name', models.CharField(max_length=50)),
                ('reg_no', models.CharField(max_length=13)),
                ('dob', models.DateField()),
                ('paper', models.TextField()),
                ('gate_score', models.IntegerField()),
                ('air', models.IntegerField()),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
