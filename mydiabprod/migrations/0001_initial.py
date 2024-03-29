# Generated by Django 2.1.3 on 2018-11-15 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mydiabdocuments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filename', models.CharField(max_length=200)),
                ('Fileurl', models.CharField(max_length=200)),
                ('Description', models.CharField(max_length=400)),
                ('DocumentDate', models.CharField(max_length=100)),
                ('Dokuowner', models.CharField(max_length=100)),
                ('EntryDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Mydiabevents2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventName', models.CharField(max_length=200)),
                ('Eventowner', models.CharField(max_length=100)),
                ('EventDate', models.DateField(null=True)),
                ('EventTime', models.TimeField(null=True)),
                ('EventDescription', models.CharField(max_length=400)),
                ('EntryDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Mydiabresults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DateTime', models.CharField(max_length=100)),
                ('HGB', models.IntegerField(default=0)),
                ('TypeOf', models.CharField(max_length=50)),
                ('DeployDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Mydiabusers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
                ('UserName', models.CharField(max_length=100)),
                ('EntryDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Mydiabwelcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WelcomeText', models.CharField(max_length=200)),
                ('WelcomeOrigin', models.CharField(max_length=200)),
                ('EntryDate', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='mydiabresults',
            name='UserName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mydiabprod.Mydiabusers'),
        ),
    ]
