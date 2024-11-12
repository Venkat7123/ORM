# Generated by Django 5.1.3 on 2024-11-12 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('Customer_ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Customer_Name', models.CharField(max_length=100)),
                ('Customer_Salary', models.IntegerField()),
                ('Customer_Age', models.IntegerField()),
                ('Req_Loan_Amt', models.IntegerField()),
            ],
        ),
    ]