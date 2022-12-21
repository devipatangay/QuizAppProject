# Generated by Django 4.1.1 on 2022-12-16 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200, null=True)),
                ('option1', models.CharField(max_length=200, null=True)),
                ('option2', models.CharField(max_length=200, null=True)),
                ('option3', models.CharField(max_length=200, null=True)),
                ('option4', models.CharField(max_length=200, null=True)),
                ('answer', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
